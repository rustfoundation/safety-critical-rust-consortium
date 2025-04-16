# ABI and FFI

## What is an ABI?

The term ABI stands for Application Binary Interface and describes a set of rules that enable different parts of a
program to interact with each other in a defined way *after these parts have been translated to a binary entity*. This
is a non-comprehensive list of properties an ABI defines:

* Size, alignment and endianness of basic data types like integers, floats or pointers
* Layout, padding and alignment of compound types like tuples and structs
* A protocol to transfer program flow to a subroutine (and back)
* A protocol to generate and handle exceptional errors

Note that not all ABIs define all mentioned categories - if a certain language does not support a certain technology,
the ABI that supports the technology isn't usually supported well - or not at all. Examples of such mechanics:

* C++ exceptions: Since Rust's FFI is C-based, C++ exceptions cannot cross language boundaries and must not bubble up to
  Rust code as Rust does not understand how to handle them and / or perform stack unwinding.
* Runtime polymorphism: Since this isn't part of C either, Rust's take on virtual methods is very different from what
  other languages do in that regard. Therefore, there is no out-of-the-box support for runtime polymorphism across the
  Rust FFI either.

It is usually the task of the linker to collect the bits of a program and merge it into an executable. This will only
result in a working program if all parts of the program agree on the same ABI. If there are ABI incompatibilities, this
will usually lead to trouble during program execution, like data corruption or crashes.

## About the "C ABI"

When you're looking for information about linking parts of a program (potentially written in different languages) on the
internet, one often comes across the term "C ABI". Due to the vast amount of code written in C, the language became a de
facto standard for compatibility on various levels. That's also the reason why you find that term in Rust source, like
`repr(C)` or `extern "C"`. However, the C language itself does not define an ABI.  This is underlined by the ISO C[^1]
standard which states in its `Scope` chapter in the second paragraph:
> 2 This International Standard does not specify
> - the mechanism by which C programs are transformed for use by a data-processing
    system;
> - the mechanism by which C programs are invoked for use by a data-processing
    system;
> ...

This basically means that the standard neither says how source is turned into an executable nor how this executable is
actually run on a computer. Therefore, the term "C ABI" is actually misleading, suggesting that there is a common
ruleset per platform and any program part that obeys this "C ABI" will work flawlessly when linked.

While the C language standard doesn't define the entire ABI, it does impose some restrictions on the ABI, e.g.

* The in-memory order of members of a struct is as declared in the struct's definition.
* The first member of a struct is located at the start of the struct - no padding at the beginning is allowed.
* For all basic types, there are minimal value ranges they need to support.

The C standard intentionally leaves a lot of other properties of an ABI open and the compiler is free to choose them so
that they leverage the full potential of the hardware the program is going to be executed on.

This also means that the exact properties of the ABI are not only influenced by the hardware architecture, but also by
tradeoffs developers choose when compiling: Some compilers allow to influence the ABI by various compiler switches that
change the ABI to generate programs that are heavily optimized by changing the ABI in a way that favors speed over
compatibility or memory consumption. On some architectures, one can change the data layout of certain basic types, e.g.
the definition of `long double` on x86, which can either be equal to a regular double, or an 80 bit x87 type, or a 128
bit type.

The bottom line is that all compilers that are involved in compiling a program need to be configured so that *each
single property* is the exact same. This is obviously also true for Rust, and just specifying `repr(C)` and a suitable
declaration of a struct is not enough. Instead, the correct target triple has to be chosen, and both the Rust compiler
and the C compiler used to compile a program part using that same struct needs to be configured such that the ABI
matches the ABI that is defined by the target triple that has been configured for the Rust crate.

## FFI in Rust

The basic building block of Rust's FFI is the support for (almost? check whether there are gaps) the whole set of the
interaction mechanics the C language offers. The major building blocks are

* The provisioning of basic data types that are compatible across language boundaries.
* Describing complex data types by means of structures, arrays and unions of other complex types or basic data types.
* Calling a subroutine with a set of parameters and at most one return value.
* Offering functions that can be called by foreign languages.
* Accessing global memory defined (and possibly initialized) by a foreign language.

All other language building blocks supported by either language need to be projected onto these building blocks.

The following sections briefly describe these building blocks. For more details one can follow the references.

### Basic data types and FFI

A lot of Rust's basic data types (especially integral types) have corresponding types in C. However, there is no direct
and universal match of Rust's basic types to C's basic types. Instead, it is a good idea to use type aliases that exist
on each side. This is a type mapping list that universally works on all platforms:

