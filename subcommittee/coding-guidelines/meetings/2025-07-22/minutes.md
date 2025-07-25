# **Coding Guidelines Subcommittee Meeting on 2025-07-22 @ 20:00 EST / 2025-07-23 @ 09:00 JST**

[Link](https://www.worldtimebuddy.com/?qm=1&lid=5,100,2643743,12,1850147,2193733,1880252,8&h=5&date=2025-7-22&sln=20-21&hf=1) to meeting time in common time zones.

| Search Key | Description |
| :---- | :---- |
| \[todo\] | Action Item |
| \[decision\] | Something decided on |
| \[important\] | Key information |

## Agenda

1. Solicitation of notetaker  
2. Acceptance of [Previous Meeting Minutes](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/coding-guidelines/meetings/2025-07-22/minutes.md)  
3. Introduction of new members  
4. Check-in with Félix Fischer about CERT C Integers rules [issue](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/6) \- 15 mins  
   * Infra issues which if solved would unblock this work:  
     * [Investigate having \> 1 compliant and non-compliant example per coding guideline](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/141)  
     * [Field for citations and references](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/128)  
5. Working session \- 20 mins  
   * Read through [CERT C rules](https://wiki.sei.cmu.edu/confluence/display/c/2+Rules) together a bit  
   * Goal: Identify a rough prioritization / ordering of the CERT C rules to build out a roadmap ([issue](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/152))  
6. Review session \- 10 mins  
   * Review open [PRs](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pulls) & [issues](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues)  
7. Round table \- 5 mins

## Check-in area

**Please add your name, and an emoji that describes your day.**

* Andrew Fernandes 👽  
* Pete LeVasseur 🖖  
* Alex Celeste 🥱  
* Félix Fischer ⚡  
* Arthur Hicken 🧐  
* Fernando Jose 🏃

**Notetaker:**

* Robert is taking notes today.

For tips on how we take notes in the Safety-Critical Rust Consortium, please see the [Meeting Notetaker Role](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/docs/notetaker-role.md) doc.

## Housekeeping section

* Document space: [coding-guidelines](https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines)  
* Zulip: [safety-critical-consortium: Coding Guidelines](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/Coding.20Guidelines)  
* [Early Alpha Milestone](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1)

## Tasks

* Search for the \[todo\] markers

## Meeting Minutes

* Review of last meeting minutes.  Last meeting consisted of discussion around provenance, CERT group working session.  
* Minute notes accepted by mutual consent.  
* No new people  
* Integer rules were discussed (presented by Felix)  
  * Mapping 7 CERT Integer rules into Rust  
  * First, third, and fourth are about integer operations  
  * Avoiding integer overflow  
  * In Rust both behave the same way, it is defined behavior.  
  * Silently wraps around on   
  * Being addressed by Douglas PR add checked arithmetic guidelines \#136  
  * Requires users to do integer arithmetic by APIs using well-defined behavior.  
  * Handle the none case, it is nonable  
  * In other cases, you can deal with just the result  
  * There might not be a one size solution  
  * Put some comments on the issue or pull requests.  
  * [https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/6](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/6)  
  * [https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/136](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/136)  
  * All the integer rules are sort of in the works with additional issues and PRs that will be opened  
* If you are interesting in writing Sphinx we need someone to resolve a defect in Investigate \> 1 compliant and non-compliant example per coding guideline \#141 pull request.  If you are interested in doing this work we need some help.  
* Need help in Field for citations and references \#128.  Need some help with this in Python and Sphinx on this one as well.  Less of a blocker but still needs to be addressed  
* Review prioritization of reviewing CERT Sections  
* \[todo\] Andrew Fernandes to review floating point rules (FLP) David Svoboda  [svoboda@cert.org](mailto:svoboda@cert.org)is also interested in this work.  
* \[todo\]  [aceleste@perforce.com](mailto:aceleste@perforce.com) is going to look at Arrays (ARR)  
* Proceed with integers, floating point, and arrays as a starting point  
* Other PRs and issues are also pressing.   
* [Robert Seacord](mailto:rcseacord@gmail.com) brought up the idea of recruiting some more experts.  Perhaps letting people contribute to writing rules on the Internet.  
* [Pete LeVasseur](mailto:pete.levasseur@woven-planet.global)adjourned the meeting.

## Material

Any material to read before the meeting should be included here.

### GitHub Project Board for Work Items

* [Work Item Board](https://github.com/orgs/rustfoundation/projects/1)
