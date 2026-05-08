# **Coding Guidelines Subcommittee Meeting on 2026-04-29 @ 1600 CEST / 1100 EDT**

[Link](https://www.worldtimebuddy.com/?qm=1&lid=5,12,2643743,8,1850147,100,14,14&h=5&date=2026-4-29&sln=11-12&hf=1) to meeting time in common time zones.

| Search Key | Description |
| :---- | :---- |
| \[todo\] | Action Item |
| \[decision\] | Something decided on |
| \[important\] | Key information |

## **Agenda**

1. Solicitation of notetaker  
2. Acceptance of [Previous Meeting Minutes](https://github.com/Safety-Critical-Rust-Consortium/safety-critical-rust-consortium/blob/main/subcommittee/coding-guidelines/meetings/2026-04-22/minutes.md)  
3. Introduction of new members  
4. Review batches for [CERT C \=\> Rust Mapping](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/336) (Pete)  
   - Let's split up again, to get some feedback on batches 1 & 2  
   - [\#427 \[CERT C Review Batch 1/5\] Review proposed Rust categorization](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/427)  
   - [\#428 \[CERT C Review Batch 2/5\] Review proposed Rust categorization](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/428)  
5. Coverage of MISRA C and CERT C in 2026 (Félix / Markus updates)  
   - MISRA C one has a [PR up](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/432) from Markus  
6. Interest in the MISRA C++ mapping  
   - Please register interest on [this Zulip thread](https://rust-lang.zulipchat.com/#narrow/channel/579369-safety-critical-consortium.2Fcoding-guidelines/topic/MISRA.20C.2B.2B.20Mapping.20Interest/with/584764785)  
   - Pete/Alex are working out how we can have some kind of copy of the MISRA documents (C, C++) held in the jurisdiction of the Rust Foundation in support of members to be able to work on coding guidelines  
7. Overview of [Safety-Critical Rust](https://rust-lang.github.io/rust-project-goals/2026/roadmap-safety-critical-rust.html) \- Rust Project Goals Roadmap (Pete)  
   - Soliciting those interested in [Establish a Spot for Safety-Critical Lints in Clippy](https://rust-lang.github.io/rust-project-goals/2026/safety-critical-lints-in-clippy.html) goal  
     * Register interest [here](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/Getting.20involved.20with.20Clippy.20for.20SCRC.20lints/with/583090116) on Rust Zulip  
   - Soliciting those interested in [Normative Documentation for Sound unsafe Rust](https://rust-lang.github.io/rust-project-goals/2026/safe-unsafe-for-safety-critical.html) goal  
     * Register interest [here](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/SCRC.20.3C.3D.3E.20t-opsem.3A.20Normative.20Documentation.20for.20Sound.20.60unsafe.60/with/586198564) on Rust Zulip  
8. Proposals and ideas for new rules (all)  
9. Progress on ongoing tasks (all)  
10. Round table

## **Check-in area**

**Please add your name, and an emoji that describes your day.**

* Jonatan Hatakeyama Zeidler 🤖  
* Oreste Bernardi 🫥  
* Pete LeVasseur ✌️  
* Max Jacinto 🏹  
* Alex Celeste 😴

**Notetaker:**

* Jonatan Hatakeyama Zeidler

For tips on how we take notes in the Safety-Critical Rust Consortium, please see the [Meeting Notetaker Role](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/docs/notetaker-role.md) doc.

## **Housekeeping section**

* Document space: [coding-guidelines](https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines)  
* Zulip: [safety-critical-consortium: Coding Guidelines](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/Coding.20Guidelines)  
* [Kanban board](https://github.com/orgs/rustfoundation/projects/1/views/3)  
  * [`contributor experience`](https://github.com/orgs/rustfoundation/projects/1/views/4) view  
  * [`coding guideline`](https://github.com/orgs/rustfoundation/projects/1/views/5) view

## **Tasks**

* Pete: Follow up with Markus on Coverage of MISRA C and CERT C in 2026  
* Pete: Reach out to someone from MISRA and talk with them about the concrete use case of a copy of MISRA C++

## **Meeting Minutes**

* Previous meeting minutes accepted  
* Max reported that he doesn’t have a copy of MISRA C++, yet  
* A question came up about whether there is a planned start date for the MISRA C++ mapping, conclusion: no fixed start or end date, just that prerequisites need to be resolved and then we can start  
* Everybody is invited to join any of the Project Goal efforts via Zulip discussion  
* The pipeline from the operational semantics team \-\> reference updated \-\> FLS will likely take them some time. In the meantime we want to be practical with getting normative documentation updated.


**Notes on CERT C Review Batch 1 of 5**

* PR31: It seems to apply indeed, because it seems to be conceptually the same in C and Rust. Even the current note seems to confirm that. Proposed advisory see [https://github.com/Safety-Critical-Rust-Consomay need to be mappedrtium/safety-critical-rust-coding-guidelines/issues/557](https://github.com/Safety-Critical-Rust-Consortium/safety-critical-rust-coding-guidelines/issues/557)  
* EXP30: It isn’t UB indeed, but we should probably still keep this rule as applicable, because there is still good reason to avoid this to prevent misleading the reader of code.  
* EXP32: There is read\_volatile and write\_volatile, which are unsafe. So this still applies in unsafe contexts.  
* ARR39: It seems to be applicable when using the offset API. So we should map it. See [https://doc.rust-lang.org/std/primitive.pointer.html\#method.offset](https://doc.rust-lang.org/std/primitive.pointer.html#method.offset)   
* FIO32: We think that this could apply, because this is not a problem of the language, but the OS. See also [https://doc.rust-lang.org/std/os/unix/io/index.html\#procselfmem-and-similar-os-features](https://doc.rust-lang.org/std/os/unix/io/index.html#procselfmem-and-similar-os-features)   
* FIO46: We agree it does not apply.

## **Material**

Any material to read before the meeting should be included here.
