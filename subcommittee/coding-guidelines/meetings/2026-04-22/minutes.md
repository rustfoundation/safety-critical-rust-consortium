# **Coding Guidelines Subcommittee Meeting on 2026-04-22 @ 1600 CEST / 1100 EDT**

[Link](https://www.worldtimebuddy.com/?qm=1&lid=5,12,2643743,8,1850147,100,14&h=5&date=2026-4-22&sln=11-12&hf=1) to meeting time in common time zones.

| Search Key | Description |
| :---- | :---- |
| \[todo\] | Action Item |
| \[decision\] | Something decided on |
| \[important\] | Key information |

## **Agenda**

1. Solicitation of notetaker  
2. Acceptance of [Previous Meeting Minutes](https://github.com/Safety-Critical-Rust-Consortium/safety-critical-rust-consortium/blob/main/subcommittee/coding-guidelines/meetings/2026-04-15/minutes.md)  
3. Introduction of new members  
4. Review batches for [CERT C \=\> Rust Mapping](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/336) (Pete)  
   - Félix can share updates from his side on reviewing feedback  
   - Let's split up again, to get some feedback on batches 1 & 2  
   - [\#427 \[CERT C Review Batch 1/5\] Review proposed Rust categorization](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/427)  
     * [https://meet.google.com/xna-qdvi-rmk](https://meet.google.com/xna-qdvi-rmk)  
   - [\#428 \[CERT C Review Batch 2/5\] Review proposed Rust categorization](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/428)  
     * [https://meet.google.com/sow-whqc-iir](https://meet.google.com/sow-whqc-iir)  
5. Coverage of MISRA C and CERT C in 2026 (Félix / Markus updates)  
   - MISRA C one has a [PR up](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/432) from Markus  
6. Interest in the MISRA C++ mapping  
   - Please register interest on [this Zulip thread](https://rust-lang.zulipchat.com/#narrow/channel/579369-safety-critical-consortium.2Fcoding-guidelines/topic/MISRA.20C.2B.2B.20Mapping.20Interest/with/584764785)  
   - Pete/Alex/Joel are working out how we can have some kind of copy of the MISRA documents (C, C++) held in the jurisdiction of the Rust Foundation in support of members to be able to work on coding guidelines  
7. Overview of [Safety-Critical Rust](https://rust-lang.github.io/rust-project-goals/2026/roadmap-safety-critical-rust.html) \- Rust Project Goals Roadmap (Pete)  
   - Soliciting those interested in [Establish a Spot for Safety-Critical Lints in Clippy](https://rust-lang.github.io/rust-project-goals/2026/safety-critical-lints-in-clippy.html) goal  
     * Register interest [here](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/Getting.20involved.20with.20Clippy.20for.20SCRC.20lints/with/583090116) on Rust Zulip  
   - Soliciting those interested in [Normative Documentation for Sound unsafe Rust](https://rust-lang.github.io/rust-project-goals/2026/safe-unsafe-for-safety-critical.html) goal  
     * Register interest [here](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/SCRC.20.3C.3D.3E.20t-opsem.3A.20Normative.20Documentation.20for.20Sound.20.60unsafe.60/with/586198564) on Rust Zulip  
8. Proposals and ideas for new rules (all)  
9. Progress on ongoing tasks (all)  
10. Round table

## **Check-in area**

**Please add your name, and an emoji that describes your day.**

* Markus Hosch  
* Oreste Bernardi🏥  
* Arshad Mahmood 🌞  
* Andreas Weis ☀️  
* Max Jacinto 👾  
* William Barsse  
* Christof Petig 🌞  

**Notetaker:**

* Markus Hosch

For tips on how we take notes in the Safety-Critical Rust Consortium, please see the [Meeting Notetaker Role](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/docs/notetaker-role.md) doc.

## **Housekeeping section**

* Document space: [coding-guidelines](https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines)  
* Zulip: [safety-critical-consortium: Coding Guidelines](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/Coding.20Guidelines)  
* [Kanban board](https://github.com/orgs/rustfoundation/projects/1/views/3)  
  * [`contributor experience`](https://github.com/orgs/rustfoundation/projects/1/views/4) view  
  * [`coding guideline`](https://github.com/orgs/rustfoundation/projects/1/views/5) view

## **Tasks**

* Markus to also review [https://github.com/Safety-Critical-Rust-Consortium/safety-critical-rust-coding-guidelines/issues/430](https://github.com/Safety-Critical-Rust-Consortium/safety-critical-rust-coding-guidelines/issues/430)  
* Oreste will create an issue on the operator precedence issue

## **Meeting Minutes**

* Previous meeting minutes accepted  
* Looking at [https://github.com/Safety-Critical-Rust-Consortium/safety-critical-rust-coding-guidelines/issues/336](https://github.com/Safety-Critical-Rust-Consortium/safety-critical-rust-coding-guidelines/issues/336), this has been split into 5 subissues, see [https://github.com/Safety-Critical-Rust-Consortium/safety-critical-rust-coding-guidelines/issues/336\#issuecomment-4040940602](https://github.com/Safety-Critical-Rust-Consortium/safety-critical-rust-coding-guidelines/issues/336#issuecomment-4040940602)   
* [https://github.com/Safety-Critical-Rust-Consortium/safety-critical-rust-coding-guidelines/pull/432](https://github.com/Safety-Critical-Rust-Consortium/safety-critical-rust-coding-guidelines/pull/432) will be merged by 04/25/26 if there are no more comments.  
* Pointed to the thread and asked for interest  
* [https://rust-lang.github.io/rust-project-goals/2026/safe-unsafe-for-safety-critical.html](https://rust-lang.github.io/rust-project-goals/2026/safe-unsafe-for-safety-critical.html): Unsafe is not documented well enough; goal is to look at the “dark corners” and shed some light; Iceoryx2 is used as an example.  
  * Q: How can you “define” undefined behavior? The spec sometimes does not say *anything* about a specific part of the language, so it is unknown whether it will (at some point) be sound or not  
  * Last FAQ point gets debated, wording seems unclear. The intent is to describe what preconditions sound code has; it is not intended to define things that are UB today.  
* New rules  
  * MISRA C rule “follow contracts” could that lead to a rule “use typestate”?  
    1. Maybe too strict. The rule should be more open to also allow other ways  
    2. Rule not very useful as it cannot be checked / enforced.  
    3. Might be useful as an implementation pattern to help enforce more high level rules or other rules  
  * Operator precedence change in the face of generics  
    1. Evaluation order changes depending on whether the left hand side of the add\_assign operator is generic or not.  
* No topics for the round table

## **Material**

Any material to read before the meeting should be included here.
