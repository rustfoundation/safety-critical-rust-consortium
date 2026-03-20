# **Coding Guidelines Subcommittee Meeting on 2026-03-18 @ 1600 CET / 1100 EDT**

[Link](https://www.worldtimebuddy.com/?qm=1&lid=5,12,2643743,8,1850147,100,14&h=5&date=2026-3-18&sln=11-12&hf=1) to meeting time in common time zones.

| Search Key | Description |
| :---- | :---- |
| \[todo\] | Action Item |
| \[decision\] | Something decided on |
| \[important\] | Key information |

## **Agenda**

1. Solicitation of notetaker  
2. Acceptance of [Previous Meeting Minutes](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/coding-guidelines/meetings/2026-03-11/minutes.md)  
3. Introduction of new members  
4. Rust readiness for ISO 26262 (kudos to Stefan Akatyschew\!)  
   - Analysis added and home page updated to guide towards that  
   - [https://arewesafetycriticalyet.org/](https://arewesafetycriticalyet.org/)  
5. Review batches for [CERT C \=\> Rust Mapping](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/336) (Félix)  
   - [\#427 \[CERT C Review Batch 1/5\] Review proposed Rust categorization](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/427)  
   - [\#428 \[CERT C Review Batch 2/5\] Review proposed Rust categorization](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/428)  
   - [\#429 \[CERT C Review Batch 3/5\] Review proposed Rust categorization](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/429)  
   - [\#430 \[CERT C Review Batch 4/5\] Review proposed Rust categorization](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/430)  
   - [\#431 \[CERT C Review Batch 5/5\] Review proposed Rust categorization](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/431)  
6. Coverage of MISRA C and CERT C in 2026 (Félix / Markus)  
   - MISRA C one has a [PR up](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/432) from Markus  
   - Félix wanted the review batches done first IIRC  
7. Progress on ongoing tasks (all)  
8. Round table

## **Check-in area**

* David Svoboda :)   
* Douglas Deslauriers 💍  
* William Barsse  
* Samuel Wright 😪  
* Félix Fischer ☕  
* Max Jacinto 🏹  
* Pete LeVasseur 📆  
* Arshad Mahmood ☀️  
* Andreas Weis 📝  
* Markus Hosch  
* Achim Kriso

**Please add your name, and an emoji that describes your day.**

**Notetaker:**

* Andreas Weis

For tips on how we take notes in the Safety-Critical Rust Consortium, please see the [Meeting Notetaker Role](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/docs/notetaker-role.md) doc.

## **Housekeeping section**

* Document space: [coding-guidelines](https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines)  
* Zulip: [safety-critical-consortium: Coding Guidelines](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/Coding.20Guidelines)  
* [Kanban board](https://github.com/orgs/rustfoundation/projects/1/views/3)  
  * [`contributor experience`](https://github.com/orgs/rustfoundation/projects/1/views/4) view  
  * [`coding guideline`](https://github.com/orgs/rustfoundation/projects/1/views/5) view

## **Tasks**

* Félix: remove “Anyone with the link can be Editor” as soon as the meeting is done  
  * **Completed\! 🙂**

## **Meeting Minutes**

* Approval of minutes from last meeting.  
* Introduction of new members: Arshad Mahmood  
* Draft roadmap to ISO26262 readiness at [https://arewesafetycriticalyet.org/docs/intro](https://arewesafetycriticalyet.org/docs/intro)

   Got feedback from safety experts. If you have experience in functional safety, please give feedback. Having reds and yellows in there is not a bad thing, because it gives an honest impression of where we stand.  
* **Question**: Why is supporting processes red?   
  * There was a discussion about this at [https://rust-lang.zulipchat.com/\#narrow/channel/445688-safety-critical-consortium/topic/ISO.2026262.20.2F.20Rust.20gap.20analysis/with/575829353](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/ISO.2026262.20.2F.20Rust.20gap.20analysis/with/575829353)  
* **Topic**: mapping CERT-C to Rust [https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/336](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/336)  
  * POS and WIN rules are omitted for now, other rules are grouped in batches and are ready for feedback. The idea is to see if we agree on the rationale and the mapping of the rules. We have links to the full rule texts. The question is whether it is useful in all of Rust or only in unsafe (especially rules dealing with undefined behaviour), or not at all.  
  * **Call to action:** please take a look at the proposed classification and give feedback. If a rule does not apply to Rust we give a rationale. Each rule will eventually become an item in the Kanban board and people can grab an item to write that guideline.  
* **Conversation:** *Why Guidelines? And why these?*  
  * Potential users of this, like Eclipse S-Core want a development environment up to ASIL B until the end of 2026\. Having coding guidelines is a prerequisite. People have internal guidelines now. Having users for these guidelines that give us feedback from real world projects is good and will help us shape those guidelines.  
  * Using the guidelines means we need a tool that enforces them automatically. The first step is to have people just read them and try to follow them, but we only get the real feedback once we have them in tools. What is useful there is a mapping from rules to already existing Clippy rules. We already enforce Clippy, but we can’t claim anything from that. If we could just switch to a safety-critical set of Clippy checks, that would be very useful.  
    1. **Note:** is a Rust project goal for 2026 to do this: [https://rust-lang.github.io/rust-project-goals/2026/safety-critical-lints-in-clippy.html](https://rust-lang.github.io/rust-project-goals/2026/safety-critical-lints-in-clippy.html)
    Contributions are very welcome. Goal period starts in April 2026\.  
    2. **Note:** guidelines currently have an item whether they are decidable/undecidable. Some rules are difficult or impossible to enforce automatically. It will be very important when writing lints for those rules, since well, a rule being undecidable means that a lint cannot exist for that rule.  
* **FAQs about CERT mapping:**  
  * We have an issue where we discuss implications of interfacing with C from Rust:  
    1. [Question](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/430#issuecomment-4071115521) about FFI in the context of CERT C,  
    2. [Answer](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/430#issuecomment-4074338619) given from the POV of the scope of CERT  
  * It will add a lot of credibility to the guidelines if we can show mapping to established guidelines.  
* **Question**: When do you plan to add this to the addendum? We should have uniform mappings for all the different guidelines in the end.  
  * The MISRA C table is good but it is missing some info.  
  * I was more worried about the form of the content. All table entries should have the same fields in the columns in the end.  
  * Reading difficulties:  
    1. With the MISRA C table not all columns fit on the page without scrolling, making it difficult to read (**note that this is a CSS issue, not a content issue**). There are no headlines in the table, only directives.  
    2. The rationale acronyms should be explained before the table, because they are required to understand the table.  
  * We can’t put the MISRA rule content in there for IP reasons.  
    1. Adding the headlines from MISRA rules is usually fine, using the body of the rule text is not. **\[todo\]** Get in contact with Andrew Banks of MISRA C to discuss details, he can sort out any IP question..  
  * **Goal of the addendum:** is to argue that our guidelines are not a step back. We need to document that we covered everything that the existing rules cared about. When you omit a rule you need a rationale so that we have proof that we did not miss anything accidentally.  
  * The aim is to finish the CERT mapping’s feedback stage by the beginning of April.   
  * Idea: maybe if the MISRA table is slightly off and we merge it like that, we can just change some of the columns later. As long as we’re not showing incorrect information.  
  * The main difference is that MISRA focuses on subsetting the language and CERT focuses on potential vulnerabilities. In format and in spirit they should look the same though.  
  * **How the two tables relate:** it would be helpful to resolve this offline and unify the format of the two tables. For now put a version in a PR what it would look like with the current categories. I think that would help to reveal any issues.  
    1. We should avoid having different approaches to different standards. The way to map should be formulaic, normative. We want a cohesive document in the end.  
    2. During mapping we may find, e.g. that we only want to apply a subset of a rule. But that should not impact the format.

## **Material**

Any material to read before the meeting should be included here.

* Milestone: [Prepare for launch to wider Rust community](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1)