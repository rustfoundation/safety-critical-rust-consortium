# Meeting 29.11.2024

## Attendees
- Arnaud Fontaine (Airbus)
- Bogdan Genis (OxidOS)
- Julius Gustavson (Volvo Cars)
- Tiago Manczak
- Sasha Pourcelot (Trust in Soft)
- Alexandru Radovici (Rust Foundation)

## Subjects
The main discussion of the meeting was to prioritize the software/tools needs. The main
action points are:

- define an equivalence table for mapping the safety critical standards (ASIL, SIL, DO) into several levels
- adjust the priority of each tool based on this table
- the main idea is to define and prioritize the needed tools using a bottom up approach from the less strict strandard to the highest standard.

The objective that we have set for the next meeting is to be able to finalize a provisional list of tools arranged in
the right priority. We would like to categorize the tools depending on the safety standard using a bottom-up approach.

## Needs (by priority)
This is the provisional order of tools priority that the group has defined so far. They are sorted in
the descending order of priority, 1 being most important and 11 the least important.

1. Report generating tools (eg: you can't get reports from clippy)
    - there is a standard for this (https://docs.oasis-open.org/sarif/sarif/v2.1.0/sarif-v2.1.0.html)
    - clippy crate (https://psastras.github.io/sarif-rs/)
2. Coding standard verifier (Rust helps a lot here)
3. Requirement tracability tools
    - https://github.com/mhatzl/mantra (https://community.infineon.com/t5/Blogs/Requirements-Traceability-with-mantra/ba-p/864822)
4. Software supply verification
    - what is being shipped in the product
    - what is used to build the product
5. SBOM generation
    - what is being shipped in the product
    - what is used to build the product
6. Source code to obj code tracing - connect the code to the binary
7. coverage tools tools
    - no-std and std
    - branch and statement tools
    - MC/DC
8. Tools do deal with unsafe code - verify it does not break the invariants
9. Defect management (if a comp version has some defect, used for recalls)
10. Worst Case Execution Time (WCET)
11. Runtime Profiler - relates to WCET - prove critical time is properly addressed
    - speed of execution
    - memory usage
    - visualization tool for flame graphs

## Standads Mapping
The following table maps several standards to Rust-Safety-Levels (RSL). Level 1 is to be considered
the less strict, while level 5 is to be considered the one with the most safety requirements.

> This is just a draft, I have mapped some of the standards to the best of my knowledge.
> Please do **send several comments** so we can fill out the table before our next
> meeting.
> The *Required Tools* column is not to be filled in now, it is just there to set the expectation of the tools list.

| | Description | Automotive | Industrial | Aerospace | Medical | Required Tools |
|---|---|---|---|---|---|---|
| RSL-1 | Least Requirements | QM | ? |  |   |   |
| RSL-2 | | ASIL-A | SIL-1 |  |  |   |
| RSL-3 | | ASIL-B | SIL-2 |  |  |   |
| RSL-4 | | ASIL-C | SIL-3 |  |  |   |
| RSL-5 | Most Requirements | ASIL-D | SIL-4 |  |  |   |

## Others
- the group discussed that it would be a good idea to involve people from MISRA and the ISO standards
- an observation that the group had was that so far the discussion seems to be going to the same path as the C/C++ certification, using the same 3rd party tools
- the question that everyone had was if there is any way to disrupt this? This is a potential goal of the group. Some proposed solutions were:
  - add several tools inside the compiler
  - do things differently (not sure how)

## Next Meeting
The next meeting will be on 6.12.2024.
