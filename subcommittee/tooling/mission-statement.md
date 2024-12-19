# Mission Statement - Tooling Subcommittee

1. Aggregate community-vetted minimal required tooling package to be able to certify Rust in safety-critical applications.
2. Provide and maintain a document with a list of the minimal required tools and their development status.
3. Possibly develop a curricula used for training in safety critical Rust (this is still te be determined of we need a different subcommittee for it).

## State of Rust Safety-Critical Tooling

| Purpose | Requirement | Tool | Status |
|---------|-------------|------|--------|
| Qualified Compiler | ? | [Ferrocene](https://ferrocene.dev/en/) | Available for `aarch64-nostd` |
| Certified Core Library | SIL-4 / ASIL-D out of context | N/A | In progress by Ferrocene / Adacore / HighTec |
| Coding Style Verification | MISRA-C, ... | Rust Compiler, Clippy and probably additional tools required to verify and evaluate the application of the coding standard developed by the Code Guidelines Subcommittee | OxidOS can provide a mapping of MISRA-C Rules to the Rust Compiler |
| MC/DC Coverage report | ... | N/A | not available - LLVM might provide some tools |
| Static Analysis Tools | probably similar to Polyspace | N/A | an assesement about what the rust compiler covers is necessary |
| Code Metrics Generator | Cyclomatic Complexity, ... | N/A | not available |
