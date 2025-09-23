# **Coding Guidelines Subcommittee Meeting on 2025-09-17 @ 1100 EDT / 1700 CEST**

[Link](https://www.worldtimebuddy.com/?qm=1&lid=5,100,2643743,12,1850147,2193733,1880252,8,6,2673730&h=5&date=2025-9-17&sln=11-12&hf=1) to meeting time in common time zones.

| Search Key | Description |
| :---- | :---- |
| \[todo\] | Action Item |
| \[decision\] | Something decided on |
| \[important\] | Key information |

## **Agenda**

1. Solicitation of notetaker
2. Acceptance of [Previous Meeting Minutes](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/coding-guidelines/meetings/2025-09-10/minutes.md)
3. Introduction of new members
4. Share launch milestone & Kanban board (Pete)
   * [Prepare for launch to wider Rust community](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1)
   * [Kanban board](https://github.com/orgs/rustfoundation/projects/1/views/3)
     * [`contributor experience`](https://github.com/orgs/rustfoundation/projects/1/views/4) view
     * [`coding guideline`](https://github.com/orgs/rustfoundation/projects/1/views/5) view
5. Review draft process for submission of coding guidelines. Feedback welcome\!
   * [Pull request](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/149) containing draft process
6. Review progress on guidelines incorporated from CERT
   * [High-level mapping of CERT rule groups to Rust](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/152)
     * Integers \- Félix
     * Arrays \- Alex
     * Floating Point \- Andrew
7. Development of FLS maintenance capabilities (Pete)
   * Pete volunteered to champion this [t-spec goal](https://rust-lang.github.io/rust-project-goals/2025h2/FLS-up-to-date-capabilities.html) because we rely on the FLS as an upstream dependency
   * Pete drafted this [FLS Team \- North Star](https://hackmd.io/@plevasseur/HJb6qomOge/edit) document as a rallying point in the Consortium to gather interest and is looking for feedback
   * Discussions are forming in the Rust Project `t-spec` team for creating a Rust Project team to maintain and develop the FLS.
   * Gathering interest here\!
   * [https://rust-lang.github.io/fls/changelog.html](https://rust-lang.github.io/fls/changelog.html)
8. Round table

## **Check-in area**

**Please add your name, and an emoji that describes your day.**

* Andrew Fernandes ☕
* Pete LeVasseur 🧑‍💻
* Christof Petig 😊
* Félix Fischer ☕
* Alex Celeste ☕
* Douglas Deslauriers 🥐
* Oreste Bernardi
* Arthur Hicken 🤖
* Koppany Pazman
* Robert C. Seacord 😪
* Markus Hosch 🥳
* Tiago Manczak
* Gideon Mueller
* Will Cunningham ☕

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

* Search for the \[todo\] markers

## **Meeting Minutes**

* Previous Meeting Minutes
  * Mostly reviewing the state of existing PRs
  * Universal Acceptance
* Introduction of New Members
  * Gideon Mueller introduction
* Milestone for launch [\[link\]](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1)
  * Before publishing to the wider Rust community, this milestone should be completed
  * Mostly covers examples, and other things that would be helpful for first time contributors
  * There is a Kanban board [\[link\]](https://github.com/orgs/rustfoundation/projects/1/views/3) which can be used to check progress and pick up a task
  * Feedback has been solicited on [\#149](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/149)
    * Covers the goals of the guidelines
  * When should we publish?
    * Perhaps it should be marked as beta
    * Stability and Completeness might be better after 1.0.0
    * Possibly after the CERT C and MISRA inspirations have been reviewed
    * Anything that may not be covered yet, could be subsetted as defacto not allowed
* Contribution Workflow
  * Solicitation of feedback [\[link\]](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/149)
  * A diagram has been created to show the workflow
  * The diagram is accessible to screen readers
  * A notion of assignment might be necessary to keep things moving, perhaps to Producers in the subcommittee
* CERT C Guidelines Update
  * [\#180](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/180) and [\#181](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/181) are currently blocked on sphinx
  * Feedback solicited on issues [\#156](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/156), [\#174](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/174) and [\#185](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/185)
  * PRs incoming on the array and pointer provenance soon
  * Floating point PRs are in progress and coming soon, tentatively Friday
* On the topic of subsetting vs defect analysis how are these marked? [\[link\]](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/205)
  * There are tags for subset/defect analysis, but it isn’t a separate field
  * It would be nice to link related guidelines, specifically the subset and defect style
  * A “see also” would be quite useful in general
* FLS Maintenance Topic
  * Pete is now the point of contact for ensuring the FLS is maintained with future stable releases of Rust
  * There should be mutual interest from tool, compiler, and library vendors in ensuring this is updated. Especially the compiler vendors
  * Solicitation of volunteers to join the FLS Team
  * Likely the work should be fairly incremental, but sometimes there are releases with many changes
  * There have been some interviews at RustConf of those in the Safety Critical safe, and it seems that the Rust foundation is quite interested in safe Rust

## **Material**

Any material to read before the meeting should be included here.

* Milestone: [Prepare for launch to wider Rust community](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1)
* FLS Maintenance: [FLS Team \- North Star](https://hackmd.io/@plevasseur/HJb6qomOge/edit)
* [Github Issue to discuss about panicking in Safety Critical](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/158)
