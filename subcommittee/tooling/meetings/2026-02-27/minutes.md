# Tooling Subcommittee Meeting on 27 February 2026 @ 4pm GMT

| Search Key | Description |
| :---- | :---- |
| \[todo\] | Action Item |
| \[decision\] | Something decided on |
| \[important\] | Key information |

## Agenda

1. Solicitation of notetaker  
2. Review [last time’s meeting minutes](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/tooling/meetings/2026-02-13/minutes.md)  
3. Present new members  
4. Discuss [PR](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/578) adding tools to website  
5. Discuss [PR](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/562) adding traffic signal readiness of Rust for safety-critical standard  
6. Check of progress / discussion:  
   1. Books topic from last week  
   2. MC/DC conversation  
7. Round table  
8. Meeting close

## Check-in area

**Please add your name, and an emoji that describes your day.**

* Xander Cesari 🔌  
* Arnaud Riess 🙂  
* Manuel Hatzl  
* Félix Fischer 👋  
* Tony Aiello  
* Stefan Akatyschew  👋😄  
* Oreste Bernardi 🦵🍩  
* Pete LeVasseur 🦀🏃

 **Notetaker:**

* Arnaud

## Housekeeping section

## Tasks

* Pete LeVasseur \- Merge Verus PR [\#548](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/548)
* Stefan Akatyschew \- Review rendering PR [\#578](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/578)

## Meeting Minutes

* Last meeting's minutes accepted.  
* Presentation of new members.  
* PR adding tools to the website:  
  * Add Verus to the list [\#548](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/548) → Pete will merge  
  * Open: mutest-rs [\#571](https://github.com/rustfoundation/safety-critical-rust-consortium/issues/571)  
  * Rendering PR*:* [\#578](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/578)  
    * Reviewers: Stefan  
* Discuss [PR \#562](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/562) adding traffic signal readiness of Rust for safety-critical standard, by Stefan  
  * Help people understand what is (functional) safety critical → in the proposal of Stefan, there are detailed explanations about ISO 26262 and the coverage of what Rust would support.  
  * Question about giving a rating from a “marketing” perspective.  
    * E.g.: Yellow may discourage users. Maybe better to mention some gaps and let people judge by themselves?   
    * Yellow/Red may be read as: Rust is not (completely) covering this topic, but could be covered by other tools/methods.  
    * We should be honest with ourselves about the state of safety critical Rust. Some people wish documents that map to safety-standards that they can share with safety people. This will help users assess the timeline of adopting safety critical Rust, setting realistic expectations.  
  * Question about data flow analysis: what is the meaning? Could be related to control flow. This may be documented as part of architecture (e.g. to prove freedom from interference is kept between criticalities). The goal is to help humans to do reasoning on data/communication flow.  At unit level, this is something that is unit-tested.  
  * Question about meaning “Simulation of dynamic behavior of the design”: it is not about unit construction, but upper in the design, with simulation tools  like SysML, Simulink, …  
  * Formal verification: is red rating correct, if safety standard doesn’t require it or says it is optional?  
  * Some of the items in the list are independent of the language.  
* Check of progress / discussion:  
  * Books topic from last meeting:  
    * PR: [https://github.com/rustfoundation/safety-critical-rust-consortium/pull/567](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/567)  
    * Everybody can add books in the PR.  
  * MC/DC conversation  
    * Conversation happening in Zulip: [https://rust-lang.zulipchat.com/\#narrow/channel/546987-project-goals.2F2026-workshop/topic/mcdc-support/with/576092827](https://rust-lang.zulipchat.com/#narrow/channel/546987-project-goals.2F2026-workshop/topic/mcdc-support/with/576092827)  
    * Observation about the proposal: pattern matching will be covered. Option\<\> and Result\<\> are the majority of types that are pattern matched in libcore \- but there are significant (30+%) additional pattern matches of relevance, so we must have (full / adequate) pattern matching to have an MVP of MC/DC.  
    * Paper on mc/dc approach: https://arxiv.org/abs/2409.08708  
* Round table  
  * Plans for the Rust week: SCRC has a room. May 21st 2026\.  
* Meeting close

