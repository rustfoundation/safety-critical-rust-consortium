# **Coding Guidelines Subcommittee Meeting on 2025-10-29 @ 1100 EDT / 1600 CET**

[Link](https://www.worldtimebuddy.com/?qm=1&lid=5,100,2643743,12,1850147,2193733,8,6,2673730,1261481&h=5&date=2025-10-29&sln=11-12&hf=1) to meeting time in common time zones.

| Search Key | Description |
| :---- | :---- |
| \[todo\] | Action Item |
| \[decision\] | Something decided on |
| \[important\] | Key information |

## **Agenda**

1. Solicitation of notetaker  
2. Acceptance of [Previous Meeting Minutes](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/coding-guidelines/meetings/2025-10-22/minutes.md)  
3. Introduction of new member  
4. Share launch milestone & Kanban board (Pete LeVasseur)  
   * [Prepare for launch to wider Rust community](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1)  
   * [Kanban board](https://github.com/orgs/rustfoundation/projects/1/views/3)  
     * [`contributor experience`](https://github.com/orgs/rustfoundation/projects/1/views/4) view  
     * [`coding guideline`](https://github.com/orgs/rustfoundation/projects/1/views/5) view  
5. [FLS Team](https://rust-lang.org/governance/teams/lang/#team-fls) started (Pete)  
   * If interested in becoming involved, feel free to visit [Zulip channel](https://rust-lang.zulipchat.com/#narrow/channel/520710-t-lang.2Ffls) or come to our first meeting (find the `.ics` [here](https://rust-lang.github.io/calendar/fls.ics))  
6. Eclipse S-CORE usage of Rust (Pete/Markus)  
   * Find their relevant meeting notes [here](https://github.com/orgs/eclipse-score/discussions/1933)  
7. Review progress on guidelines incorporated from CERT  
   * [High-level mapping of CERT rule groups to Rust](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/152)  
     * Integers \- Félix Fischer  
     * Arrays \- Alex Celeste  
     * Floating Point \- Andrew Fernandes  
8. Rule flavors discussion  
9. Round table

## **Check-in area**

**Please add your name, and an emoji that describes your day.**

* Max Jacinto 🦀  
* Alex Celeste ☕  
* Pete LeVasseur 🧑‍💻🖇️  
* Alex Senier 🤪  
* Oreste Bernardi 🏙️  
* William Cunningham   
* Julius Gustavsson 🙃  
* Christof Petig 🐛  
* Gideon Mueller  
* Douglas Deslauriers 🎃  
* Tiago Manczak  
* Dillon McEwan ☕

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

* Xx

## **Meeting Minutes**

* Introduction of new membres: non-safety-critical ECU shipping Rust in production at \[vendor\]  
* Due date removed from launch milestone but items remain priorities for preparing an announcement  
  * (some of this is automation/infra)  
  * Similar content is viewable in the Kanban board  
    * Chapter review tasks to appear here  
* FLS Team\! “If you’re interested, take a look”  
  * First meeting upcoming  
  * This is a good way to give back if your use case for the compiler is in a safety-critical project  
  * Will not be forced to contribute  
* Eclipse S-CORE: automotive companies in EU collaborating on a better/future software stack as an open-source commodity  
  * [https://eclipse.dev/score/](https://eclipse.dev/score/) and [https://github.com/eclipse-score](https://github.com/eclipse-score)  
  * There is a regular Rust meeting, Pete is attending  
    * There will be a larger meeting about Rust’s role in this upcoming  
  * Targeting a 1.0 release at the end of 2026; targeting ASIL-B development; want to be able to use Rust for this  
  * Eclipse SDV is open to the public to attend ([https://sdv.eclipse.org/](https://sdv.eclipse.org/))  
* CERT-C progress  
  * Stalled on Arrays  
  * Others not present today  
* Rules flavours  
  * Summary of topics from last week and from the breakout session in the All-hands  
  * Main driver of the discussion are Markus’s ideas  
  * \[decision\] Postpone till Markus able to join  
* Marketing collateral  
  * Company would like some content to talk about, or announced version of the coding guidelines  
  * Coding guidelines in current state doesn’t seem to be of appropriate level of maturity to market far and wide at industry event  
* Action item to create an issue for a new rule w.r.t type annotation on variable bindings  
  * A review of the C++ precedent revealed two positions: “almost always \`auto\`” vs not to do this especially in interfaces
    * Loose proposal in previous meeting to require a type annotation when the language server cannot display a “nice” type
    * Does the precedent from C++ indicate that this is not important after all? Perhaps there isn’t always intent to restrict this  
  * For C++ this is much more ambiguous than in Rust, especially because references can be implicit  
  * What do AUTOSAR and MISRA C++ say about this?  
    * Nothing in MISRA C++ (the group has no opinion)  
    * AUTOSAR has some related rules \- target the idea that \`auto\` should not be used when the resulting type is not clear, but for things like getting an iterator, typing it out is not helpful; requires strong types for interfaces  
      * Writing generic C++ code is difficult to do while staying within these guidelines as they can result in the tool complaining more  
  * It might make sense to have a guideline w.r.t clarity, but this is probably not decidable  
  * Probably not necessary to restrict type inference at the moment \- there seems to be little appetite for an undecidable rule  
    * If the compiler itself cannot infer the type at all that’s a different issue anyway  
    * Previously did not consider delayed inference, although the compiler still rejects ambiguities  
  * Concerned about an API that may do something different from what is expected because of the type selecting a behaviour through an unexpected trait  
  * Rule proposed previously was based on interaction with editing environments and what is shown to the user \- the rule may help clarity in places where the editor would display something unreadable  
    * This tool feature implies a need for the information  
    * Implicit safety requirement on the analyzer as well, to show the reviewer the right type and thus enable them to correctly understand the code  
    * The feature is often useful while editing rather than while reading \- once done making changes, it will be checked by the compiler  
  * \[todo\] The action here is to open a generic Issue, not a new-guideline Issue, to keep track of the group’s thoughts and any evolving discussion  
    * \[todo\] Request to provide an example or two to attach to the issue to illustrate  
* Next AUTOSAR release event (25-11) will have a section about Rust in the video presentation, in the Classic platform  
  * Includes some stats about errors prevented by use of Rust in Classic  
* Discussion of safety-critical in closing keynote at RustConf 2025; short but the vision doc team will write an RFC about the lessons and insights, domains identified; Pete did 20-25 interviews so safety-critical will feature prominently  
  * (link here)  
* Florian gave some examples in a presentation w.r.t guidelines for unsafe using the example of a mutex; all of the code impacting the safe justification for the unsafe block needs to be in the same module so that the impact of it can be understood  
  * Should this be a new guideline?  
    * Would this be a decidable guideline or require manual review?  
    * An unsafe block should require a justification and this justification should summarize all APIs relevant to it; by listing them it provides a list of additional points to review and this can generate proactive warnings to the reviewer; so there are useful automations associated with this, but not fully bidirectional  
    * Some users isolate all uses of \`unsafe\` into a dedicated crate for separate review  
    * Ensuring that all APIs (types and functions) which affect one specific unsafe behaviour are together makes them easier to review, not necessarily the same line of distinction  
    * The module boundary is where invariants are easiest to uphold, can be a broader boundary if split across more than one module  
  * Related to some of the discussion in Eclipse S-CORE w.r.t design guidelines around unsafety  
  * \[todo\] Another topic for a new discussion Issue  
    * We have a number of issues discussing unsafety already but maybe not capturing this angle  
    * Should cover the module-level discussion  
* The dice will have the logo printed on the 1 unless we pay extra for the 20\!

## **Material**

Any material to read before the meeting should be included here.

* Milestone: [Prepare for launch to wider Rust community](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1)  
* FLS Maintenance: [FLS Team \- North Star](https://hackmd.io/@plevasseur/HJb6qomOge/edit)  
* [Github Issue to discuss about panicking in Safety Critical](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/158)
