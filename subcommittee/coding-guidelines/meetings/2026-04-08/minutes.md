# **Coding Guidelines Subcommittee Meeting on 2026-04-08 @ 1600 CEST / 1100 EDT**

[Link](https://www.worldtimebuddy.com/?qm=1&lid=5,12,2643743,8,1850147,100,14&h=5&date=2026-4-8&sln=11-12&hf=1) to meeting time in common time zones.

| Search Key | Description |
| :---- | :---- |
| \[todo\] | Action Item |
| \[decision\] | Something decided on |
| \[important\] | Key information |

## **Agenda**

1. Solicitation of notetaker  
2. Acceptance of [Previous Meeting Minutes](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/coding-guidelines/meetings/2026-04-01/minutes.md)  
3. Introduction of new members  
4. Review batches for [CERT C \=\> Rust Mapping](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/336) (Pete)  
   - Thank you to everyone for your support in providing feedback  
   - Félix will go over this and come back in a week or two with thoughts  
5. Coverage of MISRA C and CERT C in 2026 (Félix / Markus)  
   - MISRA C one has a [PR up](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/432) from Markus  
   - Félix met with Markus and will walk us through the "harmonized" version that should work for MISRA, CERT both  
6. Overview of [Safety-Critical Rust](https://rust-lang.github.io/rust-project-goals/2026/roadmap-safety-critical-rust.html) \- Rust Project Goals Roadmap (Pete)  
   - Soliciting those interested in [Establish a Spot for Safety-Critical Lints in Clippy](https://rust-lang.github.io/rust-project-goals/2026/safety-critical-lints-in-clippy.html) goal  
   - Explanation of the work, as Pete understands from initial discussions with t-clippy  
7. Proposals and ideas for new rules (all)  
8. Progress on ongoing tasks (all)  
9. Round table

## **Check-in area**

**Please add your name, and an emoji that describes your day.**

* Pete LeVasseur 🦀✍️
* David Svoboda (-:
* Arshad Mahmood 🌞
* Max Jacinto ⚽
* Samuel Wright 🌞
* Andreas Weis 🫈
* Félix Fischer ☕
* Oreste Bernardi 🏥
* Markus Hosch 👾  
* William Barsse 🦀
* Jason Newcomb ☕
* Achim Kriso 🙂

**Notetaker:**

* Andreas Weis

For tips on how we take notes in the Safety-Critical Rust Consortium, please see the [Meeting Notetaker Role](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/docs/notetaker-role.md) doc.

## **Housekeeping section**

* Document space: [coding-guidelines](https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines)  
* Zulip: [safety-critical-consortium: Coding Guidelines](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/Coding.20Guidelines)  
* [Kanban board](https://github.com/orgs/rustfoundation/projects/1/views/3)  
  * [`contributor experience`](https://github.com/orgs/rustfoundation/projects/1/views/4) view  
  * [`coding guideline`](https://github.com/orgs/rustfoundation/projects/1/views/5) view

## **Tasks**

* \[todo\] Pete LeVasseur: Clean up meeting minutes for 2026-04-01 Meeting

## **Meeting Minutes**

* Introduction of new members  
* CERT-C mapping  
  * Rules were reviewed in smaller groups, feedback was given and is currently being worked through. Current plan is to complete this by next week.  
* Spreadsheet showing Mapping of MISRA C and CERT C  
  * [PR is prepared](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/432) for a *Standards Matrices* section in the Appendix of the guidelines document  
  * Goal is to give people a shortcut how familiar rules from other guidelines are mapped into the Rust world  
  * MISRA headlines can not be included in the table for IP reasons, so it only contains the rule numbers in the table  
  * Some rules don’t work the same for Rust, e.g. Rust Octals use different (and less confusing) literals than C, so the rationale for the C rule no longer applies  
  * Table 3 contains rules that are not applicable to Rust along with a comment explaining why it is safe to omit them for Rust. This table needs more work, many entries don’t have comments and existing comments are probably not detailed enough.  
  * Table 1 also misses entries for Rust guidelines that the rule maps to. Links need to be added there.  
  * We should focus on Mandatory and Required rules first, Advisory rules may be treated as lower priority  
  * It was discussed whether the table should be maintained in a Google Sheet for easier editing. It was agreed that the only source of truth should be the .rst file in the repo, maintaining a Google Sheet on the side is not sensible. The rate of change is expected to go down significantly once the initial version of the table is finished.  
  * Rust has the additional distinction between safe and unsafe parts, so rule applicability needs to be evaluated for those separately.  
* Rust Safety Critical Project goals and roadmap \- Writing clippy lints  
  * Some existing lints could use better explanation and rationale texts, we could contribute there  
  * Additional lints for new guidelines. We could implement them and gather feedback from clippy maintainers how to write proper lints  
  * Process for adding new lints to clippy may be slow. Having a separate process to try out and experiment with new rules quickly might make sense for us. The idea is to have a “walled off section” for experimentation.  
  * Some lints require global reasoning, which is not a good fit for clippy. Including this is in the default ruleset for clippy is probably undesirable. Clippy only works one-crate-at-a-time. Analysing across crate boundaries is not feasible.  
  * Lints with high false positive rates? High false positive rate is probably fine. It may restrict which category a lint ends up in, but it is not a problem in principle.  
    1. [https://doc.rust-lang.org/stable/clippy/lints.html\#pedantic](https://doc.rust-lang.org/stable/clippy/lints.html#pedantic)  
  * lints requiring annotations for being decidable?  
    1. Some existing lints rely on annotations on types. Annotation is not part of the type, but used by the linter to influence diagnostics.  
    2. Clippy would prefer if annotations are not necessary for a check to work, but it can be discussed.  
    3. All clippy::\* attributes are for use by clippy.  
    4. It may be useful for safety critical to be able to compile a list of all attributes that are used to deviate from clippy warnings. This can be an important artifact to hand to an assessor for safety certification.  
  * Easy way to configure a set of lints in bulk? Currently requires providing [a pre-written config file](https://doc.rust-lang.org/stable/clippy/configuration.html). There is an [RFC for lint profiles](https://github.com/rust-lang/rfcs/pull/3926) which may be helpful in this context, but it still requires someone to provide the profile.  
  * Question: Can one lint fall under multiple lint groups?  
    1. May help with the SCRC request for lints to be able to be turned on depending on different levels of safety-critical software and different standards  
* Meeting adjourned

## **Material**

Any material to read before the meeting should be included here.
