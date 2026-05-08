# **Coding Guidelines Subcommittee Meeting on 2026-04-15 @ 1600 CEST / 1100 EDT**

[Link](https://www.worldtimebuddy.com/?qm=1&lid=5,12,2643743,8,1850147,100,14&h=5&date=2026-4-15&sln=11-12&hf=1) to meeting time in common time zones.

| Search Key | Description |
| :---- | :---- |
| \[todo\] | Action Item |
| \[decision\] | Something decided on |
| \[important\] | Key information |

## **Agenda**

1. Solicitation of notetaker
2. Acceptance of [Previous Meeting Minutes](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/coding-guidelines/meetings/2026-04-08/minutes.md)
3. Introduction of new members
4. Review batches for [CERT C \=\> Rust Mapping](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/336) (Pete)
   - Félix can share updates from his side on reviewing feedback
   - Let's split up again, to get some feedback on batches 1 & 2
   - [\#427 \[CERT C Review Batch 1/5\] Review proposed Rust categorization](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/427)
     * Arshad
     * Arthur
     * Douglas
     * Félix
   - [\#428 \[CERT C Review Batch 2/5\] Review proposed Rust categorization](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/428)
     * Satoshi
     * Max
     * Pete
     * William
5. Coverage of MISRA C and CERT C in 2026 (Félix / Markus)
   - MISRA C one has a [PR up](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/432) from Markus
   - Félix met with Markus and will walk us through the "harmonized" version that should work for MISRA, CERT both
6. Interest in the MISRA C++ mapping
   - Please register interest on [this Zulip thread](https://rust-lang.zulipchat.com/#narrow/channel/579369-safety-critical-consortium.2Fcoding-guidelines/topic/MISRA.20C.2B.2B.20Mapping.20Interest/with/584764785)
   - Pete/Alex/Joel are working out how we can have some kind of copy of the MISRA documents (C, C++) held in the jurisdiction of the Rust Foundation in support of members to be able to work on coding guidelines
7. Overview of [Safety-Critical Rust](https://rust-lang.github.io/rust-project-goals/2026/roadmap-safety-critical-rust.html) \- Rust Project Goals Roadmap (Pete)
   - Soliciting those interested in [Establish a Spot for Safety-Critical Lints in Clippy](https://rust-lang.github.io/rust-project-goals/2026/safety-critical-lints-in-clippy.html) goal
   - Explanation of the work, as Pete understands from initial discussions with t-clippy
8. Proposals and ideas for new rules (all)
9. Progress on ongoing tasks (all)
10. Round table

## **Check-in area**

**Please add your name, and an emoji that describes your day.**

* Pete LeVasseur ☕☕
* Oreste Bernardi🏥
* Samuel Tardieu 🎺
* Jason Newcomb ❄️
* Douglas Deslauriers 🌞
* Arshad Mahmood 🌦️
* Félix Fischer 🙂
* William Barsse
* Max Jacinto 🫠
* Arthur Hicken 🌄🙂
* Kaneko Satoshi

**Notetaker:**

* Douglas Deslauriers

For tips on how we take notes in the Safety-Critical Rust Consortium, please see the [Meeting Notetaker Role](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/docs/notetaker-role.md) doc.

## **Housekeeping section**

* Document space: [coding-guidelines](https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines)
* Zulip: [safety-critical-consortium: Coding Guidelines](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/Coding.20Guidelines)
* [Kanban board](https://github.com/orgs/rustfoundation/projects/1/views/3)
  * [`contributor experience`](https://github.com/orgs/rustfoundation/projects/1/views/4) view
  * [`coding guideline`](https://github.com/orgs/rustfoundation/projects/1/views/5) view

## **Tasks**

* \[Pete\] Determine a list of people interested in Clippy integration and working with them
* \[Pete\] Determine an easy Clippy lint for trial run
* \[Pete\] Reach out to Markus about MISRA C mapping
* \[Doug\] Open separate issue for PRE31

## **Meeting Minutes**

* Previous meeting notes
  * No objections
* Clippy collaboration
  * The safety critical rust consortium members don’t want to have to use another separate tool to verify coding guidelines
  * There are some coding guidelines which are in a good enough space that Clippy lints could start to be implemented
  * Suggestion to have a few interactive sessions to help introduce our team to implementing or starting to implement lints
    1. What to look for when opening an issue
    2. How to best provide suggestions
  * It was suggested to open a new issue/PR against Clippy with the SCRC tag
    1. It is possible to open issues without the intention to implement a lint, a contributor will hopefully be found
  * During collaboration, the SCRC team is proposed as mostly reviewing the implementation of lints to ensure they work with all examples
  * There is are existing tutorial information, which could be a guide to SCRC members
  * Clippy is not looking to do global analysis, and will doing a crate by crate analysis
  * How does Clippy deal with undecidable rules?
    1. If Clippy can determine a violation it shows a message, if it can prove no violation then no message, the question is for when Clippy can’t know
    2. It entirely depends on the lint, some false positives are acceptable, sometimes false negatives are acceptable
  * Are most Clippy lints done on the MIR level?
    1. Clippy has its own const evaluator which is used for some lints
  * Does Clippy denote undecidable lints on [their lint page](https://rust-lang.github.io/rust-clippy/master/index.html)?
    1.  It might be good to add this to the database for SCRC use cases
    2. There are two possible ways to look at decidability, one from a theoretical point of view (guidelines), one from a tool point of view (Clippy)
    3. No objection to adding that classification, but that might be a good deal of work to label them
  * Proposed easy to implement lints
    1. [The 'as' operator should not be used with numeric operands](https://coding-guidelines.arewesafetycriticalyet.org/coding-guidelines/expressions/gui_ADHABsmK9FXz.html#gui_ADHABsmK9FXz)
    2. [Avoid out-or-range shifts](https://coding-guidelines.arewesafetycriticalyet.org/coding-guidelines/expressions/gui_LvmzGKdsAgI5.html)
    3. [Do not shift an expression by a negative number of bits or by greater than or equal to the bitwidth of the operand](https://coding-guidelines.arewesafetycriticalyet.org/coding-guidelines/expressions/gui_RHvQj8BHlz9b.html)
    4. [Do not use an integer type as a divisor during integer division](https://coding-guidelines.arewesafetycriticalyet.org/coding-guidelines/expressions/gui_7y0GAMmtMhch.html)
* MISRA C Mapping
  * The work has already been done by Alex C, etc.
  * Markus has been working on this
* MISRA C++ Mapping
  * Douglas and Max have expressed interesting performing this mapping
  * The SCRC is looking to purchase some copies for the institution
* CERT C Mapping
  * Useful feedback has been provided on all of the batches of issues
  * There are still some loose ends to some of the feedback, and the original poster may be tagged ask for clarification
* Break-out Sessions
  * Group batch 1
    1. PRE31: Agreed, might split this out into a [separate advisory guideline](https://github.com/Safety-Critical-Rust-Consortium/safety-critical-rust-coding-guidelines/issues/557)
  * Group batch 2
    1. PRE30: Agree; no observations
    2. DCL38: Agree; no observations
    3. EXP35: Agree; no observations
    4. EXP43: Agree; should only be taken into consideration when writing `unsafe` Rust and having lifetimes be involved
    5. ARR32: Agree; no observations
    6. ARR38: Agree; Would be interesting to have a general position with respect to recreating C-like behavior (e.g. a field that represents the size of a data structure) when an idiomatic Rust solution exists. However FFI does stand out as an area where this is likely to be necessary.
    7. STR32: Should be taken into consideration when writing `unsafe` Rust, specially with FFI/C-bindings (`CStrings`)
    8. FIO34: Should be taken into consideration depending on the use-case; `no-std` projects may need the raw bytes
* Round Table
  * Macros are hard
  * There is a discussion on [batch 4](https://github.com/Safety-Critical-Rust-Consortium/safety-critical-rust-coding-guidelines/issues/430#issuecomment-4074338619) about FFI, please take a look at the second part of the linked comment if you have thoughts
  * FFI is an important design space to think about guidelines in, and CERT C can teach us about interfacing with C

## **Material**

Any material to read before the meeting should be included here.
