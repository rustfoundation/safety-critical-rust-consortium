# **Coding Guidelines Subcommittee Meeting on 2025-07-16 @ 1600 BST / 1700 CEST / 1100 EDT / 2025-07-17 @ 0000 JST**

[Conversion](https://www.worldtimebuddy.com/?qm=1&lid=14,12,5,1850147&h=14&date=2025-7-16&sln=16-17&hf=1) between common time zones of attendees.

| Search Key | Description |
| ----- | ----- |
| \[todo\] | Action Item |
| \[decision\] | Something decided on |
| \[important\] | Key information |

## **Agenda**

1. Solicitation of notetaker  
2. Acceptance of [Previous Meeting Minutes](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/coding-guidelines/meetings/2025-07-02/minutes.md)  
3. Introduction of any new members  
4. Review of [revised and rescoped milestone](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1) focused on shaking out initial issues with coding guidelines process and philosophy \- 5 mins  
5. Discussion \- 15 mins  
   * Discuss provenance and the `std::ptr` API (Felix, David)  
6. Working session \- 20 mins  
   * Read through [CERT C rules](https://wiki.sei.cmu.edu/confluence/display/c/2+Rules) together a bit  
   * Identify sections and folks that would like to translate these into the Rust coding guidelines  
     * [Rule 04\. Integers (INT)](https://wiki.sei.cmu.edu/confluence/pages/viewpage.action?pageId=87152052)  
     * [Rule 05\. Floating Point (FLP)](https://wiki.sei.cmu.edu/confluence/pages/viewpage.action?pageId=87152181)  
     * [Rule 03\. Expressions (EXP)](https://wiki.sei.cmu.edu/confluence/pages/viewpage.action?pageId=87152200)  
7. Review session \- 10 mins  
   * Review open [PRs](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pulls) & [issues](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues)  
8. Round table \- 5 mins

## **Check-in area**

**Please add your name, and an emoji that describes your day.**

* Alex Celeste ☕  
* David Svoboda :)  
* Enow Scott 🙂  
* Andrew Fernandes ☕🥱  
* [Robert C. Seacord](mailto:robert.seacord@woven-planet.global) 😣  
* Douglas Deslauriers 🏙️  
* Oreste Bernardi🫤  
* Tiago Manczak ☺️  
* Achim Kriso 🦆  
* El Araby El Mahdi 🌋👍  
* Christof Petig 🌧️

**Notetaker:**

* David Svoboda

## **Housekeeping section**

* Document space: [coding-guidelines](https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines)  
* Zulip: [safety-critical-consortium: Coding Guidelines](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/Coding.20Guidelines)  
* [Early Alpha Milestone](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1)

## **Tasks**

* Search for the \[todo\] markers

## **Meeting Minutes**

* Solicitation of notetaker  
* Acceptance of [Previous Meeting Minutes](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/coding-guidelines/meetings/2025-07-02/minutes.md)  
* Introduction of any new members  
* Review of [revised and rescoped milestone](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1) focused on shaking out initial issues with coding guidelines process and philosophy \- 5 mins  
* Discussion \- 15 mins  
  * Discuss provenance and the `std::ptr` API (Felix, David), based on an informal discussion in the sync meeting yesterday after investigating INT36-C  
  * Two forms of provenance, strict and exposed, investigated based on the last three clauses of INT36 \- the new API should make it unnecessary to go through bare integer representations in order to apply things like masks with the strict provenance option; there is also the exposed option for when this is absolutely necessary i.e. for hardcoded hardware addresses  
  * Rust has the same concepts of alignment as C does; same concepts of “pointing to an entity” as C does; trap representations are more specific to C  
  * Leads to a question: does this group care about \`unsafe\` as well as safe code? Should there be a distinction in the rules? Are we currently creating guidelines applicable to \`unsafe\`? Current consensus is that the group has not yet made this distinction  
  * The second paragraph raises some interesting questions about the permissiveness of the \`as\` operator and what can be converted to/from a pointer; exposes older assumptions that \`usize\` will always be the right size for pointers; want a Clippy lint for conversions between \_any\_ pointer and integer pairings \- \`usize\` is no longer guaranteed to be sufficient for this  
  * Third paragraph is less concerning for guidelines  
  * A lot of the knowledge about this is centralized into individuals \- an issue for many aspects of the language and its operational semantics  
  * Three tiers of support, documented in https://doc.rust-lang.org/rustc/platform-support.html  
  * tier 1 \= Intel & ARM (no embedded systems)  
  * Indicates a model of support for platforms; does not indicate what Rust aims to support.  
  * Do we want a rule "use only tier 1 platforms"?  
  * This would rule out lots of embedded platforms.  
* Working session \- 20 mins  
  * Read through [CERT C rules](https://wiki.sei.cmu.edu/confluence/display/c/2+Rules) together a bit  
  * Identify sections and folks that would like to translate these into the Rust coding guidelines  
    * [Rule 04\. Integers (INT)](https://wiki.sei.cmu.edu/confluence/pages/viewpage.action?pageId=87152052)  
    * [Rule 05\. Floating Point (FLP)](https://wiki.sei.cmu.edu/confluence/pages/viewpage.action?pageId=87152181)  
    * [Rule 03\. Expressions (EXP)](https://wiki.sei.cmu.edu/confluence/pages/viewpage.action?pageId=87152200)  
* Review session \- 10 mins  
  * Review open [PRs](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pulls) & [issues](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues)  
    * [https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/132](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/132) (do not divide by zero)  
      * The spec does not indicate what x / 0 actually does, but it seems to panic on some platforms.  
      * Been reviewed by Felix, please look offline & provide feedback.  
    * Request for action item to create issue about unsafe vs. safe tag on guidelines.  
* Round table \- 5 mins  
  * Seacord: For https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/137  
  * (Use matching types at the language boundary)  
    * Seacord: Interface using\_matching\_types at language boundaries. How concerned are we about portability? At CERT we limit "safe" labels to working on a particular platform. An interface that uses C short or char would never be portable?  
    * Alex: This might warrant a guideline  
    * Svoboda: yes. There is no C interface. Instead there is one interface to x86-64-Linux-GCC C, one to x86-32-Linux-Clang, and so on. Each has implementation-defined integer sizes, and most functions rely on them.  
    * Seacord: We could use several more code examples: one with static assertions, one with fixed-width C types.  
    * Alex: This is a rich area for mistakes.  
  * Douglas: FLS Speclock file is out of date.  I will update.

## **Material**

Any material to read before the meeting should be included here.

### **GitHub Project Board for Work Items**

* [Work Item Board](https://github.com/orgs/rustfoundation/projects/1)

