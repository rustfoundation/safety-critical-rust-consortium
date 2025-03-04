# Coding Guidelines Subcommittee Meeting on 2024-12-18 @ 3pm UTC

## Agenda

1. Acceptance of [Previous Meeting Minutes](../2024-12-04/minutes.md)  
2. `unsafe` Docs Review Task Force \- progress report (Pete LeVasseur)  
3. `unsafe` Practicum Chapter Task Force \- progress report (Pete LeVasseur)  
4. Round table

Supplemental material to the agenda can be found on the [GitHub repo](https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines).

## Check-in area

**Please add your name, and an emoji that describes your day.**

* Pete LeVasseur, 🎄  
* Xander Cesari: 😪☕  
* Tyler Stevens 🙂  
* Andrew Fernandes ☕  
* Alex Celeste 😪  
* Arthur Hicken 😶  
* Douglas Deslauriers 🙂  
* Fernando Jose: 🥱  
* Andrew Herridge 😀  
* Joni Pelham 🙂  
* Oreste Bernardi 🌛  
* Lukas Wirth 🥱  
* Enow Scott 😀  
* Kyle Heins 🙂  
* Munawar Hafiz 🙂  
* Jonas Wolf 🙂  
* Joe Johnson ☕🎄


  
**Notetaker:**

* Joni Pelham

## Housekeeping section, please add

* Document space: [https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines](https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines)  
* Zulip: [safety-critical-consortium: Coding Guidelines](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/Coding.20Guidelines)

## Tasks

* 

## Meeting Minutes:

* Query regarding the AI Note taker included in the call which could not be removed by Pete.  Question for Joel. “Yuta’s AI Notetaker”  
* Discussion of the pull request to coordinate volunteers to contribute to the unsafe glossary. [\[Coding Guidelines\] Review of Unsafe Coding Guidelines Reference Glossary · Issue \#123 · rustfoundation/safety-critical-rust-consortium](https://github.com/rustfoundation/safety-critical-rust-consortium/issues/123)  
  * Timeline for outputs not set and attendees encouraged to volunteer for various topics.  
  * Some discussion from attendees of possible items they might contribute.  
* Second tracking issue for the creation of a unsafe practicum draft chapter [\[Coding Guidelines\] Learn unsafe Rust \- Practicum Chapter Draft · Issue \#122 · rustfoundation/safety-critical-rust-consortium](https://github.com/rustfoundation/safety-critical-rust-consortium/issues/122)  
* Discussion of potential to flesh out the current examples [safety-critical-rust-consortium/subcommittee/coding-guidelines/initiatives/safe-use-of-unsafe-guidelines/unsafe-example-usage.md at main · rustfoundation/safety-critical-rust-consortium](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/coding-guidelines/initiatives/safe-use-of-unsafe-guidelines/unsafe-example-usage.md)  
* Roundtable  
  * AH will we make more use of the projects area in github?  Is it worth coordinating via that?  
    * Interface mentioned as a plus point for using github  
  * AC Update \- No current progress to report due to other ongoing commitments.  Schedule for creation will be submitted to Pete.  
  * DD On Zulip OB published a PR regarding hardware safety and recommended attendees read it.  [Imported document about undefined behavior and safe api in LLD by pellico · Pull Request \#127 · rustfoundation/safety-critical-rust-consortium](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/127)  
    * Zulip link for discussion [https://rust-lang.zulipchat.com/\#narrow/channel/445688-safety-critical-consortium/topic/Coding.20Guidelines/near/488845893](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/Coding.20Guidelines/near/488845893)  
    * Pete mentioned use of crates to create HALs (Hardware abstraction layer)  
    * OB emphasized issue of hardware undefined behaviour coming through and causing issues when code that is common across architectures can have issues on one device where it would not occur elsewhere. All code that could cause such issues should be marked unsafe.  
    * AF expressed caution regarding increase of scope to attempt to mitigate hardware issues in code.  
    * JJ talking about creating best practices for creating memory maps.  Listing common errors for the devices. Never be able to replace unsafe. Rust’s safety system doesn’t guarantee nothing will fail but instead is about failing gracefully.  
    * Comment from AC in chat “over in our world we have the Rule/Directive distinction for issues like this \- not everything is machine-decidable and some things need to be expressed in terms of reviewer signoff”  
    * PL should this type of discussion be included in the unsafe coding guidelines?  
    * JW we as programmers take care of undefined behaviour and the onus is on us to accept the burden.   
    * Comment from XC in chat “I wonder if the Embedded WG has or would do guidelines on idiomatic hardware interaction? Is there standardization or practices beyond the embedded-hals?”  
    * Comment from AF in chat ”To a large extent, a lot of the issues that Oreste is bringing up WRT "the hardware doing something potentially bad" is the idea that a function may have no \*\*software\*\* side effects, but has \*\*hardware\*\* side effects. I don't think that that's a Rust problem, because it \_can't\_ be, even with lots of trait-annotation””  
    * [Behavior considered undefined \- The Rust Reference](https://doc.rust-lang.org/reference/behavior-considered-undefined.html)  
    * Discussion about how much of this is a problem for the embedded rust working group vis-a-v the safety critical rust working group.  
    * PL \- Should all interactions with hardware be considered unsafe?  
    * JW \- [https://public-docs.ferrocene.dev/main/specification/unsafety.html](https://public-docs.ferrocene.dev/main/specification/unsafety.html)

  ## Actions 

    * OB nominated as ambassador to the Rust Embedded WG  
    * Perhaps have Jonathan from the Rust Embedded WG as a guest?   
      

## Material

Any material to read before the meeting should be included here.  
