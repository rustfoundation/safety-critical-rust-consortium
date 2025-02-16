# Meeting 07.02.2025

## Participants
- Tony Aiello (AdaCore)
- Sasha Pourcelot (Trust-in-Soft)
- Oreste Bernardi (Infineon)
- Joe Johnson (Modularity)
- Arnaud Fontaine (Airbus)
- Julius Gustavson (Volvo Cars)
- Alexandru Radovici (Moderator)

## Requirements Matrix

We decided to fill the *Needs to Standards* mapping asynchronously
using GitHub comments until the next meeting. The matrix is now published in https://github.com/rustfoundation/safety-critical-rust-consortium/pull/175.

### Notes
- we would talk to the coding standard team for metrics (RustNation topic)
    - safe/unsafe
- how do we handle macros - discussion with the coding standards team (RustNation topic)
    - there is some work in the rust upstream - cargo-expand
- "undefined behavior" is to be used carefully for Rust because there is a difference between UB in Rust and UB in C, e.g. [for interger overflows](https://github.com/rust-lang/rfcs/blob/master/text/0560-integer-overflow.md). Definition of [undefined behavior for Rust](https://doc.rust-lang.org/reference/behavior-considered-undefined.html) and [what is excluded](https://doc.rust-lang.org/reference/behavior-not-considered-unsafe.html#integer-overflow) which is to be related to the C sense of UB.
    - will be addressed by the coding guidelines subcommittee

Aerospace DO-178
Automotive ISO26262

## Open topics
- To be aligned to Coding Guidelines (CG)
- Do we need static analysis for DAL-D and DAL-E?
- *Format Verification* needs to be refined at some point
- *Code Traceability* needs to be refined for DO-178

### Initial proposal

This table contains the inital proposal that we had before the meeting and that we did not copy to the output table.

| Purpose | Requirement | Tool | Status |
|---------|-------------|------|--------|
| Qualified Compiler | ? | [Ferrocene](https://ferrocene.dev/en/) | Available for `aarch64-nostd` |
| Certified Core Library | SIL-4 / ASIL-D out of context | N/A | In progress by Ferrocene / Adacore / HighTec |
| Coding Style Verification | MISRA-C, ... | Rust Compiler, Clippy and probably additional tools required to verify and evaluate the application of the coding standard developed by the Code Guidelines Subcommittee | OxidOS can provide a mapping of MISRA-C Rules to the Rust Compiler |
| Static Analysis Tools | probably similar to Polyspace | N/A | an assesement about what the rust compiler covers is necessary |
|Unambiguous graphical representation|ISO26262 ASIL B/C/D | N/A | Graphical representation specific not available. Autosar Rust defined a Enterprise Architect profile See chapter 6.6 of [Explanation of ARA Applications in Rust](https://www.autosar.org/fileadmin/standards/R23-11/AP/AUTOSAR_AP_EXP_ARARustApplications.pdf)|
|Use of naming convention| ISO26262 ASIL A/B/C/D | Clippy | Not available tool that allow to define and enforce naming convention. Clippy check only for predefined and generic naming convention |
|Measurement of execution time and reaction time of software unit| ISO 26262 6.4.2 e) | perf, Intel VTune, flamegraph, [Rapita](https://www.adacore.com/press/rapita-systems-showcases-adacores-gnat-pro-for-rust-at-hisc) |  For hard realtime application are required not intrusive profiler that are typically HW specific |
| Test runner | all | cargo-nextest, cargo, defmt-test+probe.rs | No ISO qualified tool are available. Example of qualified test runner: [VectorCast](https://www.vector.com/us/en/products/products-a-z/software/vectorcast/?gad_source=1&gclid=EAIaIQobChMIyMKCgvn3igMVM0-RBR1s9BOkEAAYASAAEgJM2_D_BwE#c336977),  [TESSY](https://www.razorcat.com/en/product-tessy.html)|
| Automatic generation of unit/integration tests based on equivalence classes and boundary values | ISO26262 Part 6 (9.4.4 & 10.4.4) ASIL B/C/D | N/A | Example of automatic test generator based on equivalence classe and boundary values: [VectorCast](https://www.vector.com/us/en/products/products-a-z/software/vectorcast/?gad_source=1&gclid=EAIaIQobChMIyMKCgvn3igMVM0-RBR1s9BOkEAAYASAAEgJM2_D_BwE#c336977),  [TESSY](https://www.razorcat.com/en/product-tessy.html) |


## Next Meeting

At Rust Nation - 19.02.2025
- please clarify the objective of this group
    - is it to help the tool vendor?
- Arnaud can create meeting links if necessary

## Presentations of interests
- Rust in avionics https://aviose-workshop.github.io/#program
- Eclipse SDV https://www.automotive-oss.org/event/d8cae729-ea4c-4a9a-8bb4-a42ab995e055/summary
