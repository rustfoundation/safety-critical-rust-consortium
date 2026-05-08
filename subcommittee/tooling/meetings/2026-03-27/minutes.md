# Tooling Subcommittee Meeting on 27 March 2026 @ 3pm GMT

| Search Key | Description |
| :---- | :---- |
| \[todo\] | Action Item |
| \[decision\] | Something decided on |
| \[important\] | Key information |

## Agenda

1. Solicitation of notetaker  
2. Review last time’s meeting minutes [https://github.com/rustfoundation/safety-critical-rust-consortium/pull/596](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/596)  
3. Present new members  
4. Tooling Task Force  
   1. Tooling PR for website [https://github.com/rustfoundation/safety-critical-rust-consortium/pull/578](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/578)  
   2. Categorization of tooling (e.g. mutest-rs) [https://github.com/rustfoundation/safety-critical-rust-consortium/issues/571](https://github.com/rustfoundation/safety-critical-rust-consortium/issues/571) postpone for when Felix Fischer can be present  
5. Rust Project Bridge Task Force  
   1. Updates from Rust Project [Safety-Critical Rust Roadmap](https://rust-lang.github.io/rust-project-goals/2026/roadmap-safety-critical-rust.html)

## Check-in area

**Please add your name, and an emoji that describes your day.**

* Alexandru Radovici 😀  
* Arnaud Riess 👨🏼‍💻  
* Pete LeVasseur 🏢  
* Manuel Hatzl  
* Tony Aiello  
* Zalán Bálint Lévai 😀  
* Stefan Akatyschew 🚄   
* Tiago Manczak  
* Kartik Ohlan 

 **Notetaker:**

* Pete LeVasseur 📓✍️

## Housekeeping section

## Tasks

* xx

## Meeting Minutes

* Approved meeting notes from last time, merged  
* New member \- none new this time  
* Tooling Task Force  
  * Tooling PR for website: [rendered preview](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/578)  
    * Migrated tooling list from YAML to JSON to make this easier to integrate with docusaurus  
    * Might need to be rebased onto main  
    * Forced line breaks for the SIL ones could be nice  
    * Categories for tools could be nice to jump to and read about easily (e.g. testing)  
    * \[todo\] @Everyone \- let’s all go leave comments on the PR  
    * \[todo\] If not all are left Alexandru will go do this  
    * Licensing of compilers \- claiming of these as being e.g. non OSS-friendly licenses could go the wrong way  
      * Example workflow \- pull from upstream, apply patches; don’t change the license; cannot change the license; when compiler is delivered as compiled binary it’s also delivered with source  
      * “Additional files” \- depends on category; if useful upstream will be upstreamed. “Raise everything to Tier 1, using Rust Project terminology” and those licenses are kept permissive for OSS and Commercial both  
  * Categorization of tooling (e.g. mutest-rs)  
    * [Discussion](https://github.com/rustfoundation/safety-critical-rust-consortium/issues/571) on-going on how to best split up tooling categories on GitHub  
    * Bringing it here to discuss  
      * Testing  
      * Profiling  
      * Compiler  
      * ... and so on  
    * Formal verification itself may be wide enough and worthwhile to make that its own category  
    * \[todo\] Manuel and Felix to discuss offline, draft up PR  
    * Mutest could be mentioned to in the ISO 26262 gap analysis at 6-10 as 1c \- fault injection, PR will be sent for feedback  
* Rust Project Task Force  
  * We have some defined Rust Goals for MC/DC \- [https://rust-lang.github.io/rust-project-goals/2026/roadmap-safety-critical-rust.html](https://rust-lang.github.io/rust-project-goals/2026/roadmap-safety-critical-rust.html)  
  * Niko added the ability to track future road maps for Rust  
    * We could add to those  
    * \[todo\] [plevasseur@gmail.com](mailto:plevasseur@gmail.com)and [Alexandru Radovici](mailto:alexandru.radovici@oxidos.io) go through the survey results to find new goals  
  * \[todo\] [plevasseur@gmail.com](mailto:plevasseur@gmail.com)link analysis page to the tooling page  
  * \[todo\] We would need people to write safety critical clippy lints as a part of one of the goals  
* Meeting  
  * In the face to face meeting, we would like to have more spntaneuty  
    * morning will be structured  
    * Afternoon \- unconference style
