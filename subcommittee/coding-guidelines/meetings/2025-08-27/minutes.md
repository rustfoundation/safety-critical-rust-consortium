# **Coding Guidelines Subcommittee Meeting on 2025-08-27 @ 1100 EDT / 1700 CEST**

[Link](https://www.worldtimebuddy.com/?qm=1&lid=14,12,1850147,5&h=14&date=2025-8-20&sln=8-9&hf=1https://www.worldtimebuddy.com/?qm=1&lid=5,100,2643743,12,1850147,2193733,1880252,8,6&h=5&date=2025-8-27&sln=11-12&hf=1) to meeting time in common time zones.

| Search Key | Description |
| :---- | :---- |
| \[todo\] | Action Item |
| \[decision\] | Something decided on |
| \[important\] | Key information |

## **Agenda**

1. Solicitation of notetaker  
2. Acceptance of [Previous Meeting Minutes](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/coding-guidelines/meetings/2025-08-20/minutes.md)  
3. Introduction of new members  
4. Share launch milestone & Kanban board (Pete)  
   * [Prepare for launch to wider Rust community](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1)  
   * [Kanban board](https://github.com/orgs/rustfoundation/projects/1/views/3)  
     * [`contributor experience`](https://github.com/orgs/rustfoundation/projects/1/views/4) view  
     * [`coding guideline`](https://github.com/orgs/rustfoundation/projects/1/views/5) view  
5. Review progress on guidelines incorporated from CERT  
   * [High-level mapping of CERT rule groups to Rust](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/152)  
     * Integers \- Félix  
     * Arrays \- Alex  
     * Floating Point \- Andrew  
6. Development of FLS maintenance capabilities (Pete)  
   * Pete volunteered to champion this [t-spec goal](https://rust-lang.github.io/rust-project-goals/2025h2/FLS-up-to-date-capabilities.html) because we rely on the FLS as an upstream dependency  
   * Pete drafted this [FLS Team \- North Star](https://hackmd.io/@plevasseur/HJb6qomOge/edit) document as a rallying point in the Consortium to gather interest and is looking for feedback  
7. Discussion session  
   * "Under what circumstances is `panic`\-ing safety-critical software okay?" (Félix)  
     * Relevant [issue](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/158)  
   * “Should we create a list of rules we intend to create? I can imagine that such a list could facilitate contributions of people who don't have the big picture but are willing to take a single rule and just write it. If so, what is a good format and where should it live to maximize contributor experience” (Alex)  
   * “(Where) do we have a place to cover higher level concepts? I'm thinking of patterns like Newtype and Typestate which can reduce errors significantly.” (Alex)  
8. Round table

## **Check-in area**

**Please add your name, and an emoji that describes your day.**

* Pete LeVasseur 🧑‍💻  
* Andrew Fernandes 🤖 ☕  
* Christof Petig 😵‍💫  
* Sam Wright 📦🏠😭  
* Alex Senier 🫨  
* Matthew Butler😀  
* Tshepang Mbambo 😶  
* Oreste Bernardi ⛰️  
* Félix Fischer 🔋  
* EL Araby El Mahdi 🐌🔥

**Notetaker:**

* Andrew Fernandes

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

* Meeting start  
  * Review and acceptance of the last meeting minutes  
  * Introduction of new meeting members  
  * No “walk-in” topics were introduced  
* Overview and discussion of the “[Coding Guidelines, Milestone 1](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1)”  
  * Also see the “pre-alpha” [Kanban Board](https://github.com/orgs/rustfoundation/projects/1/views/3) (discussion)  
    * **\[todo\] @PLeVasseur** Proper Kanban-style access permissions  
    * **\[todo\] @PLeVasseur** Incorporate the KB into the meeting agenda  
* Discussion of CERT-C rules  
  * Example working [for the `INT` rules](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/152#issuecomment-3161474482)  
  * Spirited discussion re: integer operation overflow  
    * Especially the differences between Debug and Release mode  
      * See [`checked_shl`](https://doc.rust-lang.org/core/index.html?search=%22checked_shl%22) and [`checked_shr`](https://doc.rust-lang.org/core/index.html?search=%22checked_shr%22)  
    * [New guideline draft](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/196) created for how to handle the *consistency* between D/R modes, etc  
      * Note: depending on Cargo settings means that info about behavior of the code is no longer local to the code itself  
* FLS maintenance  
  * Ask for which members are interested in helping maintain the LS  
    * Please DM @PLeVasseur  
  * How to make sure the FLS → RLS stays in sync with the compiler?  
  * Example from Ferrocene ([traceability](https://public-docs.ferrocene.dev/main/qualification/traceability-matrix.html))  
* Discussion session  
  * Items punted until next meeting

## **Material**

Any material to read before the meeting should be included here.

* Milestone: [Prepare for launch to wider Rust community](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1)  
* FLS Maintenance: [FLS Team \- North Star](https://hackmd.io/@plevasseur/HJb6qomOge/edit)  
* [Github Issue to discuss about panicking in Safety Critical](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/158)

