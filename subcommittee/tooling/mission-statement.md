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
|Statement Coverage| ISO26262 Part6 9.4.5 ASIL A/B | | |
|Function coverage| ISO26262 Part 6 10.4.6 ASIL C/D | | |
|Call coverage| ISO26262 Part 6 10.4.6 ASIL C/D | | |
|Branch Coverage | ISO26262 Part6 9.4.5 ASIL B/C/D | | | 
| MC/DC Coverage report | ISO26262 Part6 9.4.5 ASIL D | N/A | not available - LLVM might provide some tools |
| Static Analysis Tools | probably similar to Polyspace | N/A | an assesement about what the rust compiler covers is necessary |
| Code Metrics Generator | Cyclomatic Complexity, ... | N/A | not available |
|Unambiguous graphical representation|ISO26262 ASIL B/C/D | N/A | Graphical representation specific not available. Autosar Rust defined a Enterprise Architect profile See chapter 6.6 of [Explanation of ARA Applications in Rust](https://www.autosar.org/fileadmin/standards/R23-11/AP/AUTOSAR_AP_EXP_ARARustApplications.pdf)|
|Use of naming convention| ISO26262 ASIL A/B/C/D | Clippy | Not available tool that allow to define and enforce naming convention. Clippy check only for predefined and generic naming convention |
|Measurement of execution time and reaction time of software unit| ISO 26262 6.4.2 e) | perf, Intel VTune, flamegraph, [Rapita](https://www.adacore.com/press/rapita-systems-showcases-adacores-gnat-pro-for-rust-at-hisc) |  For hard realtime application are required not intrusive profiler that are typically HW specific |
| Test runner | all | cargo-nextest, cargo, defmt-test+probe.rs | No ISO qualified tool are available. Example of qualified test runner: [VectorCast](https://www.vector.com/us/en/products/products-a-z/software/vectorcast/?gad_source=1&gclid=EAIaIQobChMIyMKCgvn3igMVM0-RBR1s9BOkEAAYASAAEgJM2_D_BwE#c336977),  [TESSY](https://www.razorcat.com/en/product-tessy.html)|
| Automatic generation of unit/integration tests based on equivalence classes and boundary values | ISO26262 Part 6 (9.4.4 & 10.4.4) ASIL B/C/D | N/A | Example of automatic test generator based on equivalence classe and boundary values: [VectorCast](https://www.vector.com/us/en/products/products-a-z/software/vectorcast/?gad_source=1&gclid=EAIaIQobChMIyMKCgvn3igMVM0-RBR1s9BOkEAAYASAAEgJM2_D_BwE#c336977),  [TESSY](https://www.razorcat.com/en/product-tessy.html) |
Fault injection test | ISO26262 Part 6 (9.4.2 ASIL D, 10.4.2 ASIL C/D) | [mutagen](https://github.com/llogiq/mutagen), [cargo-mutants] (https://mutants.rs/) | No ISO qualified tools available |
Requirement based test | ISO 26262 Part 6 (9.4.2 & 10.4.2 ASIL A/B/C/D) | [mantra](https://crates.io/crates/mantra) | No ISO qualified tool available |




