# Tooling Subcommittee Meeting on 12 December 2025 @ 4pm GMT

| Search Key    | Description          |
| :------------ | :------------------- |
| \[todo\]      | Action Item          |
| \[decision\]  | Something decided on |
| \[important\] | Key information      |

## Agenda

1. Solicitation of notetaker
2. Review last time’s [meeting minutes](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/tooling/meetings/2025-11-28/minutes.md)
3. Present new members
4. Rust Project Bridge Task Force \- Project Goals
   1. Survey: [https://www.surveyhero.com/c/rust-safety-critical](https://www.surveyhero.com/c/rust-safety-critical)
   2. Zulip:
      1. [\#project-goals/2026-workshop \> Safety Critical Consortium](https://rust-lang.zulipchat.com/#narrow/channel/546987-project-goals.2F2026-workshop/topic/Safety.20Critical.20Consortium/with/561966869)
      2. [\#project-goals/2026-workshop \> mcdc-support](https://rust-lang.zulipchat.com/#narrow/channel/546987-project-goals.2F2026-workshop/topic/mcdc-support/with/563467365)
5. PRs related to Tooling Task Force
   1. [https://github.com/rustfoundation/safety-critical-rust-consortium/pull/497](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/497)
   2. [https://github.com/rustfoundation/safety-critical-rust-consortium/pull/525](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/525)
   3. [https://github.com/rustfoundation/safety-critical-rust-consortium/issues/527](https://github.com/rustfoundation/safety-critical-rust-consortium/issues/527)
6. Round-table
   1. Eclipse S-CORE (Eclipse SDV WG) is aiming for ability to do ISO 26262 ASIL B software development in Rust and C++ by end of calendar year 2026
      1. There’s a project board on which they are tracking their ability to do so, some of the items are tooling: [https://github.com/orgs/eclipse-score/projects/34](https://github.com/orgs/eclipse-score/projects/34)
   2. How can `libcore` be certified for safety, if it’s using unstable Rust programming language features?
      1. Certification is a conversation between applicant and assessor
7. Meeting close

## Check-in area

**Please add your name, and an emoji that describes your day.**

- Pete LeVasseur 🏃
- Manuel Hatzl 🚋
- Tony Aiello 👏(it’s almost the weekend\!)
- Tiago Manczak 🏒
- Oreste Bernardi 🌲
- Munawar Hafiz
- tshepang

  **Notetaker:**

- Oreste Bernardi

## Housekeeping section

## Tasks

- Oreste shall contact AbsInt to invite them to the next meeting \[Jan 26\] to explain the tool.
- Pete should contact S-Core project and invite them regarding required tools features for certification.

## Meeting Minutes

- Review last time’s meeting minutes
  - Accepted
- Rust Project Bridge Task Force
  - Requested to check Safety Critical Consortium Zulip channel
  - Member trying to motivate a compiler vendor to contribute to the safety goal.
  - Niko is putting high effort on safety goals.
  - Focus on mcdc support.
- PRs related to Tooling Task Force
  - [https://github.com/rustfoundation/safety-critical-rust-consortium/pull/497](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/497)
    - No comments. No one against. Merged
  - [https://github.com/rustfoundation/safety-critical-rust-consortium/pull/525](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/525)
    - Comment:
      - Clarify the meaning of binaries. Elf may not be identical due to meta-data but code shall be identical.
      - Not yet ready to be merged
  - [https://github.com/rustfoundation/safety-critical-rust-consortium/issues/527](https://github.com/rustfoundation/safety-critical-rust-consortium/issues/527)
    - Reviewed. It is used in the field but nobody in the call has used it.
    - AI to contact the company. See Tasks.
- Round-table
  - S-Core has an activity about tool requirements for certification.
    - Proposal to invite them to discuss the requirements.
  - Libcore uses unstable features, not specified but it could be certified with proven in use \+ test coverage arguments.
