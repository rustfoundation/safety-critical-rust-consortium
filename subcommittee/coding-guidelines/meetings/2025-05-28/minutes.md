# Coding Guidelines Subcommittee Meeting on 2025-05-28 @ 10am Eastern Time

[Conversion](https://www.worldtimebuddy.com/?qm=1&lid=5,100,2643743,12,1850147&h=5&date=2025-5-28&sln=10-11&hf=1) between common time zones of attendees.

| Search Key | Description |
| :---- | :---- |
| \[todo\] | Action Item |
| \[decision\] | Something decided on |
| \[important\] | Key information |

## Agenda

0. Solicitation of notetaker
1. Acceptance of [Previous Meeting Minutes](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/coding-guidelines/meetings/2025-05-21/minutes.md)
2. Introduction of new members
3. Review of [revised milestone](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1) focused on broad \+ deep approach to macros chapter \- 5 mins
4. Discuss [MISRA and CERT](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/75) topic \- 30 mins
   * Introduction by David Svoboda of Clippy \<=\> Guidelines spreadsheet \- 5 mins
   * Introduction of thoughts by Alex Celeste \- 5 mins
   * Discussion time\! \- 20 mins
   * Goal is not to choose one over the other, but to pick and choose the best fits\!
   * After this discussion, seal it temporarily to allow @AlexCeleste to pull together a strawman PR to discuss further
5. Housekeeping: Global Meeting Times\!
6. Coding Guidelines Issue Template
7. Working session \- 10 mins
   * Let's try to think of 1-2 guidelines ahead of time we'd like to jot down, macros are great, wider also fine
   * Note\! We'd like to aim for unambiguous guidelines at this point to build confidence in their quality
   * Spin off PRs to rough them in \- volunteers
8. Review session:
   * Review open [PRs](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pulls) & [issues](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues) \- 5 mins
9. Round table \- 5 mins

## Check-in area

**Please add your name, and an emoji that describes your day.**

* Pete LeVasseur, 🎟️
* Enow Scott 🥱
* Robert C. Seacord 😣
* Alex Celeste 😪
* Sasha Pourcelot ☀️
* Andrew Fernandes ☕🥱☕
* Douglas Deslauriers 🐦
* Koppany Pazman
* Stephen Hedrick (AdaCore) 🛠️
* Joel Marcey ⛈️
* Markus Hosch 🎮
* David Svoboda 🙂
* Lukas Wirth
* Julius Gustavsson 😐
* Tiago Manczak

**Notetaker:**

* Douglas Deslauriers

## Housekeeping section

* Document space: [coding-guidelines](https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines)
* Zulip: [safety-critical-consortium: Coding Guidelines](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/Coding.20Guidelines)
* [Early Alpha Milestone](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1)
* [Work Item Board](https://github.com/orgs/rustfoundation/projects/1)

## Tasks

* \[Alex Celeste\] To create updated guidelines PR
  * \[David Svoboda\] To review
  * \[Douglas Deslauriers\] To review
  * \[Robert Seacord\] To review (unknowingly volunteered)
* \[Robert Seacord\] To create issue about which CERT int and float rules could be ported
* \[Andrew Fernandes\] To create issue about the `std` vs `no_std` discussion

## Meeting Minutes

#### Previous Meeting Minutes

* Reviewed previous minutes' tasks
* Last meeting was mostly a report out and asking for volunteer help
* \[AC\] Motion to accept, \[SH\] second
  * Unanimous acceptance

#### New Member Introductions

* No new member introductions this week

#### Milestone Review

* [Milestone](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1)
* Opened up issues for guidelines other than macros
  * Difficult to implement macro rules in clippy
* Do we have a longer term roadmap?
  * There are all of the chapters that will be filled in the [repo](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/tree/main/src/coding-guidelines)
  * FFI would like to be added as a next priority
  * There could be more milestones created, setting “deadlines” wouldn't be as possible
* Perhaps guidelines should be in individual files such that they can be moved between chapters
  * Recategorization should be quite easy, and shouldn't be set in stone upon creation

#### Previous Standards Approach's Review

* David's Review of Clippy's Lints
  * First noticed that there are many lints around “unwrap”
  * Likely unwrap not wanted in safety critical software
  * Question on how specific (statically decidable) the guidelines should be?
* Discussion of MISRA vs. CERT
  * Language subset vs. Defect Identification
  * Seems to be a consensus around language subset rules being advisory and defect identification as mandatory
    * Ex) Do not use unwrap (advisory), Do not terminate program abruptly (mandatory)
* If there is a sound analysis which can detect the broader behavior then the having the advisory rule would need be needed
* Static analysis tools would have an easier time automating those advisory guidelines about language subset
* Would all of the core functionalities that could panic need to be reviewed (eg. integer arithmetic)? This seems like large task in order to complete rigorously and may ruffle some feathers
  * There needs to be some rounded edges around the rules to allows flexibility for implementations
* There is a large gap between `std` and `no_std` while writing Rust, similar to the safety critical subset of C
* The participants here are this group, static analysis vendors, and developers. It would be better if this group did more work to make it easier for the lives of the other participants. However there shouldn't be a capitulation to the lowest common denominator of analysis vendor

#### Global Meeting Times

* Three cyclical meetings, across different time zones
* Decisions will need to be made a asynchronous manner (or require all three meetings consensus)
* Trial period of time to see how well it works
* Reach out to Pete if you cannot make any of the meeting times

#### Coding Guidelines Issue Template

* There is now a template for filing a GitHub issue for new coding guidelines
* Automatically adds tags to the issue
* Just a proposal
  * The issue is not expected to be updated over time
* Is there a list of agreed tags?
  * There is, but we need to expand them, so right now it is a wild west to gather more tags
  * It would be good to add a list of existing tags to inspire new proposal authors with the style/type of the existing tags

#### Round Table

* There are some CERT guidelines around integers and floating point which are likely directly usable by us
  * [INT](https://wiki.sei.cmu.edu/confluence/pages/viewpage.action?pageId=87152052)
  * [FLP](https://wiki.sei.cmu.edu/confluence/pages/viewpage.action?pageId=87152181)
  * Agreement that they may be useful, and that they shouldn't be written immediately

## Material

Any material to read before the meeting should be included here.

### GitHub Project Board for Work Items

* [Work Item Board](https://github.com/orgs/rustfoundation/projects/1)
* [Coding guidelines published](https://github.com/rustfoundation/safety-critical-rust-consortium/issues/188#issue-2869798433): Proposes a way of work to tackle the coding guidelines
