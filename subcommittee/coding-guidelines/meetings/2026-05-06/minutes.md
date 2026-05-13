# **Coding Guidelines Subcommittee Meeting on 2026-05-06 @ 1600 CEST / 1100 EDT**

[Link](https://www.worldtimebuddy.com/?qm=1&lid=5,12,2643743,8,1850147,100,14,14&h=5&date=2026-5-6&sln=11-12&hf=1) to meeting time in common time zones.


| Search Key | Description          |
| ---------- | -------------------- |
| todo       | Action Item          |
| decision   | Something decided on |
| important  | Key information      |


## **Agenda**

1. Solicitation of notetaker
2. Acceptance of
  - [Previous Americas + Europe Meeting Minutes](https://github.com/Safety-Critical-Rust-Consortium/safety-critical-rust-consortium/blob/main/subcommittee/coding-guidelines/meetings/2026-04-29/minutes.md)
  - [Previous Asia Pacific + Americas Meeting Minutes](https://github.com/Safety-Critical-Rust-Consortium/safety-critical-rust-consortium/blob/main/subcommittee/coding-guidelines/meetings/2026-05-01/minutes.md)
3. Introduction of new members
4. Coverage of MISRA C and CERT C in 2026 (Félix / Markus updates)
  - MISRA C one has a [PR up](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/432) from Markus
5. Interest in the MISRA C++ mapping
  - Please register interest on [this Zulip thread](https://rust-lang.zulipchat.com/#narrow/channel/579369-safety-critical-consortium.2Fcoding-guidelines/topic/MISRA.20C.2B.2B.20Mapping.20Interest/with/584764785)
  - Pete/Alex are working out how we can have some kind of copy of the MISRA documents (C, C++) held in the jurisdiction of the Rust Foundation in support of members to be able to work on coding guidelines
6. Overview of [Safety-Critical Rust](https://rust-lang.github.io/rust-project-goals/2026/roadmap-safety-critical-rust.html)  Rust Project Goals Roadmap (Pete)
  - Soliciting those interested in [Establish a Spot for Safety-Critical Lints in Clippy](https://rust-lang.github.io/rust-project-goals/2026/safety-critical-lints-in-clippy.html) goal
    - Register interest [here](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/Getting.20involved.20with.20Clippy.20for.20SCRC.20lints/with/583090116) on Rust Zulip
  - Soliciting those interested in [Normative Documentation for Sound unsafe Rust](https://rust-lang.github.io/rust-project-goals/2026/safe-unsafe-for-safety-critical.html) goal
    - Register interest [here](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/SCRC.20.3C.3D.3E.20t-opsem.3A.20Normative.20Documentation.20for.20Sound.20.60unsafe.60/with/586198564) on Rust Zulip
7. Review batches for [CERT C  Rust Mapping](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/336) (Pete)
  - Let's split up again, to get some feedback on batch 2
  - [428 [CERT C Review Batch 2/5] Review proposed Rust categorization](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/428)
8. Round table

## **Check-in area**

Pete LeVasseur ☕☕☕
Max Jacinto ⚽
Arshad Mahmood 🌞
Oreste Bernardi ⛈️
David Svoboda (-:
Andreas Weis 🧐
Achim Kriso
Christof Petig ⏲️

**Notetaker:**

- Arshad Mahmood

For tips on how we take notes in the Safety-Critical Rust Consortium, please see the [Meeting Notetaker Role](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/docs/notetaker-role.md) doc.

## **Housekeeping section**

- Document space: [coding-guidelines](https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines)
- Zulip: [safety-critical-consortium: Coding Guidelines](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/Coding.20Guidelines)
- [Kanban board](https://github.com/orgs/rustfoundation/projects/1/views/3)
  - `[contributor experience](https://github.com/orgs/rustfoundation/projects/1/views/4)` view
  - `[coding guideline](https://github.com/orgs/rustfoundation/projects/1/views/5)` view

## **Tasks**

- Andreas will put Pete in touch with MISRA leadership to follow-up on use cases for having an SCRC copy of MISRA C, MISRA C++
- Pete to think about how breakdown the MISRA C++ mapping work
- Pete to meet with folks at Rust All-Hands
- Pete to share with t-opsem about the work that Andreas has done for iceoryx2 thus far
- Pete to meet the team re: clippy to set goals

## **Meeting Minutes**

- Accepted the prevision session meeting notes
- MISRA C PR is up, note has been sent for review feedback a response not yet received
- MISRA C leadership - mapping to C language makes sense, it was done by MISRA C committee.
- MISRA C++ anyone interested please reach out link to zulip here - XXX . Some preliminary work has been done, see the zulip thread for more information.
- MISRA C++ process for building up the mapping discussed via github issues.
- MISRA C++ standards docs getting them for the groups usage, security considerations being discussed due to copyright issues.
- Decided to start the MISRA C++2023 mapping by creating new sheet (MISRA C++ Mapping ([https://docs.google.com/spreadsheets/d/12e9Tr8PUTvVr87nUH0MQTwL31yU6YihQVxlvkqlo9SA/edit?usp=sharing](https://docs.google.com/spreadsheets/d/12e9Tr8PUTvVr87nUH0MQTwL31yU6YihQVxlvkqlo9SA/edit?usp=sharing))) to work collaboratively
- Clippy has been discussed previously, new action added to tasks,
- Some training material available for clippy, which can be shared with us for getting some training for members working on the clippy workstream.
- Moving onto the normative documentation, the current version was shared for review. Some comments were already received which are being looked at. There is a zulip thread - where discussion is taking place
- An example of iceroyx2 was shared as an example (the library is a pub-sub, but the subscribers get a virtual address mapped to the same physical address for in process pub-sub. So different virtual pointer but the same physical location).- does rust aliasing rules and pointer provenance ensure we don’t have this issue?
- Rustweek may be a good time to discuss some of these topics, some pre-session research will be done to scope out issues such as this.
- Some other potential issues have also been documented, worth reviewing to get a better idea of these issues (see zulip thread for links - Zulip thread ([https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/SCRC.20.3C.3D.3E.20t-opsem.3A.20Normative.20Documentation.20for.20Sound.20.60unsafe.60](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/SCRC.20.3C.3D.3E.20t-opsem.3A.20Normative.20Documentation.20for.20Sound.20.60unsafe.60))).
- The process of how to manage this was discussed, perhaps a table or list.
- The need for operational semantics is an important goal to pursue, but it’s going to be a major piece of work. Perhaps we can break down this task to manage the process. Checkout the zulip thread - Zulip thread ([https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/SCRC.20.3C.3D.3E.20t-opsem.3A.20Normative.20Documentation.20for.20Sound.20.60unsafe.60](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/SCRC.20.3C.3D.3E.20t-opsem.3A.20Normative.20Documentation.20for.20Sound.20.60unsafe.60)) .
- A paper that has been accepted relating to an application of the rust borrow checker for analysing was mentioned by one of the members (not yet published, link will be sent once published).
- Batch 2 CERT C mapping was not discussed, but will be on the agenda for the next session. It may be taken to the round table.

## **Material**

Any material to read before the meeting should be included here.