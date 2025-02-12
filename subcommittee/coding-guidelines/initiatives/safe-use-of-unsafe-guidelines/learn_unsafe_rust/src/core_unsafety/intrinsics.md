
# Intrinsics

Rust provides a set of compiler intrinsics as part of `core` and `std` respectively (https://doc.rust-lang.org/std/intrinsics/index.html).

Most of them are marked as experimental, unstable and useable in nightly versions of the compiler.

For many, there is already stabilized API available.

Thus, the clear recommendation is not using the experimental compiler intrinsics in a safety-critical project.

There are only few functions that are not marked as experimental: `copy`, `copy_nonoverlapping`, `write_bytes`, `transmute`.
`transmute` is probably the most well-known and widely used of these APIs.
`transmute` is handled in other parts of the guidelines.

