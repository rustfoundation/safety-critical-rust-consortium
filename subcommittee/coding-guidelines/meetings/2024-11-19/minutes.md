# Coding Guidelines Subcommittee Meeting on 2024-11-19 @ 6pm UTC

## Agenda

0. Meeting recordings / transcriptions - Live discussion
1. Acceptance of [Previous Meeting Minutes](../2024-November-05/minutes.md)
2. Shift meeting time 2 hours earlier to accommodate Asia participants (Pete LeVasseur)
3. Contributor Expectations - Approval (Pete LeVasseur)
4. Safe Usage of Unsafe Guidelines - Check-in (Pete LeVasseur)
  * [Learn `unsafe` Rust](https://github.com/google/learn_unsafe_rust) - Offline Review & Q&A
  * [Examples of unsafe patterns](../../initiatives/safe-use-of-unsafe-guidelines/unsafe-example-usage.md) - Chapter writeup
5. MISRA + Rust (Alex Celeste)
6. Round table

Supplemental material to the agenda can be found on the [GitHub repo](https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines).

## Check-in area

**Please add your name, and an emoji that describes your day.**

* Sarah Dietrich 😃
* Andrew Herridge 😀
* Munawar Hafiz 🙂
* Felix Gilcher 🙂
* Julius Gustavsson 🙂 
* Chai: 🥶

(Also attending: Alex C, Andrew H, Chaitanya RK, Felix G, Jonas W, Julius G, Peter L, Sarah D, Munawar H)

**Notetaker:** 

Alex Celeste

## Housekeeping section, please add 

* Document space: https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines
* Zulip: [safety-critical-consortium: Coding Guidelines](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/Coding.20Guidelines)

## Tasks

* [Peter](mailto:plevasseur@gmail.com): put a link to previous meeting's minutes in next meeting's agenda
* [Peter](mailto:plevasseur@gmail.com): put together another LettuceMeet poll to establish the new timeslot
* [Peter](mailto:plevasseur@gmail.com): put the call for reviewers for the "safe usage of unsafe" material on Zulip, and explain the review strategy there
* [Alex](mailto:aceleste@perforce.com): update the draft of the MISRA Applicability Matrix and Iron Carbide onto the Subcommittee Google Drive

## Meeting Minutes

### Recording or transcription of sessions

Proposal to record or otherwise keep a full transcription of discussion in order to better facilitate offline and async workflow.

AH: more importantly to establish a full audit trail for the development of the design decisions that will impact safety-critical work.

PL places a poll in the chat (not everybody votes).

Felix: against - full video and transcripts are simply not good records, require much trawling. Automation can make them searchable but this also means the discussions become fully on-the-record, which would reduce contributions as participants feel inhibited to speak freely.

AC: MISRA and WG14 explicitly follow the [Chatham House rule](https://en.wikipedia.org/wiki/Chatham_House_Rule), this is really useful when tool vendors come together and can speak openly

Felix: it enables frank discussion of actual issues.

(it was observed that the rule does not imply freedom to violate confidentiality during discussions)

AH: would still like to be careful that we fully document all decisions, in order to be able to justify them to adopters.

Felix: minutes must aim to capture all relevant details and the results of votes.

Based on the number of objections, PL withdraws the poll and the proposal.

### Acceptance of previous minutes

Unanimous consent.

Felix: request that each agenda includes a link to the previous minutes for ease of access.

**ACTION** Peter to add a link to the previous minutes to each agenda for future meetings.

### Shift meeting time by two hours

At least one contributor is not able to engage live with a meeting held at 1800 UTC.

JW: this is already late for EU participants.

AH what would be the impact on participants in PST?

MH: personally would be okay with this.

JG: also okay with this.

**ACTION** Peter to put together another LettuceMeet poll to establish the best new timeslot.

### Approval of revised contributor expectations

PL: good concerns raised last time, a new document has been drafted by PL and Florian G, much longer but also a more flexible requirement and setting the participant's expectations. This will remain a living document and can be revisited at any time if our needs change.

Unanimous consent.

### "Safe Usage of Unsafe" Guidelines

PL: the current "guidelines" are more like a reference manual. Also the "Learn Unsafe Rust" book, more about the "why" of `unsafe` and when UB matters or is desirable, than traditional guidelines. More "meaty" practical explanations. Provides a possible starting point for the group.

Currently hosted on a Google repository but they are happy to receive PRs and maybe even to move to Foundation ownership.

Last time 8-9 people raised hands to review this. Consider splitting into work groups, to review the first book, to review the other book and look for missing pieces, and a third workgroup to review example material and the practical concerns to keep in mind when writing unsafe code. Aim to produce a practical "how to".

JW: agree with this, and would add "why _would_ you use `unsafe`", because of the variety of applications. Memory-mapped IO and transmutes are common in embedded for ostensible performance reasons that apply less and less over time. Memory-mapped IO is a practical starting bullet point.

PL calls for an initial group of reviewers for the two named books.

**ACTION** Peter to put this call for reviewers on Zulip due to the large number of participants not actually on the call, and explain the review strategy there.

Noted that the original link in the agenda was broken before the meeting.

MH: the Rustonomicon is also a suitable resource for this exercise.

### MISRA and Rust

AC reports from the MISRA all-WG meeting the previous week where Rust and the SCRC were a discussion topic.

MISRA is friendly towards the SCRC and wishes to collaborate. For the record, MISRA _does not_ view Rust as any kind of threat entity, and encourages its use.

MISRA plans to release an official Applicability Matrix of MISRA C Guidelines to the Rust language. This will be an official WG document freely available in the public domain. The derived "Iron Carbide" guidelines will be handed over to the Subcommittee to review or extend (or not) as it sees fit. At some future stage MISRA would like to be able to publish a derived work of whatever the Subcomittee produces, under red-triangle branding.

JW: so does this mean MISRA is developing Guidelines in parallel?

AC: no, it wants to avoid duplication of work and wants to let the experts here take the lead.

JG: believe such a review was done by Florian G as part of his work.

Felix G: PolySync did a review a few years ago. ([link provided in chat](https://github.com/PolySync/misra-rust/blob/master/MISRA-Rules.md))

PL: seeing these as parallel development tracks which may collide or converge in future, with the "known safe" uses of unsafe code as the other main development track.

**ACTION** Alex to update the draft of the Applicability Matrix and Iron Carbide onto Google Drive before the next meeting.

### Round Table

Referred to the "Topics of Interest" board in the GitHub. Currently has no new topics.

### Other business

AC requesting information about the London meeting. PL directs such inquiries onward to Joel.

Previous issues with contributors being able to access Zulip were resolved and all members are now able to communicate there.

### Adjournment
