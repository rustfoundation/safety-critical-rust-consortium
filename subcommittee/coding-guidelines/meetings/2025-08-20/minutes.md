# **Coding Guidelines Subcommittee Meeting on 2025-08-20 @ 0800 BST / 0900 CEST / 1600 JST /  0300 EDT**

[Link](https://www.worldtimebuddy.com/?qm=1&lid=14,12,1850147,5&h=14&date=2025-8-20&sln=8-9&hf=1) to meeting time in common time zones.

| Search Key | Description |
| ----- | ----- |
| \[todo\] | Action Item |
| \[decision\] | Something decided on |
| \[important\] | Key information |

## **Agenda**

1. Solicitation of notetaker  
2. Acceptance of [Previous Meeting Minutes](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/coding-guidelines/meetings/2025-08-06/minutes.md)  
3. Introduction of new members  
4. Review progress on guidelines incorporated from CERT  
   * [High-level mapping of CERT rule groups to Rust](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/152)  
     * Integers \- Félix  
     * Arrays \- Alex  
     * Floating Point \- Andrew (he will be unable to attend next few meetings; caught up offline and it's on his todo list)  
5. Infrastructure \- review [milestone](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1) ahead of launch to wider Rust community  
   * [References per guideline, generate reference addendum](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/147)  
     * Sam will begin work here; if anyone is interested in collaborating reach out  
   * [Extract and test Compliant and Non-compliant code blocks](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/91)  
     * Mehdi is getting this close, but worth discussing open items found during discussion [here](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/91#issuecomment-3166713858) and [here](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/91#issuecomment-3172402940)  
6. Development of FLS maintenance capabilities  
   * Pete volunteered to champion this [t-spec goal](https://rust-lang.github.io/rust-project-goals/2025h2/FLS-up-to-date-capabilities.html) because we rely on the FLS as an upstream dependency  
   * Pete drafted this [FLS Team \- North Star](https://hackmd.io/@plevasseur/HJb6qomOge/edit) document as a rallying point in the Consortium to gather interest  
7. Discussion session  
   * Pointers and provenance \-- how to categorize?  
   * Performance, other observations, recommendations vs rationale ([177](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/177))?  
8. Round table

## **Check-in area**

**Please add your name, and an emoji that describes your day.**

* Alex Celeste ☕  
* Alex Senier 😴  
* Oreste Bernardi⛰️  
* Tiago Manczak ☕  
* Achim Kriso 🍵  
* Christof Petig 😴  
* Tshepang Mbambo 😶

**Notetaker:**

* Christof Petig

For tips on how we take notes in the Safety-Critical Rust Consortium, please see the [Meeting Notetaker Role](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/docs/notetaker-role.md) doc.

## **Housekeeping section**

* Document space: [coding-guidelines](https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines)  
* Zulip: [safety-critical-consortium: Coding Guidelines](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/Coding.20Guidelines)  
* [Early Alpha Milestone](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1)

## **Tasks**

* Search for the \[todo\] markers

## **Meeting Minutes**

* US/APAC schedule is not popular enough to be sustainable. Please raise your voice if you want it continued.  
* Question about when to create an issue: Issues are good for discussion, they are not ideal for content creation. An issue is a good anchor for a topic.  
  * Agreement that every new rule created as a PR should be accompanied by an Issue for discussion  
* Question about whole document review: This is the purpose of the third review stage. Should be added to the process documentation. Being able to view the document as a  whole helps reviewing. Sourcing contributions from outside the consortium is part of that review process.  
  * For now we concentrate on creating content.  
* We are still looking for a good way to link to MISRA because of not public accessibility of rules.  
* The tooling group is looking for volunteers to help with FLS updates.  
  * Ideally the FLS would become part of the language evolution and provide value beyond qualification. If a benefit is found it could help language evolution itself.  
  * The SCRC should advertise this goal across the Rust community. On C/++ the spec helps the whole project.  
  * Right now neither the FLS nor the Reference is the source of truth, most of the time the compiler is the definition of the language.  
* Pointers and provenance: The name seems to be a good description of the topic.  
* Proposal: Guidelines could also help with performance if a more specific code would be more performant. Traditionally guidelines ignore performance, it is clearly of lower importance. Better maintainability or understandability of the code is usually accepted as providing value for safety guidelines.  
  In the context of division and zero checked we look for examples, once rules offer little additional value we can clearly deprioritize them and return to them later.  
* Proposal: a Kanban board for issues could help focusing on issues which are in progress.  
* The SCRC could try to contact the organization behind [the ANSSI guidelines](https://github.com/ANSSI-FR/rust-guide/) to see whether there is still momentum behind current activity on github.  
  * Author is a member of the Consortium so this should be possible to arrange

## **Material**

Any material to read before the meeting should be included here.

* Milestone: [Prepare for launch to wider Rust community](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1)  
* FLS Maintenance: [FLS Team \- North Star](https://hackmd.io/@plevasseur/HJb6qomOge/edit)

### **GitHub Project Board for Work Items**

* [Work Item Board](https://github.com/orgs/rustfoundation/projects/1)

