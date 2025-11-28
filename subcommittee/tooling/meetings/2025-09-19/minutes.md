# Tooling Subcommittee Meeting on 19 September 2025 @ 4pm GMT

| Search Key | Description |
| :---- | :---- |
| \[todo\] | Action Item |
| \[decision\] | Something decided on |
| \[important\] | Key information |

## Agenda

1. Present new members  
2. How to start a discussion with the Rust project about adding safety critical tooling to the Rust compiler  
3. Divide the subcommittee in task forces that  
   1. Handle tooling submissions  
   2. Facilitate contributions to the Rust project  
   3. Design a certification path  
   4. Other areas of interest?

## Check-in area

**Please add your name, and an emoji that describes your day.**

* Stephen Hedrick 🏄‍♂️  
* tshepang 😶  
* Arnaud Fontaine 🥱  
* Alexandru Radovici   
* Xander Cesari 🍜  
* Manuel Hatzl 🐻‍❄️  
* Oreste Bernardi 🦀🦀  
* Pete LeVasseur 🦀🧑‍💻  
* Tiago Manczak ☀️  
* Orson Pessin  

**Notetaker:**

* Pete LeVasseur

## Housekeeping section

* 

## Tasks

* See \[todo\] below ⏬

## Meeting Minutes

* Present new members  
  * Tshepang Mbambo joined us  
* How to start a discussion with the Rust project about adding safety critical tooling to the Rust compiler  
  * Open discussion from Safety-Critical Rust Consortium with members that are interested in contributing to the MC/DC feature (and others)  
  * How about we solicit contributions from Consortium members for things that the Safety-Critical community cares about?  
  * Task force forming which could help with this  
  * How do we make a bridge between Rust Project and Safety-Critical?  
    * Unconf table at RustConf2025 saw some broad appeal of attendees: “Tell me how I can get into doing what you do”  
      * Compiler / tool folks came and were asking good questions  
    * Closing keynote of RustConf2025 included shoutout for safety-critical  
      * [https://github.com/nikomatsakis/rustconf-25/blob/main/RustConf%202025.pdf](https://github.com/nikomatsakis/rustconf-25/blob/main/RustConf%202025.pdf)  
    * How can we start to build out appetite for flagship goals?  
      * Nearterm: MC/DC 2026H1 goal set  
      * Longer term: be flagship goal  
    * Concern about “hype” vs “complex” things for compiler engineers  
  * FLS Team being formed for maintaining the FLS  
  * [MCP](https://forge.rust-lang.org/compiler/proposals-and-stabilization.html#how-do-i-submit-an-mcp) is one process for making compiler changes; less heavy-weight than the RFC process  
* Divide the subcommittee in task forces that  
  * Tooling Submissions Task Force  
    * Some PRs are coming in with tool submissions; needs organization and addition to list  
    * Volunteers?  
      * Tiago Manczak  
      * Manuel Hatzl  
      * Arnaud Fontaine (github @af-airbus)  
    * Decided to collect tools with relatively low bar to solicit submission of tools  
    * Triage the list when tools are capture  
    * Objective in next two weeks: a list published to website  
      * Agreed by taskforce  
  * Safety-Critical Tooling, Rust Project Bridge Task Force  
    * Finding the right “door” to the Rust Project to collaborate  
    * Volunteers?  
      * Alexandru Radovici  
      * Xander Cesari  
      * Pete LeVasseur  
    * Offline: figure out model to collect feedback from Consortium members and bridge for contributions  
    * Suggestion: potential to use Survey results from earlier this year to motivate feature work  
    * We should come up with some sort of list of “things you care about in safety-critical” in request for feedback from Consortium members to solicit targeted feedback  
    * How to get things done:  
      * [https://rustc-dev-guide.rust-lang.org](https://rustc-dev-guide.rust-lang.org)  
    * [TrustZone](https://saschawise.com/highway-to-the-trustzone-m-2/) is now being addressed at Tweede Golfe  
    * Could we come up with wishlist and way of saying “waiting for funding”, put into some goals, then it could be someone with the engineering talent could implement  
    * Drive-by contributions vs open source contributors  
      * Long-term Rust Project member that could speak for ensuring correct architecture and long-term maintenance  
    * Rust Foundation could hold moneys contributed from members for the purposes of distributing to engineers that would implement features  
      * In this way funding can be shared among multiple compiler vendors who ship safety-qualified Rust compilers  
    * Idea: Lobbying / convincing compiler vendors for compiler features, tooling vendors for tooling features  
      * They are kind of a proxy for the customer  
      * Customer expects from features  
      * Maybe they have a higher weight vote for prioritizing features from the list  
    * High chance of being successful to land features is for Rust Project goals  
      * [https://rust-lang.github.io/rust-project-goals/index.html](https://rust-lang.github.io/rust-project-goals/index.html)  
      * [https://rust-lang.github.io/rust-project-goals/about/flagship\_goals.html](https://rust-lang.github.io/rust-project-goals/about/flagship_goals.html)  
    * Example of Rust Project Goal:  
      * [https://rust-lang.github.io/rust-project-goals/2025h2/FLS-up-to-date-capabilities.html](https://rust-lang.github.io/rust-project-goals/2025h2/FLS-up-to-date-capabilities.html)  
    * Typical at chip vendors, which are not software companies, to struggle in funding employees to work on open source software  
      * Gives some weight to the idea of certain companies being more able to contribute funds into e.g. the Rust Foundation to hold funds and distribute them to engineers  
    * Desire from members to ensure that monies contributed to Rust Foundation for certain purposes would be ear-marked and used for that purpose.  
    * Folks from companies that ship safety-qualified versions of Rust compilers may be the right path for having their employees contribute upstream  
  * Design a certification path  
    * e.g. ISO 26262, DO 178  
    * Alex Celeste, chair of Liaison Subcommittee is good with owning this process and delivering this artifact  
    * Move the activity into the Liaison Subcommittee  
* Website Subcommittee?  
  * Pete will think about this, maybe delegates from each other Subcommittee
