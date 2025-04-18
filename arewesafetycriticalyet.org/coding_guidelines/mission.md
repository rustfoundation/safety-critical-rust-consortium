# Mission Statement

Develop a community-vetted coding guideline for Rust in safety-critical applications. A living document that is updated as features are added to Rust and we learn more by doing.

The following are relevant safety-critical coding guidelines. We are also interested in adopting knowledge obtained that may currently be in company-specific documents and incorporating these into the coding guideline.

## State of Rust Safety-Critical Coding Guidelines

### SAE: SAfEr Rust Task Force

An effort led out of [SAE](https://www.sae.org/) titled the [SAfEr Rust Task Force](https://standardsworks.sae.org/standards-committees/safer-rust-task-force) has the following mission statement:

> Rust is a new programming language which combines high run time efficiency and modern design patterns with rigorous compile time checks.The scope of the task force will be to document best practices for the use of Rust that can be applied to Safety-Related Systems development.The scope will not include repetition of existing guidelines, but will summarize and point to them; if existing guidelines differ from this document, these will be noted.Objectives of this task force will be to: 1. Evaluate the Rust ecosystem to identify a Safer subset of Rust. 2. Develop guidelines with respect to the Rust subset for: a. Integrating Rust into automotive and aerospace safety-related applications b. Avoiding programming mistakes and failures that could lead to hazards, and c. Increasing confidence in its use in the automotive and aerospace industry 3. Document evidence to support the guidelines, and to 4. Provide general recommendations for the use of Rust to support safety and cybersecurity.

There is a draft version of these recommendations available [here](https://www.sae.org/standards/content/ja1020/) as JA1020. Because it is a draft, it's not viewable unless you join the SAfEr Rust Task Force as an SAE member.

### AUTOSAR Foundation: Working Group for Functional Safety (WG-SAF)

An effort led out of the [AUTOSAR Foundation](https://www.autosar.org/) titled the [Working Group for Functional Safety (WG-SAF)](https://www.autosar.org/news-events/detail?tx_news_pi1%5Baction%5D=detail&tx_news_pi1%5Bcontroller%5D=News&tx_news_pi1%5Bnews%5D=139&cHash=b332c8babc7aad27723ab939f9723fc6) has the following mission statement:

> [...] The decision to form a subgroup within the Working Group for Functional Safety (WG-SAF) is a consequence. The subgroup will officially get started on April 2022 and plans to produce two documents. One of the documents will be providing guidance on how Rust can be utilized in the context of AUTOSAR Adaptive Platform projects. The other document will propose Coding Guidelines on Rust.

An outcome of this working group is the [Explanation of ARA Applications in Rust](https://www.autosar.org/fileadmin/standards/R23-11/AP/AUTOSAR_AP_EXP_ARARustApplications.pdf) document which outlines the API which can be used to write Rust applications within an Adaptive AUTOSAR environment.

## Other Safety-Critial Guidelines

### MISRA C, C++

[MISRA](https://misra.org.uk/) creates rules for usage of C and C++ in safety-critical systems.

There was an [effort](https://github.com/PolySync/misra-rust/blob/master/MISRA-Rules.md) taken to identify which MISRA C rules are enforceable, not enforceable, or not applicable when using Rust.

## Existing Guidelines (currently not public)

We would like to put out a request for those that have used Rust in safety-critical applications, may be familiar with `unsafe` best practices, or otherwise feel they have guidelines or experience to contribute to please reach out to us!

As we adopt pieces of these documents we can keep track of contribution provenance here.

