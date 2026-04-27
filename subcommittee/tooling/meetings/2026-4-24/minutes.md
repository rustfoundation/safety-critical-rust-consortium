# Tooling Subcommittee Meeting on 24 April 2026 @ 4pm GMT

| Search Key    | Description          |
| :------------ | :------------------- |
| \[todo\]      | Action Item          |
| \[decision\]  | Something decided on |
| \[important\] | Key information      |

## Agenda

1. Solicitation of notetaker
2. Review last and last-last time’s meeting minutes
   1. [https://github.com/Safety-Critical-Rust-Consortium/safety-critical-rust-consortium/pull/622](https://github.com/Safety-Critical-Rust-Consortium/safety-critical-rust-consortium/pull/622)
   2. [https://github.com/Safety-Critical-Rust-Consortium/safety-critical-rust-consortium/pull/625](https://github.com/Safety-Critical-Rust-Consortium/safety-critical-rust-consortium/pull/625)
3. Present new members
4. Tooling Task Force
   1. [https://github.com/Safety-Critical-Rust-Consortium/safety-critical-rust-consortium/pull/632](https://github.com/Safety-Critical-Rust-Consortium/safety-critical-rust-consortium/pull/632) ... improves the tooling categories
   2. [https://github.com/Safety-Critical-Rust-Consortium/safety-critical-rust-consortium/pull/630](https://github.com/Safety-Critical-Rust-Consortium/safety-critical-rust-consortium/pull/630) ... rearrange sidebar (mostly to not land on the members page first)
   3. [https://github.com/Safety-Critical-Rust-Consortium/safety-critical-rust-consortium/pull/629](https://github.com/Safety-Critical-Rust-Consortium/safety-critical-rust-consortium/pull/629) ... adds Verus to tools list
   4. [https://github.com/Safety-Critical-Rust-Consortium/safety-critical-rust-consortium/issues/606](https://github.com/Safety-Critical-Rust-Consortium/safety-critical-rust-consortium/issues/606) ... closing this one as off-topic tool
   5. [https://github.com/Safety-Critical-Rust-Consortium/safety-critical-rust-consortium/issues/608](https://github.com/Safety-Critical-Rust-Consortium/safety-critical-rust-consortium/issues/608) ... tool submission from Alex Celeste
5. Rust Project Bridge Task Force
   1. Updates from Rust Project [Safety-Critical Rust Roadmap](https://rust-lang.github.io/rust-project-goals/2026/roadmap-safety-critical-rust.html)
   2. Soliciting those interested in [Establish a Spot for Safety-Critical Lints in Clippy](https://rust-lang.github.io/rust-project-goals/2026/safety-critical-lints-in-clippy.html) goal
      1. Register interest [here](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/Getting.20involved.20with.20Clippy.20for.20SCRC.20lints/with/583090116) on Rust Zulip
   3. Soliciting those interested in [Normative Documentation for Sound unsafe Rust](https://rust-lang.github.io/rust-project-goals/2026/safe-unsafe-for-safety-critical.html) goal
      1. Register interest [here](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/SCRC.20.3C.3D.3E.20t-opsem.3A.20Normative.20Documentation.20for.20Sound.20.60unsafe.60/with/586198564) on Rust Zulip
6. Rust Commercial Network (RCN)

## Check-in area

**Please add your name, and an emoji that describes your day.**

- Oreste Bernardi ☕
- Manuel Hatzl
- Zalán Bálint Lévai 🎉
- Stefan Akatyschew 🫩
- Tony Aiello
- Pete LeVasseur 🏃📆

**Notetaker:**

- Oreste Bernardi

## Housekeeping section

xx

## Tasks

- \[todo\] Pete to follow up with Joel Marcey on potential root cause \-- change of org from rustfoundation to Safety-Critical-Rust-Consortium
  - \[todo\] Manuel will check into if the previews of the website are not broad enough to cover instances of updates to .json files etc that now effect the website
  - \[todo\] Manuel to check into why the website may currently be broken and not deployed
- \[todo\] Pete to ask Alex Celeste to follow-up on this PR for Perforce tooling: [https://github.com/Safety-Critical-Rust-Consortium/safety-critical-rust-consortium/issues/608](https://github.com/Safety-Critical-Rust-Consortium/safety-critical-rust-consortium/issues/608)
- \[todo\] Pete to talk with Lori, the Outreach Director of the Rust Foundation, about potential to have some work at the Foundation / some kind of track (RustConf 2026?) about marketing / technical marketing

## Meeting Minutes

- Last meeting minutes has been merged
- No new members
- Tooling task force
  - Tool categories PR
    - [https://github.com/Safety-Critical-Rust-Consortium/safety-critical-rust-consortium/pull/632](https://github.com/Safety-Critical-Rust-Consortium/safety-critical-rust-consortium/pull/632) .
    - Presented PR tool categories proposal, package manager
    - Asked feedback
    - **Merge approved**
  - Rearrange sidebar PR
  - [https://github.com/Safety-Critical-Rust-Consortium/safety-critical-rust-consortium/pull/630](https://github.com/Safety-Critical-Rust-Consortium/safety-critical-rust-consortium/pull/630) ..
  - Asked live preview but it not works.
  - Asked feedback
  - **Merge approved**
  - Add Verus to tool list
    - [https://github.com/Safety-Critical-Rust-Consortium/safety-critical-rust-consortium/pull/629](https://github.com/Safety-Critical-Rust-Consortium/safety-critical-rust-consortium/pull/629)
    - Asked feedback
    - **Merge approved**
  - Closing off-topic tool proposal
    - [https://github.com/Safety-Critical-Rust-Consortium/safety-critical-rust-consortium/issues/606](https://github.com/Safety-Critical-Rust-Consortium/safety-critical-rust-consortium/issues/606)
    - Proposed to close it without merge
    - **Agreed to close for now**.
  - New Tool submission
    - [https://github.com/Safety-Critical-Rust-Consortium/safety-critical-rust-consortium/issues/608](https://github.com/Safety-Critical-Rust-Consortium/safety-critical-rust-consortium/issues/608)
    - Discussed if we need to track IEC60880 (Nuclear)
    - Proposed to ask for more info about this standard then create PR for the tool.
- Rust Project Bridge Task Force
  - Some effort has been spent on Eclipse iceoryx2 (tbd) to catalog some patterns and usage.
    - Asked interested people to declare interest in Zulip.
    - Initial scope is memory safety not FFI. Maybe in the future.
    - This will help to create a safety case.
  - Calling for contributors to Clippy Lints
  - Stabilization of releases of FLS
    - FLS release is and will be refer to last Rust version \-1
  - MC/DC
    - MC/DC activities are moving forward but slowly.
    - Some technical discussion in background.
- Proposed to link “Normative Documentation for Sound unsafe Rust” to FLS instead of Rust Reference.
  - In the Rust project there are 2 documents FLS and Rust Reference. The approach is Rust Reference is a leading document and FLS is a lagging document.
- Rust Commercial Network: [https://github.com/Rust-Commercial-Network/rcn](https://github.com/Rust-Commercial-Network/rcn)
  - Promote Rust in commercial applications and support networking among companies.
  - Asked to review RCN site and give some feedback
  - Which is the difference between Rust Society and RCN ?
    - The difference is not yet clear to us; it’s still being worked out.
- Proposed to create a group/subcommittee for SW marketing people where to discuss:
  - Networking
  - Joint promotion
  - How to promote Rust in commercial space
