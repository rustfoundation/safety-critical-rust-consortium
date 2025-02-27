# Coding Guidelines Subcommittee Meeting on 2024-11-05

## Agenda

1. Acceptance of [Previous Meeting Minutes](../2024-10-22/minutes.md)
2. Contributor Expectations - Online discussion (Pete LeVasseur)
3. Safe Use of Unsafe Guidelines - Online discussion (Pete LeVasseur)
4. MISRA + Rust (Alex Celeste)
5. Round table

Supplemental material to the agenda can be found on the [GitHub repo](https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines).

## Check-in area

**Please add your name, and an emoji that describes your day.**

* Marc Schoolderman, 🤧
* Daniel Glazman, 🫥
* Julius Gustavsson 🙂
* Florian Gilcher, 🦀]
* Felix Gilcher
* Lukas Elmer 🚀
* Arthur Hicken ✈️
* Munawar Hafiz, 😰
* Walter Pearce, 😶‍🌫️
* Jonas Wolf, 🫥
* Sarah Dietrich, 🫥
* Kyle Heins, 🫥
* Alexandru Vochescu, 🙂
* Alex Celeste, 🫥
* Andrew Herridge 😀

**Notetaker:**

Julius Gustavsson


## Housekeeping section, please add

* Document space: https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines
* Zulip: [safety-critical-consortium: Coding Guidelines](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/Coding.20Guidelines)

## Tasks

* [ ] Pete to remove the current contributor document from the PR and recreate one in a separate PR
* [ ] (see volunteers below) Author the Safe Use of Unsafe Guidelines document
* [ ] Alex C to present the MISRA + Rust documents to the group for review


## Meeting Minutes:

* Meeting introduction and check-in
* Meeting minutes from last meeting were quickly reviewed and accepted

### Contributor Expectations \- Online discussion

* Contributor expectations doc on GitHub were updated to use the Rust Foundation’s CoC
* Discussion about how to phrase the sentence of who can be a contributor and how much should they contribute.
* Everyone who joins in should be contributed
* General consensus that the wording made it sound like a unnecessary barrier.
* Pete takes an action to remove the current contributor document from the PR and recreate one in a separate PR


### Safe Use of Unsafe Guidelines \- Online discussion

* Proposal was presented and suggested to become the first major item for the group to discuss
* Suggestion to use the outcome of Unsafe Guideline document to nudge the Rust project to adopt the guidelines as official
* Guidelines should both show patterns that are generally known to be good, and what patterns are known to be generally bad.
* The purpose of the guideline is to define how the unsafe code should be written and not about the functions that contain the unsafe code
* A Rust module boundary is the actual boundary for unsafe code. This is not properly documented anywhere.
* People that volunteered to help author the document were:

  * Marc S
  * Felix G
  * Walter P
  * Florian G
  * Pete L
  * Alex C
  * Daniel G
  * Jonas W

* Choice of collaboration tool TBD due to various network restriction at companies

### MISRA \+ Rust

* MISRA will publish a whitepaper detailing _possible_ applicability of the existing C rules to Rust (without changes, except to Category; no new rules,
  not a freestanding guidelines document), but probably won't enthrone a WG any time in the near future due to lack of membership and redundancy w.r.t this Subcommittee;
* "Iron Carbide" is an IP-neutral take on the applicable rules, plus a few original rules to plug really big gaps; this aims to be a document mirroring
  MISRA's structure w.r.t compliance etc. and rule descriptions; MISRA is _not_ currently planning to publish this so we'd like to hand it over to the Subcommittee for review instead
* The Subcommittee can then take "moral ownership" of it (with a big "whatever that means" to be decided later)
* and maybe pass it back to MISRA at some point for duplicate publication under the red triangle logo, but retaining Rust Foundation oversight
* There's meetings and discussion happening on the MISRA side next week so the applicability matrix will be available to review before then; and hopefully the main
  document will be reviewable by a Subcommittee meeting or two after that
* So there was a question to the group about whether anyone would like to review, and whether anyone thought this was a good idea, and an unresolved question about how much and where
  this would overlap with the Safe Use of Unsafe document


* Meeting finished abruptly due to Google Meet’s time limit. Will be continued next meeting.

## Material

Any material to read before the meeting should be included here.
