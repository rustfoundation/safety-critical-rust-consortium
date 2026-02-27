# Tooling Subcommittee Meeting on 13 February 2026 @ 4pm GMT

| Search Key | Description |
| :---- | :---- |
| \[todo\] | Action Item |
| \[decision\] | Something decided on |
| \[important\] | Key information |

## Agenda

1. Solicitation of notetaker
2. Review last time’s meeting minutes
3. Present new members
4. [Safety-Critical Rust Flagship Theme](https://rust-lang.github.io/rust-project-goals/2026/roadmap-safety-critical-rust.html#safety-critical-rust)

## Check-in area

**Please add your name, and an emoji that describes your day.**

* Alexandru Radovici
* Félix Fischer 😁
* Pete LeVasseur 🦀🪩
* Arnaud Riess 🙃
* Oreste Bernardi 🍵🫨
* Tony Aiello
* Tiago Manczak

 **Notetaker:**

* Tiago Manczak

## Housekeeping section

## Tasks

* Tiago Manczak \- Publicate the list of the tools in the website
* Oreste Bernardi \- Prepare a PR with the listing of books

## Meeting Minutes

* New members presented themselves.
* Last time meeting minutes reviewed approved and merger ( [https://github.com/rustfoundation/safety-critical-rust-consortium/pull/561/changes](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/561/changes))
* \[Project Goals 2026\] Presented the content of [https://rust-lang.github.io/rust-project-goals/2026/roadmap-safety-critical-rust.html\#safety-critical-rust](https://rust-lang.github.io/rust-project-goals/2026/roadmap-safety-critical-rust.html#safety-critical-rust)
  * Review from Rust Project until march 2026
    * Initial scope is fine from Rust project but further comments are welcome over Zulip
  * Since the unsafe is still a work in progress in the Rust language the goal of a normative unsafe targets a kind of “safe unsafe” guideline for productive code.
  * \[[Stabilize FLS Release Cadence](https://rust-lang.github.io/rust-project-goals/2026/stabilize-fls-releases.html) \] How it relates to the compiler versions, editions and features? What would happen for example if there is a conflict between the FLS and the compiler. The final point is how compiler vendors will use the FLS to qualify their compilers and maintain long term support versions. Qualification of the rust compiler would be against a FLS and the compiler version in the case of an eventual bug on the compiler version the vendor will have to align on each case and customer. The qualification takes in consideration also the flags and configuration and any necessary deviation would require a reassessment on the qualification.
    * Proactively going back to old versions of the FLS and reviewing it is not a sustainable model but accepting contributions to it(old FLS versions) from external (non-FLS team) people might be a workable model.
    * For safety the match between the compiler behaviour and the specification is the main concern in the end of the day
    * There are still many fundamental changes foreseen in the Rust language that will impact the FLS preventing the FLS from taking a normative role in the Rust project.
* \[Publication of the Tools in the Website\] Tiago will take over the action item to publish the content
* \[Books\] \- Listing of books
  * Can we have a listing?
    * What are the criteria to include the book in the list?
    * Classify the level of the book: basic, medium advanced
    * Topics: concurrency( Mara’s book), macros, etc…
    * The list will be created and a first proposal will be done until next meeting
* \[Rust Project Goal MC/DC\]
  * Is someone already working on that?
    * Adacore has started working on it and will upstream and maintain it
    * Other stakeholders could also join the work
    * There is a [MCDC support thread in Zulip](https://rust-lang.zulipchat.com/#narrow/channel/546987-project-goals.2F2026-workshop/topic/mcdc-support/with/563031414) where developers working on that can be contacted
