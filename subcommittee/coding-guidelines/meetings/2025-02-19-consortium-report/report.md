# Safety-Critical Rust Consortium Report from Coding Guidelines Subcommittee

Date: Feb 19, 2025

Location: London, UK

_Note_: This is a coding guidelines-specific report out from our group. For more detailed, consortium-wide notes please see these excellent [notes and summary](https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/meetings/19-February-2025).

# Executive Summary

Many folks in industry have existing coding guidelines, but many are waiting to be unblocked by having some open coding guidelines available. Clear mandate for a prioritization of coding guidelines above all other activities on-going and planned. Guidance is that someone in the consortium or we as a subcommittee should have a baseline document for coding guidelines into which other organizations can contribute (this tends to be more permitted by organizations, instead of contributing documents wholesale.) Interest was shown by organizations to help contribute to such a baseline document.

# Status Prior to Consortium

Subcommittee has worked on fleshing out Learn unsafe Rust as a means to work together in a structured fashion. We have some material together that can form the start of some chapters.

# Prioritized List of Activities for Group

We came out of the consortium meeting with a clear mandate for prioritization of work in the following fashion:

| Activity                                                             | Priority (P0 = higher, P3 = lower) | Rationale                                                                                                                                      |
|----------------------------------------------------------------------|------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Coding Guidelines                                                    | P0                                 | Blocker for some organizations to adoption                                                                                                     |
| Coding Guidelines Standards Matrix and Rationale                     | P0                                 | Blocker for some organizations to adoption                                                                                                     |
| Review and consider use case for MISRA draft of guidelines for Rust  | P0                                 | Existing material in draft status can be a good starting point for many organizations                                                          |
| Useful safe patterns, e.g. compile-time deadlock prevention          | P1                                 | Practical ways to make Rust code more suitable to safety-critical are great to share                                                           |
| “Decoder ring” pamphlet between safety-critical and Rust communities | P2                                 | “Safe” between safety-critical and Rust can mean different things and can lead to confusion                                                    |
| How-to on edge cases, e.g. C++ exceptions over FFI, panic unwinding  | P3                                 | Less (or not) documented issues that may come up and be challenging to solve if unaware                                                        |
| Learn unsafe Rust contributions                                      | P3                                 | Useful hands-on material to use if stuck in an edge case where unsafe is needed. Unsafe comes up fairly often in safety-critical and embedded. |
# Action Items

The below action items came out of our discussions. Marking these as all the responsibility of Pete LeVasseur to either complete or delegate.

* Stay current on and try to attend Tooling Subcommittee to stay in alignment as they are our customer  
* Organize our work in GitHub with tracking issues for our large goals, break work out, and flesh out project board to make contributing easier  
* Revise mission statement based on discussions to better reflect priorities  
* Follow up to have more examples of challenging edge cases that are relevant for safety-critical  
* Find those items we may need support on from the Rust Project before RustWeek
