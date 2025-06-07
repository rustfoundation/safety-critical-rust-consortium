# Coding Guidelines Subcommittee Meeting on 2025-06-04 @ 11am Eastern Time

[Conversion](https://www.worldtimebuddy.com/?qm=1&lid=5,100,2643743,12,1850147,2193733&h=5&date=2025-6-4&sln=11-12&hf=1) between common time zones of attendees.

| Search Key | Description |
| :---- | :---- |
| \[todo\] | Action Item |
| \[decision\] | Something decided on |
| \[important\] | Key information |

## Agenda

0. Solicitation of notetaker  
1. Acceptance of [Previous Meeting Minutes](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/coding-guidelines/meetings/2025-05-28/minutes.md)
2. Introduction of new members  
3. Review of [revised milestone](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1) focused on broad \+ deep approach to macros chapter \- 5 mins  
4. Discuss work Alex Celeste has on-going for rewriting style guideline \- 20 mins  
5. Working session \- 20 mins  
   * Let's try to think of 1-2 guidelines ahead of time we'd like to jot down, macros are great, wider also fine  
   * Note\! We'd like to aim for unambiguous guidelines at this point to build confidence in their quality  
   * Spin off PRs to rough them in \- volunteers  
6. Review session:  
   * Review open [PRs](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pulls) & [issues](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues) \- 5 mins  
7. Round table \- 5 mins

## Check-in area

**Please add your name, and an emoji that describes your day.**

* Andrew Fernandes 🤖☕  
* Samuel Wright 😪  
* Enow Scott 🙂  
* Pete LeVasseur, 🤹  
* Douglas Deslauriers ⛵  
* Sasha Pourcelot 🚄  
* El Mahdi El Araby 🔥  
* David Svoboda 😟  
* Tiago Manczak  
* Markus Hosch  
* Arthur Hicken  
* Alex Celeste ☕  
* Lukas Wirth

**Notetaker:**

* Andrew Fernandes

## Coding Guidelines Thoughts {#coding-guidelines-thoughts}

* Do not divide by 0 (CERT INT33-C)  
  * \[todo\] by Douglas  
* Avoid lossy conversions (CERT INT31-C and FLP34-C)  
  * \[todo\] by Alex Celeste  
* Do not allow Injections (SQL, XSS, OS Command injection, etc.)  
  * \[todo\] by David  
* Do not dereference a raw pointer that is dangling or unaligned ([FLS](https://rust-lang.github.io/fls/expressions.html#fls_5cm4gkt55hjh))  
  * \[todo\] by   
* Do not allow recursion (advisory?) \- there’s a clippy lint that was suggested  
  * \[todo\] by Oreste  
* Static stack size analysis must be done  
  * Note that `emit-stack-sizes` is [nightly-only](https://github.com/rust-lang/rust/issues/54192), not slated for stabilization  
  * Recursion is currently allowed, tail-call elision is not guaranteed  
  * Might *have* to be derived from static object-code analysis  
* Prefer macros which could be expanded and included as expanded source should safety-qualification needs dictate (advisory?)  
  * \[todo\] by Sasha

## Housekeeping section

* Document space: [coding-guidelines](https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines)  
* Zulip: [safety-critical-consortium: Coding Guidelines](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/Coding.20Guidelines)  
* [Early Alpha Milestone](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1)  

## Tasks

* See **above** for the \[todo\] markers

## Meeting Minutes

* Last week’s meeting minutes were accepted  
* Intro for the (absent) new members  
* Review of the [revised milestone](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1) board, emphasis that dates are advisory only  
* Discussion on the ongoing style guideline rewrite  
  * Discussion of what goes into the guideline  
  * *Example* blanket requirement as per MISRA style  
  * Authors are asked to think about *who* the rule is going to target  
  * Appeal that more people will be *reading* the guideline rather than writing it  
  * Mandatory and Required guidelines are the priority  
  * Ask to read [PR \#27](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/127) and comment for everyone  
* Working session discussion  
  * See [Coding Guidelines Thoughts](#coding-guidelines-thoughts), above  
  * Discussion re procedural vs declarative macros: hygiene is much more complex and nuanced than may be first realized  
  * Macro hygiene is fundamentally a tooling problem  
  * Ask for volunteers to *test-run* the issue template on GitHub

## Material

Any material to read before the meeting should be included here.

### GitHub Project Board for Work Items

* [Work Item Board](https://github.com/orgs/rustfoundation/projects/1)  
