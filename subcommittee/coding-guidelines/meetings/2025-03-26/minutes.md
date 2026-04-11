# Coding Guidelines Subcommittee Meeting on 2025-03-26 @ 3pm UTC

| Search Key  | Description          |
|-------------|----------------------|
| [todo]      | Action Item          |
| [decision]  | Something decided on |
| [important] | Key information      |

## Agenda

1. Acceptance of [Previous Meeting Minutes](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/coding-guidelines/meetings/2025-03-12/minutes.md)
2. Intro for new members
3. Housekeeping
   a. Time slot - UTC 3pm or fixed to some time zone? 10am Eastern? (Pete LeVasseur)
   b. Meeting frequency - make weekly? Agenda seems full 😅 (Pete LeVasseur)
4. [MISRA C Addendum 6 (Rust)](https://misra.org.uk/app/uploads/2025/03/MISRA-C-2025-ADD6.pdf) Brief (Alex Celeste)
5. [Safety Pamphlet Decoder Ring](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/coding-guidelines/initiatives/safety-pamphlet/decoding-safety-critical-code.md) - merged, let's briefly review (Andrew Fernandes)
6. Proposal to ensure upstreamed Ferrocene Language Specification with t-spec keeps [paragraph-ids.jsoni](https://spec.ferrocene.dev/paragraph-ids.json) with paragraph IDs tied to content hashes - topic to discuss with Rust Project at RustWeek? (Pete LeVasseur)
7. Review [April 28th milestone](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1) ahead of RustWeek & [work item board](https://github.com/orgs/rustfoundation/projects/1/views/1) (Pete LeVasseur)
8. Review task force progress, share work if available - (Pete: Macros, Andrew: Unsafety, Jonas: Concurrency)
   a. [Declarative Macro PR Review](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/16) (if time allows)
9. arewesafetycriticalyet.org
   a. Alexandru R. signed up to scaffold out website (docusaurus)
   b. Looking to gather content providers for home page
10. Round table

Supplemental material to the agenda can be found on the [GitHub repo](https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines).

## Check-in area

**Please add your name, and an emoji that describes your day.**

* Pete LeVasseur, ☕👏
* Oreste Bernardi 😶‍🌫️
* Jordan McQueen 🇯🇵🐟☺️
* Samuel Wright ☁️
* Douglas Deslauriers ⭐
* Andrew Fernandes ☕☕🥱☕☕
* Dillon McEwan ☕🌅
* Alex Celeste 🙂
* Robert C. Seacord
* Julius Gustavsson
* Walter Pearce (Rust Foundation) ☕
* Andrew Herridge 😀
* Lukas Wirth 🙁
* Espen Albrektsen 🙂
* Markus Hosch
* Enow Scott 🙂
* Achim Kriso 🙂
* Koppany Pazman
* Joel Marcey 🤗
* Arthur Hicken 🫥

**Notetaker:**

* Markus Hosch

## Housekeeping section

* Document space: [coding-guidelines](https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines)
* Zulip: [safety-critical-consortium: Coding Guidelines](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/Coding.20Guidelines)
* [Work Item Board](https://github.com/orgs/rustfoundation/projects/1)

## Tasks

## Meeting Minutes

#### Acceptance of previous meeting minutes

* Minutes from last meeting got accepted by the crowd

#### Intro for new members

* Robert Seacord introducing himself

#### Housekeeping (Time slot and frequency)

3 pm UTC was chosen so that it’s equally inconvenient for everyone ;)
There’s a Zulip poll for an alternative slot: https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/Coding.20Guidelines/near/504615992
Meeting frequency: Should we increase frequency? Agenda’s always packed. [todo] Pete will open a topic on Zulip?
Might be an exception today
Weekly until RustWeek? Accepted by the crowd, [todo] Pete will increase frequency

#### MISRA C Addendum 6 (Rust) Brief

(Presenting the MISRA addendum PDF)
Published on 10th of March
Table with rules and their applicability to Rust (yes / no / partial) with comment
Estimate is that about 50% of the rules are not relevant
Thanks a bunch, good starting point
Can we copy the format / categories of the MISRA guidelines? There shouldn’t be a (™) on that, MISRA C 2020 is designed to be picked up, so copying the format should be fine
How do we make development efficient by helping devs by linking rule implementations with the MISRA standard?
Could be a topic for the liaison subcommittee.
MISRA is traditionally a bit more strict here, US laws should be “liberal enough”
Fair use should be a guideline, not directly copying entire rules, referencing chapters shouldn’t be a problem at all
Thanks to people involved in MISRA contribution, Rust Foundation can also give legal counsel here, liaison subcommittee should take over here

#### Safety Pamphlet Decoder Ring

(Presenting the pamphlet on the coding guidelines subcommittee repo)
First version has ben published under https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/coding-guidelines/initiatives/safety-pamphlet/decoding-safety-critical-code.md 
Define “unsafe” & “safety-critical”
Definition of “unsafe code”
Case study in avionics: There is no “unsafe” but “code that does/doesn’t follow sane & meaningful rules”. If the code follows the rules, it is considered good enough without further measuring its failure rate
Safety is always to be seen in context (example: timer)
Call for suggestions
What’s missing is a clear definition of unsafety in Rust, it’s also version dependent and as such is not defined sharply enough.
Agreement, this needs to be defined
The pamphlet might just say that this has to be defined on a project, it’s the obligation to do that if you use Rust in a safe field
This might be picked up and sharpened together with the rust project to streamline the definition of unsafe in the language

#### Ferrocene Language Specification

Let’s get in touch with the Rust project to ensure that things stay in sync. Let’s prepare upfront!

#### Review April 28th milestone

Milestones exist. Call for contributions to the milestones.
Q: How to start working on rules?
Generator script for rules exists, the README.md tells how to use the tool
Request: Demonstrate the process once?
PR exists that demonstrates this, maybe next meeting? (Good idea)

#### arewesafetycriticalyet.org

Suggestion to create a website “arewesafeyet.rs” / “arewesafetycriticalyet.org” (or something akin).
[info] Alex R. will help here. Call for content for such a website.
[todo] Action item for Pete to organize content gathering for the website

#### Review task force progress

(Showing guideline for writing a declarative macro, PR: https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/16)
There is a CI job generating html
Info: Live preview can be added to CI actions, open source solutions exist

#### Round table

Info: Assessors coming, let’s see what’s happening ^^
[todo] Call for reviews for https://github.com/rustfoundation/safety-critical-rust-consortium/pull/182 
Suggestion: Move of pamphlet to the coding guidelines repo?

## Material

### Any material to read before the meeting should be included here.

* [Safety Pamphlet](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/coding-guidelines/initiatives/safety-pamphlet/decoding-safety-critical-code.md)

### GitHub Project Board for Work Items

* [Work Item Board](https://github.com/orgs/rustfoundation/projects/1)
* [Coding guidelines published: Proposes a way of work to tackle the coding guidelines](https://github.com/rustfoundation/safety-critical-rust-consortium/issues/188#issue-2869798433)

### Tracking Issues

* [Early Alpha Milestone ahead of meeting at RustWeek](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1)
