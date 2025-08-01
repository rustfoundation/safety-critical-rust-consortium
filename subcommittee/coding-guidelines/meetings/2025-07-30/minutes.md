# **Coding Guidelines Subcommittee Meeting on 2025-07-30 @ 0800 BST / 0900 CEST / 1600 JST**

[Link](https://www.worldtimebuddy.com/?qm=1&lid=14,12,1850147&h=14&date=2025-7-30&sln=8-9&hf=1) to meeting time in common time zones.

| Search Key | Description |
| ----- | ----- |
| \[todo\] | Action Item |
| \[decision\] | Something decided on |
| \[important\] | Key information |

## **Agenda**

1. Solicitation of notetaker  
2. Acceptance of [Previous Meeting Minutes](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/coding-guidelines/meetings/2025-07-22/minutes.md)  
3. Introduction of new members  
4. Infrastructure  
   * [New Issue to PR system is live](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/122)  
   * [More than one pair of examples per guideline](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/141)  
5. Review progress on guidelines incorporated from CERT  
   * [High-level mapping of CERT rule groups to Rust](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/152)  
   * [INT34-C](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/156) adoption  
6. Checked arithmetic guidelines  
   * [Division by zero](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/132)  
   * [Checked arithmetic operations](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/136)  
   * [Use of the `unchecked` APIs](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/148)  
7. Other reviews  
   * [Recursive functions](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/135) (ready to merge \- test signoff system)  
8. Emergent discussions:  
   * From checked arithmetic: rules about `unsafe` (part of the [overall guideline strategy w.r.t “defects” vs “subsets”](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/142))  
   * [From matching types at the language boundary](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/137)  
   * [Rules about `panic`](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/158)  
   * From INT36-C adoption: New section for pointers and provenance (affects [ordering](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/157))  
9. Round table

## **Check-in area**

**Please add your name, and an emoji that describes your day.**

* Alex Celeste ☕  
* Fernando Jose ☕  
* Achim Kriso 🐦  
* Christof Petig 🚲  
* Tiago Manczak

**Notetaker:**

* Fernando

For tips on how we take notes in the Safety-Critical Rust Consortium, please see the [Meeting Notetaker Role](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/docs/notetaker-role.md) doc.

## **Housekeeping section**

* Document space: [coding-guidelines](https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines)  
* Zulip: [safety-critical-consortium: Coding Guidelines](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/Coding.20Guidelines)  
* [Early Alpha Milestone](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1)

## **Tasks**

* Search for the \[todo\] markers

## **Meeting Minutes**

* Approval of previous minutes.  
* No new people introduced.  
* Infrastructure topic, more than one pair of examples per guideline. Mention the other infrastructure topic.  
* CERT guidelines.  
  * Unless we overlooked, it appeared that guidelines corresponding to CERT  INT32-C and INT35-C hadn't been added.
  * Taking a look at [the issue inspired by INT34-C](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/156). Call for comments.  
    * It is asked if this is already covered by the checked arithmetic guideline. Encouraged to comment on the issue. A comment will be added \[todo\].  
  * Taking a look at [the issue about categorization](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/152). Call for comments. No comments.  
  * Taking a look at the checked arithmetic and division by zero pull requests. Discussion on the overlap, which comes from the CERT rules.  
  * [Discussing the issue about unchecked](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/148)   
    * Stemming from [the comment about unsafe](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/148#issuecomment-3089428786): subset-oriented approach and unsafe. Different approaches are possible based on how to deal with unsafe (blocks).  
      * Historical context about the use of unsafe added. 3rd party code in cybersecurity. Probably wanted to ban unsafe in that case. In functional safety, differently, "everything is under control". Then, there are interesting categories relating to drivers and what the actual definition of unsafe is; beyond the Rust definition? All in all, avoiding unsafe is desired, but banning it totally is going too far. It would rather be desired to push it to the bottom of the code. A follow-up comment: there will be rules (guidelines) which are only sensible to apply in the context of unsafe.  
    * It’s suggested to refrain from considering the unchecked operations in insolation \[important\].  
  * [https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/137](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/137)  
    * Recommendation to only use types without fixed bitwidths at the language boundaries. But, is it practical?  
  * [https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/158](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/158)  
    * [Similar in CERT C++](https://wiki.sei.cmu.edu/confluence/pages/viewpage.action?pageId=88046339)  
  * Call for comments on a new section for pointers and provenance.  
    * It sounds good. It is suggested that provenance isn’t part of integers. It can be part of unsafe, noting that the unsafe section may become rather large.  
  * [https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/135](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/135)  
    * Looks like it is in a good state. Should it be moved to the new system? We start doing it during the meeting. Adding the label. The action is triggered and a pull request opened. It looks like a good start, the code example may have not been copied over correctly \[todo\]  
  * Round table  
    * About panics, in addition to static analysis, since they’re in a way similar to unsafe, would it be feasible to use a way similar to what’s used for unsafe? In terms of documentation, justifying it the panicking state.   
      * An initial reaction is checked exceptions.  
      * Maybe there’s wording for it already in SAE.

## **Material**

Any material to read before the meeting should be included here.

### **GitHub Project Board for Work Items**

* [Work Item Board](https://github.com/orgs/rustfoundation/projects/1)

