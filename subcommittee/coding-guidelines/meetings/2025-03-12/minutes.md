# Coding Guidelines Subcommittee Meeting on 2025-03-12 @ 3pm UTC

| Search Key  | Description          |
|-------------|----------------------|
| [todo]      | Action Item          |
| [decision]  | Something decided on |
| [important] | Key information      |

## Agenda

1. Acceptance of [Previous Meeting Minutes](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/coding-guidelines/meetings/2025-02-26/minutes.md)
2. Review proposal(s) for coding guidelines against requirements (Pete, others?)
3. Proposal to ensure upstreamed Ferrocene Language Specification with t-spec keeps paragraph-ids.json with paragraph IDs tied to content hashes (Pete)
4. MISRA C Addendum 6 (Rust) Brief (Alex) [todo] -- we run out of meeting time
5. `unsafe` Formulate Chapter Material Task Force \- report (Markus, Jonas, Pete)  
6. `unsafe` Practicum Chapter Task Force \- report (Joni)  
7. Safety Pamphlet \- progress (Andrew Fernandes) [todo] -- didn't get to it during the meeting although progress's happened in the [PR](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/212)]
8. Round table

Supplemental material to the agenda can be found on the [GitHub repo](https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines).

## Check-in area

**Please add your name, and an emoji that describes your day.**

* Pete LeVasseur, 😄
* Andrew Fernandes (way more awake)
* Oreste Bernardi 😴
* Alexandru Vochescu 😴
* Douglas Deslauriers 🙂
* Alex Celeste 🥱
* Julius Gustavsson 🙂
* Marc Schoolderman 😶‍🌫️
* Walter Pearce (Rust Foundation) 👾
* Fernando Jose 🤓
* Sarah Dietrich 😀
* Christof Petig 🙂
* Koppany Pazman
* Andrew Herridge 😀
* Sasha Pourcelot ☕

**Notetaker:**

* Fernando

## Housekeeping section

* Document space: [coding-guidelines](https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines)  
* Zulip: [safety-critical-consortium: Coding Guidelines](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/Coding.20Guidelines)
* [Work Item Board](https://github.com/orgs/rustfoundation/projects/1)

## Tasks

* 

## Meeting Minutes

1. [Previous meeting minutes](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/coding-guidelines/meetings/2025-02-26/minutes.md) accepted without further discussion after mentioning a few of its main topics.
1. Review coding guidelines proposals
* Way of working of the guidelines. What are the goals? What are the requirements from the tooling subcommittee?
* PL opened [an initial proposal](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/226) with the intention of gathering feedback:
  * It uses Sphinx and Sphinx-Needs.
  * Demo walk-through: the build generates doctrees and build directories. [important]
    * .html with organization of the coding guidelines into chapters mapping how it’s done in Ferrocene.
    * We look into the Types and Traits (source in src/coding-guidelines/types-and-traits.rst) as an example.
    * Breakdown of the guideline, box with description, status, fls link. "child" requirements, bad and good examples, etc. 
    * Questions about this output? There was one question.
      * Regarding the link on top of the guideline, can there be a more human-friendly ID as in MISRA (in the case of the Types and Traits example it looks like gui\_xztNdXA...)?
      * It is brought to attention that making IDs more human-friendly increases the chances they would collide (e.g. also when web-searching for IDs).
      * ID stability is discussed when taking into account it may come from a checksum. Having it as a checksum is good for differentiating when the guideline evolves and tools may be implementing or supporting different versions of it. [decision]
1. Guidelines discussions / round table
* Following-up an example about usage of unwrap, it was discussed how guidelines should cross-reference each other, considering if they overlap, and it was suggested to refrain from rules that prohibit some usage.
* Following MISRA's way of organizing, different "enforcement" levels may help to organize these use cases. A rule may be required via automatic tool, or via review, another rule recommended.
  * On the one hand, there’s a risk that the guidelines become a template to be modified. That would oppose a goal of becoming a set of guidelines to aim to comply with.
  * On the other hand, having broader scope would welcome more users.
* The [MISRA's compliance open document](https://misra.org.uk/app/uploads/2021/06/MISRA-Compliance-2020.pdf) was cited. [important]
1. Chapter selection for initial guidelines [GH issue](https://github.com/rustfoundation/safety-critical-rust-consortium/issues/188): [decision]
* DRI for unsafety: Andrew
  * Contributing: Jonas, Julius, Oreste
* DRI for concurrency: Jonas
  * Contributing: Andrew
* DRI for macros: Pete
  * Contributing: Oreste, Julius

## Material

Any material to read before the meeting should be included here.

### GitHub Project Board for Work Items

* [Work Item Board](https://github.com/orgs/rustfoundation/projects/1)
* [Coding guidelines published](https://github.com/rustfoundation/safety-critical-rust-consortium/issues/188#issue-2869798433): Proposes a way of work to tackle the coding guidelines

### Tracking Issues

* [\[Coding Guidelines\] Learn unsafe Rust \- Practicum Chapter Draft](https://github.com/rustfoundation/safety-critical-rust-consortium/issues/122)  
* [\[Coding Guidelines\] Formulate Chapter Material for Learn unsafe Rust](https://github.com/rustfoundation/safety-critical-rust-consortium/issues/123)

