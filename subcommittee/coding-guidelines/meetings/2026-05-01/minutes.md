# **Coding Guidelines Subcommittee Meeting on 2026-05-01 @ 0800 JST / 1900 EDT**

[Link](https://www.worldtimebuddy.com/?qm=1&lid=5,12,2643743,8,1850147,100,14,14&h=5&date=2026-4-30&sln=19-20&hf=1) to meeting time in common time zones.

| Search Key    | Description          |
| :------------ | :------------------- |
| \[todo\]      | Action Item          |
| \[decision\]  | Something decided on |
| \[important\] | Key information      |

## **Agenda**

1. Solicitation of notetaker
2. Acceptance of Previous Meeting Minutes
3. Introduction of new members
4. Review batches for [CERT C \=\> Rust Mapping](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/336) (Pete)
   - Let's split up again, to get some feedback on batches 1 & 2
   - [\#427 \[CERT C Review Batch 1/5\] Review proposed Rust categorization](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/427)
   - [\#428 \[CERT C Review Batch 2/5\] Review proposed Rust categorization](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/428)
5. Coverage of MISRA C and CERT C in 2026 (Félix / Markus updates)
   - MISRA C one has a [PR up](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/432) from Markus
6. Interest in the MISRA C++ mapping
   - Please register interest on [this Zulip thread](https://rust-lang.zulipchat.com/#narrow/channel/579369-safety-critical-consortium.2Fcoding-guidelines/topic/MISRA.20C.2B.2B.20Mapping.20Interest/with/584764785)
   - Pete/Alex are working out how we can have some kind of copy of the MISRA documents (C, C++) held in the jurisdiction of the Rust Foundation in support of members to be able to work on coding guidelines
7. Overview of [Safety-Critical Rust](https://rust-lang.github.io/rust-project-goals/2026/roadmap-safety-critical-rust.html) \- Rust Project Goals Roadmap (Pete)
   - Soliciting those interested in [Establish a Spot for Safety-Critical Lints in Clippy](https://rust-lang.github.io/rust-project-goals/2026/safety-critical-lints-in-clippy.html) goal
     - Register interest [here](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/Getting.20involved.20with.20Clippy.20for.20SCRC.20lints/with/583090116) on Rust Zulip
   - Soliciting those interested in [Normative Documentation for Sound unsafe Rust](https://rust-lang.github.io/rust-project-goals/2026/safe-unsafe-for-safety-critical.html) goal
     - Register interest [here](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/SCRC.20.3C.3D.3E.20t-opsem.3A.20Normative.20Documentation.20for.20Sound.20.60unsafe.60/with/586198564) on Rust Zulip
8. Proposals and ideas for new rules (all)
9. Progress on ongoing tasks (all)
10. Round table

## **Check-in area**

**Please add your name, and an emoji that describes your day.**

- Mikhail Antoshkin ☕
- Max Jacinto 🍜
- Pete LeVasseur 🖖
- Yuchen Shen ☕

**Notetaker:**

- Mikhail Antoshkin

For tips on how we take notes in the Safety-Critical Rust Consortium, please see the [Meeting Notetaker Role](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/docs/notetaker-role.md) doc.

## **Housekeeping section**

- Document space: [coding-guidelines](https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines)
- Zulip: [safety-critical-consortium: Coding Guidelines](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/Coding.20Guidelines)
- [Kanban board](https://github.com/orgs/rustfoundation/projects/1/views/3)
  - [`contributor experience`](https://github.com/orgs/rustfoundation/projects/1/views/4) view
  - [`coding guideline`](https://github.com/orgs/rustfoundation/projects/1/views/5) view

## **Tasks**

- None

## **Meeting Minutes**

- Agenda discussion
  - Coverage of MISRA C and CERT C and mapping to Rust
  - MISRA C++
    - Lacking copies of MISRA C/C++ for consortium members, trying to procure
  - Roadmap
    - If you are interested in working on clippy lints - register your interest on Zulip, though time slot might be not the most comfortable for APAC
    - [Normative Documentation for Sound unsafe Rust](https://rust-lang.github.io/rust-project-goals/2026/safe-unsafe-for-safety-critical.html) goal
      1. Same as clippy, if you are interested - register on Zulip
      1. Doing what was done for zerocopy for [iceoryx2](https://github.com/eclipse-iceoryx/iceoryx2), extracting the unsafe usage patterns
- Working on batch 1 of mapping CERT C rules
  - CERT C website had some issues, members were not able to access it
  - ENV34
    - Does not map to _safe_ Rust, but falls under “don’t break safety contract of an unsafe function”
  - CON37
    - Agreed, not in std
  - MSC30
    - Agreed, not in std
  - FLP37
    - It maps to rust, let’s have a guideline that prohibits this
    - [https://doc.rust-lang.org/std/primitive.f64.html#method.to_bits](https://doc.rust-lang.org/std/primitive.f64.html#method.to_bits)
  - STR31
    - CStr is null-terminated [https://doc.rust-lang.org/std/ffi/struct.CStr.html](https://doc.rust-lang.org/std/ffi/struct.CStr.html)
    - The string types interfaces are preventing you from breaking the rule though, needs more investigation
  - DCL40
    - Agreed, compiler is checking this
    - The only time it can come up is C FFI, but it’s, as wth ENV34, safety contracts
  - DCL39
    - Agreed, but needs more investigation
  - INT36
    - [https://doc.rust-lang.org/std/ptr/index.html#using-strict-provenance](https://doc.rust-lang.org/std/ptr/index.html#using-strict-provenance) maybe we can work in strict provenance into this guideline
  - CON40
    - Agreed, we should have a guideline to point people to use APIs on atomics
  - CON36
    - Agreed, the only additional note is “spuriously” is a load-bearing word here, since some logic might require wake up even if condition still does not hold
  - EXP40
    - Agreed, but let’s move it from “maybe” to a becoming a rule about statics, since it’s not about const for rust
    - Probably maps directly to Unsafe Rust
  - STR30
    - Agreed, but let’s move it from “maybe” to a becoming a rule about statics, since it’s not about const for rust
    - Probably maps directly to Unsafe Rust
  - EXP39: Agreed; worth checking out the Safe Transmute Project as mentioned
  - CON32: Agreed; might be good to generate rules around `Send` and `Sync`
  - CON43: Agreed; might be good to generate rules around `Send` and `Sync`

## **Material**

Any material to read before the meeting should be included here.
