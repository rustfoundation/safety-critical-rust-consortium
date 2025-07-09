# **Coding Guidelines Subcommittee Meeting on 2025-07-09 @ 0800 BST / 0900 CEST / 2025-07-09 @ 1600 JST**

[Conversion](https://www.worldtimebuddy.com/?qm=1&lid=14,12,1850147&h=14&date=2025-7-9&sln=8-9&hf=1) between common time zones of attendees.

| Search Key | Description |
| ----- | ----- |
| \[todo\] | Action Item |
| \[decision\] | Something decided on |
| \[important\] | Key information |

## **Agenda**

1. Solicitation of notetaker  
2. Acceptance of [Previous Meeting Minutes](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/coding-guidelines/meetings/2025-07-02/minutes.md)  
3. Introduction of new members  
4. Review of [revised and rescoped milestone](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1) focused on shaking out initial issues with coding guidelines process and philosophy \- 5 mins  
5. Working session \- 20 mins  
   * Read through [CERT C rules](https://wiki.sei.cmu.edu/confluence/display/c/2+Rules) together a bit  
   * Goal: Do some straightforward translations to ease into the writing of guidelines\!  
   * Identify sections and folks that would like to translate these into the Rust coding guidelines  
     * [Rule 04\. Integers (INT)](https://wiki.sei.cmu.edu/confluence/pages/viewpage.action?pageId=87152052)  
     * [Rule 05\. Floating Point (FLP)](https://wiki.sei.cmu.edu/confluence/pages/viewpage.action?pageId=87152181)  
     * [Rule 03\. Expressions (EXP)](https://wiki.sei.cmu.edu/confluence/pages/viewpage.action?pageId=87152200)  
6. Review session \- 20 mins  
   * Review open [PRs](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pulls) & [issues](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues)  
7. Round table \- 5 mins

## **Check-in area**

**Please add your name, and an emoji that describes your day.**

* Alex Celeste ☕  
* Oreste Bernardi 🥐☕  
* Fernando Jose 🙂  
* Achim Kriso 🙂  
* Christof Petig 🙃  
* Jonas Wolf 😵‍💫

**Notetaker:**

* Alex

## **Housekeeping section**

* Document space: [coding-guidelines](https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines)  
* Zulip: [safety-critical-consortium: Coding Guidelines](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/Coding.20Guidelines)  
* [Early Alpha Milestone](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1)

## **Tasks**

* Search for the \[todo\] markers

## **Meeting Minutes**

* Unclear what the process of approving a PR is and getting it merged  
  * Can everyone approve, or just Pete and Joel?  
  * Good feedback on process for assigning the rule to be developed, but there needs to be an assignment to a reviewer too  
  * Single rules are quite granular and can be approved by one or two reviewers as part of the async workflow, for group review later  
* SAE JA 1020 update: there was a ballot before which produced a large amount of feedback  
  * Feedback has been integrated and are mostly not significant, but because there were more than 5 corrections a new ballot is needed  
  * Ballot will end after Aug 4  
  * After approval by the functional safety committee, RTCA will need to look over the document as well \- not sure of the process (not sure which form of ballot it is)  
  * Should pass through now \- most feedback was close-reading of sentences related to other Standards and addition of more examples (list of changes was recorded as part of the new ballot)  
  * Comment on specification of the compiler \- there is a working specification in the form of the adopted FLS, and the new wording reflects that (contrast the ISO IS that exist for C and C++) \- the new wording clarifies that the specification as it currently exists is enough to qualify a compiler  
* What is the roadmap or delivery date for a first release of the SCRC Guidelines?  
  * There is a roadmap  
  * Still currently filling things out based on CERT at the moment \- taking a more agile approach will allow for a faster delivery cadence compared to the very slow pace of development of SAE and similar groups  
* \[TODO\] Oreste to review the CERT C INT rules and convert Felix’s comments to concrete rule text proposals  
* Question about the scope of the rules: are “rules” that require understanding and enforcement without specifying any particular remediation in scope?  
  * This is partially, but not completely, in line with the “CERT philosophy” for some rules; in general this reflects more high-level and language-agnostic approaches  
* Article from the day before the meeting suggested for the group to read, by Synopsys: [https://semiengineering.com/driving-the-future-how-rust-and-virtual-ecus-are-transforming-autosar-classic-automotive-software/](https://semiengineering.com/driving-the-future-how-rust-and-virtual-ecus-are-transforming-autosar-classic-automotive-software/)  
  * Blessing of Rust by a big semiconductor (and recognizing the importance of AutoSAR Classic)  
  * Informal internal estimates that 60% of bugs and 80% of internal security issues would have been prevented by using Rust  
* Press release about Rust from S-CORE: [https://www.vda.de/en/press/press-releases/2025/250624\_PM\_Automotive\_industry\_signs\_Memorandum\_of\_Understanding](https://www.vda.de/en/press/press-releases/2025/250624_PM_Automotive_industry_signs_Memorandum_of_Understanding)  
  * Rust officially preferred over C++

## **Material**

Any material to read before the meeting should be included here.

### **GitHub Project Board for Work Items**

* [Work Item Board](https://github.com/orgs/rustfoundation/projects/1)

