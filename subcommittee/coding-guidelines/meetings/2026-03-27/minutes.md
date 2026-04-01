# **Coding Guidelines Subcommittee Meeting on 2026-03-27 @ 0800 JST / 1600 PDT**

[Link](https://www.worldtimebuddy.com/?qm=1&lid=5,12,2643743,8,1850147,100,14&h=5&date=2026-3-25&sln=11-12&hf=1) to meeting time in common time zones.

| Search Key | Description |
| :---- | :---- |
| \[todo\] | Action Item |
| \[decision\] | Something decided on |
| \[important\] | Key information |

## **Agenda**

1. Solicitation of notetaker  
2. Acceptance of [Previous Meeting Minutes](https://docs.google.com/document/d/1-199gUHkqoV5gZp6Pmv67oBCaj-FIUcoiHKDR1bse90/edit?tab=t.0#heading=h.a85rlz5fz80p)  
3. Introduction of new members  
4. Review batches for [CERT C \=\> Rust Mapping](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/336) (Pete)  
   - [\#427 \[CERT C Review Batch 1/5\] Review proposed Rust categorization](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/427)  
   - [\#428 \[CERT C Review Batch 2/5\] Review proposed Rust categorization](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/428)  
   - [\#429 \[CERT C Review Batch 3/5\] Review proposed Rust categorization](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/429)  
   - [\#430 \[CERT C Review Batch 4/5\] Review proposed Rust categorization](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/430)  
   - [\#431 \[CERT C Review Batch 5/5\] Review proposed Rust categorization](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/431)  
5. Discuss running Asia-Pacific meeting organization  
6. Proposals and ideas for new rules (all)  
7. Progress on ongoing tasks (all)  
8. Round table

## **Check-in area**

* Mikhail Antoshkin ☕  
* Pete LeVasseur 🖖  
* Yuchen Shen ☕

**Please add your name, and an emoji that describes your day.**

**Notetaker:**

* Yuchen

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

* Have mapping between Cert C to Rust and Misra C to Rust in FY26  
* MEM34 partially applicable to Rust, only in unsafe  
  * We don’t do a lot manual allocations in Rust  
  * There is case that user creates bindings to libc memory API  
  * Do we need a specific rule for FFI?  
  * List all the possibilities for Rust programmer to use free() and dealloc() in the mapped rule  
* CON35 applicable but probably change the name to not mention “by the predefined order” but just “avoid deadlock”. Rust has better API to avoid deadlock  
  * Parking\_lot has the experimental mechanism to prevent deadlock  
  * [https://fuchsia-docs.firebaseapp.com/rust/lock\_order/index.html](https://fuchsia-docs.firebaseapp.com/rust/lock_order/index.html)  
  * [https://crates.io/crates/lock\_ordering](https://crates.io/crates/lock_ordering)  
* EXP36 cast itself should be safe? Only the access can cause undefined behavior.   
  * But it doesn’t make sense to just cast the pointer without using the casted pointer. So better to just say do not cast the pointers.  
  * What “strictly aligned” mean here?  
    * Like cast a pointer to byte to pointer to a data structure, then the pointer can point into unaligned location in the data structure  
* MEM35-C  
  * We probably can reduce the work we do to have a single rule to say “do not break safety contracts” to cover all possible cases and refine later to specific cases.  
  * It is good to explicitly document “do not break safety contracts” even it is obvious.  
* Copy the discussion above into issue \#431

## **Material**

Any material to read before the meeting should be included here.  
