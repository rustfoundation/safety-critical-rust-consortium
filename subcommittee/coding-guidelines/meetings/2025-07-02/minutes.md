# Coding Guidelines Subcommittee Meeting on 2025-07-01 @ 8pm Eastern Time / 2025-07-02 @ 9am JST

[Conversion](https://www.worldtimebuddy.com/?qm=1&lid=5,100,2643743,12,1850147,2193733,1880252&h=5&date=2025-7-1&sln=20-21&hf=1) between common time zones of attendees.

| Search Key | Description |
| :---- | :---- |
| \[todo\] | Action Item |
| \[decision\] | Something decided on |
| \[important\] | Key information |

## Agenda

0. Solicitation of notetaker
1. Acceptance of [Previous Meeting Minutes](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/coding-guidelines/meetings/2025-06-25/minutes.md)
2. Introduction of new members
3. Review of [revised and rescoped milestone](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1) focused on shaking out initial issues with coding guidelines process and philosophy \- 5 mins
4. Working session \- 20 mins
   * Read through [CERT C rules](https://wiki.sei.cmu.edu/confluence/display/c/2+Rules) together a bit
   * Goal: Do some straightforward translations to ease into the writing of guidelines\!
   * Identify sections and folks that would like to translate these into the Rust coding guidelines
     * [Rule 04\. Integers (INT)](https://wiki.sei.cmu.edu/confluence/pages/viewpage.action?pageId=87152052)
     * [Rule 05\. Floating Point (FLP)](https://wiki.sei.cmu.edu/confluence/pages/viewpage.action?pageId=87152181)
     * [Rule 03\. Expressions (EXP)](https://wiki.sei.cmu.edu/confluence/pages/viewpage.action?pageId=87152200)
5. Review session \- 20 mins
   * Review open [PRs](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pulls) & [issues](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues)
6. Round table \- 5 mins

## Check-in area

**Please add your name, and an emoji that describes your day.**

* Pete LeVasseur, 🗾
* Yuchen Shen, 🇯🇵
* Robert C. Seacord 👏
* Matthew Butler 🙂
* Arthur Hicken,
* Fernando Jose 🙂
* Félix Fischer ⚡⚡

**Notetaker:**

* Yuchen Shen

## Housekeeping section

* Document space: [coding-guidelines](https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines)
* Zulip: [safety-critical-consortium: Coding Guidelines](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/Coding.20Guidelines)
* [Early Alpha Milestone](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1)

## Tasks

* Search for the \[todo\] markers

## Meeting Minutes

* [Rule 04\. Integers (INT)](https://wiki.sei.cmu.edu/confluence/pages/viewpage.action?pageId=87152052)
  * INT30-C, INT32-C, INT33-C are being handled in opened [PRs](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/136)
  * [INT35-C. Use correct integer precisions](https://wiki.sei.cmu.edu/confluence/display/c/INT35-C.+Use+correct+integer+precisions)
    * Noted as not relevant by Robert C. Seacord. Processors supported by Rust don't have to deal with padding bits.
* Prioritization of level of rules in CERT useful to customers that want “mostly” correct code to begin with, i.e. where to spend resources and in which order
* \[todo\] **Félix Fischer** stepped in to lead this effort of [Early alpha coding guidelines published for a section of CERT C](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/6)
  * Take the integer section in CERT-C and map to 4.3.3.2 Integers, generate coding guidelines in the next few weeks.
  * Follow along with the style suggested by Alex Celeste in her [PR](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/127)
  * Coordinate efforts among others to have these PRs merged
  * Mapping from coding guidelines to the referenced material
    * Please ensure that [this issue](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/128) from Alex is also tackled to allow us to reference cited material
    * Build bibliography out of this reference option, e.g. take a look at [CWE](https://cwe.mitre.org/) for some useful examples of metadata to include
    * Try to build the right metadata now and figure out how to visualize it later

## Material

Any material to read before the meeting should be included here.

### GitHub Project Board for Work Items

* [Work Item Board](https://github.com/orgs/rustfoundation/projects/1)
