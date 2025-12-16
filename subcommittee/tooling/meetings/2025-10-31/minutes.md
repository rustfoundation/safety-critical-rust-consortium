# Tooling Subcommittee Meeting on 31 October 2025 @ 4pm GMT

| Search Key | Description |
| :---- | :---- |
| \[todo\] | Action Item |
| \[decision\] | Something decided on |
| \[important\] | Key information |

## Agenda

1. Solicitation of notetaker  
2. Update on Rust Project Bridge Task Force   
3. Update from Tooling Submissions Task Force[manuel.hatzl@ferrous-systems.com](mailto:manuel.hatzl@ferrous-systems.com)

## Check-in area

**Please add your name, and an emoji that describes your day.**

* Tshepang 😀  
* Xander Cesari 🚆  
* Manuel Hatzl 🍕  
* Pete LeVasseur 👋  
* Alexandru Radovici 👶🪑  
* Dorian Peron  
* Oreste Bernardi 🏙️  

**Notetaker:**

* Xander Cesari

People interested in joining the **Rust Project Bridge Task Force**

* Manuel Hatzl

## Housekeeping section

* 

## Tasks

* See \[todo\] below ⏬

## Meeting Minutes

* Introduction of Satoshi Kaneko, currently an observer  
* Manuel Hatzl prepared flow chart diagram showing how to handle the new tool submissions  
  * Being discussed in PR 497: [https://github.com/rustfoundation/safety-critical-rust-consortium/pull/497](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/497)  
    * Assigning phase \- works through who will take over new issues and which committee/taskforce it goes to  
    * Review New Issues flow takes over after the issue is assigned  
  * Feedback:  
    * It’s nice to split up these large charts into smaller files/charts to make it easier to review/refer to.  
      * This might make it tricky to maintain cross links between different sections of the diagram but more research into Mermaid would probably enable it.  
    * How do we make this an actual workflow?  
      * Currently flowing into the subcommittee/tooling/flow folder with raw files.  
      * Having links from the issue templates to the rendered versions of these diagrams would be good.  
      * Mermaid diagrams automatically render directly in GitHub and also via docasaurus  
    * Might consider explicitly tracking which state an issue is in so we can place each one on the flow chart and better track what they need next.  
* Updates to the PR for machine readable file format for tools and desired compile features:  
  * [https://github.com/rustfoundation/safety-critical-rust-consortium/pull/463](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/463)  
  * Licenses can be complex depending on usage restrictions. Suggesting to have `license` and `license-note` field to make a machine readable license field and an arbitrary string with more information.  
    * License limitations can be complicated and arbitrary; like an open source software that might have a paid safety manual available to make it certifiable.  
    * Perhaps a `liability` field to indicate an open source but commercial software where the commercializer is taking liability?  
    * We might need a glossary or a description of why there’s more complexity in this software licensing categorization than most open source projects.  
    * If there isn’t a good reason to make this data highly machine sortable then perhaps we should just stick with arbitrary strings and description?  
    * We could put any liability notes into the `license-note` field but license is often an unexciting discussion point whereas `liability` jumps out and is more differentiated.  
  * What should go in the description? How long should it be, how much marketing speak should be allowed?  
    * An easy way to minimize marketing speak is “put what your tool does, not how well it does it”. This skews towards descriptions like “a static code analyzer” and away from “the fastest static code analyzer on the market”.  
    * We can deal with overly sales-y descriptions as the submissions come in.  
* New first-time member joining: Dorian Peron, from AdaCore, working on bringing MC/DC back into the compiler  
  * Upcoming meeting with the Rust Project to discuss alignment and MC/DC will certainly come up  
* Update from the RFC process  
  * Pete: RFC process is still in review  
  * Pete: Hope to have the process reviewed and merged next week  
  * Pete: Will then make RFC repo public  
  * Pete: will then create the “zeroth RFC”, describing the current state of the safety critical consortium  
* Rust project bridge task force update?  
  * Aforementioned meeting between members of the task force and members of the Rust Project to discuss industry support
