# **Coding Guidelines Subcommittee Meeting on 2026-01-27 @ 20:00 EST / 2026-01-28 @ 10:00 JST**

[Link](https://www.worldtimebuddy.com/?qm=1&lid=2643743,12,8,5,1850147&h=5&date=2026-1-27&sln=20-21&hf=1) to meeting time in common time zones.

| Search Key | Description |
| :---- | :---- |
| \[todo\] | Action Item |
| \[decision\] | Something decided on |
| \[important\] | Key information |

## **Agenda**

1. Solicitation of notetaker  
2. Acceptance of [Previous Meeting Minutes](../2025-12-17/minutes.md)  
3. Introduction of new members  
4. `@guidelines-bot` and its use (Félix)  
   * Helps fairly distribute reviews in round-robin fashion to Producers  
   * Other abilities too, leave a comment as @guidelines-bot /commands to see what's possible  
5. Tags for coding guidelines (Félix)  
   * [Tags List for Safety Critical Guidelines](https://docs.google.com/spreadsheets/d/1SPhThaQhJOTvMyuyq8Buu-OVZ2D1CiosofrUmOGONqk/edit?gid=0#gid=0)  
6. [CERT C \=\> Rust Mapping](http://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/336) (Félix)  
   * Some [open questions](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/336#issuecomment-3678192763)  
7. Round table

## **Check-in area**

* Félix Fischer 🙂  
* Pete LeVasseur 🖖  
* Matthew Butler  
* Max Jacinto 🫠

**Please add your name, and an emoji that describes your day.**

**Notetaker:**

* Pete LeVasseur

For tips on how we take notes in the Safety-Critical Rust Consortium, please see the [Meeting Notetaker Role](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/docs/notetaker-role.md) doc.

## **Housekeeping section**

* Document space: [coding-guidelines](https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines)  
* Zulip: [safety-critical-consortium: Coding Guidelines](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/Coding.20Guidelines)  
* [Kanban board](https://github.com/orgs/rustfoundation/projects/1/views/3)  
  * [`contributor experience`](https://github.com/orgs/rustfoundation/projects/1/views/4) view  
  * [`coding guideline`](https://github.com/orgs/rustfoundation/projects/1/views/5) view

## **Tasks**

* xx

## **Meeting Minutes**

* `@guidelines-bot` and its use  
  * Showcase of how to create a Coding Guideline via the [issue template](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/new?template=CODING-GUIDELINE.yml)  
* Helps manage reviews (assignment, in round-robin)  
* Helps check for completeness of code examples, e.g. whether compiles when expected  
* Helps convert from Markdown to the reStructuredText (rST) format used in the guideline text  
* Bot detects and makes note of any warnings or errors  
* Bit of dialogue with the bot until all passing  
* Some bot-commands are known issues, there have been issues opened to resolve it  
  * **\[todo: PLeVasseur\]**: Command to @guidelines-bot to approve directly  
* Then can take the generated reStructuredText and copy \+ paste it into a new file in the correct location. Bot informs on how to do it.  
* Example issue, example PR  
  * **\[todo: PLeVasseur\]**: Last-minute Final Comment Period (FCP) of \~10 days before merge, perhaps?  
  * Could we have a way to have a scale of complexity, maybe improved tags to help people pick up issues to work on coding guidelines?  
* Seems challenging, since people’s experience and their familiarity may be not very easy to categorize  
* [CERT C \=\> Rust Mapping](http://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/336)  
  * Bite-sized pieces of CERT C categorized to allow for picking up and writing coding guidelines  
  * Making good progress of shrinking the “Unknown to me” table through help and support from others  
  * Some categorizations, with a call for help  
* [List of rules that DO NOT map to Rust, and why](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/336#issuecomment-3677559154)  
* [List of rules that DEFINITELY map to Rust, and how](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/336#issuecomment-3678206011)  
* [Rules that map to Unsafe Rust, and how / why](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/336#issuecomment-3678212946)  
* [WIP (Félix)](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/336#issuecomment-3678187509): I'm actively working out if / how they map to Rust  
* [Unknown to me](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/336#issuecomment-3678192763): **please help me fill those\!**  
* Tags for coding guidelines  
  * [Tags List for Safety Critical Guidelines](https://docs.google.com/spreadsheets/d/1SPhThaQhJOTvMyuyq8Buu-OVZ2D1CiosofrUmOGONqk/edit?gid=0#gid=0)  
  * Currently comma-separated value list in the Coding Guideline issue template  
  * Will fail the build if tag you use doesn’t currently exist in the `conf.py` listing of tags  
  * Idea is to crowd-source tags to allow for a cohesive set to be gathered  
  * **\[todo: PLeVasseur\]**: Can we make tags selectable, e.g. by multiple selections to make this easier on the Coding Guideline issue template?

## **Material**

Any material to read before the meeting should be included here.

* Milestone: [Prepare for launch to wider Rust community](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1)

