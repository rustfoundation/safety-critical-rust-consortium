# **Coding Guidelines Subcommittee Meeting on 2025-11-12 @ 0800 UTC / 0900 CET / 1700 JST**

[Link](https://www.worldtimebuddy.com/?qm=1&lid=14,12,1850147,5&h=14&date=2025-11-12&sln=8-9&hf=1) to meeting time in common time zones.

| Search Key | Description |
| ----- | ----- |
| \[todo\] | Action Item |
| \[decision\] | Something decided on |
| \[important\] | Key information |

## **Agenda**

1. Solicitation of notetaker  
2. Acceptance of [Previous Meeting Minutes](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/coding-guidelines/meetings/2025-11-04/minutes.md)  
3. Introduction of new member  
4. Share launch milestone & Kanban board (Pete LeVasseur)  
   * [Prepare for launch to wider Rust community](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1)  
   * [Kanban board](https://github.com/orgs/rustfoundation/projects/1/views/3)  
     * [`contributor experience`](https://github.com/orgs/rustfoundation/projects/1/views/4) view  
     * [`coding guideline`](https://github.com/orgs/rustfoundation/projects/1/views/5) view  
5. [FLS Team](https://rust-lang.org/governance/teams/lang/#team-fls) started (Pete)  
   * If interested in becoming involved, feel free to visit [Zulip channel](https://rust-lang.zulipchat.com/#narrow/channel/520710-t-lang.2Ffls) or come to our first meeting (find the `.ics` [here](https://rust-lang.github.io/calendar/fls.ics))  
6. Review [Goals and Contribution Process PR](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/149)  
7. Review progress on guidelines incorporated from CERT  
   * [High-level mapping of CERT rule groups to Rust](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/152)  
     * Integers \- Félix Fischer  
     * Arrays \- Alex Celeste  
     * Floating Point \- Andrew Fernandes  
8. Review macro guidelines  
   * Substantial duplication \- what directions do we want to proceed in?  
9. Round table

## **Check-in area**

**Please add your name, and an emoji that describes your day.**

* Alex Celeste ☕  
* Mikhail Antoshkin 🌆  
* Alex Senier 🥱  
* Samuel Wright 🥱  
* Markus Hosch  
* Oreste Bernardi  
* Daniel Krippner ☕

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

* \[todo\] Final review of PR 149 over the next day or so  
  * Add comments with minor wording tweaks (clarifying optional steps etc)  
* \[todo\] Two new rules for Unsafety  
  * A new subset rule requiring every unsafe function to annotate its preconditions  
  * A new mitigation rule requiring that the specified preconditions are not violated  
* \[todo\] Add the description of tier flavours to the contributing guide (in a separate PR, do not delay the GOALS PR)  
* \[todo\] Add a new field for the relationship links to the rule template and a description to the contributing guide  
* \[todo\] Process discussion on Zulip for establishing transparent handling of large lists of mapped items from other standards  
  * Review how the Clippy-lints list has been handled and what this informs for the next pipeline iteration

## **Meeting Minutes**

* [Patterns for Defensive Programming in Rust](https://corrode.dev/blog/defensive-programming/) post shared, but not reviewed this time  
  * \[todo\] Come back to the defensive programming chapter at a later meeting  
  * The actual post is structured more like concrete rules, some of which may be adoptable  
* [GOALS.md](http://GOALS.md)  
  * Many thumbs up  
  * The PR to be reviewed over the course of the next 48 hours and then marked as Approved  
  * “Looks Good To Me\!” mode, enhance our throughput  
  * Remember that the rule text is not itself safety critical and pushing things through is OK if it enhances item visibility  
    * There will be more review steps before publication, including review of whole chapters and the whole document in context  
  * Some immediate proposed tweaks \- make clear which steps are optional in the subheadings  
* CERT ARRay Rules  
  * Mostly just need Rationales \- likely to skip this as coming up with ways to say “dereferencing out of bounds is bad” is redundant  
  * All of the rules map neatly except for ARR38-C, which is specific to the C Standard Library  
  * Concluded that the C Standard Library is out of scope for this document  
    * \[decision\] An equivalent rule for the Rust library can absolutely be created, but it is not a mapping to ARR38-C  
  * Led into discussion of the precondition comments \- this rule is saying that preconditions should not be violated  
    * Two new rules proposed for the currently-empty Unsafety chapter \- every unsafe interface should state its preconditions; and that those preconditions shall not be violated  
* Macro rules section  
  * Solicited thoughts: there is duplication in this section and also quite a lot of default placeholder text directly in the document  
  * This should be brought up again next meeting when the original authors have a chance to consider  
  * Potentially, have CI check whether placeholder text has been edited before merging  
* Rule flavours discussion  
  * \[decision\] Three flavours more or less settled on: catch-all; subset; mitigation  
  * These form tiers of enforcement although the first tier is not decidable  
  * Should catch-all rules be encoded as rules, or as preamble text, or as something else?  
  * Start by encoding some examples of rule and non-rule text to gain feedback on which covers the respective issues better  
    * MISRA C Rule 1.3 provides precedent in both directions  
      * It’s a coherent “shall” requirement…  
      * …but it’s too broad  
    * \[decision\] Explicitly encode in the GOALS etc. that where a more specific tier of rule applies, it supersedes the more generic rule (MISRA failed to encode this policy)  
      * This would leave very few items under the sole jurisdiction of the equivalent of Rule 1.3, making it manageable  
  * [Links can form a machine-checkable language for building a guidelines selection per-project](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/218)  
    * Whether actual automation is useful here is probably QoI but having this formal link is very helpful to the reader to reason about their chosen enforcement set  
    * At least in theory a tool can say whether a set is coherent  
    * Hard-linking to other rules is never a mandatory part of the process  
      * Because it would create a circular dependency  
      * Because it isn’t actually a *problem* if rules quietly overlap, just better if we can encode it  
  * \[decision\] Linked relations are distinct from a generic “see also”, which can exist but should not interfere with checkability  
* Discussion of MISRA C ADD-6  
  * Do we want to bring this whole list in?  
  * If so, *how* do we want to bring the whole list in? As separate tickets? As review chunks?  
  * Tags will help keep the Issues list navigable

## **Material**

Any material to read before the meeting should be included here.

* Milestone: [Prepare for launch to wider Rust community](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1)  
* FLS Maintenance: [FLS Team \- North Star](https://hackmd.io/@plevasseur/HJb6qomOge/edit)  
* [Github Issue to discuss about panicking in Safety Critical](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/158)

