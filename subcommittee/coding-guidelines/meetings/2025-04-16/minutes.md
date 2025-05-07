# Coding Guidelines Subcommittee Meeting on 2025-04-16 @ 10am Eastern Time

[Conversion](https://www.worldtimebuddy.com/?qm=1&lid=5,100,2643743,12,1850147&h=5&date=2025-4-16&sln=10-11&hf=1) between common time zones of attendees.

| Search Key | Description |
| :---- | :---- |
| \[todo\] | Action Item |
| \[decision\] | Something decided on |
| \[important\] | Key information |

## Agenda

1. Acceptance of [Previous Meeting Minutes](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/coding-guidelines/meetings/2025-04-09/minutes.md)
2. Introduction of new members
3. Working session: style guideline
  * Look over [PR contents](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/27) for feedback
  * Continue reviewing contents of style guideline
  * We want to ensure language used is consistent and the meanings of terms well understood for contributors.
4. Review session:
  * Review of [open PRs](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pulls)
  * Troubleshooting getting coding guidelines working
5. Round table

## Check-in area

**Please add your name, and an emoji that describes your day.**

- Pete LeVasseur, 🏃
- Sam Wright ✈️
- AndrewFernandes ☕🙂
- Douglas Deslauriers 🥱
- Koppany Pazman
- Jonas Wolf 👂
- El Mahdi EL Araby ⛰️
- Achim Kriso 🦆
- Walter Pearce (Rust Foundation) 🙃
- Arthur Hicken 🤖
- Christof Petig 🥚🐇
- Joel Marcey (Rust Foundation) ✌️
- Alex Celeste 😔
- Alexandru Vochescu 🙃
- Andrew Herridge 😀
- Lukas Wirth

**Notetaker:**

* Andrew Fernandes

## Housekeeping section

* Document space: [coding-guidelines](https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines)  
* Zulip: [safety-critical-consortium: Coding Guidelines](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/Coding.20Guidelines)
* [Work Item Board](https://github.com/orgs/rustfoundation/projects/1)

## Tasks

* 

## Meeting Minutes

- Meeting Minutes Review
  - Only up to item 4 on the last task list was completed
  - Douglas Deslauriers moves to accept the minutes
- Working Session: Style Guidelines
  - PL reviewed how to contribute via PR
  - Working through remainder of style guideline (picking up from last week)
  - Style guidelines:
    - Discussion WRT the definition of “Scope”
      - Compare and contrast with MISRA definitions
      - MISRA’s definition of “Scope” is also under active evolution
      - Possible looking at preconditions, postconditions, and invariants to provide scope
    - Tags
      - Prescriptive, not proscriptive
    - Guideline Content
      - Amplification
      - Exceptions and Deviations (as per MISRA)
        - an exception is what allows for avoiding needing to apply the rule and is baked into the rule
        - a deviation is something that you'd have to do if not applying a required or advisory rule
    - Rationale
      - JW brought up the fact that MISRA is often blindly followed
        - This can lead to poor outcomes and “blind dislike” of rules
        - AF suggested that “simple, easy deviations” are a core requirement in order to disincentivize blind rule-following
  - **ASK** for members to review current PRs on the [style guidelines](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pulls)
- Review Session
  - PL requested minor review and improvements to the CI/CD system

## Material

Any material to read before the meeting should be included here.

### GitHub Project Board for Work Items

* [Work Item Board](https://github.com/orgs/rustfoundation/projects/1)
* [Coding guidelines published](https://github.com/rustfoundation/safety-critical-rust-consortium/issues/188#issue-2869798433): Proposes a way of work to tackle the coding guidelines

### Tracking Issues

* [Early Alpha Milestone](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1) ahead of meeting at RustWeek

