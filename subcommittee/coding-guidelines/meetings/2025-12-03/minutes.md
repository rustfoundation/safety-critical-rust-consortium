# **Coding Guidelines Subcommittee Meeting on 2025-12-03 @ 0800 UTC / 0900 CET / 1700 JST / 0300 EST**

[Link](https://www.worldtimebuddy.com/?qm=1&lid=14,12,1850147,5&h=14&date=2025-12-3&sln=8-9&hf=1) to meeting time in common time zones.

| Search Key | Description |
| :---- | :---- |
| \[todo\] | Action Item |
| \[decision\] | Something decided on |
| \[important\] | Key information |

## **Agenda**

1. Solicitation of notetaker  
2. Acceptance of Previous Meeting Minutes  
   * Minutes for 2025-11-19 are missing  
3. Introduction of new members  
4. “Reviewer circle”  
   * Volunteers to go on a list of assignable reviewers  
   * If you want a PR reviewed for you, you could review the next one  
   * New policy: correct \> complete  
5. Merging of [https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/149](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/149) has happened  
   * Have a read on GOALS.md, README.md and CONTRIBUTING.md and think about valuable additions and clarifications  
   * Please start incorporating updates (e.g. from review comments) as separate PRs  
6. Focused PR reviews  
   * “Seacord’s Section”:  
     * [https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/234](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/234)  
     * [https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/220](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/220)  
     * [https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/232](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/232)  
   * Promoted issues:  
     * [https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/225](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/225/files)  
7. Proposals and ideas for new rules  
   * Idea: Give room for the optional step 0 in our contributing guideline, aka "round table for new rules".  
8. Grooming of rule issues \- promote to PRs if appropriate  
9. Round table

## **Check-in area**

**Please add your name, and an emoji that describes your day.**

* Markus Hosch 🍀  
* Alex Celeste ☕  
* Tiago Manczak  
* Oreste Bernardi  
* Achim Kriso  
* Christof Petig 🥣  
* X  
* X

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

* Minutes from 2025-11-19 need to be updated  
* Can only accept minutes from a slot everybody actually attended  
* Reviewer list to be written down either as a membership-style list or as a GitHub automation  
* Fix non-unique IDs on [https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/220](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/220)   
* Check whether non-unique IDs would be detected by CI  
* Merge [https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/232](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/232)  
* Figure out how to cross-reference rules inline (e.g. to refer to a title without literally repeating it). Exercise on an open PR  
* Emphasize the MISRA, CERT, Clippy etc work so that people check on Zulip whether there is already something in the works that watches their guideline suggestion

## **Meeting Minutes**

* Not accepting the meeting from 2025-11-19, PR needs to be updated, see [https://github.com/rustfoundation/safety-critical-rust-consortium/pull/510](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/510) \[TODO: Markus H.\]  
* Check for the meeting minutes from the NA/Pacific meeting \[TODO: ??\]  
* No new members  
* Call for volunteers for PR reviewers  
* Would we want to make all Producers to be reviewer? If no, we need to add another list of reviewers. We might also make Github auto-assign people to new PRs. \[TODO\]  
* Correct \> complete → We should actually formalize this a bit, so that it’s clear that a small but correct piece of content for each chapter is enough to get stuff merged.  
* Reviewing [https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/220](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/220)  
  * Maybe too many compliant examples? We might want to create an issue to reduce the number of examples to make the rule easier to comprehend  
  * Q: Does every subsection also have a state? → Yes, that’s how thie guidelines were designed  
  * Q: How do compiler flags influence the rule? → Seems there were some out-of-band discussions to avoid panics/aborts. We might want to consider compiler flags in the future  
  * Examples have the same ID from the examples, which is unintentional. Needs to be fixed before PR merge. Would CI see that? \[TODO: Alex or David: Update PR to use unique IDs\]  
  * PR can be merged after ID update  
* Review [https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/232](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/232)  
  * We might want to enable the tooling to refer to the title by link instead of repeating  
  * Having links inline makes the source harder to read → Do we want to add this to the guidelines as a general rule?  
  * Otherwise approved  
* Review [https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/234](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/234)   
  * Rule gets “reused” → We should not do that but create new rule, with the old rule being deprecated  
  * We might want to also support linking deprecated rules to other rules that replace the now-deprecated rule → Could be implemented by the rules linking facility used for subset vs defect. \[TODO: Markus H.\]  
  * Content is fine, though, we will progress with the merge once the rule has been turned into a new one.  
* Round table  
  * We would want to coordinate rule work by also using Zulip to find out whether someone else is working on that, e.g. because a similar rule is inside MISRA, CERT etcpp  
  * Same story for clippy lints. One could work on lints, but coordinating might still be beneficial to avoid double work.  
  * We might want to link that to the reviewer circle?

## **Material**

Any material to read before the meeting should be included here.

* Milestone: [Prepare for launch to wider Rust community](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1)  
* FLS Maintenance: [FLS Team \- North Star](https://hackmd.io/@plevasseur/HJb6qomOge/edit)  
* [Github Issue to discuss about panicking in Safety Critical](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/158)

