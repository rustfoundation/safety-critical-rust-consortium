# **Coding Guidelines Subcommittee Meeting on 2025-12-16 @ 20:00 EST / 2025-12-17 10:00 JST**

[Link](https://www.worldtimebuddy.com/?qm=1&lid=5,1850147,212&h=5&date=2025-12-16&sln=20-21&hf=1) to meeting time in common time zones.

| Search Key | Description |
| ----- | ----- |
| \[todo\] | Action Item |
| \[decision\] | Something decided on |
| \[important\] | Key information |

## **Agenda**

1. Solicitation of notetaker
2. Acceptance of [Previous Meeting Minutes](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/coding-guidelines/meetings/2025-11-26/minutes.md)
3. Introduction of new members
4. Merging of [https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/251](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/251) has happened to update [CONTRIBUTING.md](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/blob/main/CONTRIBUTING.md) to latest workflow
   * Mini walkthrough
   * Have a read on GOALS.md, README.md and CONTRIBUTING.md and think about valuable additions and clarifications
   * If you can think of other ways to improve contribution, please open an issue with
5. Proposals and ideas for new rules
   * Idea: Give room for the optional step 0 in our contributing guideline, aka "round table for new rules".
6. Grooming of rule issues - promote to PRs if appropriate
7. Round table

## **Check-in area**

**Please add your name, and an emoji that describes your day.**

* Robert C. Seacord/@rcseacord
* Pete LeVasseur/@PLeVasseur
* Mikhail Antoshkin/@mikhailantoshkin
* Slava Barinov/@rayslava

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

* Mikhail Antoshkin - leave comment on [#284](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/284) regarding Sphinx versioning.

## **Meeting Minutes**

* Accepted the [Previous Meeting Minutes](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/coding-guidelines/meetings/2025-11-26/minutes.md)
* Issue Grooming
  * Discussion of [#303](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/303): agreed that the approach seems good.
  * Discussion of [#286](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/286): discussion of terms and standards.
    * SAE [JA1020](https://www.sae.org/standards/ja1020-recommendations-rust-programming-language-safety-related-systems) uses the "safety-related" term.
    * The naming is still to be discussed in the issue comments.
  * Discussion of [#284](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/284):
    * Accepted the idea of splitting into different pages.
  * Discussion of [#272](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/272)
    * Accepted that versioning is definitely needed for standards/guidelines.
  * Discussion of [#271](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/271)
	* There are no defined standards for publishing to align with.
	* We don't want to align with ISO requirements due to their complex processes.
  * Checking the [#255](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/255)
	* Current version works just fine, waiting for more feedback in the comments.

## **Material**

Any material to read before the meeting should be included here.

* Milestone: [Prepare for launch to wider Rust community](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1)
* FLS Maintenance: [FLS Team \- North Star](https://hackmd.io/@plevasseur/HJb6qomOge/edit)
* [Github Issue to discuss about panicking in Safety Critical](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/158)
