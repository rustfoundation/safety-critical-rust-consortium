# **Coding Guidelines Subcommittee Meeting on 2025-10-08 @ 1100 EDT / 1700 CEST**

[Link](https://www.worldtimebuddy.com/?qm=1&lid=5,100,2643743,12,1850147,2193733,8,6,2673730,1261481&h=5&date=2025-10-8&sln=11-12&hf=1) to meeting time in common time zones.

| Search Key | Description |
| :---- | :---- |
| \[todo\] | Action Item |
| \[decision\] | Something decided on |
| \[important\] | Key information |

## **Agenda**

1. Solicitation of notetaker  
2. Acceptance of [Previous Meeting Minutes](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/coding-guidelines/meetings/2025-10-01/minutes.md)  
3. Introduction of new members  
4. October 14th, 15th \- Global Virtual Meetup (Pete LeVasseur)  
   * Agenda posted to Zulip and shared on mailing list  
   * [Link](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/2025.20Late.20Year.20Global.20Virtual.20Meetup/near/540871684) to Zulip message with agenda in PDF  
5. Share launch milestone & Kanban board (Pete LeVasseur)  
   * [Prepare for launch to wider Rust community](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1)  
   * [Kanban board](https://github.com/orgs/rustfoundation/projects/1/views/3)  
     * [`contributor experience`](https://github.com/orgs/rustfoundation/projects/1/views/4) view  
     * [`coding guideline`](https://github.com/orgs/rustfoundation/projects/1/views/5) view  
6. Review Clippy lint \=\> coding guidelines categorization (David Svoboda, Félix Fischer)  
   * [Tracking issue: Identify Clippy lints suitable for creating safety-critical guidelines](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/86)  
7. Discuss collaboration with ANSSI regarding their Secure Rust Coding Guidelines (Pete LeVasseur)  
   * [deployed version](https://anssi-fr.github.io/rust-guide/)  
   * [repo](https://github.com/ANSSI-FR/rust-guide)  
8. \<= triage line \=\>   
9. WG23 Involvement \[Alex Celeste\]  
10. Review progress on guidelines incorporated from CERT  
    * [High-level mapping of CERT rule groups to Rust](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/152)  
      * Integers \- Félix Fischer  
      * Arrays \- Alex Celeste  
      * Floating Point \- Andrew Fernandes  
11. Round table

## People Pete had to admit, i.e. we need another Google Meet-friendly email address on file

* Daniel Krippner  
* Tshepang  
* Christof  
* Lachlan  
* Gideon  
* Max Jacinto

## **Check-in area**

**Please add your name, and an emoji that describes your day.**

* Pete LeVasseur ✈️🧑‍💻  
* Oreste Bernardi 🪂  
* Daniel Krippner 🙂  
* William Barsse :)  
* David Svoboda :)   
* Christof Petig (missing a wasm unicode symbol)  
* Félix Fischer 🥱☕  
* Samuel Wright 🌞   
* Robert C. Seacord 😣  
* Tshepang  
* Max Jacinto 👾

**Notetaker: Oreste Bernardi**

For tips on how we take notes in the Safety-Critical Rust Consortium, please see the [Meeting Notetaker Role](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/docs/notetaker-role.md) doc.

## **Housekeeping section**

* Document space: [coding-guidelines](https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines)  
* Zulip: [safety-critical-consortium: Coding Guidelines](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/Coding.20Guidelines)  
* [Kanban board](https://github.com/orgs/rustfoundation/projects/1/views/3)  
  * [`contributor experience`](https://github.com/orgs/rustfoundation/projects/1/views/4) view  
  * [`coding guideline`](https://github.com/orgs/rustfoundation/projects/1/views/5) view

## **Tasks**

* Is there a rule about type inference in Misra C++ ?   
* \[Pete\] Which is the strategy regarding the rule checking between Clippy and Rust compiler ?

## **Meeting Minutes**

* [Previous Meeting Minutes](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/coding-guidelines/meetings/2025-10-01/minutes.md) accepted  
* Introduction of new members:  
  * Daniel Kripper   
  * Lachlan Dowling  
  * William Barsse  
  * Max Jacinto Mestanza  
* Global Virtual Meetup  
  * Discussed information location (see agenda)  
  * Request to discuss with our organization on funding in person meetup.  
  * Presented agenda. If members have topics, it is possible to allocate them.  
* Launch milestone & Kanban board  
  * Open for contribution. Milestone reviewed.  
  * Kanban board presented.   
* Review Clippy lint  
  * David and Felix worked on which rules of Clippy can be useful.  
  * Presented a spreadsheet that is used to track the Clippy rule activity.  
  * Most of "suspicious" could become a good guideline rule.  
  * Some of the Clippy rules look like they address uncommon situations. Focus on useful rules. Red rules (not good rules), green good rules.  
  * Question: Do we need a general coding guidelines rule about type inference ? → Maybe a recommendation  
  * Question which is the strategy about warnings check in Clippy and compiler:  
    * Deprecated language features goes in compiler  
    * Performance rules to Clippy  
    * When a suspicious/correctness rule is stabilized, it could be moved from Clippy to Rust compiler  
* Discuss collaboration with ANSSI regarding their Secure Rust Coding   
  * There is an overlap with safety coding guidelines.  
  * The license is strange.  
  * It is not possible to be safe without being secure. → Make sense to have one guideline.  
* Round table  
  * Big appreciation of the presentation [Rust@Rivian](https://youtu.be/3RIxy9YE-Yk?list=PL2b0df3jKKiRFEuVNk76ufXagOgEJ9sBZ). Wish to have more companies coming out on Rust usage. 


## **Material**

Any material to read before the meeting should be included here.

* Milestone: [Prepare for launch to wider Rust community](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1)  
* FLS Maintenance: [FLS Team \- North Star](https://hackmd.io/@plevasseur/HJb6qomOge/edit)  
* [Github Issue to discuss about panicking in Safety Critical](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/158)

