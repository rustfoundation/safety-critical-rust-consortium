# Coding Guidelines Subcommittee Meeting on 2025-04-30 @ 10am Eastern Time

[Conversion](https://www.worldtimebuddy.com/?qm=1&lid=5,100,2643743,12,1850147&h=5&date=2025-4-30&sln=10-11&hf=1) between common time zones of attendees.

| Search Key | Description |
| :---- | :---- |
| \[todo\] | Action Item |
| \[decision\] | Something decided on |
| \[important\] | Key information |

## Agenda

1. Acceptance of [Previous Meeting Minutes](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/coding-guidelines/meetings/2025-04-23/minutes.md)
2. Introduction of new members
3. Review of [milestone](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1) ahead of RustWeek meetup
4. Working session:
   * Goal: Everyone submits a draft PR to the repo which passes build locally and in PR with stubbed contents
      * Pick one of the existing issues, [unsafety](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/8), [macros](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/10), [concurrency](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/9)
      * Use `./generate-guideline-templates.py`
      * Find the corresponding FLS paragraph-id from [live FLS site](https://spec.ferrocene.dev/index.html)
   * Troubleshooting getting coding guidelines build working
5. Discuss standards matrix and bidirectional linking between guidelines and matrix (matrices?)
6. Review session:
   * Review [proposed subcommitee agenda](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/270#discussion_r2064068874) at RustWeek Consortium meeting, gather more items
   * Review open [PRs](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pulls) & [issues](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues)
7. Round table

## Check-in area

**Please add your name, and an emoji that describes your day.**

- Pete LeVasseur, 🧬
- Alex Celeste ☺️
- Samuel Wright ☕☕⚰️
- Koppany Pazman
- Placeholder
- Arthur Hicken 🤖
- Julius Gustavsson 
- Sasha Pourcelot 🍕
- Andrew Fernandes 💤☕
- Placeholder
- Placeholder
- Lukas Wirth
- Enow Scott
- Achim Kriso
- El Araby El Mahdi 🐌☕

**Notetaker:**

* Andrew Fernandes

## Housekeeping section

* Document space: [coding-guidelines](https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines)  
* Zulip: [safety-critical-consortium: Coding Guidelines](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/Coding.20Guidelines)
* [Early Alpha Milestone](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1) ahead of meeting at RustWeek
* [Work Item Board](https://github.com/orgs/rustfoundation/projects/1)

## Tasks

* See below for the [todo] markers

## Meeting Minutes

- *The Hunt for Today’s Notetaker (™)*
- Review of last weeks’ minutes
  - Proposed accepting, unanimous pass
- Discussion on “[How Do We Treat Macros?](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/59)”
- **[Ask]** for PR fill on [Agenda for May Consortium Meeting](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/270)
  - **[Ask]** for review of open PRs and issues
- Review of “Scaffold out down to subsection-level”
- Suggestion that it was better to have coverage over completion
- Mention that guidelines *can* overlap
  - This is to allow fine-grained control
- **[todo]** **(Action Items)**
  - **(Pete LeVasseur)** Make the sphinx built output “less noisy”
  - **(Pete LeVasseur)** Use the “ruff” python formatter on python code (from the “uv” folks)
  - **(Samuel Wright)** Template generation needs to have extraneous whitespace removed
  - **(Pete LeVasseur)** For next meeting to return to the punted “Discuss standards matrix and bidirectional linking”
  - **(Lukas Wirth)** and **(Achim Kriso)** Create PRs (content not neeed, just start them)
- Sphinx PR build can show diffs of the HTML documentation
  - Works better at the word/paragraph level rather than “whole page” level
  - Worked through [this example](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/61)
- Desire to add other active contributors as additional approvers to the GitHub workflow
- Two volunteers requested for creating PRs and fleshing out the process (see "todo", above)
  - Content not needed, just the start of PRs
- Quick review session

## Material

Any material to read before the meeting should be included here.

### GitHub Project Board for Work Items

* [Work Item Board](https://github.com/orgs/rustfoundation/projects/1)
* [Coding guidelines published](https://github.com/rustfoundation/safety-critical-rust-consortium/issues/188#issue-2869798433): Proposes a way of work to tackle the coding guidelines

