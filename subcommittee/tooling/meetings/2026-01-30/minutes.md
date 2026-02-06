# Tooling Subcommittee Meeting on 30 January 2026 @ 4pm GMT

| Search Key    | Description          |
| :------------ | :------------------- |
| \[todo\]      | Action Item          |
| \[decision\]  | Something decided on |
| \[important\] | Key information      |

## Agenda

1. Solicitation of notetaker
2. Review last time’s meeting minutes
3. Present new members
4. PRs related to Tooling Task Force
   1. [https://github.com/rustfoundation/safety-critical-rust-consortium/pull/545](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/545)
   2. [https://github.com/rustfoundation/safety-critical-rust-consortium/pull/553](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/553)
5. Rust Project Bridge Task Force \- Project Goals
   1. [https://rust-lang.github.io/rust-project-goals/2026/stabilize-fls-releases.html](https://rust-lang.github.io/rust-project-goals/2026/stabilize-fls-releases.html)
   2. [https://rust-lang.github.io/rust-project-goals/2026/mcdc-coverage-support.html](https://rust-lang.github.io/rust-project-goals/2026/mcdc-coverage-support.html)
   3. [Establish a Home for Safety-Critical Lints in Clippy](https://hackmd.io/@plevasseur/r199Y_lS-l)
      1. [Pete LeVasseur](mailto:plevasseur@gmail.com) will make a PR for this today
   4. [Normative Documentation for Sound `unsafe` Rust](https://hackmd.io/@plevasseur/BkvXPUtLWx)
      1. [Pete LeVasseur](mailto:plevasseur@gmail.com) will make a PR for this today
6. Round-table
   1. Bringing tools YAML list to filterable table on web page
   2. Documentation and traceability for doing safety-systems development
   3. Safety-assessor / auditor joined the Consortium, interested in supporting “how to apply standards to Rust”
   4. [https://coding-guidelines.arewesafetycriticalyet.org/](https://coding-guidelines.arewesafetycriticalyet.org/)
      1. [https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/360](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/360)
      2. [https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/370](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/370)
   5. Pete talking next week about Rust \+ Security:
      1. [https://github.com/rust-sig/rust-sig](https://github.com/rust-sig/rust-sig)
7. Meeting close

## Check-in area

**Please add your name, and an emoji that describes your day.**

- Pete LeVasseur 🦀⛑️
- Oreste Bernardi ⇗⇖
- Manuel Hatzl
- Arnaud Riess 🎧
- Arnaud Fontaine 😃
- Tony Aiello 🙂

  **Notetaker:**

- Oreste Bernardi

## Housekeeping section

## Tasks

- xx

## Meeting Minutes

- Review pullrequest [https://github.com/rustfoundation/safety-critical-rust-consortium/pull/545](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/545) about aiT Tools.
  - Merged \!
- Review of pull request “Adjust tools flow” [https://github.com/rustfoundation/safety-critical-rust-consortium/pull/553](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/553)
  - Merged\!
- [https://rust-lang.github.io/rust-project-goals/2026/stabilize-fls-releases.html](https://rust-lang.github.io/rust-project-goals/2026/stabilize-fls-releases.html)
  - More people get involved in FLS. Phase1 seems quite ease
- [https://rust-lang.github.io/rust-project-goals/2026/mcdc-coverage-support.html](https://rust-lang.github.io/rust-project-goals/2026/mcdc-coverage-support.html)
  - Defined the goal. It is going to be implemented. It will not be a separate tool. It will be integrated in the compiler.
  - Previously there was no decision coverage with new implementation we will get it as byproduct.
- [Establish a Home for Safety-Critical Lints in Clippy](https://hackmd.io/@plevasseur/r199Y_lS-l)
  - Not yet decided the organization, one group or separated lint group. Decision on going.
- [Normative Documentation for Sound `unsafe` Rust](https://hackmd.io/@plevasseur/BkvXPUtLWx)
  - Identified weakness in the definition of unsafe definition \-\> Rust project is involved in the improvement.
  - During development of zero copy crate developed some guidelines about how to write unsafe code.
  - Proposal to make visible the present outcome/documentation.
- Agreed to go public in the website as soon as HTML/CSS is fixed. Suggested usage of AI.
  - Proposed to make public before Embedded World 2026
- A member started evaluation of tool for code traceability.
- Expected contribution from new member who is a consultant and assessor in safety critical space.
- Coding guidelines have not yet reached a great state.
  - Improved contributing experience.
  - New security guidelines from ANSSI will be released shortly. They are going to be translated in French.
  - Wish to have common guidelines for cybersecurity and safety but sometimes they can conflict.
