# **Coding Guidelines Subcommittee Meeting on 2025-12-10 @ 1700 CEST / 1100 EDT**

[Link](https://www.worldtimebuddy.com/?qm=1&lid=5,100,2643743,12,1850147,2193733,8,6,2673730,1261481&h=5&date=2025-12-10&sln=11-12&hf=1) to meeting time in common time zones.

| Search Key | Description |
| ----- | ----- |
| \[todo\] | Action Item |
| \[decision\] | Something decided on |
| \[important\] | Key information |

## **Agenda**

1. Solicitation of notetaker  
2. Acceptance of [Previous Meeting Minutes](https://github.com/darkwisebear/safety-critical-rust-consortium/blob/f63c6e4e3faf967e7a56157d6947300aa034b04f/subcommittee/coding-guidelines/meetings/2025-11-19/minutes.md)  
3. Introduction of new members  
4. Review progress on guidelines incorporated from CERT  
   * [High-level mapping of CERT rule groups to Rust](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/152)  
     * Integers \- Félix Fischer  
     * Arrays \- Alex Celeste  
     * Floating Point \- Andrew Fernandes  
5. Merging of [Add GOALS.md, revise contribution process, freshen up to use arewesafetycriticalyet.org](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/149) has happened  
   * Any comments & updates here? Any new issues created?  
   * [Issue 237](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/237): We need to document how to add labels. Would we want to define them?  
6. Improvements to the markdown have been merged:  
   * [Issue \-\> PR conversion of hyperlinks](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/226)   
   * [Issue \-\> PR conversion of code blocks](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/227)   
   * [Issue \-\> PR conversion of tables](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/228)   
   * Example: [Bot Comment: RST Preview for Coding Guideline](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/246#issuecomment-3618884352)   
7. Call for opinions: What’s the role definition of a producer?  
8. Proposals and ideas for new rules  
9. Progress on ongoing tasks  
   * [Defensive Programming Rules](https://corrode.dev/blog/defensive-programming/)  
     * (Félix) The [fallible\_impl\_from](https://rust-lang.github.io/rust-clippy/master/index.html#fallible_impl_from) lint is in the nursery group, which means it’s not even close to production ready. So I don’t like that they recommended it.  
       The other lints are fine (at least technically)  
   * [PR 220 (merged)](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/220): alignment done between David and Felix?  
   * [Issue 97 (\[Guideline\] Avoid Complex or Recursive Macro Constructs)](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/97):   
     	No update. Should we just let it linger?  
     * (Felix) I’ve been researching this:  
       [\#wg-macros \> What would you say makes a Decl. Macro hard to maintain?](https://rust-lang.zulipchat.com/#narrow/channel/404510-wg-macros/topic/What.20would.20you.20say.20makes.20a.20Decl.2E.20Macro.20hard.20to.20maintain.3F/with/562037901)  
     * Also [I've formalized a proof that macro expansion is Turing Complete](https://lukaswirth.dev/tlborm/decl-macros/minutiae/turing-completeness.html)   
       This constrains our static analysis capabilities re: declarative macros  
   * [Issue 133 (\[Guideline\] Prevent OS command injection)](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/133):   
     	Imo mergeable, can we proceed?  
   * [Issue 259 (\[Guideline\] Do not perform ordering comparisons on pointers from different allocations)](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/259): Needs a reviewer  
   * [Issue 257 (UCG \- Rust's Unsafe Code Guidelines)](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/257): How do we organize the work?  
10. Round table

## **Check-in area**

Please add your name, and an emoji that describes your day.

* Pete LeVasseur 🖍️  
* Markus Hosch  
* Robert C. Seacord 😣  
* Christof Petig 🎄  
* Fernando Jose 🙂  
* Félix Fischer 😪☕  
* Lachlan Dowling  
* Oreste Bernardi 🫥  
* Kaneko Satoshi

Notetaker:

* Pete LeVasseur

For tips on how we take notes in the Safety-Critical Rust Consortium, please see the [Meeting Notetaker Role](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/docs/notetaker-role.md) doc.

## **Housekeeping section**

* Document space: [coding-guidelines](https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines)  
* Zulip: [safety-critical-consortium: Coding Guidelines](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/Coding.20Guidelines)  
* [Kanban board](https://github.com/orgs/rustfoundation/projects/1/views/3)  
  * [contributor experience](https://github.com/orgs/rustfoundation/projects/1/views/4) view  
  * [coding guideline](https://github.com/orgs/rustfoundation/projects/1/views/5) view  
* [Un-promoted Guideline Issues grooming list](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues?q=is%3Aissue%20state%3Aopen%20-label%3A%22sign-off%3A%20create%20pr%20from%20issue%22%20label%3A%22coding%20guideline%22)

## **Tasks**

* See **\[todo\]** tags below in Meeting Minutes

## **Meeting Minutes**

* 2\. Acceptance of [Previous Meeting Minutes](https://github.com/darkwisebear/safety-critical-rust-consortium/blob/f63c6e4e3faf967e7a56157d6947300aa034b04f/subcommittee/coding-guidelines/meetings/2025-11-19/minutes.md)  
  * Accepted, merged  
* 4\. Review progress on guidelines incorporated from CERT  
  * Integers \- Félix Fischer  
    * Progress on-going, some guidelines have been merged  
  * More inflow from folks seen on Rust Zulip, helps give additional insights and credibility  
  * Make the check-in still a regular cadence, but monthly rather than each meeting  
* 5\. Merging of [rustfoundation/safety-critical-rust-coding-guidelines\#149](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/149) has happened  
  * Any comments & updates here? Any new issues created?  
  * [Issue 237](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/237): We need to document how to add labels. Would we want to define them?  
    * Good to have in documentation on how to do it  
    * \[todo\] Pete to tackle this issue  
  * \[todo\] Markus to create issue ([https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/267](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/267)) for generating from `src/conf.py` into some part of the rendered document and/or the documentation in Markdown in the repo in an automated fashion  
  * \[todo\] Robert to document the ISO document he’s using for tags  
* 6\. Improvements to the markdown have been merged  
  * Feel free to open issues if you have thoughts on how to improve contributing  
* 7\. Call for opinions: What’s the role definition of a producer?  
  * As we get more coding guidelines contributions, it’ll be important to provide more consistent feedback  
  * Pete shared [proposal](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/.5BChange.20Proposal.5D.20Coding.20Guidelines.20Producers.20to.20Review/with/562990966)  
    * Feedback welcome on that Zulip topic  
  * Tip shared on using bot like in Clippy repo. [Example](https://github.com/rust-lang/rust-clippy/pull/16211#issuecomment-3637592322)  
    * \[todo\] Pete to open issue on how to automate in similar manner if we’d like to proceed if it fits  
* 8\. Proposals and ideas for new rules  
  * Robert posted up a few sets of ideas  
    * [https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/233](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/233)  
    * [https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/254](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/254)  
  * Suggestion to start to open coding guidelines issues for the ones that have rationale at a minimum  
  * MISRA / CERT coverage?  
    * Worthwhile to go through for ideas  
    * No need to limit, can still create issues  
  * Being transparent on what’s being worked on in issues and pull requests is worthwhile here to ensure double work isn’t done  
  * Kanban-style board would be worthwhile  
    * Exists here, open to improve how it works: [https://github.com/orgs/rustfoundation/projects/1/views/5](https://github.com/orgs/rustfoundation/projects/1/views/5)  
  * Usage of AI for guidelines discussion  
    * Initial quality seems quite low from what was seen on a couple of them  
    * Concern over reviewers wasting time  
    * Thought: Do a poll regarding what sorts of practices cause issues in safety-critical to derive some common items in Rust that could be targeted.  
    * Concern over burning credibility with Rust Project folks  
    * Two ways to get feedback on the internet:  
      * Please help: nobody helps  
      * Write something stupid: people want to jump in and help  
    * Ideally our internal group reviews it first, then having outside folks, e.g. Rust Project have review  
      * Goes back to same challenge: getting people in the group more actively reviewing PRs  
    * Posting somewhat incomplete, perhaps vague things happens and this is still worthwhile for soliciting feedback  
  * Until close to “release” it’s possible that up till now folks had not been reviewing in great detail. Once we’re close to release, we’ll probably get a lot of feedback in a burst.  
  * Suggestion for improvement: it’s possible to start PRs as draft to iterate among coding guidelines group, then upgrade from draft  
    * Issues already kind of like this?  
  * Found issues to be wrong place to iterate on coding guidelines, cannot pick a particular line to comment on  
    * Would suggest contributor to create PR right away to make review easier  
    * Issue more as a quick check for whether it makes sense  
* 9\. Progress on ongoing tasks  
  * [Defensive Programming Rules](https://corrode.dev/blog/defensive-programming/)  
    * \[todo\] Oreste to open general issue to capture this so we keep track of it  
    * Some of the suggestions in the linked article above might not be a good fit, since it might entail turning on a Clippy rule which is not mature enough yet (i.e. in nursery)  
  * [Issue 97 (\[Guideline\] Avoid Complex or Recursive Macro Constructs)](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/97)  
    * Félix added some of the links he’s aware of for context to the linked issue  
  * [Issue 133 (\[Guideline\] Prevent OS command injection)](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/133)  
    * \[todo\] David Svboda \- Let’s proceed to having a PR opened  
  * [Issue 259 (\[Guideline\] Do not perform ordering comparisons on pointers from different allocations)](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/259)  
    * Should we be doing `unsafe` keyword guidelines right now?  
    * Yes, it’s a part of the language and important to highlight these and do the work  
    * Rust’s memory model is not clearly enough specified in some cases, so we should be careful in what we right down  
    * It’s good to post when there’s an “uncharted area” to make sure it’s clear  
    * Some areas where consensus has been reached are more in the clear for guidelines  
      * \[todo\] Félix to add a tracking issue on what’s been settled when it comes to Rust’s memory model to help guide us

## **Material**

Any material to read before the meeting should be included here.

* Milestone: [Prepare for launch to wider Rust community](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1)  
* FLS Maintenance: [FLS Team \- North Star](https://hackmd.io/@plevasseur/HJb6qomOge/edit)  
* [Github Issue to discuss about panicking in Safety Critical](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/158)
