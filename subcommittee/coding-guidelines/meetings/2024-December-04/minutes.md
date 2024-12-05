# Coding Guidelines Subcommittee Meeting on 2024-12-04 @ 3pm UTC

## Agenda

1. Acceptance of [Previous Meeting Minutes](../2024-November-19/minutes.md)
2. Open a discussion on timelines/milestones for goals (Pete LeVasseur)
3. `unsafe` Practicum Chapter Task Force - progress report (Pete LeVasseur)
4. `unsafe` Docs Review Task Force - progress report (Pete LeVasseur)
5. Round table

Supplemental material to the agenda can be found on the [GitHub repo](https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines).

## Check-in area

**Please add your name, and an emoji that describes your day.**

* Pete LeVasseur, ✌️
* Joel Marcey, 🥱
* Kyle Heins,  🥱
* Andrew Fernandes 🥱☕️
* Joni Pelham 😣
* Marc Schoolderman 🎅
* Alexandru Vochescu 🥱
* Dillon McEwan 😴
* Jordan McQueen 😴🗻❄️
* Jonas Wolf 😀
* Joe Johnson 😴
* Vincent Eckert 😃
* Douglas Deslauriers 😀
* Arthur Hicken 😀🔦🔬
* Nadhmi JAZI  😀
* Christof Petig 🎅
* Walter Pearce 🤘
* Enow Scott 😀
* Wayne Chang 🎅
* Munawar Hafiz 🙂
* Oreste Bernardi


**Notetaker:**

* Douglas Deslauriers

## Housekeeping section, please add

* Document space: https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines
* Zulip: [safety-critical-consortium: Coding Guidelines](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/Coding.20Guidelines)

## Tasks

* [PL](mailto:plevasseur@gmail.com): Create a set of milestones for progress moving forward

## Meeting Minutes:

* JW: Motion to accept the previous minutes
* Meeting minutes were accepted unanimously

### Timelines and Milestones for Goals

* PL: Two task forces have been proposed, one for creation, one for review. More details on Zulip
* DD: Would the two task forces meet outside of these meetings?
* PL: That is possible
* PL: Proposal: First step for Practicum group is to create some prose for safe
  use of unsafe to accompany [the examples](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/coding-guidelines/initiatives/safe-use-of-unsafe-guidelines/unsafe-example-usage.md)
* JM: Wants to add prose to the examples
* AF: Would like to help add prose, but time constrained
* JJ: Would also like to help. Wonders whether the standard/core library or both unsafe behaviour would be covered in the document?
* PL: The idea would be to target both audiences that use standard library and not
* CP: [Embassy](https://github.com/embassy-rs/embassy) would be a good example of unsafe usage
* AF: There are many patterns in the C world that are accepted, and giving people design patterns would be useful to help the transition
* JM: In response to the previous Practicum group proposal, agreed good first steps.
* PL: Proposal for document review task group, to review the [Rust unsafe code
  guidelines](https://github.com/rust-lang/unsafe-code-guidelines)
* DD: Agreed, would be beneficial
* It was suggested that multiple people should review the guidelines

### Practicum Chapter Task Force Progress

* JM: Mostly looking where to start, and perhaps annotating the examples as suggested earlier
* JM: Would the idea to be supplement the Learn Unsafe Rust book with coding guidelines
* PL: Spoke to an author the book and was open to contributions and may even be able to transfer ownership to the Rust Foundation
* JJ: The book has a good starting framework

### Docs Review Task Force Progress

* PL: Mostly review the unsafe code guidelines glossary

### Round Table

* WC: Interested in supply chain security of rust packages?
* JM: This may be more relevant to the Tooling committee
* AF: This may be out of scope, but is certainly would be looked at from a regulatory perspective
* DD: The largest extent that of the coding guidelines would be tell users to have the coding guidelines apply to used packages as well
* WP: Google has [Rust crate audits](https://github.com/google/rust-crate-audits), using [Cargo Vet](https://github.com/mozilla/cargo-vet)

---

* OB: Wanted to determine what unsafe/undefined behaviour is in reference to the hardware
* PL: There is a section on undefined behaviour in the Learn Unsafe Rust book
* OB: Can share document on safety in the scope of low level driver

---

* AH: Is the meeting going to be in January?
* JM: It will be nearby to Rust Nation in February, on the 19th
* PL: Would the venue be outside of Rust Nation?
* JM: **It would be outside of the venue, and would not require tickets to Rust Nation**
* JM: About 20 people have responded to the poll as going face to face

---

* JP: Different levels of assurance for different guidelines may be useful
* AF: The definition of unsafe, means that the code will be unproven
* JP: It should be clear in the guidelines that some unsafe should be used
* JM: We should have specific recommendations with what to do with unsafe code
* JJ: We shouldn’t just focus on the unsafe keyword
* AF: Deadlocks and checked/unchecked arithmetic are examples of stuff outside of this
* WP: Would this committee want to bless Cargo Vet or create recommendations for crates?
* PL: Getting involved with Cargo Vet is a good idea
* PL: Niko expressed a [thought](https://github.com/rust-lang/rfcs/pull/3484#issuecomment-2039501484) to change the safe keyword to trusted in Rust 2027
* JW: Addressing the unsafe keyword first is good idea until different certifications are published
* DD: Different levels of assurance could be addressed by annotating guidelines with levels of severity
* PL: It does make sense to categorize how unsafe each example and pattern would be

---

* OB: In MISRA, there is emphasis on making code easy to read and understand. It would be a good idea to get an idea of common misunderstandings and propose guidelines that address them, even if the itself isn’t exactly necessarily unsafe.
* OB: Should we address these misunderstandings and create guidelines to avoid them?
* PL: Computers execute the code, but humans read it. Indeed we want to put out code review guidelines for unsafe

### Adjournment

## Material

Any material to read before the meeting should be included here.