| Rust type               | C type               |
|-------------------------|----------------------|
| `u8`                    | `uint8_t`            |
| `i8`                    | `int8_t`             |
| `u16`                   | `uint16_t`           |
| `i16`                   | `int16_t`            |
| `u32`                   | `uint32_t`           |
| `i32`                   | `int32_t`            |
| `u64`                   | `uint64_t`           |
| `i64`                   | `int64_t`            |
| `std::ffi::c_char`      | `char`               |
| `std::ffi::c_schar`     | `signed char`        |
| `std::ffi::c_uchar`     | `unsigned char`      |
| `std::ffi::c_int`       | `(signed) int`       |
| `std::ffi::c_uint`      | `unsigned int`       |
| `std::ffi::c_short`     | `(signed) short`     |
| `std::ffi::c_ushort`    | `unsigned short`     |
| `std::ffi::c_long`      | `(signed) long`      |
| `std::ffi::c_ulong`     | `unsigned long`      |
| `std::ffi::c_longlong`  | `(signed) long long` |
| `std::ffi::c_ulonglong` | `unsigned long long` |
| `std::ffi::c_double`    | `double`             |
| `std::ffi::c_float`     | `float`              |

Pointers are guaranteed to be compatible. There's a slight gotcha, though: It is legal in Rust to create so-called fat
pointers. This happens if you create a pointer to a slice or a trait object, since both entities need more than just a
pointer to the start of the data. However, the Rust compiler will warn in case such a pointer is used on an FFI
boundary.

### Complex types

Rust (like the majority of other languages) allows for combining basic datatypes to complex datatypes in various ways.
A subset thereof can also be used across language boundaries. This is true for arrays, structs and unions. Arrays and
structs are declared just like the native Rust counterpart with an added `#repr(C)` annotation. Unions are less common
in normal Rust code since they do not store which variant is used a a particular moment which makes them difficult to
use due to the unsafe blocks needed to read from them. However, some C APIs do contain unions so that they also have to
be used on Rust side. Notice that they still need to be annotated with `repr(C)`, despite their C-heavy usage:

```rust
#[repr(C)]
union JsonValue {
    integer: std::ffi::c_int,
    float: std::ffi::c_double,
    string: *const std::ffi::c_char,
}
```

Contrary to these data types, enums and tuples cannot be used and doing so will lead to a compiler warning:

```rust
#[repr(C)]
struct X {
    t: (u32, u32),
}

unsafe extern {
    fn test(x: *mut X);
}
```
leads to
```
warning: `extern` block uses type `(u32, u32)`, which is not FFI-safe
  --> src/main.rs:7:21
   |
 7 |     fn test(x: *mut X);
   |                ^^^^^^ not FFI-safe
   |
   = help: consider using a struct instead
   = note: tuples have unspecified layout
   = note: `#[warn(improper_ctypes)]` on by default
```

When defining types that are used across the language boundary it is of utmost importance to define the same type with
the exact same layout as in the other language. Failing to do so will inevitably lead to data corruption and undefined
behavior.

Although data definitions can be a potential source of undefined behavior, they are _not_ marked `unsafe` since the
definitions themselves do not cause undefined behavior. The actual trigger for such undefined behavior is in fact a
`extern` function definition or global variable definition, respectively: If such objects reference a data definition
that does not fit the definition of the data type in the foreign language, such a type usage acts like an unchecked,
unsafe type cast. Since the compiler cannot check type consistency across languages, these items need to be marked
`unsafe`:

```c
struct X {
    uint64_t val;
};

X EXPORTED_DATA = { 17 };
```

```rust
// Not unsafe, although the definition does not match the type in C with the same name.
#[repr(C)]
struct X {
    val: u32,
}

// This, however, needs to be unsafe since we now import an external definition and the compiler cannot check whether
// the type definitions match:
unsafe extern "C" {
    static EXPORTED_DATA: X;
}

