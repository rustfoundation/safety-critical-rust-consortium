# Coding Guidelines Subcommittee Meeting on 2025-02-12 @ 3pm UTC

## Agenda

1. Acceptance of [Previous Meeting Minutes](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/coding-guidelines/meetings/2025-January-29/minutes.md)  
2. Consortium report (Pete LeVasseur)  
   * Work items  
   * Status  
   * Roadmap  
   * Items we'd like to bring to wider consortium attention  
3. `unsafe` Formulate Chapter Material Task Force \- progress report (Markus, Jonas, Pete)  
4. `unsafe` Practicum Chapter Task Force \- form task force (Pete LeVasseur)  
5. Safety Pamphlet \- progress report (Andrew Fernandes)  
6. Round table

Supplemental material to the agenda can be found on the [GitHub repo](https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines).

## Check-in area

**Please add your name, and an emoji that describes your day.**

* Enow Scott 😀  
* Pete LeVasseur, ✈️😴  
* Joni Pelham 😀  
* Julius Gustavsson 😀  
* Douglas Deslauriers 🙂  
* Xander Cesari 😶‍🌫️  
* Andrew Herridge 😀  
* Koppany Pazman  
* Vincent EckSie 😀  
* Sasha Pourcelot ☕  
* Arthur Hicken 🚀  
* Jonas Wolf 🙂  
* Joel Marcey 🥱  
* Lukas Wirth  
* Christof Petig 🏔️🥾

**Notetaker:**

* Joni Pelham

## Housekeeping section

* Document space: [coding-guidelines](https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines)  
* Zulip: [safety-critical-consortium: Coding Guidelines](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/Coding.20Guidelines)

## Tasks

* 

## Meeting Minutes

1. Xander Cesari proposed the minutes of the last meeting be accepted and it was agreed unopposed.  
2. Reminder of the Hybrid consortium meeting occurring Wednesday next week.  
* PL suggested the group start work on a roadmap for the necessary items that should be addressed and how the work should be organised.  
  * DD suggested one start point would be with MISRA Rust work being formulated by Alex.  
  * OB suggested a marker to indicate that a particular feature is automatically checked. This comes from his work in the Tooling subcommittee.  A definition of undefined behaviour should be part of the glossary being produced by this subcommittee.  
  * DV cited the issue of deadlocks in rust not leading to undefined behaviour but can have safety implications in use.  
  * XC curious what blockers are from companies using rust in production. PL plugged software defined vehicle work group activity in response to this.  
  * JW discussed organisation practices with Rust development and mentioned the use of internal review whenever the unsafe keyword was required.  
  * JA1020 standard cited.  [JA1020 (WIP) Recommendations for the Rust Programming Language in Safety-Related Systems \- SAE International](https://www.sae.org/standards/content/ja1020/) should they be an inspiration?  
  * JP suggested use of tutorial development may be a useful way to help drive adoption once coding guidelines are done. Similar to Software Carpentry content. [Software Carpentry Lessons | Software Carpentry](https://software-carpentry.org/lessons/)  
3. `unsafe` Formulate Chapter Material Task Force  
   * JW progress being made re intrinsics and highlighted some functions that need more attention [https://github.com/rustfoundation/safety-critical-rust-consortium/pull/148](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/148)  
     * Transmute one example  
   * PL limited progress due to time constraints. Fernando made some progress on dangling and unaligned pointers.  [Example reading unaligned pointers. by iglesias · Pull Request \#154 · rustfoundation/safety-critical-rust-consortium · GitHub](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/154)  
4. `unsafe` Practicum Chapter Task Force  
* PL emphasised the need for work on the development on the Practicum. JP volunteered to assist.  
5. Safety Pamphlet \- progress report  
* Andrew Fernades unable to attend but he is still formulating what the safety pamphlet will look like.  
6. Round table  
   1. JW what is the agenda for next weeks meeting. [Add proposed agenda for February consortium meeting by JoelMarcey · Pull Request \#149 · rustfoundation/safety-critical-rust-consortium · GitHub](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/149)

      

## Material

Any material to read before the meeting should be included here.

### Tracking Issues

* [\[Coding Guidelines\] Learn unsafe Rust \- Practicum Chapter Draft](https://github.com/rustfoundation/safety-critical-rust-consortium/issues/122)  
* [\[Coding Guidelines\] Formulate Chapter Material for Learn unsafe Rust](https://github.com/rustfoundation/safety-critical-rust-consortium/issues/123)
