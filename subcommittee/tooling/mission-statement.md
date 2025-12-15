# Mission Statement - Tooling Subcommittee

1. Aggregate community-vetted minimal required tooling package to be able to certify Rust in safety-critical applications.
2. Provide and maintain a document with a list of the minimal required tools and their development status.
3. Possibly develop a curricula used for training in safety critical Rust (this is still te be determined of we need a different subcommittee for it).

## State of Rust Safety-Critical Tooling

| Need ID | Minimum Relevant Standard Rule | Tools | Notes |
|---------|--------------------------------|-------|-------|
| DC Coverage | ASIL-D, DAL-B | llvm (19, rustc 1.82) | - unstable, no macros / pattern matching  |
| MC Coverage | ASIL-C. DAL-A | llvm (19, rustc 1.82) | - AdaCore report generator plans to stabilize the feature by end of 2025 <br> - unstable, no macros / pattern matching |
| Statement Coverage | ASIL-A, DAL-C | llvm (19, rustc 1.82), [cargo-tarpaulin](https://github.com/xd009642/tarpaulin) | - unstable, no macros / pattern matching  |
| Function coverage | ASIL-C, DAL-C | llvm (19, rustc 1.82) - unstable, no macros / pattern matching, [cargo-tarpaulin](https://github.com/xd009642/tarpaulin) |
| Call coverage | ASIL-C, DAL-C | llvm (19, rustc 1.82), [cargo-tarpaulin](https://github.com/xd009642/tarpaulin) | - unstable, no macros / pattern matching |
| Branch Coverage | ASIL-B, DAL-C | llvm (19, rustc 1.82), [cargo-tarpaulin](https://github.com/xd009642/tarpaulin) | - unstable, no macros / pattern matching |
| Qualified Compiler | ASIL-D, DAL-D  | ferroccene, Ada Core |
| Fault Injection Tests | ASIL-D, DAL-D | N/A | |
| Test Coverage | ASIL-, DAL-D | llvm (19), cargo-test, [mantra?](https://crates.io/crates/mantra) | |
| Underfined Behaviour Absence | ASIL-A, DAL-C | ensured by static analysis and source code confirmity |
| Static Analysis Tools | DAL-C | | - make sure coding guidelines specify some rules, probably similar to Polyspace, <br> - an assessment about what the rust compiler covers is necessary <br> - for DO-178 such tools support the *source code conformity* objective |
| Unambiguous Graphical Representation | ASIL-B | UML like too, but for Rust, AUTOSAR suggests - [Explanation of ARA Applications in Rust](https://www.autosar.org/fileadmin/standards/R23-11/AP/AUTOSAR_AP_EXP_ARARustApplications.pdf) |
| Formal Verification | ASIL-C (recommended), DAL-C (recommended) | - [verifast](https://github.com/verifast/verifast) WIP <br> - [creusot](https://github.com/creusot-rs/creusot) WIP, works only for safe rust <br> - gillian-creusot WIP, not in a usable state, works for unsafe rust, [kani](https://model-checking.github.io/kani/) | - prove absence of UB <br> - prove that the code does what it should do <br> - using some spec (different language, eg SPARC or CodeProver, prove that an output is not possible) |
| Code Metrics - Cyclomatic Complexity | DAL-C | clippy - knows some sort of estimation as it complains if a function is too long. | - DO-178 linked to source code conformity - tightly linked the code guidelines <br> - Ada Core has a tool on the roadmap eventually  |
| Code Traceability | DO-178 TBD | [mantra](https://crates.io/crates/mantra) - uses code annotation | |
| Use of naming convention | ASIL-A | Clippy | Not available tool that allow to define and enforce naming convention. Clippy check only for predefined and generic naming convention |
| Measurement of execution time and reaction time of software unit | ASIL-A (depends in the requirements) | perf, Intel VTune, flamegraph, [Rapita](https://www.adacore.com/press/rapita-systems-showcases-adacores-gnat-pro-for-rust-at-hisc) | For hard realtime application are required not intrusive profiler that are typically HW specific |
| Test runner | all | - [cargo-nextest](https://nexte.st) <br> - cargo <br> - defmt-test + probe.rs | No ISO qualified tool are available. Example of qualified test runner: [VectorCast](https://www.vector.com/us/en/products/products-a-z/software/vectorcast/?gad_source=1&gclid=EAIaIQobChMIyMKCgvn3igMVM0-RBR1s9BOkEAAYASAAEgJM2_D_BwE#c336977),  [TESSY](https://www.razorcat.com/en/product-tessy.html) <br> - tightly linked to the coverage level |
| Automatic generation of unit/integration tests based on equivalence classes and boundary values | ASIL-B | | Example of automatic test generator based on equivalence classe and boundary values: [VectorCast](https://www.vector.com/us/en/products/products-a-z/software/vectorcast/?gad_source=1&gclid=EAIaIQobChMIyMKCgvn3igMVM0-RBR1s9BOkEAAYASAAEgJM2_D_BwE#c336977),  [TESSY](https://www.razorcat.com/en/product-tessy.html) |

## Standards Used

- Automotive: ISO-26262 (ASIL)
- Aerospace: DO-178 (DAL)
