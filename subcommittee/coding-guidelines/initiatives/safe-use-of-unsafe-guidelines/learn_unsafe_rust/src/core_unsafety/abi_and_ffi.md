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
