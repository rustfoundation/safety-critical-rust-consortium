# **Coding Guidelines Subcommittee Meeting on 2026-05-13 @ 1600 CEST / 1100 EDT**

[Link](https://www.worldtimebuddy.com/?qm=1&lid=5,12,2643743,8,1850147,100,14,14,1835848&h=5&date=2026-5-13&sln=11-12&hf=1) to meeting time in common time zones.

| Search Key | Description |
| :---- | :---- |
| todo | Action Item |
| decision | Something decided on |
| important | Key information |

## **Agenda**

1. Solicitation of notetaker  
2. Acceptance of [Previous Meeting Minutes](https://github.com/Safety-Critical-Rust-Consortium/safety-critical-rust-consortium/blob/main/subcommittee/coding-guidelines/meetings/2026-05-06/minutes.md)  
3. Introduction of new members  
4. Coverage of MISRA C and CERT C in 2026 (Félix / Markus updates)  
- MISRA C one has a [PR up](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/432) from Markus  
- Chatted with Félix yesterday and he'll work on getting a v0.1 PR up for CERT C  
5. Interest in the MISRA C++ mapping  
- Please register interest on [this Zulip thread](https://rust-lang.zulipchat.com/#narrow/channel/579369-safety-critical-consortium.2Fcoding-guidelines/topic/MISRA.20C.2B.2B.20Mapping.20Interest/with/584764785)  
- Pete/Alex are working out how we can have some kind of copy of the MISRA documents (C, C++) held in the jurisdiction of the Rust Foundation in support of members to be able to work on coding guidelines  
6. Overview of [Safety-Critical Rust](https://rust-lang.github.io/rust-project-goals/2026/roadmap-safety-critical-rust.html)  Rust Project Goals Roadmap (Pete)  
- Soliciting those interested in [Establish a Spot for Safety-Critical Lints in Clippy](https://rust-lang.github.io/rust-project-goals/2026/safety-critical-lints-in-clippy.html) goal  
  - Register interest [here](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/Getting.20involved.20with.20Clippy.20for.20SCRC.20lints/with/583090116) on Rust Zulip  
- Soliciting those interested in [Normative Documentation for Sound unsafe Rust](https://rust-lang.github.io/rust-project-goals/2026/safe-unsafe-for-safety-critical.html) goal  
  - Register interest [here](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/SCRC.20.3C.3D.3E.20t-opsem.3A.20Normative.20Documentation.20for.20Sound.20.60unsafe.60/with/586198564) on Rust Zulip  
7. SCRC Room at Utrecht, NL  
   - Think about which topics you might want to bring  
   - We’ll have morning structured, afternoon unstructured bit be more “unconference”-style  
8. Review batches for [CERT C  Rust Mapping](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/336) (Pete)  
- Let's split up again, to get some feedback on batch 2  
- [428 \[CERT C Review Batch 2/5\] Review proposed Rust categorization](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/428)  
8. Round table

## **Check-in area**

* Pete LeVasseur 🗑️  
* William Barsse  
* Oreste Bernardi 🦥  
* Julius Gustavsson  
* Max Jacinto 📗  
* Markus Hosch  
* Douglas Deslauriers 📷  
* Arshad Mahmood ☔  
* Samuel Wright 😪  
* Michael Henn 🍵  
* Christof Petig 😫  
* Achim Kriso 🦆

**Notetaker:**

- Max Jacinto

For tips on how we take notes in the Safety-Critical Rust Consortium, please see the [Meeting Notetaker Role](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/docs/notetaker-role.md) doc.

## **Housekeeping section**

- Document space: [coding-guidelines](https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines)  
- Zulip: [safety-critical-consortium: Coding Guidelines](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/Coding.20Guidelines)  
- [Kanban board](https://github.com/orgs/rustfoundation/projects/1/views/3)  
  - [`contributor experience`](https://github.com/orgs/rustfoundation/projects/1/views/4) view  
  - [`coding guideline`](https://github.com/orgs/rustfoundation/projects/1/views/5) view

## **Tasks**

- xx

## **Meeting Minutes**

- **\[Checking of previous meeting notes\]** Mention of the UB/Unsound project as a reminder; nobody against, all approved  
- **\[Introduction of new members\]** Introduction of a new member (welcome\!). Works at a company focused on defense with projects in Rust needing to be certified; interested in HOW the certification can be achieved as well as viability. Gives Rust lectures at the University of Ulm.  
- Would be good as the Coding Guidelines Subcommittee to make clear how everybody can help, considering a lot of people are not being paid for the job. Issues opened later regarding why X rule does or does not map to Rust. Idea to set up a “milestone” in GitHub centered around tracking completion  
- **\[MISRA C\]**   
  - PR already submitted; requires review to see if it can be merged soon. More updates incoming given new findings. The plan is to have 3 mapping tables for already established standards to prove concreteness to prove Rust is at least as good as C and C++. If the table is filled enough those covered standards would make a claim for Rust to be up to par with C/C++.  
  - *Question*: Certain rationale cannot be followed or isn’t as clear; are there plans to provide better matching?  
    *Answer*: Yes, through three main tables: 1\. Table for everything that’s safe; 2\. Table for unsafe; 3\. Table for why are certain rules not to be followed. These are all addressed in a PR  
  - In the PR, there’s a left column named “Category” which is for MISRA and the right “Category” is for Rust. For a lot of cases if they differ the columns should at least explain why they do.  
- The guidelines we’ll write at the beginning may not be perfect but it’s okay to merge them initially to get things going. Better to be incomplete than to be incorrect\!  
- **\[SCRC Project Goals\]**  
  - Normative Documentation: discussion can be found in the previous meeting’s minutes as well as the dedicated Zulip thread.  
  - Clippy: folks from the Clippy team have come to our meetings and there has been alignment shown; preferred to put our lints in their “own” corner. Chance that there’s an onboarding session at RustWeek and remotely; details still being ironed out. Discussion can be found on the Zulip threads in both the SCRC and Clippy team channels.  
- **\[SCRC Room\]**  
  - The value proposition of getting together wasn’t entirely clear yet; what’s proposed is to have a morning that’s more structured (report-out, Q\&A) afternoon less structured (un-conference-like) with more break-out groups, “showcase” sort of section from attendees.  
  - Showcase/Talk idea about the different coding guidelines we have access to and how to get the most out of all of them  
- **\[CERT C Batch 2 Reviews\]**  
  - Group 1:  
    1. DCL38: We agree to the assessment because there is no such thing as a flexible array. Slices do have a known size, and transmuting from a raw pointer to the beginning of a c array to a slice is unsafe anyway.  
    2. EXP35: Debate about what is a "temporary object". Conclusion: Not existing in safe Rust. Unsafe has pointers, though, so no lifetime checking is done here. Question: Is there a defined lifetime of temporaries in Rust? How does that change if that temporary gets converted to a reference or eve to a pointer?  
    3. EXP43: Does this apply to creating multiple \*mut pointers to the same object? That'll definitely UB in unsafe Rust.  
  - Group 2:  
    1. FIO44: Agreed; check juuuust in case about the UB in `Seek`’s APIs, preferably add those details into the table if possible.  
    2. ERR33: Agreed; there are also specific Clippy lints for this ([https://rust-lang.github.io/rust-clippy/master/index.html?search=must\_\#let\_underscore\_must\_use](https://rust-lang.github.io/rust-clippy/master/index.html?search=must_#let_underscore_must_use)). Find a way to show the compiler enforcement, otherwise we’d be forced to use something like Ferrocene. However, it should be worth it to note, and with a big BUT, that if we have no real return value then we have a function with a side effect which can be enforced by Clippy but otherwise it’s just a “let’s see what happens”  
    3. MSC37: Agreed; would be good to provide evidence/examples of the compiler error in case this happens  
    4. INT30: Agreed; again, would be good to provide an example (`overflow-checks = true`)  
  - **FEEDBACK**: Would be good to translate the C examples to PROVE why the rules do map/do not map to Rust with proper evidence  
  - **FEEDBACK**: Alongside coding guidelines, we should also have a sort of environment guidelines (related to what was written in INT30)

## **Material**

Any material to read before the meeting should be included here.  
