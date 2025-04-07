# Coding Guidelines Subcommittee Meeting on 2025-04-02 @ 10am Eastern Time

[Conversion](https://www.worldtimebuddy.com/?pl=1&lid=5,100,2643743,12,1850147&h=5&date=4/2/2025%7C6&hf=1) between common time zones of attendees.

| Search Key | Description |
| :---- | :---- |
| \[todo\] | Action Item |
| \[decision\] | Something decided on |
| \[important\] | Key information |

## Agenda

1. Acceptance of [Previous Meeting Minutes](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/coding-guidelines/meetings/2025-03-26/minutes.md)
2. Intro for new members
2. Walkthrough of how to create a coding guideline (Pete)
3. Check-in with milestone DRIs: (Andrew, Jonas, Pete)
4. Work session:
  * Review of open PRs
  * Troubleshooting getting coding guidelines working
5. Round table

## Check-in area

**Please add your name, and an emoji that describes your day.**

* Pete LeVasseur 📆
* Florian Gilcher 🛬🥱
* Lukas Wirth 🙂
* Alex Celeste 🙂
* Julius Gustavsson 😐
* Alexandru Radovici 🙂
* Achim Kriso 🦆
* Arthur Hicken 🌨️
* Fernando Jose 🙂
* Koppany Pazman
* Douglas Deslauriers 🙃
* Christof Petig 😊
* Andrew Herridge 😃
* Jordan McQueen 🇯🇵🌃
* El Araby El Mahdi 🏔️🧗

**Notetaker:**

* Douglas Deslauriers

## Housekeeping section

* Document space: [coding-guidelines](https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines)
* Zulip: [safety-critical-consortium: Coding Guidelines](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/Coding.20Guidelines)
* [Work Item Board](https://github.com/orgs/rustfoundation/projects/1)

## Tasks

* \[Pete\] Fill out the “How to Read” and importantly “How to Write” documents
  in the [repo](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/blob/main/src/overview/how-to-read.rst)
* \[Pete\] Add references section for each guideline

## Meeting Minutes

### Acceptance of Previous Minutes

* Andrew Herridge puts forth a motion to accept
* Unanimous acceptance

### New Member introduction

* Achim Kriso
* El Araby El Mahdi

### Walkthrough of Creating a Coding Guideline

* Clone the
  [repo](://github.com/rustfoundation/safety-critical-rust-coding-guidelines)
* Review
  [license](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/blob/main/COPYRIGHT),
  [code of conduct](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/blob/main/CODE_OF_CONDUCT.md), and
  [contributing guide](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/blob/main/CONTRIBUTING.md)
* Install prerequisites and follow build guide in
  [README.md](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/blob/main/README.md)
* Visit the ferrocene language specification to find a reference for what the guideline will cover
  * In the example presented will be a suggested guideline which covers
    [declarative](https://spec.ferrocene.dev/macros.html#declarative-macros) and
    [procedural macros](https://spec.ferrocene.dev/macros.html#procedural-macros)
  * Grab the FLS paragraph ID marker from the source of the page using
    [developer tools](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Tools_and_setup/What_are_browser_developer_tools)
* Run the [guideline template script](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/blob/main/generate-guideline-templates.py)
* Copy the output of the template script into the appropriate \*.rst files in the coding-guidelines folder
  * The example references will be in
    [macros](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/blob/main/src/coding-guidelines/macros.rst)
* In [conf.py](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/blob/main/src/conf.py)
  there are different categories and tag which can be used
  * As discussed for the example it was considered how much we should discourage procedural macros, and it was decided this should be an advisory rule
  * This rule was discussed to be decidable
  * Decided that the scope was module scope
  * Added a new tag as needed for “certifiability” and choose that
* Draft the guideline title, description, and rationale
  * More precise guidance on drafting these will be discussed at the next meeting
  * Discussed adding a general references section
* Create non-compliant example(s)
  * Should comply with every other rule, but this one
* Create compliant example(s)
  * Should comply with this rule, but as close to the line as possible
* Run [make.py](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/blob/main/make.py)
  to build guidelines
  * Inside will be an index.html which will contain the rendered guidelines

## Material

Any material to read before the meeting should be included here.

### GitHub Project Board for Work Items

* [Work Item Board](https://github.com/orgs/rustfoundation/projects/1)
* [Coding guidelines published](https://github.com/rustfoundation/safety-critical-rust-consortium/issues/188#issue-2869798433): Proposes a way of work to tackle the coding guidelines

### Tracking Issues

* [Early Alpha Milestone](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1) ahead of meeting at RustWeek