fn main() {
    unsafe {
        println!("{}", EXPORTED_DATA.val);
    }
}
```

### Calling subroutines from Rust

When one wants to call a subroutine that is implemented by a foreign language, this subroutine has to be declared in an
`extern` block. A simple example of such a block looks like this (2024 edition):

```rust
unsafe extern "C" {
    fn externally_defined_routine(arg1: u32, arg2: *mut Complex) -> bool;
}
```

Since the Rust compiler cannot check whether the signature of the declaration matches the declaration of the subroutine
on the foreign language, the whole `extern` block is marked as unsafe (Note: The `unsafe` keyword was optional in older
editions but doesn't change the semantics of subroutine declarations in the `extern` block).

Calling such a subroutine almost works like calling an ordinary function. However, since the Rust compiler cannot know
whether the called subroutine violates any of the Rust safety guarantees, calling an external subroutine also needs to
be wrapped in an `unsafe` block by default, like this:

```rust
let mut complex = Complex { ... };
let success = unsafe {
    externally_defined_routine(24, &mut complex)
};
...
```

You can, however, explicitly declare an external function declaration as `safe`, in which case you can call this
function just like an ordinary Rust function. This makes sense if there is no parameter combination that triggers
undefined behavior in the foreign subroutine; it is therefore advisable to only do this if there is no parameter that,
by definition, cannot be checked for its validity, e.g. pointers. Since the compiler cannot verify this, it is only
allowed to put the `safe` qualifier inside an `unsafe` external block and the developer is obligated to check for the
absence of any unsafe behavior on certain input parameters. Such a declaration then looks like this:

```rust
unsafe extern "C" {
    safe fn simple_callable(data: u32) -> bool;
}

// ...

fn some_function(val: u32) {
    // No `unsafe` required here!
    if simple_callable(val) {
        // ...
    }
}
```

If we assume that this function is defined for any value of its input parameters (which is something that the developer
has to manually validate!), then it can be declared as `safe` and no `unsafe` block is needed when using it.

Notice that the Rust compiler also checks whether the subroutine signature is compatible with the C language. If a type
is used which is not supported by C, the Rust compiler emits a warning. It is strongly advised to rework the signature
if such an `improper_ctype` warning (see [Complex types](#complex-types)) appears as the chances for undefined behavior
are high. And even if the program works in a particular version of Rust, this might change any time the memory layout
of such a type changes due to the updated Rust version changing Rust's native ABI, which is at the time of this writing
not stable.

While this (and following) chapter usually mean `extern "C"` when talking about external linkage, there are also
other calling conventions that sometimes are used as an alternative to the "standard" C calling convention for a certain
triple. While these calling conventions are equivalent feature-wise, they emphasize a different optimization target by
changing aspects like how parameters are being transferred to the subroutine and who is dong the cleanup of the stack.
Examples are the x86 "fastcall" or "stdcall" calling conventions. Usually, these calling conventions also have to be
explicitly set also on the C or C++ side. While it is optional to specify the calling convention when declaring a
function as external and "C" is the default calling convention when omitted, it is recommended to always specify the
calling convention explicitly so that it's always clear which convention is used on a specific declaration or
definition.

### Offering subroutines to a foreign language

Strictly speaking, this is not really a thing for the Learn Unsafe Rust endeavour since offering a callable over the
foreign function interface is not unsafe by itself since the Rust compiler can prove the absence of unsafe code _inside_
Rust code just fine. However, this does not mean that you cannot cause undefined behavior here in the same way this
happens also for the other direction: If the signatures are not compatible, this will almost ineviatably lead to
misinterpretation of data and undefined behavior. But since the cause is not on Rust's side, there is no need to mark
such functions as `unsafe`:

Rust side:
```rust
#[repr(C)]
struct SampleType {
    ...
}

#[no_mangle]
extern "C" callable_from_the_outside(val: &SampleType)
{
    ...
}
```

C side:
```c
struct SampleType {
    ...
};

void callable_from_the_outside(const char* val);

int main()
{
    callable_from_the_outside("Hello, Undefined Behavior!");
}
```

`const char*` has the same size and layout as a Rust reference since pointers and Rust references have the same layout
(see [the reference](https://doc.rust-lang.org/reference/type-layout.html#r-layout.pointer.intro)). Since (thin)
pointers in C and Rust always have the same size and layout no matter what the pointed-to type is, this will be
compatible layout-wise. However, Rust expects a struct whereas this example will call the function with an arbitrary
string which invokes undefined behavior due to the incompatible pointed-to type.

### Shared static data

It is also possible to use static data that has been defined by program parts that have been written in another
language. Such data is also declared inside an `extern` block, just like foreign functions. However, since they're
externally defined, they do not need an initializer as it is the responsibility of the foreign translation unit to
initialize statics before the execution of the program's entry point. Since the compiler cannot verify whether the data
type definition fits the one from the foreign language, any access to such a static variable is unsafe by default. Just
like with foreign subroutine, you can also declare such a variable as `safe` so that you can access it just like a Rust
static variable.

Notice that Rust requires static data to be initialized before _any_ Rust code runs. This is typically fine since any
static data will, in usual environments, be initialized by code that runs before the actual `main` function is called.
For C, this is true even if the static does not have an explicit initializer. In this case, the memory is zeroed.

## Appendix

### References

[^1]: [ISO/IEC 9899:2024 "Information technology - programming languages - C"](https://www.iso.org/standard/82075.html)
