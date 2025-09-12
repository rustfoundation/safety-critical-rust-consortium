# **Coding Guidelines Subcommittee Meeting on 2025-09-10 @ 0900 CEST**

[Link](https://www.worldtimebuddy.com/?qm=1&lid=5,100,2643743,12,1850147,2193733,1880252,8,6&h=5&date=2025-9-2&sln=20-21&hf=1) to meeting time in common time zones.

| Search Key | Description |
| :---- | :---- |
| \[todo\] | Action Item |
| \[decision\] | Something decided on |
| \[important\] | Key information |

## **Agenda**

1. Solicitation of notetaker  
2. Acceptance of [Previous Meeting Minutes](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/coding-guidelines/meetings/2025-09-02/minutes.md)  
5. Review guidelines that are in-progress as Github issues
   * [List of in-progress issues](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues?q=state%3Aopen%20label%3A%22coding%20guideline%22%20label%3A%22status%3A%20draft%22)

## **Check-in area**

**Please add your name, and an emoji that describes your day.**

* Christof Petig
* Oreste Bernardi
* Markus Hosch
* Sam Wright

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

* Search for the \[todo\] markers

## **Meeting Minutes**

* Previous notes accepted
* List of issues we looked at:
  * https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/97
    Heads-up to author
  * https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/133
    Heads-up to the autor, added some questions
  * https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/137
    Heads-up to author, covert to PR?
  * https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/174
    Check already-existing comments and point out that the compiler should be able to catch that / tell the developer
    where it _could_ be a problem, at least for constants. Point out the human readability issue?
  * https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/156
    Looks very similar to #174. How to handle?
  * https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/185
    What about explicitly allowing smaller -> larger while not changing the signedness? There's already a clippy lint
    that warns you in case one's using "as" in non-safe scenarios, so why not allow that?

## **Material**

Any material to read before the meeting should be included here.

* Milestone: [Prepare for launch to wider Rust community](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1)  
* [Github Issue to discuss about panicking in Safety Critical](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/158)

