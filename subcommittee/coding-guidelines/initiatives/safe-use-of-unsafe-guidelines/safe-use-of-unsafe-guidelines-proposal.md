# Safe Use of Unsafe Guidelines Proposal

## Motivation

By default, Rust is a safe programming language. Outside of  `unsafe`,  Rust programs do not have undefined behavior or invalid memory access.

There are reasonable use cases to use the `unsafe` keyword such as:

* interop through Rust’s C FFI  
* complex safety invariants that cannot be verified by the Rust compiler

Currently, no public document on safely developing unsafe code exists. `unsafe` coding and review guidelines will aid teams, ensuring they are able to uphold Rust’s invariants when using `unsafe`. Those guidelines should be useful for all industries.

## Mission

We aim for the publish of the following to the entire Rust community, regardless of safety-criticality:

1. `unsafe` Rust coding guidelines  
2. `unsafe` Rust review guidance

### `unsafe` Rust coding guidelines

The coding guidelines should:

* prevent the introduction of memory-unsafety  
* inform code linters and tools  
* be analyzable (to the extent possible)  
* be customizable towards end users’ needs, similar to other coding guidelines.

### `unsafe` Rust review guidance

The review practice guidance should:

* Be usable during code review to allow catching of `unsafe` misuse  
* Teach and guide teams on how to set up unsafe review workflows

## Proposal

Our proposal is:

1. Collaboration with an engineer that has worked with `unsafe` Rust, reviewed, and documented review guidance.  
2. Base it on the Ferrocene spec first, as this is the document with the most mindshare in the safety critical working group.  
3. Research if any of the companies with internal guidelines are willing to donate them as an initial starting point.

## Previous work

The Rust project has produced the unsafe code guidelines reference, which is mainly a collection of facts about unsafe, not a guide. This document is a useful input into any planned effort \[1\].

The Rust project has also produced the Rustonomicon, which goes at some places into unsafe capabilities, particularly around FFI, but is not focused on practical guidelines \[2\].

SAE International’s JA1020 (WIP) is also ongoing work in this space \[3\].

\[1\]: [https://rust-lang.github.io/unsafe-code-guidelines/](https://rust-lang.github.io/unsafe-code-guidelines/)  
\[2\]: [https://doc.rust-lang.org/nomicon/](https://doc.rust-lang.org/nomicon/)  
\[3\]: [https://www.sae.org/standards/content/ja1020/](https://www.sae.org/standards/content/ja1020/)  

