# Coding Guidelines Subcommittee Meeting on 2026-02-11 @ 1700 CET / 1100 EDT

[Link](https://www.worldtimebuddy.com/?qm=1&lid=2643743,12,8,5&h=5&date=2026-2-11&sln=11-12&hf=1) to meeting time in common time zones.

| Search Key | Description |
| :---- | :---- |
| \[todo\] | Action Item |
| \[decision\] | Something decided on |
| \[important\] | Key information |

## **Agenda**

1. Solicitation of notetaker
2. Acceptance of [Previous Meeting Minutes](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/coding-guidelines/meetings/2026-01-21/minutes.md)
3. Introduction of new members
4. Mention review/merge workflow issue (See [example](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/302), [example](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/402#issuecomment-3874829138))
5. Discuss change to meeting weekly at this time
6. Discuss how to handle low-quality submissions (AI disclosure policy?)
7. Review of open issues
8. Review of open PRs
9. Round table

## **Check-in area**

* Pete LeVasseur 🦀⛑️
* Oreste Bernardi 🥷
* Sam Wright 🏃
* Max Jacinto ✏️
* Markus Hosch 🦄
* William Barsse
* David Svoboda (-:
* Douglas Deslauriers ❄️
* Andreas Weis 👋
* Roberto Bagnara
* Christof Petig 🦀

**Please add your name, and an emoji that describes your day.**

**Notetaker:**

* Markus Hosch

For tips on how we take notes in the Safety-Critical Rust Consortium, please see the [Meeting Notetaker Role](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/docs/notetaker-role.md) doc.

## **Housekeeping section**

* Document space: [coding-guidelines](https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines)  
* Zulip: [safety-critical-consortium: Coding Guidelines](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/Coding.20Guidelines)  
* [Kanban board](https://github.com/orgs/rustfoundation/projects/1/views/3)  
  * [`contributor experience`](https://github.com/orgs/rustfoundation/projects/1/views/4) view  
  * [`coding guideline`](https://github.com/orgs/rustfoundation/projects/1/views/5) view

## **Tasks**

* Open PR to make review checklist more measureable
* Open issue about AI policy
* Open issue about how to deal with low quality submissions

## **Meeting Minutes**

* Hot potato handed over (aka notetaker)
* Notes from previous meeting accepted
* (Not so) new members introducing themselves (2 people)
* Review of the merge workflow:
  * PR has been merged that documents the workflow, see https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/blob/main/CONTRIBUTING.md
  * Focus on first-time contributors
  * Q: What about the checklist for reviewers? Where will it be? Quick recap on the topic: How does a reviewer know that their duty is done? What’s the minimum standard on PRs?
  * A: Bot will post a review checklist. Example: https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/370#issuecomment-3879379076
  * Wording needs to be more precise, e.g. when is “appropriately” appropriate enough? Request: Open up a PR to make the wording more precise.
* Change of meeting schedule.
  * It might be more interesting to have the same spot each week instead of a rotating time slot. Since participation from the Pacific region is rather low, this time slot will most likely be located such that it fits EUR / US.
  * In addition, there will be a meeting for the Pacific timezone once per month. New meeting schedule will be effective ~beginning of March.
  * Opinion: Current schedule emphasizes the global nature of the SCRC, might regress with the suggested schedule.
  * Experience was that attendance didn’t really build up after some month
  * Suggestion: Have a “champion” from the Pacific TZ run the meeting and decide on their own on the frequency.
  * Takeaway: Try to make the voices still audible, look for a champion
* Low-quality and/or AI contributions:
  * TLDR: Do we need a policy about AI contributions? Some apparent(?) contributions appeared lately, how to deal with them?
  * Opinion: Why does it matter whether it’s AI or not? We should deal with the question how to deal with low-quality contributions
  * Seems that the tag “good-first-issue” is prone to AI bots
  * Opinion: AI is able to “flood” (by number of PRs or PR size), which is time consuming for reviewers, so we need to find a way to quickly deal with new PRs to not drown in slop
  * Opinion: Check how responses from the author look like to see whether we can expect improvements
  * Opinion: Adding the AI-tag doesn’t add a lot of value, since the “bad guys” will not do it anyway. Counteropinion: It helps using AI in a responsible way by having the good guys disclose the AI usage
  * Opinion: Refusing “too chatty” PRs will also remove some people from contributing since its their nature to not be concise. Rather count on “earned trust” when choosing reviews.
  * Opinion: Having to disclose whether AI was used would also “stigmatize” the use of things like grammar checkers
  * Opinion: Have a well-maintained checklist will help fight the flood by being able to quickly refuse things on a well-defined basis
  * Bottom line: Let’s focus on low vs. high quality and enforce this with the help of a good checklist & guidelines
  * Opinion: Labeling won’t be very helpful as “evil AI” won’t label itself anyway
* Review of open issues
  * It is probably not obvious for reviewers that they have been assigned, as this is only one single comment in the respective PR
  * Not so easy to implement without giving a lot more people elevated rights
  * Suggestion: Use a search query with the bot’s message to find all “assigned” tickets
  * Improvements will be made to make people more aware of assigned reviews
* Roundtable
  * US / EUR meeting slot will most likely stay Wed afternoon (CET) / late morning (US)

## **Material**

Any material to read before the meeting should be included here.

* Milestone: [Prepare for launch to wider Rust community](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/milestone/1)
