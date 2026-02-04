# **Coding Guidelines Subcommittee Meeting on 2026-01-21 @ 1700 CEST / 1100 EDT**

[Link](https://www.worldtimebuddy.com/?qm=1&lid=2643743,12,8,5&h=5&date=2026-1-21&sln=11-12&hf=1) to meeting time in common time zones.

| Search Key | Description |
| :---- | :---- |
| \[todo\] | Action Item |
| \[decision\] | Something decided on |
| \[important\] | Key information |

## **Agenda**

1. Solicitation of notetaker  
2. Acceptance of [Previous Meeting Minutes](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/coding-guidelines/meetings/2026-01-14/minutes.md)  
3. Introduction of new members  
4. `@guidelines-bot` and its use (Pete)  
   * Helps fairly distribute reviews in round-robin fashion to Producers  
   * Other abilities too, leave a comment as @guidelines-bot /commands to see what's possible  
5. Tags for coding guidelines (Félix)  
   * [Tags List for Safety Critical Guidelines](https://docs.google.com/spreadsheets/d/1SPhThaQhJOTvMyuyq8Buu-OVZ2D1CiosofrUmOGONqk/edit?gid=0#gid=0)  
6. CERT C \=\> Rust Mapping (Félix / David)  
   * Some [open questions](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/336#issuecomment-3678192763)  
7. Batch of rules from Robert C. Seacord involving `unsafe`. Who could support that’s `unsafe`\-knowledgable? (Félix)  
   * You can “@guidelines-bot /claim” on these if you feel it’s possible to support reviewing these issues / PRs  
8. Rust Project Goals (Pete)  
9. Proposals and ideas for new rules (all)  
10. Progress on ongoing tasks (all)  
11. Round table

## **Check-in area**

* Pete LeVasseur 🦀⛑️  
* David Svoboda (:  
* Douglas Deslauriers ⛷️  
* Julius Gustavsson 🤕  
* Fernando :-)  
* Oreste Bernardi 🫥   
* Markus Hosch 🥳  
* Félix Fischer 😪  
* Max Jacinto ⚽  
* Alex Celeste ☕  
* Arthur Hicken 🎙️

**Please add your name, and an emoji that describes your day.**

**Notetaker:**

* David Svoboda (:

For tips on how we take notes in the Safety-Critical Rust Consortium, please see the [Meeting Notetaker Role](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/docs/notetaker-role.md) doc.

## **Housekeeping section**

* Document space: [coding-guidelines](https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines)  
* Zulip: [safety-critical-consortium: Coding Guidelines](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/Coding.20Guidelines)  
* [Kanban board](https://github.com/orgs/rustfoundation/projects/1/views/3)  
  * [`contributor experience`](https://github.com/orgs/rustfoundation/projects/1/views/4) view  
  * [`coding guideline`](https://github.com/orgs/rustfoundation/projects/1/views/5) view

## **Tasks**

* xx

## **Meeting Minutes**

* Notetaker: David Svoboda  
* Acceptance of [Previous Meeting Minutes](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/coding-guidelines/meetings/2026-01-14/minutes.md)  
  * Any concerns?  None  
* Introduction of new members  
  * None  
* `@guidelines-bot` and its use (Pete)  
  * Guidelines bot used to automate nagging people to review guidelines within 14 days.  Could make it into Github app.  Assigns review of new coding guidelines to SC reviewers in a round-robin fashion.  Overview of creating a new guideline and how to review it.  
  * Markus: We decided a reviewer could be distinct from an assignee.  
  * Douglas: Assignee on an issue is responsible for writing the coding guideline. Assignee on a merge request reviews it and makes comments.  
  *   
* Felix: Have you seen this [spreadsheet](https://docs.google.com/spreadsheets/d/1SPhThaQhJOTvMyuyq8Buu-OVZ2D1CiosofrUmOGONqk/edit?gid=0#gid=0) which lists guideline tags?    
  If you provide a tag not on this list, you need to modify a Python code file to add it. Alternatively, we could add tags and have the document provide a list of tags. Our current system has the advantage that each tag has a description.  
  * Pete: Good idea. Tags are free-form. Our tag list is not comprehensive.  
* CERT C \=\> Rust Mapping (Félix)  
  * We could use a good task list. I've created an [issue](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/336) about which CERT C rules would make good Rust guidelines. David and I are reviewing this list because some rules map well, others may map poorly or not at all.  I have a table of CERT rules (mostly about concurrency) that I need better Rust understanding to determine their Rust eligibility. We welcome your review of which rules would apply, such as MEM30-C.  
  * Oreste: Do we restrict these rules to Rust, the core library…what?  
  * Felix:  The idea is to never go outside the standard library. For example, serde is popular, so we might decide to include it.  
  * Oreste: We should document that then, that we just cover core \+ standard library.  
  * Felix: For example CON30-C is not applicable to the Rust core, but does in the standard library (thread-local storage).  
  * Pete: I've raised an [issue](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/245) about our scope.  
* [Batch of rules](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pulls/rcseacord) involving `unsafe` \- knowledgeable folks? (Félix)  
  * Created by Robert, with open pull requests. They need reviewers…any volunteers?  
  * David: Robert did not use our rule autogenerator, but instead created a raw AST file. I'll try to look at one of these.  
  * Pete: You can use the guidelines bot to claim one of these.  
* Rust Project Goals (Pete)  
  * In progress. I hope to be done by late January or early February.  
* Proposals and ideas for new rules (all)  
* Progress on ongoing tasks (all)  
* Round table  
  * David: A client has requested a complete Rust security standard before they start coding in Rust. So we'd like it done ASAP, in theory. Even if we release an incomplete draft standard.  
  * Arthur: I've heard the same from our clients.

## **Material**

Any material to read before the meeting should be included here.

* Milestone: [Prepare for launch to wider Rust community](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1)

