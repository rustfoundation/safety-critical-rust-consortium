# Coding Guidelines Subcommittee Meeting on 2026-02-25 @ 17:00 JST / 09:00 CET

[Link](https://www.worldtimebuddy.com/?qm=1&lid=2643743,12,5,1850147,100&h=2643743&date=2026-2-25&sln=8-9&hf=1) to meeting time in common time zones.

| Search Key | Description |
| :---- | :---- |
| \[todo\] | Action Item |
| \[decision\] | Something decided on |
| \[important\] | Key information |

## **Agenda**

* Solicitation of notetaker
* Acceptance (and approval) of Previous Meeting Minutes
* Introduction of new members
* PSA: Change to meeting weekly at 5 pm CET on Wed
  * Monthly meeting Japan mornings time Pete will inform.
* Suggestions for topics & issues/PRs to discuss
* Update on rule inflow, e.g. what about CERT rule translation
* Releasing: Check milestone and discuss timeline / further needed actions.
* Progress on mapping rules to clippy lints (or vice versa?). How to document our desired strategy aka merging the following PRs:
  * https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/82
  * https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/78
  * https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/86
  * https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/201
* Handling of uncovered language parts (https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/394)
* Round table


## **Check-in area**

* Samuel Wright ☕
* Oreste Bernardi 🚶
* Markus Hosch &☕
* Yuchen Shen ☕
* Andrew Herridge

**Please add your name, and an emoji that describes your day.**

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

* Set up a matrix for CERT C and MISRA rule as PR to add them to the rendered guidelines
* Add the milestone review to the US/EU and US/Asia agendas
* Try to consolidate clippy issues into the two discussed
* Find someone in S-Core who can present the S-Core safety process

## **Meeting Minutes**

1. (Not so) temporary notetaker found
2. Previous minutes accepted by consensus
3. No new members so far
4. Asia/Pacific meeting now monthly, Pete will inform next week about EU/Asia meeting
5. Additional topics?
   * Update on rule status
6. Progress on rule topics
   * Clippy lints: (find issue, discussed in point 8)
   * CERT C tracking issue: https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/336, progress to be discussed here.
   * Question: Would we need to label issues that “import” from other sources?
   * Question: How to determine the MVP for the ruleset. Suggestion: Work on adding issues to the milestone, let this be the single point of truth.
7. Releasing the rules
   * A clear definition of MVP is needed.
     * Industry standards like CERT & MISRA have to be mapped, the mapping needs to be “sufficiently good” → All rules have been considered and mapped to SCR coding guidelines.
     * Mapping means either mapped to (an) existing rule(s), or it’s naked as not covered → An issue needs to exist to make that rule covered.
     * Create issues for remaining missing topics based on the completeness of the MISRA/CERT lists and add them to the MVP milestone.
8. Consolidate clippy vs rules
   * No more than two issues should exist:
     * Translate clippy lints to rules
     * Link existing rules to clippy lints
   Common agreement: Neither of the tasks need to be part of the MVP. Reasoning: Standards are mandatory, rule checking can be done within projects first.
9. Dealing with uncovered language parts (skipped)
10. Round table
    * S-Core wants to release Rust software that is qualifiable by the end of Feb
    * S-Core claims safety qualified OSS. Suggestion: Have a presentation at the Rust SIG inside Eclipse

## **Material**

Any material to read before the meeting should be included here.

* Milestone: [Prepare for launch to wider Rust community](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1)
