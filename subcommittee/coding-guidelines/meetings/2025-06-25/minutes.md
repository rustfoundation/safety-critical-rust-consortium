# **Coding Guidelines Subcommittee Meeting on 2025-06-25 @ 15:00 UTC / 16:00 BST / 11:00 EDT**

[Conversion](https://www.worldtimebuddy.com/?qm=1&lid=5,14,8,12&h=5&date=2025-6-25&sln=11-12&hf=1) between common time zones of attendees.

| Search Key | Description |
| ----- | ----- |
| \[todo\] | Action Item |
| \[decision\] | Something decided on |
| \[important\] | Key information |

## **Agenda**

1. Solicitation of notetaker  
2. Acceptance of [Previous Meeting Minutes](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/coding-guidelines/meetings/2025-06-18/minutes.md)  
3. Introduction of new members  
4. Review \- clippy lints suitable for creating safety-critical guidelines \~10m  
   * [https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/86](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/86)  
   * [https://docs.google.com/spreadsheets/d/1rRhB9ch0r5hpg5Mb65Prn5Nto05CZ4EjSOdBEZWwVIo/edit?gid=0\#gid=0](https://docs.google.com/spreadsheets/d/1rRhB9ch0r5hpg5Mb65Prn5Nto05CZ4EjSOdBEZWwVIo/edit?gid=0#gid=0)  
   * Anyone else interested in contributing? Feel free to put your name in the notes\!  
5. Review \- Defects vs Subsets \~10m  
   * [https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/127](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/127)  
6. Roundtable items  
7. Review session \- 20 mins  
   * Review open [PRs](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pulls) & [issues](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues)

## **Check-in area**

**Please add your name, and an emoji that describes your day.**

* Alex Celeste 🙂  
* David Svoboda 🙂  
* Pete LeVasseur, 💤  
* Andrew Fernandes ☺️ ☕  
* Robert C. Seacord 🙈  
* Oreste Bernardi😶‍🌫️  
* Douglas Deslauriers 🐦  
* El Mahdi El Araby 🦭   
* Sam Wright 💤  
* Stephen Hedrick 🤠  
* Markus Hosch 🪄  
* Félix Fischer 😪  
* Christof Petig 😐

### **Notetaker**

* Andrew Fernandes 

## **Housekeeping section**

* Document space: [coding-guidelines](https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines)  
* Zulip: [safety-critical-consortium: Coding Guidelines](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/Coding.20Guidelines)  
* [Early Alpha Milestone](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1)

## **Tasks**

* 

## **Meeting Minutes**

* No new members  
* Review of [Clippy Lints to/from Coding Guidelines](https://docs.google.com/spreadsheets/d/1rRhB9ch0r5hpg5Mb65Prn5Nto05CZ4EjSOdBEZWwVIo/edit?gid=0#gid=0)  
  * Concern: “Everyone has their own definition of ‘Safety Critical’”  
  * Additional Discussion: [Identify Clippy lints suitable for creating safety-critical guidelines \#86](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/86)  
* Review of [Defects vs Subsets](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/86)  
  * Discussion of “category: required” and “decidability: undecidable”  
  * Is it because it is impossible, or because specific tools cannot do it?  
  * Possible reframing from “undecidable” to “decidable with manually verified restrictions”  
* Roundtable Items  
  * How to think about “unintended integer division by zero”? Is it unsafe? How is it verified or not or annotated?  
  * In `C` it is undefined behavior, but Rust does not have that (we hope)

## **Material**

Any material to read before the meeting should be included here.

### **GitHub Project Board for Work Items**

* [Work Item Board](https://github.com/orgs/rustfoundation/projects/1)

