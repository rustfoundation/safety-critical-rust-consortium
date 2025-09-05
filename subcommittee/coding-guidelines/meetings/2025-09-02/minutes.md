# **Coding Guidelines Subcommittee Meeting on 2025-09-02 @ 2000 EDT / 2025-09-03 0900 JST**

[Link](https://www.worldtimebuddy.com/?qm=1&lid=5,100,2643743,12,1850147,2193733,1880252,8,6&h=5&date=2025-9-2&sln=20-21&hf=1) to meeting time in common time zones.

| Search Key | Description |
| :---- | :---- |
| \[todo\] | Action Item |
| \[decision\] | Something decided on |
| \[important\] | Key information |

## **Agenda**

1. Solicitation of notetaker  
2. Acceptance of [Previous Meeting Minutes](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/coding-guidelines/meetings/2025-08-27/minutes.md)  
3. Introduction of new members  
4. Share launch milestone & Kanban board (Andrew)  
   * [Prepare for launch to wider Rust community](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1)  
   * [Kanban board](https://github.com/orgs/rustfoundation/projects/1/views/3)  
     * [`contributor experience`](https://github.com/orgs/rustfoundation/projects/1/views/4) view  
     * [`coding guideline`](https://github.com/orgs/rustfoundation/projects/1/views/5) view  
5. Review progress on guidelines incorporated from CERT (Andrew)  
   * [High-level mapping of CERT rule groups to Rust](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/152)  
     * Integers \- Félix  
     * Arrays \- Alex  
     * Floating Point \- Andrew  
6. Discussion session  
   * "Under what circumstances is `panic`\-ing safety-critical software okay?" (Félix)  
     * Relevant [issue](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/158)  
   * “Should we create a list of rules we intend to create? I can imagine that such a list could facilitate contributions of people who don't have the big picture but are willing to take a single rule and just write it. If so, what is a good format and where should it live to maximize contributor experience”  
     * Relevant [issue](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/197)  
   * “(Where) do we have a place to cover higher level concepts? I'm thinking of patterns like Newtype and Typestate which can reduce errors significantly.”  
     * Relevant [issue](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/198)  
7. Round table

## **Check-in area**

**Please add your name, and an emoji that describes your day.**

* Félix Fischer 🥱  
* Yuchen Shen  
* Andrew Fernandes  
* Matthew Butler

**Notetaker:**

* Andrew Fernandes

For tips on how we take notes in the Safety-Critical Rust Consortium, please see the [Meeting Notetaker Role](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/docs/notetaker-role.md) doc.

## **Housekeeping section**

* Document space: [coding-guidelines](https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines)  
* Zulip: [safety-critical-consortium: Coding Guidelines](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/Coding.20Guidelines)  
* [Kanban board](https://github.com/orgs/rustfoundation/projects/1/views/3)  
  * [`contributor experience`](https://github.com/orgs/rustfoundation/projects/1/views/4) view  
  * [`coding guideline`](https://github.com/orgs/rustfoundation/projects/1/views/5) view

## **Tasks**

* Search for the \[todo\] markers

## **Meeting Minutes**

* Bit of a kerfuffle migrating to a new meeting **without** an AI notetaker  
* Previous minutes were accepted  
* No new members  
* Review of the Kanban board  
  * Prepare to launch page review  
  * Review of the integer CERT C rules as per rust  
  * Review of all the [integer CERT C rules](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/152#issuecomment-3161474482) (status table)  
  * No update on arrays or floats  
  * ~~\[todo\]~~ **ask** have an item in each rule saying “you can check for this rule with these clippy lints” [(new issue added](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/201))  
    * This is very similar to “[Should we create a list of rules we want to create](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/197)?”  
* Discussion Section  
  * “Should we create a list of rules we intend to create?”  
    * Discussed above  
  * “(Where) do we have a place to cover higher level concepts?”  
    * Sort-of-rough consensus is that “design patterns” are not necessarily a good fit for low-level safety-critical guidelines because context (like FFI) are often the most important condition.   
    * For example, `unsafe` is necessary a lot in embedded work.  
  * "Under what circumstances is panic-ing safety-critical software okay?"  
    * \[todo\] Andrew to write up thoughts re: explicit behaviour that is driven by requirements, and differs between `std` and `no_std`.

## **Material**

Any material to read before the meeting should be included here.

* Milestone: [Prepare for launch to wider Rust community](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1)  
* [Github Issue to discuss about panicking in Safety Critical](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/158)

