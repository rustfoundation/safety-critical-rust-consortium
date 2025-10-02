# **Coding Guidelines Subcommittee Meeting on 2025-10-01 @ 0800 BST / 0900 CEST / 1600 JST / 0300 EDT**

[Link](https://www.worldtimebuddy.com/?qm=1&lid=14,12,1850147,5&h=14&date=2025-10-1&sln=8-9&hf=1) to meeting time in common time zones.

| Search Key | Description |
| ----- | ----- |
| \[todo\] | Action Item |
| \[decision\] | Something decided on |
| \[important\] | Key information |

## **Agenda**

1. Solicitation of notetaker  
2. Acceptance of [Previous Meeting Minutes](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/coding-guidelines/meetings/2025-09-17/minutes.md)  
3. Introduction of new members  
4. October 14th, 15th \- Global Virtual Meetup  
   * Agenda posted to Zulip and shared on mailing list  
   * [Link](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/2025.20Late.20Year.20Global.20Virtual.20Meetup/near/540871684) to Zulip message with agenda in PDF  
5. Share launch milestone & Kanban board (Pete)  
   * [Prepare for launch to wider Rust community](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1)  
   * [Kanban board](https://github.com/orgs/rustfoundation/projects/1/views/3)  
     * [`contributor experience`](https://github.com/orgs/rustfoundation/projects/1/views/4) view  
     * [`coding guideline`](https://github.com/orgs/rustfoundation/projects/1/views/5) view  
6. Review Clippy lint \=\> coding guidelines categorization (David, Félix)  
   * [Tracking issue: Identify Clippy lints suitable for creating safety-critical guidelines](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/86)  
7. Review progress on guidelines incorporated from CERT  
   * [High-level mapping of CERT rule groups to Rust](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/152)  
     * Integers \- Félix  
     * Arrays \- Alex  
     * Floating Point \- Andrew  
8. Round table

## **Check-in area**

**Please add your name, and an emoji that describes your day.**

* Alex Celeste ☕  
* Antoshkin Mikhail 👻  
* Samuel Wright ☕☕☕  
* Oreste Bernardi 🧑‍💼  
* Alex Senier 😶‍🌫️  
* Markus Hosch ✍️  
* Joni Pelham 🐕  
* Tiago Manczak  
* Achim Kriso  
* Daniel Krippner 🆕  
* Tshepang (arrived 30m late)

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

* Suggestion: Accept meeting minutes in the matching timeslot  
* New member introducing himself  
* Call to everyone: Add things to the agenda for Oct 14th, 15th  
  * Suggestion: Rule flavors (\[todo\] Markus will post on Zulip)  
  * Suggestion: Discuss “rule buddies” / review partners (\[todo\]: Markus will post on Zulip)  
* Checking the Kanban board, general impression: progress is slow atm, due to availability, maybe also lack of review comments?  
* Items 6 and 7: Not much progress that could be reported  
* Discussions on “don’t use proc macros”: Probably necessary as a stop gap until we can refine the rule so that in less restrictive tiers we can then reduce workloads on projects, removing the need for argumentations on rules  
* Possibly thin line between “too generic and unusable” and “guidelines never get finished”  
* Comment on “no macros”: Trick used on C compilers is “do not qualify the macro machinery, check the generated code”. Seems not feasible on Rust at the moment (\[todo\] Alex: Find the compiler issue on github/rust-lang)  
* Tooling offers to add this to their list, list to be done. Tolling will ping once the list is available.  
* Round table  
  * Discussion on two coding guidelines: Provide safe abstractions, Do not cause undefined behavior  
    * Rules are very general: We could add those rules, but as a different kind, being the ground truth that can be detailed by other rules. The rules themselves do not help developers a lot, and from a project point of view, arguing that such a general rule is fulfilled becomes a ruleset of its own. Suggestion: There is a comprehensive list of undefined behavior or behavior where it’s not known whether its UB, and the rule should be broken into these points.  
    * How to make progress: As soon as the formal requirements are fulfilled, things should get merged.  
    * Discussion on guideline scope. MISRA rules are applied to whole products, so that system knowledge can be assumed  
    * \[todo: Markus\] Create ticket to add the scope for the guidelines in their preamble  
    * Question: Would documenting deviations (in this case, use of the unsafe keyword) be put into a rule? Would it be better to “document” preconditions as attributes?  
    * Rule is actually a duplicate: The Rust reference manual already says that, but it’s not a problem and repetition might be desirable.  
  * Call for help: wg23-language-vulnerabilities needs helping hands, please respond on Zulip if you’re interested

## **Material**

Any material to read before the meeting should be included here.

* Milestone: [Prepare for launch to wider Rust community](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1)  
* FLS Maintenance: [FLS Team \- North Star](https://hackmd.io/@plevasseur/HJb6qomOge/edit)  
* [Github Issue to discuss about panicking in Safety Critical](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/158)

