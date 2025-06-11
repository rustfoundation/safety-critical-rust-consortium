# Coding Guidelines Subcommittee Meeting on 2025-06-10 @ 8pm Eastern Time / 2025-06-11 @ 9am JST

[Conversion](https://www.worldtimebuddy.com/?qm=1&lid=5,100,2643743,12,1850147,2193733&h=5&date=2025-6-10&sln=20-21&hf=1) between common time zones of attendees.

| Search Key | Description |
| :---- | :---- |
| \[todo\] | Action Item |
| \[decision\] | Something decided on |
| \[important\] | Key information |

## Agenda

0. Solicitation of notetaker  
1. Acceptance of [Previous Meeting Minutes](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/coding-guidelines/meetings/2025-06-04/minutes.md)
2. Introduction of new members  
3. Review of [revised milestone](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1) focused on shaking out initial issues with coding guidelines process and philosophy \- 5 mins  
4. Fleshing out Coding Guidelines portion of [arewesafetycriticalyet.org](http://arewesafetycriticalyet.org) (looking for a volunteer to work with the core team\!) \- 5 minutes
   1. Add deployment of coding guidelines to [coding-guidelines.arewesafetycriticalyet.org](http://coding-guidelines.arewesafetycriticalyet.org)
   2. Flesh in other contents, e.g. MISRA C Rust Addendum working with Tooling & Liaison
5. Working session \- 20 mins
   * Let's try to think of 1-2 guidelines ahead of time we'd like to jot down, macros are great, wider also fine  
   * Note\! We'd like to aim for unambiguous guidelines at this point to build confidence in their quality  
   * Spin off PRs to rough them in \- volunteers  
6. Review session - 20 mins
   * Review open [PRs](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pulls) & [issues](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues)
7. Round table \- 5 mins

## Check-in area

**Please add your name, and an emoji that describes your day.**

* Pete LeVasseur, 🌃  
* Jordan McQueen ☕🌅  
* Félix Fischer 🍂  
* Fernando ☕  
* Andrew Fernandes ☕

**Notetaker:**

* Fernando 
 
## Coding Guidelines Thoughts

* Mine the Rustonomicon for `unsafe` coding guidelines  
  * May give rise to some `undecidable` guidelines due to some properties being unable to be verified statically  
* Mine The Little Book of Rust Macros for macro coding guidelines  
* \[todo\] Jordan writing a guideline for having a SAFETY comment above `unsafe` block and tie into the corresponding clippy lint  
  * Show the bidirectional linking  
  * [Undocumented unsafe block Clippy Lint](https://rust-lang.github.io/rust-clippy/master/index.html?groups=restriction#undocumented_unsafe_blocks)  
* \[todo\] MC/DC coverage limitations as a guideline  
  * By limiting to some subset it may be feasible to enable MCDC sooner / at all

## Housekeeping section

* Document space: [coding-guidelines](https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines)  
* Zulip: [safety-critical-consortium: Coding Guidelines](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/Coding.20Guidelines)  
* [Early Alpha Milestone](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1)  

## Tasks

* Search for the \[todo\] markers

## Meeting Minutes

* Acceptance of previous meeting minutes  
  * Highlights: [pull request with guidelines](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/127), demo on how to to propose a new coding guideline via [a GitHub issue](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/new?template=CODING-GUIDELINE.yml).  
* New member introduction.  
  * [Pull request with direct-recursion clippy lint](https://github.com/rust-lang/rust-clippy/pull/15006).  
* Review of [revised milestone](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1): [todo] all, call for reviewing
  * Specificity for macros needed.  
  * Check if the workflow to contribute with guidelines is user-friendly enough.  
* [arewesafetycriticalyet.org](http://arewesafetycriticalyet.org)  
  * Deployment of coding guidelines to [coding-guidelines.arewesafetycriticalyet.org](http://coding-guidelines.arewesafetycriticalyet.org) already done\! [todo] PL, thank who took care of it 💌
  * Fill in resources.md at [docs coding\_guidelines](https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/arewesafetycriticalyet.org/docs/coding_guidelines) \[todo\] by Jordan.  
* Working session  
  * Guidelines discussion  
    * Safety comments on unsafe blocks. Is any resistance to such a guideline expected?  
      * Similar guidelines in AUTOSAR (existance of Doxygen comments) and MISRA (document assembly, advisory) exist. It's probably not a CERT-style guideline, though. 
      * Existing clippy lint (cf. [Coding Guidelines Thoughts](#coding-guidelines-thoughts)).  
    * MCDC for rustc in the works. Interesting challenges with `match`. How to handle in the guideline wording; “if using language feature X, then MCDC property Y cannot be achieved”.  
      * The wording sounds sensible. It could be a guideline.
      * Some material shared on the topic during the discussion:  
        [_Annotating Control-Flow Graphs for Formalized Test Coverage Criteria_ in arXiv](https://arxiv.org/abs/2407.04144v1) ([IEEE Xplore](https://ieeexplore.ieee.org/document/10675739))  
        [cargo-llvm-cov](https://crates.io/crates/cargo-llvm-cov)
 
Other information and references shared:

Re: last meeting’s notes regarding stack frames and tail recursion

* [https://rust-lang.github.io/rust-clippy/master/index.html\#large\_stack\_frames](https://rust-lang.github.io/rust-clippy/master/index.html#large_stack_frames) lint for large stack frames  
* Explicit Tail Calls RFC work: [https://github.com/rust-lang/rfcs/pull/3407](https://github.com/rust-lang/rfcs/pull/3407)   
  * It is intended for guaranteeing tail calls do happen (and the stack frame gets reutilized) 

Re: today’s talk about Unsafe Rust stuff:

* Rustonomicon: [https://doc.rust-lang.org/nomicon/](https://doc.rust-lang.org/nomicon/)  
* Ralf Jung’s Blog: [https://www.ralfj.de/blog/](https://www.ralfj.de/blog/)  
  * Tree Borrows, the latest memory model for Rust: [https://www.ralfj.de/blog/2023/06/02/tree-borrows.html](https://www.ralfj.de/blog/2023/06/02/tree-borrows.html)  
* Miri, an interpreter for MIR in which you can dynamically check that the invariants your code must uphold are not broken: [https://github.com/rust-lang/miri](https://github.com/rust-lang/miri)   
* Unsafe Code Guidelines: [https://rust-lang.github.io/unsafe-code-guidelines/](https://rust-lang.github.io/unsafe-code-guidelines/)  
  * Repo: [https://github.com/rust-lang/unsafe-code-guidelines](https://github.com/rust-lang/unsafe-code-guidelines)

Re: Clippy lints that might directly correlate to Coding Guidelines

* [https://rust-lang.github.io/rust-clippy/master/index.html?groups=restriction](https://rust-lang.github.io/rust-clippy/master/index.html?groups=restriction)  
  * [Arithmetic Side Effects](https://rust-lang.github.io/rust-clippy/master/index.html?groups=restriction#arithmetic_side_effects)  
  * [panic\!](https://rust-lang.github.io/rust-clippy/master/index.html?groups=restriction#panic)  
  * [Undocumented unsafe Blocks](https://rust-lang.github.io/rust-clippy/master/index.html?groups=restriction#undocumented_unsafe_blocks)  
  * [Float Arithmetic](https://rust-lang.github.io/rust-clippy/master/index.html?groups=restriction#float_arithmetic)  
  * [as Conversions](https://rust-lang.github.io/rust-clippy/master/index.html?groups=restriction#as_conversions)


## Material

Any material to read before the meeting should be included here.

### GitHub Project Board for Work Items

* [Work Item Board](https://github.com/orgs/rustfoundation/projects/1)  
