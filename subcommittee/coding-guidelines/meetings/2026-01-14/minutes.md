# **Coding Guidelines Subcommittee Meeting on 2025-12-03 @ 0800 UTC / 0900 CET / 1700 JST / 0300 EST**

[Link](https://www.worldtimebuddy.com/?qm=1&lid=14,12,1850147,5&h=14&date=2026-01-14&sln=8-9&hf=1) to meeting time in common time zones.

| Search Key | Description |
| :---- | :---- |
| \[todo\] | Action Item |
| \[decision\] | Something decided on |
| \[important\] | Key information |

## **Agenda**

1. Solicitation of notetaker  
2. Acceptance of [Previous Meeting Minutes](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/coding-guidelines/meetings/2025-12-03/minutes.md)
3. Introduction of new members
4. Review progress on guidelines incorporated from CERT
   * High-level mapping of CERT rule groups to Rust
     * Integers - Félix Fischer
     * Arrays - Alex Celeste
     * Floating Point - Andrew Fernandes
5. Proposals and ideas for new rules  
6. Progress on ongoing tasks
   * PR https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/256 seems stalled. Should we assign someone?
   * PR https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/240 seems stalled. Should we assign someone?
   * Issue https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/29 should be split into coding guidelines. Discuss their headlines.
7. Round table

## **Check-in area**

* Jonatan H. Zeidler ☺️
* Roberto Bagnara 🏃‍♂️
* Markus Hosch 🧐
* Fernando Jose 🙂
* William Barsse

**Please add your name, and an emoji that describes your day.**

**Notetaker:**

* Jonatan H. Zeidler

For tips on how we take notes in the Safety-Critical Rust Consortium, please see the [Meeting Notetaker Role](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/docs/notetaker-role.md) doc.

## **Housekeeping section**

* Document space: [coding-guidelines](https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines)  
* Zulip: [safety-critical-consortium: Coding Guidelines](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/Coding.20Guidelines)  
* [Kanban board](https://github.com/orgs/rustfoundation/projects/1/views/3)  
  * [`contributor experience`](https://github.com/orgs/rustfoundation/projects/1/views/4) view  
  * [`coding guideline`](https://github.com/orgs/rustfoundation/projects/1/views/5) view

## **Tasks**

Markus Hosch: Find out whether and where we have rules on how to structure a guideline (e.g. order of sections, length of rationale etc.). This should probably be in Contributing.md.
Oreste Bernardi: Take ownership of PR 256 (foster the completion)
Markus Hosch: talk with Pete about whether there is an issue in CI (PR 240 and 256 seem blocked)
Markus Hosch: will turn Issue #29 into separate issues

## **Meeting Minutes**

1. Solicitation of notetaker -> done
2. Acceptance of Previous Meeting Minutes -> accepted
3. 2 new members introduced themselves (Jonatan H. Zeidler and Roberto Bagnara)
4. Review progress on guidelines incorporated from CERT
   * Involved people are not present -> skipping
5. Progress on ongoing tasks
   * PR https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/256 seems stalled. Should we assign someone?
     * Seems rather complete (also: correctness over completeness)
     * Contributing.md does not have anything about structure (e.g. about the need and extend of a rationale)
     * Oreste Bernardi takes ownership (as main reviewer)
   * PR https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/240 seems stalled. Should we assign someone?
   * Issue https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/29 should be split into coding guidelines. Discuss their headlines.
     * Discussed first bullet point about offsetting raw pointers. There was no clear consensus about whether raw pointers to zero sized types should be prohibited in the first place or just offset operations on it.
     * \*const/mut () might be simply incorrect when used for type erasure, because `()` is the unit type being a unique value not in memory
     * `core::ffi::c_void` is not zero-sized btw
     * Markus will split the issue into multiple issues
6. Proposals and ideas for new rules
7. Round table
   * A question was raised about central coordination of writing the guidelines -> there is a Kanban board in Github
   * A question was raised about the ultimate goal
     * limit what you can with the language via guideline and enable tool committee to enforce this by lints
     * On the one hand it is meant to prevent pitfalls, on the other hand being even stricter by disallowing correct code patterns to reduce complexity and thus improve safety, there may be strict rules as well as enforced user based decisions


## **Material**

Any material to read before the meeting should be included here.

* Milestone: [Prepare for launch to wider Rust community](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1)  
* FLS Maintenance: [FLS Team \- North Star](https://hackmd.io/@plevasseur/HJb6qomOge/edit)  
* [Github Issue to discuss about panicking in Safety Critical](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/158)

