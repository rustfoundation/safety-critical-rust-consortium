# **Coding Guidelines Subcommittee Meeting on 2026-02-04 @ 09:00 CET / 17:00 JST**

[Link](https://www.worldtimebuddy.com/?qm=1&lid=2643743,12,8,5,1850147&h=5&date=2026-1-27&sln=20-21&hf=1) to meeting time in common time zones.

| Search Key | Description |
| :---- | :---- |
| \[todo\] | Action Item |
| \[decision\] | Something decided on |
| \[important\] | Key information |

## **Agenda**

1. Solicitation of notetaker  
2. Acceptance of [Previous Meeting Minutes](https://docs.google.com/document/d/1K_4TFNVc6i44KkLjCl_oF_pwNpkNFDXJtXHYCo5rjtk/edit?tab=t.0#heading=h.hrxjgzxf7k7k)  
3. Introduction of new members  
4. Mention review/merge workflow issue (See [example](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/302))  
5. Review of `contributor experience` issues (Sam)  
6. Review of open issues (Sam)  
7. Review of open PRs (Sam)  
8. Round table

## **Check-in area**

* Samuel Wright ☕☕☕  
* [Yuchen Shen](mailto:yuchen.shen@woven-planet.global)  
* Andreas Weis 👋Xx  
* Oreste Bernardi ⛰️  
* Christof Petig 🌞  

**Please add your name, and an emoji that describes your day.**

**Notetaker:**

* Christof Petig

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

* Minutes from last meeting were accepted without corrections  
* New member introduction: Andreas Weis of ekxide IO  
* Going through the middle column of the Kanban board  
* Question about the process to assign a reviewer for a pull request: \#331  
  \[todo\] We are missing a criterion for ready for review.  
  This PR is blocking activity, but the situation is known  
  * It should be easy for people to contribute  
  * \[info\] MISRA uses maturity level tags  
  * Pete stated that even a merge is not equal to a release, a release will involve an in-depth review process. We agree to the concept of a working document.  
    Question: Is this clear enough in the contributing guidelines?  
  * Proposal: The FCP process should start after the merge  
  * \[info\] The assignment bot should randomly assign a person, who can then reply to the bot if blocked for the review within the next two weeks  
  * \[todo\] The reviewer can’t tell the bot that the PR is approved, yet. Known problem.  
* Looking at the Guidelines view:  
  * \#235: We are looking for a valid use case (value initialized by HW but not known from within the abstract machine) which would violate the rule.  
    1. \[todo\] There is no compliant example, this would help clarify the situation. One option is DMA, another option mmap of shared memory.  
  * 240: skipped after brief inspection (pr for 235\)  
  * 246: We clarified the implications of provenance.  
    E.g. taking a pointer to the struct and offset of a field is valid, but inferring a pointer to a field from a pointer to a different field is violating provenance.  
    1. A link to a good explanation of provenance would clearly help understanding.  
       We wondered about the difference between strict and exposed provenance.  
       [https://doc.rust-lang.org/std/ptr/index.html\#strict-provenance](https://doc.rust-lang.org/std/ptr/index.html#strict-provenance)   
       \[info\] Potential (non authoritative) link: [https://www.ralfj.de/blog/2018/07/24/pointers-and-bytes.html](https://www.ralfj.de/blog/2018/07/24/pointers-and-bytes.html)   
    2. There are already architectures which cryptographically generate provenance on pointers, and you can’t create a pointer from an integer only.  
    3. Rust has not decided on whether to go for the more secure provenance or the more practical (on classic hardware) traditional model.  
    4. \[decision\] We should recommend strict provenance because of the safety benefits, turning it off with good reasons is still possible.

## **Material**

Any material to read before the meeting should be included here.

* Milestone: [Prepare for launch to wider Rust community](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1)

