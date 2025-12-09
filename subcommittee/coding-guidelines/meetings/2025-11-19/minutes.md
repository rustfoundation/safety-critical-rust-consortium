# **Coding Guidelines Subcommittee Meeting on 2025-11-19 @ 1100 EDT / 1700 CET**

[Link](https://www.worldtimebuddy.com/?qm=1&lid=5,100,2643743,12,1850147,2193733,8,6,2673730,1261481&h=5&date=2025-11-19&sln=11-12&hf=1) to meeting time in common time zones.

| Search Key | Description |
| :---- | :---- |
| \[todo\] | Action Item |
| \[decision\] | Something decided on |
| \[important\] | Key information |

## **Agenda**

1. Solicitation of notetaker  
2. Acceptance of [Previous Meeting Minutes](https://github.com/AlexCeleste/safety-critical-rust-consortium/blob/2405d36fa0b4a9f5dd406640b4e18b8345fdc14d/subcommittee/coding-guidelines/meetings/2025-11-12/minutes.md)  
3. Introduction of new members
4. Review progress on guidelines incorporated from CERT  
   * [High-level mapping of CERT rule groups to Rust](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/152)  
     * Integers \- Félix Fischer  
     * Arrays \- Alex Celeste  
     * Floating Point \- Andrew Fernandes
5. Merging of https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/149 has happened
   * Have a read on GOALS.md, README.md and CONTRIBUTING.md and think about valuable additions and clarifications
   * Please start incorporating updates (e.g. from review comments) as separate PRs
6. Proposals and ideas for new rules
   * Idea: Give room for the optional step 0 in our contributing guideline, aka "round table for new rules".
7. Grooming of rule issues - promote to PRs if appropriate
8. Round table

## **Check-in area**

**Please add your name, and an emoji that describes your day.**

* Markus Hosch 🚗
* Pete LeVasseur 😴
* Félix Fischer 🙂
* Sam Wright ❄️
* Oreste Bernardi
* Douglas Deslauriers 🍂
* Tiago Manczak
* Alex Celeste ☕
* David Svoboda :) 
* William Barsse
* Max Jacinto 🫠
* Daniel Krippner 🧑‍🦯

**Notetaker:**

* Alex Celeste

For tips on how we take notes in the Safety-Critical Rust Consortium, please see the [Meeting Notetaker Role](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/docs/notetaker-role.md) doc.

## **Housekeeping section**

* Document space: [coding-guidelines](https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines)  
* Zulip: [safety-critical-consortium: Coding Guidelines](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/Coding.20Guidelines)  
* [Kanban board](https://github.com/orgs/rustfoundation/projects/1/views/3)  
  * [`contributor experience`](https://github.com/orgs/rustfoundation/projects/1/views/4) view  
  * [`coding guideline`](https://github.com/orgs/rustfoundation/projects/1/views/5) view

## **Tasks**

* Now the Process has been merged, add a recurring item for an open call for new rule ideas, distinct from the rest of the Roundtable
* New PRs and similar can be discussed during this section
* Someone to modify the Issue automation to dump a comment with “PR content” at the bottom of the same Issue, instead of creating the PR directly
* Review RCS’s new rules
* Needs a tier (defect)
* Review the Defensive Patterns list (https://corrode.dev/blog/defensive-programming/) to consider which ones are suitable to import as rules, via Issues
* Issue 97 needs minimal improvement to meet baseline for inclusion
* Review PR 225
* If Clippy statistics over crates.io exist, someone to submit and share for discussion next time

## **Meeting Minutes**

* Previous minutes accepted; no new members
* Progress on CERT
  * Integer rules are waiting on some remaining blockers; most things should now be solved
    * PR 181 depends on 180 (180 merged during meeting)
    * Following guidelines are in progress but blocked by these PRs
    * Next up is the rule about shifts (INT34) and conversions not losing data (INT31), each with a defect-oriented and subset-oriented version
    * Soliciting wording review
    * There is an existing rule in the document so content will need to be merged or otherwise made non-redundant
  * Progress being made on the long list of Clippy lints - 10-20 per week, out of 800 total, first block of 100 done
  * Progress stalling on wording
    * Don’t overthink it, explanation of why indexing off the end of a buffer is bad, isn’t really needed
    * No equivalent to the rule about the C Standard Library; mark this one as explicitly unmapped, and instead create an approximate equivalent that instead refers to actual Rust features, not falling down to C Library features (ARR38)
    * Similar concern in the integer section w.r.t library
  * Do we have a canonical list of CERT C rules to work on?
    * Not a shared one at this time, proceeding adhoc; DS has a list that may be suitable to use as a shared basis
* If there are any further comments on the Process or Goals, please create follow-up issues or PRs as appropriate
  * Minor comment about the optional nature of the zeroth step
  * Discussion about whether the creation of the PR marks a hard line vs. going back to the Issue stage (not necessarily well-supported by the GitHub workflow)
  * Thinking about Markdown is easier for most folks than working directly in ReST
    * It is easy to modify the branches the automation creates with minor tweaks, but does this depend on having write privileges?
    * If not, users might not be able to modify the PR
    * It is also possible to branch from the automatically-created branch in a private fork, and create a PR from that
  * Opening a PR on your own fork is the intended GH workflow and something people know how to do
    * [decision] If the automation gets in the way by creating the wrong kind of PR, we can always dump the content in an Issue comment instead and let people create their own PRs
    * [todo] Need someone to change this to dump a comment instead of directly creating a PR
* Discussion of PR 220, covering INT30-C and INT32-C
  * Similar to what Felix has been working on already
  * Attested in Issue 152, both as Applicable + WIP status
  * Came to exactly the same conclusion as RCS, to combine them into a single rule as the distinction between the CERT rules is mostly a C thing
  * [todo] verify that this aligns with the intent of existing work
  * Lots of examples, very good example rule
* Defensive Programming Rules post at https://corrode.dev/blog/defensive-programming/
  * All work done already by the author to make these into enforceable Clippy rules
  * Not focused on safety-critical concerns, only on general code quality (but this affects safety-critical same as everything else)
  * [todo] open up Issues for appropriate suggestions in this list? Would need to review which proposals are useful
* Issues ready to promote to PRs:
  * Should have an attached “mentor” to review and promote to PR
  * Issue 97: lot of TODO, but the macros section is underdeveloped anyway and this wouldn’t make it worse
    * No Rationale at all though, which is below the bar for inclusion
    * A rule has to be actionable and this doesn’t define what “complex” means
    * When discussing what order to proceed, was agreed to start on the areas of the language that we have a better grasp on in order to evolve our own understanding of how to write guidelines and what they are meant to achieve
    * The rules about macros are difficult to say how they actually affect safety-critical, and are therefore maybe something to defer
    * We probably want something like this but at least has to have minimal Rationale, something that hints how the user can apply it
    * Getting rid of “complex” from the normative title might be an improvement, at least “recursive” is definable
    * [todo] improve this rule so it meets minimum bar for inclusion
    * [decision] we should define an absolute minimal bar for inclusion of placeholders, which we might have a reason to merge in an incomplete state but they do have to say something
    * [decision] Issue Assignee should record the “mentor”
  * Issue 133: feedback provided by mentor, ready for author to progress
    * Very complete text, should only need minor formatting improvements and clarifications
  * Issue 137: actually already agreed in a previous meeting
    * Should be as simple as adding a label to the Issue but apparently forgotten in a previous meeting
    * Label added during meeting, converted to PR 225
  * Issue 174: already promoted (will use a filtered list)
* [decision] In future, devote more of the meeting time to the Issue grooming (30 minutes?)
* Discussion about feedback on the macro rule - clarify that this should apply to declarative macros?
  * Difficult to say anything much about procedural macros
  * Difficult to deduce many things from macros, complexity etc. doesn’t apply in the same way as to source code
* The reviews of the RFC process have been processed and will hopefully be merged now
  * This will unblock producing additional RFCs
* Lints in “nursery” are defined by not being production-ready, be careful with these ones in the list
  * “fallible impl from” is affected in the list
  * Has someone tried to run all Clippy rules on all of crates.io to gather statistics about most-violated rule etc?
    * Some attempts but mostly to gauge which lints are disabled
    * Such statistics would be interesting if they exist

## **Material**

Any material to read before the meeting should be included here.

* Milestone: [Prepare for launch to wider Rust community](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1)  
* FLS Maintenance: [FLS Team \- North Star](https://hackmd.io/@plevasseur/HJb6qomOge/edit)  
* [Github Issue to discuss about panicking in Safety Critical](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/158)
