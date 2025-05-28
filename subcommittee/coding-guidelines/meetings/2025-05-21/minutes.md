# Coding Guidelines Subcommittee Meeting on 2025-05-21 @ 10am Eastern Time

[Conversion](https://www.worldtimebuddy.com/?qm=1&lid=5,100,2643743,12,1850147&h=5&date=2025-5-21&sln=10-11&hf=1) between common time zones of attendees.

| Search Key | Description |
| :---- | :---- |
| \[todo\] | Action Item |
| \[decision\] | Something decided on |
| \[important\] | Key information |

## Agenda

1. Having a notetaker
2. Acceptance of [Previous Meeting Minutes](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/coding-guidelines/meetings/2025-05-07/minutes.md) ([temporary link](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/ae944768533f529f3002460102f9da4b5d034b66/subcommittee/coding-guidelines/meetings/2025-05-07/minutes.md), as it’s still in PR)
3. Introduction of new members
4. Core Guidelines Team Discussion \- If you’re happy to take on a bit more ownership 👍- 5 mins
   1. Alex Celeste, Lukas Wirth, Sam Wright, Pete LeVasseur currently
   2. Meet up once extra per week for 15 \- 30 minutes to check into progress of owned bits
5. Review of [revised milestone](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1) focused on broad \+ deep approach to macros chapter \- 5 mins
6. Identify Clippy lints to go "backwards" from and create guidelines for (looking for a volunteer to work with the core team\!) \- 5 mins
   1. Step 1: Identify the clippy checks that seem worthwhile: David S.
   2. Step 2: Come up with strategy that works for linking bidirectionally
7. Discuss the logistics of pushing coding guidelines through to Clippy lints \- 10 mins
   1. Lukas Wirth will try this in parallel with Pete LeVasseur
   2. Met with Vitaly Bragilevsky this morning, discussed potential for 3-5 guidelines being implemented in RustRover IDE as suggestions (looking for a volunteer to work with the core team\!)
      * He emphasized they are open to helping community efforts\!
      * Could be a test bed for suggestions to check if they make sense as Clippy lints\!
8. Fleshing out Coding Guidelines portion of [arewesafetycriticalyet.org](http://arewesafetycriticalyet.org) (looking for a volunteer to work with the core team\!) \- 5 minutes
   1. Add deployment of coding guidelines to [coding-guidelines.arewesafetycriticalyet.org](http://coding-guidelines.arewesafetycriticalyet.org)
   2. Flesh in other contents, e.g. MISRA C Rust Addendum working with Tooling & Liaison
9. Working session:
   1. Based on feedback of Clippy team on difficulty of macros for Clippy, let's open up for any chapter's guidelines \- 10 mins
10. Discuss [proposal](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/75#issuecomment-2885697090) for how to proceed with coding guidelines style / scope \- 10 mins
11. Review session:
    1. Review open [PRs](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pulls) & [issues](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues) \- 5 mins
12. Round table \- 5 mins

## Check-in area

**Please add your name, and an emoji that describes your day.**

* Pete LeVasseur, 🏃💨🙊
* Enow Scott 🤧
* Robert C. Seacord 🙊
* Oreste Bernardi
* Andrew Fernandes ☕☕☕
* Douglas Deslauriers 🧵
* Lukas Wirth 🤧
* El Araby El Mahdi 🏔️🌋
* Joni Pelham 🤧
* Jonas Wolf 🦀
* Alex Celeste ☕
* David Svoboda ;)
* Koppany Pazman
* Tiago Manczak
* Fernando 😴
* Markus Hosch 🦀
* Christof Petig 🤹
* Alexandru Vochescu

**Notetaker:**

* Andrew Fernandes

## Housekeeping section

* Document space: [coding-guidelines](https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines)
* Zulip: [safety-critical-consortium: Coding Guidelines](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/Coding.20Guidelines)
* [Early Alpha Milestone](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1)
* [Work Item Board](https://github.com/orgs/rustfoundation/projects/1)

## Tasks

* See below for the \[todo\] markers

## Ideas for Coding Guidelines\! {#ideas-for-coding-guidelines!}

* Clippy lint 2 “absurd comparisons” (concrete defect)
* Ordered refutable patterns behind irrefutable? (stylistic/subset)
* If a function makes use of unsafe its body, then the function shall be marked unsafe.

## Meeting Minutes

**\[TODO\]**

* \[Pete L\] Ask vendor if they want to be named in the minutes
* \[Pete L\] Create list of “asks from the group to the vendor”
  * Give the vendor “first bragging rights” or “enhanced functionality” for safety critical, possibly?
* \[Alex C\] [arewesafetycriticalyet.org](http://arewesafetycriticalyet.org) items, below
* \[Markus H\] Coding guidelines chapter ([ABI & FFI](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/85))
* Note that Procedural macros can create arbitrary spans, and that’s what makes them more dangerous, so they need their own guidelines.

**Minutes**

* Review of previous meeting minutes, accepted
* Introduction of new members
* Agenda is large, items will have to be triaged
* There is now a small “core guidelines” team/sub-team
  * “Not more authority, just more work to do” 😆
  * They meet 15-30 min extra per week, everyone welcome
* Review of [revised milestone](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1) focused on broad \+ deep approach
  * Deadline might be unrealistic given rate of progress
* **\[ASK\]** Help investigate Integrating coding guideline lints with [Clippy lints](https://rust-lang.github.io/rust-clippy/master/index.html)
  * Investigate the possibility of going the “other direction”, meaning for a “safety critical” Clippy profile, have it bidirectionally link to the Safety Critical Coding Guidelines
  * Suggestion to start at the “rule” and use them to form the Clippy profile
    * Implies every SCCG should be linked to one or more Clippy lints
  * Discussion of how to use a hypothetical “safer Clippy”
    * [Partial RFC: Custom lint profiles](https://hackmd.io/@Manishearth/BJi8K8AGJg)
  * **Note**: there are actually **two** linters in Rust, Clippy and `rustc`
    * [Rustc lint list](https://doc.rust-lang.org/rustc/lints/listing/allowed-by-default.html)
  * There was a volunteer to begin triaging Clippy lints
  * Suggestion to allow vendors to contribute lints
    * Vendors see this as “kinda’ marketing”
    * But it gets people excited and gets *actual contributions*
  * Clippy will have a 12-week feature freeze starting on 2025-06-26
    * Small numbers of lints are created, modified, etc continually
  * Logistics of pushing coding guidelines to Clippy lints
    * There were early discussions with a commercial tool vendor about integrating lints
    * Possibility of working with the vendor to implement (currently) missing embedded functionality in “exchange” for being “first to the post” or “bragging rights”
* Looking for a volunteer to work on the Coding Guidelines portion of [arewesafetycriticalyet.org](http://arewesafetycriticalyet.org)
* Open “what to work on” session, ask for volunteers
  * Open section above for [Ideas for Coding Guidelines\!](#ideas-for-coding-guidelines!)
* Re-opening of discussion of “macro safety”
  * Declarative *vs* Procedural macros
  * Procedural macros can create arbitrary spans, and that’s what makes them more dangerous
  * There were some tabled items re how and what to approach this complex topic
* More discussion re: generic \+ trait complexity

## Material

Any material to read before the meeting should be included here.

### GitHub Project Board for Work Items

* [Work Item Board](https://github.com/orgs/rustfoundation/projects/1)
* [Coding guidelines published](https://github.com/rustfoundation/safety-critical-rust-consortium/issues/188#issue-2869798433): Proposes a way of work to tackle the coding guidelines
