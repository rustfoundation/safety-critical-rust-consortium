# Coding Guidelines Subcommittee Meeting on 2025-01-15 @ 3pm UTC

## Agenda

1. Acceptance of [Previous Meeting Minutes](../2024-12-18/minutes.md)
2. Discuss organizing the `unsafe` topics we cover to be able to form a chapter per person for Learn unsafe Rust (Pete LeVasseur)
3. Distinction in work items for `unsafe` and other safety-critical topics (Andrew Fernandes)
4. `unsafe` Docs Review Task Force - progress report (Pete LeVasseur)
5. `unsafe` Practicum Chapter Task Force - progress report (Jordan McQueen)
6. Scheduling next meeting (Pete LeVasseur)
7. Round table

Supplemental material to the agenda can be found on the [GitHub repo](https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines).

## Check-in area

**Please add your name, and an emoji that describes your day.**

* Pete LeVasseur, 🎊
* Kyle Heins, 🙂
* Andrew Fernandes 🥱 ☕
* Marc Schoolderman 🤓
* Joni Pelham :-)
* Arthur Hicken 
* Joel Marcey 🤔
* Enow Scott 🙂
* Jonas Wolf 🥱
* Lukas Wirth 🤧
* Felix Gilcher 🙂
* Douglas Deslauriers🙂
* Joe Johnson ☕
* Walter Pearce, Rust Foundation, 🥶
* Julius Gustavsson 🤧
* Alex Celeste
* Andrew Herridge😀
* Alexandru Vochescu 🙂
* Tyler Stevens 🙂
* Nadhmi JAZI 🤧
* Munawar Hafiz 🙂

**Notetaker:**

* Douglas Deslauriers

## Housekeeping section

* Document space: [coding-guidelines](https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines)
* Zulip: [safety-critical-consortium: Coding Guidelines](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/Coding.20Guidelines)

## Tasks

* Pete LeVasseur will add the volunteers and interested persons to the Learn unsafe Rust chapter assignments
    * The volunteers and interested persons each have the task to contribute content
* Markus Hosch, Oreste Bernardi, Andrew Fernandes volunteer to coordinate to create a “booklet” to help define the terms
    * Andrew Fernandes will be the responsible organizer
* Douglas Deslauriers will create an agenda for the next meeting slot


## Meeting Minutes:

### Acceptance of previous meeting minutes

* Douglas Deslauriers puts forward a motion to accept the previous minutes
* Unanimous acceptance of the minutes

### Delivering Artifacts for the Learn unsafe Rust book

* A new focus on creating deliverables for the Learn Unsafe Rust book would be helpful
    * See tracking issue for “Learn unsafe Rust” for more discussion
    * The Learn unsafe Rust book is in the Google namespace and would require accepting the [Google Open Soure contribution license](https://cla.developers.google.com/about)
    * Drafting would be done in our safety critical [Github repo](https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines),
then committed to the [Google Github repo](https://github.com/google/learn_unsafe_rust)
    * A preface article defining what is safe and unsafe Rust and what is covered would be nice
    * Coding guidelines being a goal of the subcommittee, linking to chapters of the Learn unsafe Rust could be helpful. However, should the scope of the committee be more oriented toward guidelines rather than learning material.
* Markus Hosch volunteers to be responsible for “ABI and FFI”
* Oreste Bernardi is interested in “ABI and FFI”
* Chistof Petig is interested in “ABI and FFI”
* Joe Johnson is interested in “ABI and FFI”
* Pete LeVasseur volunteers to be responsible for “Pointer aliasing”
* Marc Schoolderman is interested in “Pointer aliasing”
* Alexandru Vochescu is interested in “Pointer aliasing”
* Jonas Wolf volunteers to be responsible for “Intrinsics”
* Douglas Deslauriers is interested in “Intrinsics”

### Distinction in work items for unsafe and other safety-critical topics

* There seems to be a distinction from unsafe technical concept, mostly the keyword in Rust and overall unsafe behavior
* Additionally, safety-critical means doesn't mean the same thing for different
  industries, and is similar to “high-assurance Rust”. A [book](https://github.com/tnballo/high-assurance-rust) has been written on this
* Markus Hosch, Oreste Bernardi, Andrew Fernandes volunteer to coordinate to create the distinction and write some words to sort this out
* There was a [Zulip discussion](https://rust-lang.zulipchat.com/#narrow/channel/136281-t-opsem/topic/What.20actually.20is.20unsafe.20and.20undefined.20behavior.3F/near/479727350) a few months ago that covers some of these definitions.
* The Rustinomicon also has some definitions for unsafe as well
* There is a distinction between (internal and external) system safety and software safety as well

### unsafe Docs Review Task Force - progress report

* No progress to note

### Scheduling next meeting

* Pete may not be here for the next meeting due to a business trip
* Douglas Deslauriers has volunteered to run the next meeting and create the agenda

### Round table

* MISRA addendum is working its way through the publishing process
    * Should be after the Embedded World date in March
* The in-person meeting will be in February ahead of the [Rust Nation meeting](https://www.rustnationuk.com/) in London
    * It will be 9-4, local time, in a single room
    * Please respond to the invitation if you will attend in person or not

## Material

Any material to read before the meeting should be included here.

### Tracking Issues

[\[Coding Guidelines\] Learn unsafe Rust \- Practicum Chapter Draft](https://github.com/rustfoundation/safety-critical-rust-consortium/issues/122)
[\[Coding Guidelines\] Review of Unsafe Coding Guidelines Reference Glossary](https://github.com/rustfoundation/safety-critical-rust-consortium/issues/123)
