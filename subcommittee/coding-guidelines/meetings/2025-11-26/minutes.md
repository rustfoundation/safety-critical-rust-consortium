# **Coding Guidelines Subcommittee Meeting on 2025-11-25 @ 20:00 EST / 2025-11-26 10:00 CET**

[Link](https://www.worldtimebuddy.com/?qm=1&lid=5,100,2643743,12,1850147,2193733,8,6,2673730,1261481&h=5&date=2025-11-25&sln=20-21&hf=1) to meeting time in common time zones.

| Search Key | Description |
| :---- | :---- |
| \[todo\] | Action Item |
| \[decision\] | Something decided on |
| \[important\] | Key information |

## **Agenda**

1. Solicitation of notetaker
2. Acceptance of [Previous Meeting Minutes](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/coding-guidelines/meetings/2025-11-12/minutes.md)
3. Introduction of new members
4. Review progress on guidelines incorporated from CERT
   * [High-level mapping of CERT rule groups to Rust](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/152)
     * Integers - Félix Fischer
     * Arrays - Alex Celeste
     * Floating Point - Andrew Fernandes
5. Merging of [https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/149](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/149) has happened
   * Have a read on GOALS.md, README.md and CONTRIBUTING.md and think about valuable additions and clarifications
   * Please start incorporating updates (e.g. from review comments) as separate PRs
6. Proposals and ideas for new rules
   * Idea: Give room for the optional step 0 in our contributing guideline, aka "round table for new rules".
7. Grooming of rule issues \- promote to PRs if appropriate
8. Round table

## **Check-in area**

**Please add your name, and an emoji that describes your day.**

* Pete LeVasseur 🦀💤
* Mikhail Antoshkin ☕
* Slava Barinov 👂
* Yuchen Shen
* Robert C. Seacord

**Notetaker:**

* Slava Barinov

For tips on how we take notes in the Safety-Critical Rust Consortium, please see the [Meeting Notetaker Role](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/docs/notetaker-role.md) doc.

## **Housekeeping section**

* Document space: [coding-guidelines](https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines)
* Zulip: [safety-critical-consortium: Coding Guidelines](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/Coding.20Guidelines)
* [Kanban board](https://github.com/orgs/rustfoundation/projects/1/views/3)
  * [`contributor experience`](https://github.com/orgs/rustfoundation/projects/1/views/4) view
  * [`coding guideline`](https://github.com/orgs/rustfoundation/projects/1/views/5) view

## **Tasks**

* \[todo\] @PLeVasseur: reply to [#202](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/202)
* \[todo\] @rcseacord: discuss the [#185](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/185) details

## **Meeting Minutes**

* CERT status
  * Integer PRs  [#180](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/180) and [#181](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/181) were merged.
  * PRs [#220](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/220) for arithmetic overflow has been prepared.
* Floating Point [requests](https://wiki.sei.cmu.edu/confluence/pages/viewpage.action?pageId=87152181) are marked as a good place to start contribution.
  * New contributors can check the [Contribution Guidelines](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/blob/main/CONTRIBUTING.md) to begin.
* Merge of [#149](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/149) happened and introduced basic structure for further guideline development.
* Splitting guidelines’ parts into safe and unsafe and explicitly.
  * \[idea\] Align with CERT C and highlight the differences from Rust.
  * Currently there’s a draft [#152](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/152)  of mapping from CERT C to Rust
  * \[idea\] check if there are other certified languages (FORTRAN, ADA?) to compare and check if there are guides for FFI and other cross-language related parts.
* Issue backlog grooming
  * Issue [#202](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/202)
    * This looks related to the "Attributes" section in the Man Pages project: description of thread and memory safety. Possibly, the approach can be reused.
    * Ideally this should be checked by compiler or tooling. Currently the contracts exploration issue [#137134](https://github.com/rust-lang/rust/issues/137134) exists.
  * Issue [#185](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/185)
    * \[idea\] Need to add saturation semantics usage into the proposal?

## **Material**

Any material to read before the meeting should be included here.

* Milestone: [Prepare for launch to wider Rust community](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1)
* FLS Maintenance: [FLS Team - North Star](https://hackmd.io/@plevasseur/HJb6qomOge/edit)
* [Github Issue to discuss about panicking in Safety Critical](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/158)
