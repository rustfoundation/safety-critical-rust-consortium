# Tooling Subcommittee Meeting on 5 September 2025 @ 4pm GMT

| Search Key | Description |
| :---- | :---- |
| \[todo\] | Action Item |
| \[decision\] | Something decided on |
| \[important\] | Key information |

## Agenda

1. Present new members  
2. Discussion about the removal of [MC/DC](https://en.wikipedia.org/wiki/Modified_condition/decision_coverage) related code from the Rust compiler and next steps that we would like to take as stakeholders  
3. 

## Check-in area

**Please add your name, and an emoji that describes your day.**

* Tony Aiello  
* Manuel Hatzl  
* Arnaud Fontaine   
* Florian Gilcher  
* Oreste Bernardi  
* Xander Cesari 🌇  
* Pete LeVasseur 😪  
* Tiago Manczak

**Notetaker:**

* Tony Aiello

## Housekeeping section

* 

## Tasks

* See \[todo\] below ⏬

## Meeting Minutes

* …  
* Discussion about MC/DC  
  * **\[important\]** experimental/nightly features may be pulled by the project at any time  
    * stronger commitment to unstable  
    * very strong commitment to stable  
  * we should have an internal process that allows us to agree upon asks to the Project that might become Goals  
    * alternatively, we could use the RFC template as a way to establish goals, e.g., coverage (including MC/DC)  
    * **\[important\]** should also help with signaling to the community  
    * Project Goals generally are given attention, and the Project has a fair amount of capacity to pursue goals  
  * let’s engage with the Project to get SCRC concerns represented on their roadmap  
    * e.g., we might be able to target 2026H1 (2025H2 is closed)  
    * **\[important\]** project goals is the means to get features on the path from experimental → stable  
  * we need to build a stronger connection to the Project  
    * **\[todo: [Pete LeVasseur](mailto:plevasseur@gmail.com)\]** inform SCRC members of the importance of Project goals  
    * **\[todo: [Pete LeVasseur](mailto:plevasseur@gmail.com)\]** inform the Project of our concerns so that they can understand better what’s driving safety-critical  
      * we need to get them to care about safety; MC/DC doesn’t look interesting outside of safety-critical  
      * we’ve appealed to ethos (“it would be great to have Rust in your car\!”) but we may need to make this more real, e.g., there will be more upstreaming; there will be more contributors  
      * it would be great if the Project viewed safety at least at the level of Rust in Linux  
* What might we want? ← we could put this on github for discussion  
  * Embedded-WG discussion about desired feature list: [https://github.com/rust-embedded/wg/discussions/838](https://github.com/rust-embedded/wg/discussions/838)  
    * (Are these nested?)  
      * Stack protector  
      * Low-footprint for panic handling  
      * Atomic-volatile  
  * Coverage (up to MC/DC)  
  * Macro expansion (e.g., result of cargo-expand is compilable)  
      
* “Virtue Signalling”   
  * the SCC looked like a strong signal to the safety-critical community  
  * … a Project effort like Rust for Safety (à la Rust for Linux) could help a lot with this  
* Tooling Subcommittee needs are being discussed  
  * What about other needs broadly within the SCRC? e.g. specification of the language