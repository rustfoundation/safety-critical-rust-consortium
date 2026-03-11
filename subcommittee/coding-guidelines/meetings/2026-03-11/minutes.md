# **Coding Guidelines Subcommittee Meeting on 2026-03-11 @ 1600 CET / 1100 EDT**

[Link](https://www.worldtimebuddy.com/?qm=1&lid=5,12,2643743,8,1850147,100,14&h=5&date=2026-3-11&sln=11-12&hf=1) to meeting time in common time zones.

| Search Key | Description |
| :---- | :---- |
| \[todo\] | Action Item |
| \[decision\] | Something decided on |
| \[important\] | Key information |

## **Agenda**

1. Solicitation of notetaker
2. Acceptance of [Previous Meeting Minutes](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/coding-guidelines/meetings/2026-03-04/minutes.md)
3. Introduction of new members
4. CERT C \=\> Rust Mapping (Félix / David / Jubilee)
   * WIPs are resolved\!
5. Coverage of MISRA C and CERT C in 2026 (Félix / Markus)
   * i.e. “create a table” and “create corresponding issues”
6. Proposals and ideas for new rules (all)
7. Progress on ongoing tasks (all)
8. Round table

## **Check-in area**

* Pete LeVasseur 🦀🏃
* Douglas Deslauriers ⛷️
* Oreste Bernardi 🥷
* Markus Hosch 🫥
* Félix Fischer :)
* Julius Gustavsson 🙂

**Please add your name, and an emoji that describes your day.**

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

* \[Pete\] Use the review bot to assign producers to chunks of CERT C mapping rationales
* \[Markus\] Open a PR for a MISRA C mapping in a separate appendix file
* \[Félix\] Open a PR for the CERT C mapping in a separate appendix file

## **Meeting Minutes**

* Previous meeting minutes
  * Unanimous acceptance
* CERT C \=\> Rust Mapping
  * First step in the process can be considered completed
  * A preliminary mapping has been created for
    1. Rules that do NOT map to Rust
    2. Rules that do map to safe Rust
    3. Rules that map to unsafe Rust
    4. Unsure if it maps
  * This mapping will add legitimacy to our guidelines, since safety critical assessors are already familiar with MISRA and CERT C
  * All CERT C rules have been reviewed, and have been sorted \[important\]
  * A request to review rationale for the entire table in the [Github issue \#336](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/336) has been made
    1. The rules will be chunked and assigned with the bot \[todo\]
    2. The reviews will occur and be placed in the issue
  * It was noted that the rationale for many mapping references Zulip, and a published document should embed the quotations or information directly
  * Most rationale for the mappings are quite short, especially for rules that do not map
  * The (much) longer rationales could be separated from the table, and just contain a short sentence with a link or footnote
  * Proposed placing the mappings in the Appendix \[decision\]
* Round Table
  * Time could be used during meeting for detailed discussions on existing Github issues

## **Material**

Any material to read before the meeting should be included here.

* Milestone: [Prepare for launch to wider Rust community](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1)

