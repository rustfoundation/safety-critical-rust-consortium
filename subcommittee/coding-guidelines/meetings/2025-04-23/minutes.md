# Coding Guidelines Subcommittee Meeting on 2025-04-23 @ 10am Eastern Time

[Conversion](https://www.worldtimebuddy.com/?qm=1&lid=5,100,2643743,12,1850147&h=5&date=2025-4-23&sln=10-11&hf=1) between common time zones of attendees.

| Search Key | Description |
| :---- | :---- |
| \[todo\] | Action Item |
| \[decision\] | Something decided on |
| \[important\] | Key information |

## Agenda

1. Acceptance of [Previous Meeting Minutes](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/coding-guidelines/meetings/2025-04-16/minutes.md)
2. Introduction of new members
3. Review of [milestone](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1) ahead of RustWeek meetup
4. Working session:
   * Goal: everyone has the ability to build the coding guidelines locally
   * Troubleshooting getting coding guidelines working
5. Review session:
   * Review [declarative macro guideline PR](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/16)
      * attempt to merge Monday the following week
   * Review other open PRs & issues
6. Round table

## Check-in area

**Please add your name, and an emoji that describes your day.**

* Pete LeVasseur, 🥱
* Espen Albrektsen, 🙂
* Andrew Fernandes ☕☕☕
* Samuel Wright ☕☕☕
* Alex Celeste 🙂
* Markus Hosch 🤧
* Walter Pearce (Rust Foundation) 😴
* Douglas Deslauriers 🙂
* Joel Marcey (Rust Foundation) 🥱
* Christof Petig 🤯
* Alexandru Vochescu 😴
* Andrew Herridge 😀
* Achim Kriso 🦆
* Enow Scott 🥱
* Lukas Wirth

**Notetaker:**

* Markus Hosch

## Housekeeping section

* Document space: [coding-guidelines](https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines)  
* Zulip: [safety-critical-consortium: Coding Guidelines](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/Coding.20Guidelines)
* [Work Item Board](https://github.com/orgs/rustfoundation/projects/1)

## Tasks

* See below for the [todo] markers

## Meeting Minutes

* No new members present, so no introduction(s)
* First guidelines milestone:
  * Three chapters have been introduced, 5 guidelines each as a start / blueprint, see
    [milestone 1](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1)
  * Request to open one PR per chapter to assess the process and make progress, will also be broadcast on Zulip
* Working session
  * Request to test the guidelines build by checking out the repo, running “make” to see whether ItWorksEverywhere™
  * [todo] \(PL to open an issue) Add a prerequisites section to the README.md
  * [todo] \(PL on same issue as above) document “--offline” build flag
  * [todo] \(EA to open a PR) Document how to build on Windows
  * Verified platforms: Linux, Windows (minor changes needed), macOS/WSL (Directly running make.py)
  * Running a local server doesn’t work out of the box due to missing deps → [todo] AK to create a PR fixing that
* Interlude: Link to survey “Rust adoption in the industry”: https://www.surveyhero.com/c/rustscadoption25
* Discussion of first guideline PR (https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/16)
  * Lots of comments, thanks for that!
  * Shows the necessity to clarify terms
  * Question: Code coverage and macros: Would we essentially prohibit macros by requiring coverage?
    * Given requirements on the macro, one could test its functionality by covering those
    * Would we need one or more guidelines to cover testing macros?
    * MISRA has some guidelines on code generation, might be used as a source for Rust guidelines
    * Macro testing: “Trusting the generator” means “trusting the compiler doing the transformation right”. Given this,
      we could still end up with bad code since macros behave very differently, depending on what the input does. We can
      solve this in two ways:
      - Fully cover the generated code
      - Put constraints on the allowed inputs (like assumptions of use for safety elements out of context as done to
        other system parts)
    * Rust behaves similar to C in terms of macros since they behave different depending on the surroundings and the
      context 
    * We might want to differentiate between the macro types (procedural vs. declarative macros)
    * C++ also has a similar “macro system”, called templates (esp. with SFINAE being [over]used). Same issues appear
      here as well and the C++ folks also need to tackle it, sometimes to the extent of prohibiting macros, which isn’t
      really useful.
    * [todo] \(MH/AC) Issue shall be opened for “How to treat macros in safety critical context”
      * We should find a way how to check whether “the right input” is used (tests that are supposed to fail? Have some
        sort of static checks in place? Is something missing here?)
  * Merge target for PR #16 is Monday, Apr 28th
* [todo] Add an agenda point for next time, talking about the standards matrix
  (https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/7)
* Skimming thru the open issues for the coding guidelines


## Material

Any material to read before the meeting should be included here.

### GitHub Project Board for Work Items

* [Work Item Board](https://github.com/orgs/rustfoundation/projects/1)
* [Coding guidelines published](https://github.com/rustfoundation/safety-critical-rust-consortium/issues/188#issue-2869798433): Proposes a way of work to tackle the coding guidelines

### Tracking Issues

* [Early Alpha Milestone](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1) ahead of meeting at RustWeek

