# Coding Guidelines Subcommittee Meeting on 2025-01-29 @ 3pm UTC

## Agenda

1. Acceptance of [Previous Meeting Minutes](../2025-01-15/minutes.md)
2. `unsafe` Docs Review Task Force - progress report (Douglas Deslauriers)
3. `unsafe` Practicum Chapter Task Force - progress report (Jordan McQueen)
4. Progress report on booklet to define `unsafe` terms and scope (Andrew Fernandes)
5. Round table

Supplemental material to the agenda can be found on the [GitHub repo](https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines).

## Check-in area

**Please add your name, and an emoji that describes your day.**

* Enow Scott 🙂
* Andrew Fernandes ☕ 🥱
* Joe Johnson ☕💤
* Joni Pelham 🙂 🐶
* Pietro Albini **😄**
* Andrew Herridge 😀
* Asko Kauppi
* Koppany Pazman
* Sarah Dietrich 🙂
* Alexandru Vochescu 🙂
* Sasha Pourcelot 🙂
* Julius Gustavsson 😀
* Lukas Wirth 🙂
* Arthur Hicken 😃
* Walter Pearce 🥸
* Douglas Deslauriers 🙂
* Joel Marcey 🧠
* Tyler Stevens 🙂

**Notetaker:**

* Julius Gustavsson

## Housekeeping section

* Document space: [coding-guidelines](https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines)
* Zulip: [safety-critical-consortium: Coding Guidelines](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/Coding.20Guidelines)

## Tasks

*

## Meeting Minutes

#### Acceptance of previous meeting minutes

* Douglas Deslauriers puts forward a motion to accept the previous minutes
* Accepted unanimously by the meeting participants

#### `unsafe` Docs Review Task Force \- progress report

*  The general tracking issue can be found here [https://github.com/rustfoundation/safety-critical-rust-consortium/issues/123](https://github.com/rustfoundation/safety-critical-rust-consortium/issues/123)
* The content for chapter “ABI and FFI” is tracked here [https://github.com/rustfoundation/safety-critical-rust-consortium/issues/150](https://github.com/rustfoundation/safety-critical-rust-consortium/issues/150)
* As well as a discussion surrounding the use of `unwrap` in a safety setting can be found here [https://github.com/rustfoundation/safety-critical-rust-consortium/issues/145](https://github.com/rustfoundation/safety-critical-rust-consortium/issues/145)

#### `unsafe` Practicum Chapter Task Force \- progress report

* Little progress made on this point due to other priorities

#### Progress report on booklet to define `unsafe` terms and scope

* Progress being made. “Ada safe coding guidelines” a good starting point to set the scope.
* Pull request in the works to set the outline bullet list. Plan to have it uploaded before next meeting.
* Important to highlight the distinction between what Rust considers unsafe (i.e. the `unsafe` keyword) and
  unsafe practices using safe Rust code (e.g. a deadlock or unconditional unwrapping).

#### Round table

* The MISRA guidelines for Rust are expected to be released soon but at the earliest at Embedded World 2025. This
  guideline will not be a list of Do’s and Don’ts for Rust code but rather a comparison with the C guidelines and
  if/how they are applicable to Rust.
* Important to understand the reason and context behind a certain (MISRA or other external-) guideline to better assess
  if the same issue still applies on the Rust side.
* The guidelines produced by this consortium will mostly likely be consumed by a wider group than those that have
  certification requirements. Examples are e.g. hyperscalers and others that have very similar safety/reliability
  requirements without needed certification. Therefore it is important that the guidelines are usable for the broadest
  possible audience without getting stuck in the minutiae of a certain safety standard.
* The guidelines produced should come with well defined rules (and properly highlighted in the text) and ideally an
  example of a coding pattern, tool etc that demonstrates how to adhere to the rule.

## Material

Any material to read before the meeting should be included here.

### Tracking Issues

[\[Coding Guidelines\] Learn unsafe Rust \- Practicum Chapter Draft](https://github.com/rustfoundation/safety-critical-rust-consortium/issues/122)
[\[Coding Guidelines\] Review of Unsafe Coding Guidelines Reference Glossary](https://github.com/rustfoundation/safety-critical-rust-consortium/issues/123)
