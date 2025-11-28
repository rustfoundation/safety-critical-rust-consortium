# **Coding Guidelines Subcommittee Meeting on 2025-11-04 @ 2000 EST / 2025-11-05 1000 JST**

[Link](https://www.worldtimebuddy.com/?qm=1&lid=5,100,2643743,12,1850147,2193733,8,6,2673730,1261481&h=5&date=2025-11-4&sln=20-21&hf=1) to meeting time in common time zones.

| Search Key    | Description          |
| :------------ | :------------------- |
| \[todo\]      | Action Item          |
| \[decision\]  | Something decided on |
| \[important\] | Key information      |

## **Agenda**

1. Solicitation of notetaker
2. Acceptance of [Previous Meeting Minutes](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/coding-guidelines/meetings/2025-10-29/minutes.md)
3. Introduction of new members
4. Share launch milestone & Kanban board (Pete)
   * [Prepare for launch to wider Rust community](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1)
   * [Kanban board](https://github.com/orgs/rustfoundation/projects/1/views/3)
     * [`contributor experience`](https://github.com/orgs/rustfoundation/projects/1/views/4) view
     * [`coding guideline`](https://github.com/orgs/rustfoundation/projects/1/views/5) view
5. Review progress on guidelines incorporated from CERT (Pete)
   * [High-level mapping of CERT rule groups to Rust](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/152)
     * Integers \- Félix (Pete subbing in)
6. Round table

## **Check-in area**

**Please add your name, and an emoji that describes your day.**

* Pete LeVasseur 🥤
* Mikhail Antoshkin ☕
* Max Jacinto 👾
* Slava Barinov 🦀
* xx
* xx
* xx
* xx

**Notetaker:**

* Mikhail Antoshkin

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

* New member introduction: more observers from automotive industry
* Discussion on possibility to introduce Rust into IoT sector in mining industry
  * Best course of action is to ask on Rust Zullip
* Milestone to lunch to wider Rust community
  * Short overview of issues from the milestone
  * Introduction of kanban board for the milestone
    * Has more focus on contributor experience
  * Work is voluntary, so no hard deadlines
  * How to grab tickets
    * For now no clear process or marking of responsible person
    * If you see something that interests you in the milestone \- feel free to take it
* Guidelines progress
  * Mapping rules from CERT C
    * [https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/152](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/152)
    * Work on INT30-INT36 rules is in progress
    * Some sections like ARR need more discussion
  * Clippy
    * Subset of clippy lints that can be applicable to safety critical
    * What can be extracted into a coding guideline
* Round table
  * What is a good first issue and how to better organize the issues?
    * Good first issue is dependent on the skillset of the person
    * Issues need a look to prioritize them
    * \[todo\] have a mapping of issues with reasons for it ranking
  * How to decide what issue to grab
    * Prioritize unassigned or stale issues with no progress
      1. \[todo\]: mark stale issues/PRs to make it clear where help is needed
         * Copying the approach from Rust repo is a good first step
    * Milestone is first priority when deciding what issue to grab

## **Material**

Any material to read before the meeting should be included here.

* Milestone: [Prepare for launch to wider Rust community](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1)
* [Github Issue to discuss about panicking in Safety Critical](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/158)
