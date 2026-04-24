# Coding Guidelines Subcommittee Meeting on 2026-04-01 @ 1600 CEST / 1100 EDT

[Link](https://www.worldtimebuddy.com/?qm=1&lid=5,12,2643743,8,1850147,100,14&h=5&date=2026-4-1&sln=11-12&hf=1) to meeting time in common time zones.

| Search Key | Description |
| :---- | :---- |
| \[todo\] | Action Item |
| \[decision\] | Something decided on |
| \[important\] | Key information |

## **Agenda**

1. Solicitation of notetaker  
2. Acceptance of [Previous Meeting Minutes from last instance](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/coding-guidelines/meetings/2026-03-25/minutes.md), [Previous Meeting Minutes from last Asia Pacific \+ Americas meeting](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/coding-guidelines/meetings/2026-03-27/minutes.md)  
3. Introduction of new members  
4. Overview of [Safety-Critical Rust](https://rust-lang.github.io/rust-project-goals/2026/roadmap-safety-critical-rust.html) \- Rust Project Goals Roadmap (Pete)  
   - Soliciting those interested in [Establish a Spot for Safety-Critical Lints in Clippy](https://rust-lang.github.io/rust-project-goals/2026/safety-critical-lints-in-clippy.html) goal  
   - Great way to get mentored and onboarded if interested in Clippy  
5. Macros chapter rework (Alex)  
6. Review batches for [CERT C \=\> Rust Mapping](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/336) (David)  
   - [\#427 \[CERT C Review Batch 1/5\] Review proposed Rust categorization](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/427)  
   - [\#428 \[CERT C Review Batch 2/5\] Review proposed Rust categorization](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/428)  
   - [\#429 \[CERT C Review Batch 3/5\] Review proposed Rust categorization](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/429)  
   - [\#430 \[CERT C Review Batch 4/5\] Review proposed Rust categorization](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/430)  
   - [\#431 \[CERT C Review Batch 5/5\] Review proposed Rust categorization](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/431)  
7. Coverage of MISRA C and CERT C in 2026 (Félix / Markus)  
   - MISRA C one has a [PR up](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/432) from Markus  
   - Félix wanted the review batches done first IIRC; also not feeling well so we pause  
8. Proposals and ideas for new rules (all)  
9. Progress on ongoing tasks (all)  
10. Round table

## **Check-in area**

**Please add your name, and an emoji that describes your day.**

* David Svoboda (-:  
* Samuel Wright 😷  
* Pete LeVaseur 🍵  
* Douglas Deslauriers 🖌️  
* Max Jacinto 🍕  
* Markus Hosch 👽  
* William Barsse  
* Christof Petig 🚲  
* Arshad Mahmood 🕺  
* Oreste Bernardi🏥  
* Alex Celeste 🍵

**Notetaker:**

* Alex Celeste \+ Pete

For tips on how we take notes in the Safety-Critical Rust Consortium, please see the [Meeting Notetaker Role](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/docs/notetaker-role.md) doc.

## **Housekeeping section**

* Document space: [coding-guidelines](https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines)  
* Zulip: [safety-critical-consortium: Coding Guidelines](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/Coding.20Guidelines)  
* [Kanban board](https://github.com/orgs/rustfoundation/projects/1/views/3)  
  * [`contributor experience`](https://github.com/orgs/rustfoundation/projects/1/views/4) view  
  * [`coding guideline`](https://github.com/orgs/rustfoundation/projects/1/views/5) view

## **Tasks**

* \[todo\] Pete: post the invitation to participate in writing Clippy lints to Zulip  
* \[todo\] request Felix’s opinion of the comments that have been added, when he is available and not before  
* \[todo\] Pete to put out the list of available spaces for the Rust Week meeting; anyone interested in going, to contact Pete to claim one of them

## **Meeting Minutes**

* Safety-Critical Rust Roadmap \- brought under the purview of the Rust Project, four current goals listed but more can be added  
  * Place any new items into a sequence leading into 2027, 2028  
  * Opportunity for anyone wanting to get involved with the Project / interested in static analysis / interested in Clippy:  
    * Task to take Guidelines produced by the Subcommittee and turn them into actionable, configurable lints  
    * Reach out to Pete; room for 2-3 people to get hands-on mentoring \[a couple of volunteers express interest in the room\]  
* Macros chapter cleanup  
  * Sitting there in “be provocative” and “force documentation of features” way  
  * Curious to see if there are directions folks would like to see it move in  
  * E.g. if interested in auditability   
  * Forbidding / subsetting today is suitable in a sense  
    * Some thoughts that in ISO 26262 ASIL D it’s probably fine to forbid macros  
    * Use generated macro code and run the same sorts of analysis on them as normal Rust code  
  * We could be more specific or be more broad  
  * Are we okay with “you shall not use macros” and encourage using the generated code instead?  
    * Kind of okay with this; could treat this more as a tool rather than a language construct  
    * Test of our feedback mechanism/exception writing process of the guidelines to start dialog with users   
    * Macros in C vs Rust  
      - with C you can get the exact code out of the preprocessor  
      - with Rust that’s not necessarily the case  
      - might need new compiler extension to test this correctly  
    * If using many macros, this could become onerous and painful  
      - feedback that one commercial tool does this check of whether the macro-generated code doesn’t change the meaning  
      - check that the code does the same thing before/after macro expansion  
    * Useful tool that could be looked into:  
      - [https://github.com/scrabsha/cargo-hexpand](https://github.com/scrabsha/cargo-hexpand)  
  * What about projects where macros are used? Heavily?  
    * e.g. a project using mantra for traceability  
    * would this require deviation at each point of expansion?  
      - No, not necessarily; could be kind of a “blanket” deviation  
    * It would be up to the auditor whether or not they agree it would be justified to deviate once for all uses of that one specific macro  
    * Nightly compiler required for macro expansion  
  * Usage of standard library is kind of a separate concern, if using e.g. `println!(..)`  
  * Usage of tools  
    * How easy/hard it is to mitigate issues with tools  
    * How impactful any issue with tool  
    * Can derive Tool Confidence Level (TCL)  
    * MISRA has [“MISRA AC”](https://misra.org.uk/misra-autocode/) as a separate standard  
  * `fmt!()` and friends are a part of libcore; could be already a part of some newly safety-certified code coming up  
  * For ASIL D restricting usage of macros can make sense; for ASIL B it seems to be too restrictive  
  * Macros are important for variable number of arguments; not possible with functions currently  
  * Feedback from Eclipse S-CORE:  
    * If inspecting macro output itself doesn’t work this is a challenge  
    * Different levels of ASIL have different rules; differences between e.g. ASIL B, D  
    * Some issues with this in practice if the coding guidelines are not explicit  
    * required is fine so long as project-wide justifications for Deviations are provided: in practice this is accepted by ASIL-D  
  * Summary of section: distinction between writing and expanding macros  
    * Required axis for writing macros, esp proc  
    * Required axis for using macros, with the possibility of Deviation at either an expansion site or by macro name  
    * Safety level \- too restrictive for the lower (e.g. ASIL A, B) safety levels to ban them all but this will test our ability to follow up  
      - Want the ability to tag guidelines as relevant to specific safety level user profiles  
      - Onerous for more idiomatic uses of the language and its direction of evolution  
    * Specific exceptions can be directly integrated into the guidelines for known named macros or builtins  
* Review of the CERT C mapping  
  * Three out of the five “buckets” were examined last week; the table for each bucket has been reviewed by David with comments added where necessary (comments not added when they didn’t add anything but all mappings reviewed)  
    * For example, once comment added on the fifth bucket to add missing context on a specific rule (DCL37-C)  
  * Tables are not yet fully updated \- not many comments to address which might change them  
    * Additional feedback comments can be added offline  
    * Further actions pending Felix’s availability  
  * MISRA C 2023 has an Addendum with a mapping to CERT C; this content will also be imported to CERT C itself  
    * Some possible discrepancies on things like the definition of “decidable” (MISRA “decidable” approximately equals CERT “detectable”)  
* We heard back from MISRA and their stance is to disallow permission to use the MISRA C rule headlines  
  * Possible arrangement to be made in future but not currently for use in public  
  * CERT C may have permission to use the titles (unclear where this came from)  
  * Rule numbers are always OK to use  
    * Hopefully not a huge problem in practice for readability  
* MISRA C++ committee producing an equivalent to MISRA C ADD6  
  * Alex brought this to them; got the “okay” for it being signed off on by the C++ experts  
  * Someone from the Rust world would need to write it, they had not agreed on writing it as they are not Rust experts  
  * Another potentially useful tool for credibility with auditors etc.  
* Free spaces in the Rust Week meeting (see todo)  
  * Some of the free spaces can be used for non-SCRC members who are already at Rust Week and may want to participate  
* Adjourned.

## **Material**

Any material to read before the meeting should be included here.
