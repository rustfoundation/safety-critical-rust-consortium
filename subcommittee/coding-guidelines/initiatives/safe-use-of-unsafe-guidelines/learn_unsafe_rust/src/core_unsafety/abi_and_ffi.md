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
the ABI that supports the technology isn't usually supported well - or not at all.

It is usually the task of the linker to collect the bits of a program and merge it into an executable. This will only
result in a working program if all parts of the program agree on the same ABI. If there are ABI incompatibilities, this
will usually lead to trouble during program execution, like data corruption or crashes.

## About the "C ABI"

When you're looking for information about linking parts of a program (potentially written in different languages) on the
internet, one often comes across the term "C ABI". Due to the vast amount of code written in C, the language became a de
facto standard for compatibility on various levels. That's also the reason why you find that term in Rust source, like
`repr(C)` or `extern "C"`. However, the C language itself does not define an ABI. Therefore, the term "C ABI" is
actually misleading, suggesting that there is a common ruleset per platform and any program part that obeys this "C ABI"
will work flawlessly when linked.

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

| Rust type             | C type             |
|-----------------------|--------------------|
| u8                    | uint8_t            |
| i8                    | int8_t             |
| u16                   | uint16_t           |
| i16                   | int16_t            |
| u32                   | uint32_t           |
| i32                   | int32_t            |
| u64                   | uint64_t           |
| i64                   | int64_t            |
| std::ffi::c_char      | char               |
| std::ffi::c_schar     | signed char        |
| std::ffi::c_uchar     | unsigned char      |
| std::ffi::c_int       | (signed) int       |
| std::ffi::c_uint      | unsigned int       |
| std::ffi::c_short     | (signed) short     |
| std::ffi::c_ushort    | unsigned short     |
| std::ffi::c_long      | (signed) long      |
| std::ffi::c_ulong     | unsigned long      |
| std::ffi::c_longlong  | (signed) long long |
| std::ffi::c_ulonglong | unsigned long long |
| std::ffi::c_double    | double             |
| std::ffi::c_float     | float              |

Pointers are guaranteed to be compatible. There's a slight gotcha, though: It is legal in Rust to create so-called fat
pointers. This happens if you create a pointer to a slice or a trait object, since both entities need more than just a
pointer to the start of the data. However, the Rust compiler will warn in case such a pointer is used on an FFI
boundary.

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
be wrapped in an `unsafe` block, like this:

```rust
let mut complex = Complex { ... };
let success = unsafe {
    externally_defined_routine(24, &mut complex)
};
...
```

Notice that the Rust compiler also checks whether the subroutine signature is compatible with the C language. If a type
is used which is not supported by C and warns in such a case. It is strongly advisable to rework the signature if such
an `improper_ctype` warning appears as the chances for undefined behavior are high, and even if the program works in
a particular version of Rust, this might change any time in case the memory layout of such a type changes due to the
updated Rust version.