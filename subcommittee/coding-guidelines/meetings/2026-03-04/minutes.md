# **Coding Guidelines Subcommittee Meeting on 2026-03-04 @ 1700 CET / 1100 EST**

[Link](https://www.worldtimebuddy.com/?qm=1&lid=5,2643743,12,8,1850147,100,14&h=5&date=2026-3-4&sln=11-12&hf=1) to meeting time in common time zones.

| Search Key | Description |
| :---- | :---- |
| \[todo\] | Action Item |
| \[decision\] | Something decided on |
| \[important\] | Key information |

## **Agenda**

1. Solicitation of notetaker  
2. Acceptance of [Previous Meeting Minutes](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/coding-guidelines/meetings/2026-02-25/minutes.md)  
3. Introduction of new members  
4. [Safety-Critical Rust Flagship Theme](https://rust-lang.github.io/rust-project-goals/2026/roadmap-safety-critical-rust.html) (Pete)  
5. Embedded World: shout out of SCRC (Alex Celeste)  
6. Reviewer Bot: How's it going? (Pete)  
   * Bugged out, [fix incoming](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/423) 😅  
7. Coverage of MISRA C and CERT C in 2026 (Markus)  
8. CERT C \=\> Rust Mapping (Tentative: Félix / David)  
   * WIPs are resolved\!  
9. Proposals and ideas for new rules (all)  
10. Progress on ongoing tasks (all)  
11. Round table

## **Check-in area**

* David Svoboda (-;  
* Christof Petig 🫖  
* Alex Celeste ☕  
* Samuel Wright 😩  
* Oreste Bernardi 🏢  
* Max Jacinto 🏋️  
* Pete LeVasseur 🖖  
* Julius Gustavsson  
* Markus Hosch 🌞xx

**Please add your name, and an emoji that describes your day.**

**Notetaker:**

* David Svoboda

For tips on how we take notes in the Safety-Critical Rust Consortium, please see the [Meeting Notetaker Role](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/docs/notetaker-role.md) doc.

## **Housekeeping section**

* Document space: [coding-guidelines](https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines)  
* Zulip: [safety-critical-consortium: Coding Guidelines](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/Coding.20Guidelines)  
* [Kanban board](https://github.com/orgs/rustfoundation/projects/1/views/3)  
  * [`contributor experience`](https://github.com/orgs/rustfoundation/projects/1/views/4) view  
  * [`coding guideline`](https://github.com/orgs/rustfoundation/projects/1/views/5) view

## **Tasks**

* xx

## **Meeting Minutes**

* Solicitation of notetaker  
  * David Svoboda will take minutes  
* Acceptance of [Previous Meeting Minutes](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/coding-guidelines/meetings/2026-02-25/minutes.md)  
  * Accepted by unanimous consent  
* Introduction of new members  
  * None  
* [Safety-Critical Rust Flagship Theme](https://rust-lang.github.io/rust-project-goals/2026/roadmap-safety-critical-rust.html) (Pete)  
  * Niko wanted a flagship theme for the goals Pete suggested.  I request everyone with a safety-critical interest in Rust read. There is some interest in getting SCRC members to help write Clippy linters.  
  * Oreste: Re: goals: Macro expansion. Is this considered relevant to SCRC?  
  * Pete: We should have a listing of things that we care about. Perhaps an issue to gather things we care about, to turn into project goals in the future.  
  * David: I interpret this to mean what is the scope of the coding guidelines?  I think we intended the Rust standard language & library to be our scope. So this would include macro expansion.  
  * Pete: Oreste, when you create the issue, note two paths.  
  * Christof: Need serialization to be in scope for function safety.  
* Embedded World: shout out of SCRC at Embedded World (Alex Celeste)  
  * Is there anything people want to point out that is especially important for my upcoming venue?  
  * Christof: Currently in another ballot in the Motor Vehicle Council (regarding SAE JA-1020, to get this published).  
    “Link” to the standard [https://www.sae.org/standards/ja1020-recommendations-rust-programming-language-safety-related-systems](https://www.sae.org/standards/ja1020-recommendations-rust-programming-language-safety-related-systems)   
  * Pete: Alex, also take this to Zulip.  
* Reviewer Bot: How's it going? (Pete)  
  * Bugged out, [fix incoming](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/423) 😅  
  * Julius: I did a review, it seemed to work.  
  * Sam: I added some additional documentation that went into effect today.  
  * Marcus: These comments "hey can you please review" are easy to miss.  I also lacked rights to click things I was told I need to click.  
  * Pete: Try to review Sam's documentation that clarifies the process (partially complete).  
  * Pete is working to improve the situation, e.g. see [https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/411](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/411)  
* Coverage of MISRA C and CERT C in 2026 (Markus)  
  * Meeting last Friday. Minutes: [JA1020 : Recommendations for the Rust Programming Language in Safety-Related Systems \- SAE International](https://www.sae.org/standards/ja1020-recommendations-rust-programming-language-safety-related-systems)  
  * Coverage of [CERT C work by Felix/David](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/336) and the MISRA C work by Alex Celeste ([https://misra.org.uk/app/uploads/2025/03/MISRA-C-2025-ADD6.pdf](https://misra.org.uk/app/uploads/2025/03/MISRA-C-2025-ADD6.pdf))  
  * A way of dealing with two standards: we have links to rules on our side. Some rules apply only to unsafe Rust, others apply to both safe & unsafe Rust. Initial delivery would be a list of applicable CERT rules & MISRA rules.  
  * David: We will also eventually want mappings for CERT C++ & CERT Java.  
  * The Clippy lint mappings is not part of the MVP.  
  * Sam: We should give people discrete things they can work on in an open-source manner.  
  * Pete: Marcus, please post to Zulip, requesting a volunteer to build Rust rules corresponding to the MISRA rules that should map to Rust rules, which Alex completed.  
  * David: Each individual rule should be its own task, On average it takes me 1 day to write 1 rule (for CERT).  
  * Max: Should we support MISRA C++ in parallel with CERT C++ or do CERT first?   
* CERT C \=\> Rust Mapping (Tentative: Félix / David)  
  * WIPs are resolved\! (tabled until next week)  
* Proposals and ideas for new rules (all) (tabled)  
* Progress on ongoing tasks (all) (tabled)  
* Round table  
  * None

## **Material**

Any material to read before the meeting should be included here.

* Milestone: [Prepare for launch to wider Rust community](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1)

