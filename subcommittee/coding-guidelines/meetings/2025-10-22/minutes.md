# **Coding Guidelines Subcommittee Meeting on 2025-10-22 @ 0800 BST / 0900 CEST / 1600 JST / 0300 EDT**

[Link](https://www.worldtimebuddy.com/?qm=1&lid=14,12,1850147,5&h=14&date=2025-10-22&sln=8-9&hf=1) to meeting time in common time zones.

| Search Key | Description |
| ----- | ----- |
| \[todo\] | Action Item |
| \[decision\] | Something decided on |
| \[important\] | Key information |

## **Agenda**

1. Solicitation of notetaker  
2. Acceptance of [Previous Meeting Minutes](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/coding-guidelines/meetings/2025-10-01/minutes.md)  
3. Introduction of new members  
4. Share launch milestone & Kanban board (Pete LeVasseur)  
   * [Prepare for launch to wider Rust community](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1)  
   * [Kanban board](https://github.com/orgs/rustfoundation/projects/1/views/3)  
     * [`contributor experience`](https://github.com/orgs/rustfoundation/projects/1/views/4) view  
     * [`coding guideline`](https://github.com/orgs/rustfoundation/projects/1/views/5) view  
5. Review progress on guidelines incorporated from CERT  
   * [High-level mapping of CERT rule groups to Rust](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/152)  
     * Integers \- Félix Fischer  
     * Arrays \- Alex Celeste  
     * Floating Point \- Andrew Fernandes  
6. Additional rule areas discussion  
   * Type inference rules  
   * Macro and identifier rules  
7. Rule flavours discussion  
8. Round table

## **Check-in area**

**Please add your name, and an emoji that describes your day.**

* Alex Celeste ☕  
* Markus Hosch 😫  
* Oreste Bernardi 🏙️  
* Tiago Manczak 😪  
* Achim Kriso 🦀

**Notetaker: Alex Celeste**

For tips on how we take notes in the Safety-Critical Rust Consortium, please see the [Meeting Notetaker Role](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/docs/notetaker-role.md) doc.

## **Housekeeping section**

* Document space: [coding-guidelines](https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines)  
* Zulip: [safety-critical-consortium: Coding Guidelines](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/Coding.20Guidelines)  
* [Kanban board](https://github.com/orgs/rustfoundation/projects/1/views/3)  
  * [`contributor experience`](https://github.com/orgs/rustfoundation/projects/1/views/4) view  
  * [`coding guideline`](https://github.com/orgs/rustfoundation/projects/1/views/5) view

## **Tasks**

* Is there a rule about type inference in Misra C++ ?  
* Poll the preference of the Guidelines team about a type annotation rule:  
  * First, yes/no  
  * Second, a choice between  
    * Always allowed  
    * Write an annotation as soon as the tool shows a complicated type  
    * …  
    * Always required  
* \[todo\] Oreste: Type annotation Issue to be created in Github listing the available points and options  
* Build up a list of RFCs that are relevant to guideline evolution going forward  
* \[todo\] Markus Hosch: create Issue w.r.t Guideline Flavours 

## **Meeting Minutes**

* Launched into discussion w.r.t type inference rule:  
  * May make declarations more difficult to understand by hiding information; or easier to understand by hiding type spam  
  * “You should use an editor with language server support”  
    * Many users do not use such an editor  
  * “It may be possible to unintentionally propagate a change and introduce a bug”  
  * Editor may still display types that are difficult to understand  
    * Or the wrong type: the editor becomes an essential tool during code review and therefore part of the safety pipeline  
  * There does not appear to be an equivalent MISRA C++ rule to use as precedent  
  * Gather options and propose a poll to the whole group:  
    * Only types when required by the compiler  
    * Put types everywhere they can be written  
    * Limited exceptions to the minimalist approach (trivial cases? What is the boundary of obviousness?)  
  * Declaration based on the traits (i.e. this iterator yield type… rather than is from …) is the more useful information to the human reader  
    * RFC-2071 ([https://github.com/rust-lang/rust/issues/63065](https://github.com/rust-lang/rust/issues/63065)) but has no champions atm  
    * May change future evolution of Guidelines  
  * Should we enforce explicit lifetime annotation?  
    * Probably not because the human is more likely to get this wrong than the compiler\!  
    * Lifetimes need to be invented (“out of thin air”) when going from unsafe to safe \- this should go in a separate area w.r.t unsafe code though  
    * Do not feel the argument about enhancing readability applies to lifetimes  
* Type aliases rule to avoid long names in explicit type declaration  
  * Existing Clippy lint for “type complexity” to recommend use of an alias when certain properties are met  
  * Need some basis for type complexity (and one which is useful and not “just” objective)  
    * E.g. limiting the levels of type element nesting within brackets  
    * Limiting the number of elements total in the type expression, both parameterizable  
    * This has MISRA precedent as well  
* Question about what additional rules can be added to make macros safe to pre-expand  
  * More important to make the macro understandable to the reader  
  * Some assist from identifier reuse vs identifier shadowing rules  
    * Use of syntactic prefixing could help here  
    * “Do not reuse identifier”?  
    * “Do not shadow identifier”?  
  * This would allow better testing and ability to check coverage of code that makes use of macros  
    * Testing of the code itself  
    * Code generators still ask the user to test generated code rather than guarantee it is safe: same applies to macros  
* Rule flavours (no issue yet)  
  * Agreement on the basic items: tiered approach, two additional properties  
  * Open questions  
    * should we fix the tiers or allow others to be defined?  
    * Is the direction for associated rules a satisfied-by or a satisfies?  
* Open PR outlining the contribution process  
  * https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/149  
  * There isn’t a ban on direct PRs if those are the right tool for the job  
  * Writing down the process is essential to work out whether the process is working, whether we need to be more proactive in forcing review to happen, etc  
  * The RFC process applies but is not used for most content changes, only structural changes  
* How to collect interesting language issues to present back to the developers?  
  * See the RFC above that would be beneficial for readability \- to link back to it in a Guidelines Issue  
  * In the Tooling group we have a process to collect these requirements \- JSON file to be rendered on AWSCY creating a goto for tooling authors to look at  
  * https://github.com/rustfoundation/safety-critical-rust-consortium/pull/492

## **Material**

Any material to read before the meeting should be included here.

* Milestone: [Prepare for launch to wider Rust community](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1)  
* FLS Maintenance: [FLS Team \- North Star](https://hackmd.io/@plevasseur/HJb6qomOge/edit)  
* [Github Issue to discuss about panicking in Safety Critical](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/158)

