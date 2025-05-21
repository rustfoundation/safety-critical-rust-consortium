# Coding Guidelines Subcommittee Meeting on 2025-05-07 @ 10am Eastern Time

[Conversion](https://www.worldtimebuddy.com/?qm=1&lid=5,100,2643743,12,1850147&h=5&date=2025-5-7&sln=10-11&hf=1) between common time zones of attendees.

| Search Key | Description |
| :---- | :---- |
| \[todo\] | Action Item |
| \[decision\] | Something decided on |
| \[important\] | Key information |

## Agenda

1. Notetaker role
2. Acceptance of [Previous Meeting Minutes](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/coding-guidelines/meetings/2025-04-30/minutes.md)
3. Introduction of new members
4. Review of [revised milestone](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1) focused on broad \+ deep approach to macros chapter \- 5 mins
5. Working session:
   * Goal: Sketch out broad strokes of macros chapter guidelines titles, everyone snags a guideline to work on
     * Together we sketch in as many titles as we can to identify "shape" of chapter \- 30 mins
       * PRs from everyone suggesting ideas\!
     * We divvy up the sketched in titles to folks \- 10 mins
6. Review session:
   * Review material subcommittee will present at RustWeek Consortium meetup, solicit feedback \- 5 mins
   * Review open [PRs](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pulls) & [issues](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues) \- 5 mins
7. Round table \- 5 mins

## Check-in area

**Please add your name, and an emoji that describes your day.**

* Pete LeVasseur, 🖱️
* Robert C. Seacord
* Espen Albrektsen, 🙂
* Marc Schoolderman 🫨
* El Mahdi El Araby ⛰️
* Andrew Fernandes 🥱
* Alex Celeste ☕
* Stephen Hedrick 🤠
* Oreste Bernardi
* Jonas Wolf 🦀
* Douglas Deslauriers 🙂
* Enow Scott 🙂
* Lukas Wirth
* Markus Hosch 🤓
* Arthur Hicken 🤖
* Joel Marcey 🤔
* Achim Kriso 🙂

**Notetaker:**

* Andrew Fernandes

## Housekeeping section

* Document space: [coding-guidelines](https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines)
* Zulip: [safety-critical-consortium: Coding Guidelines](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/Coding.20Guidelines)
* [Early Alpha Milestone](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1) ahead of meeting at RustWeek
* [Work Item Board](https://github.com/orgs/rustfoundation/projects/1)

## Tasks

* See below for the \[todo\] markers

## Macros Chapter Guidelines {#macros-chapter-guidelines}

Add here\! We will PR these in\!

* Always use fully qualified module paths in macros (`::std::vec::Vec`)
  * Important to always write the rationale\!
* **[todo]** **[Espen]** Do not hide unsafe blocks within macro expansions
  * Robert: from CERT / “right” 😆perspective a little too strong, too prohibitive
    * E.g. in CERT may instead require some sort of annotation
  * E.g. what does “hide” mean in this instance?
    * Good word for headline so long as amplification explains this
  * How do we write this rule in a fashion to make clear its importance?
  * How do we write this in a positive manner?
* **[todo]** **[Alex]** use path-based scoping for macro identifiers
* Establish a strategy how to test macros
* **[todo]** **[Andrew]** Macros should be *testable* (both positive and negative tests)
  * Is *“complete testability”* necessary and sufficient for “safety” of macros?
* **[todo]** **[Alex]** procedural macros shall not access external resources
* **[todo]** **[Marc]** procedural macros shall be side effect free (pure)
* **[todo]** **[Mahdi]** a macro should not be used in place of a function
* **[todo]** **[Oreste]** Cyclomatic complexity of macro.
  * Rationale: In some cases using a macro is safer than not using it. Macro protect from human error when replicating the same code. However complex macros can be more dangerous than manual code. A cyclomatic complexity index could help to decide when is safer to use a macro.
  * “Clone extraction” / “outlining”?

## Useful material in introduction

* Compare and contrast Rust macros with:
  * The C/C++ Preprocessor
  * C++ Metatemplate Programming
* Discussion of the differences between Procedural and Declarative Rust macros
* Macro use cases for unsafe code to make it safer

## Meeting Minutes

* **\[todo\] list**
  * (OB) Add a GitHub issue regarding macro testability
  * (multiple) assignments for [Macros Chapter Guidelines](#macros-chapter-guidelines)
* Review of the [revised milestone](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1)
* **Ask** for everyone in the corporate world to comment in GitHub to show, publicly, interest in Safety Critical Rust
* Discussion of “How to test Macros” among members
  * Spirited discussion regarding the basic *“How to test macros?”* question
  * Discussion of Rust macros *vs* C++ templates and monomorphization, or the addition of linker veneers, or link-time optimization…
  * Overview of [MISRA’s view, recapped](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/59#issue-3029401380)
* Group “macro guidelines” discussion
  * Use “positive” language, rather than “negative” or “thou shalt not” language
  * This is a bit of a “cultural divide” within the safety critical community
    * Rationale (as per MISRA) is that “thou shalt not rules” are for *non-technical* people to understand and provides “falsifiability”
    * This encourages the development of “deviations” or “exceptions” that must be *explicitly* produced.
  * Assignments of people to open GH issues for discussion and action in [Macros Chapter Guidelines](#macros-chapter-guidelines)
* Ask that the Coding Guidelines apply to the source code, and the source code only. This is a contrast between the CERT and MISRA “positive *vs* negative” approaches.
* Overview of next week’s Coding Guidelines meeting/milestone

## Material

Any material to read before the meeting should be included here.

### GitHub Project Board for Work Items

* [Work Item Board](https://github.com/orgs/rustfoundation/projects/1)
* [Coding guidelines published](https://github.com/rustfoundation/safety-critical-rust-consortium/issues/188#issue-2869798433): Proposes a way of work to tackle the coding guidelines

