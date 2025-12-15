# Tooling Subcommittee Meeting on 28 November 2025 @ 4pm GMT

| Search Key | Description |
| :---- | :---- |
| \[todo\] | Action Item |
| \[decision\] | Something decided on |
| \[important\] | Key information |

## Agenda

1. Solicitation of notetaker  
2. New members presentation  
3. Involve the Safety Critical Consortium tools folk in a 2026 goal

## Check-in area

**Please add your name, and an emoji that describes your day.**

* Pete LeVasseur 🦵🤖  
* Tiago Manczak  
* Manuel Hatzl  
* Xander Cesari 🦃  
* Oreste Bernardi 🏙️  
* Tshepang

**Notetaker:**

* Xander Cesari

## Housekeeping section

* 

## Tasks

* See \[todo\] below ⏬

## Meeting Minutes

* No new members  
* Update from the group bringing the tools into the list  
  * There are two PRs still open about the tooling list and the RFC process  
  * RFC for tools list maintenance flows  
    * [PR link](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/497)  
    * [Document preview link](https://deploy-preview-497--safety-critical-rust-consortium.netlify.app/tooling/rfc-tools-review/)  
    * Participants in this meeting read the document live on the call before offering feedback  
    * Which are the criteria for the evaluation of the tool and whether it should be accepted to the list? Is that part of this document or another? Criteria like how good is the Rust support for the tooling?  
      * The plan for this process is still to keep the criteria very loose initially to cast a wide net for tools. But we can add specific acceptance criteria into this document as we develop them.  
    * It’s interesting that this is phrased as an “RFC”. This is more of a potential RFC that could be there. But this was developed before the RFC process existed so maybe this shouldn’t be an RFC and this is just our current existing process? It’s more documentation of the existing process than a request for comment on a process change.  
    * Also some minor formatting changes on the document, can that be left on the PR?  
      * Yes that would be ideal  
    * How should a tooling suggestion issue be created?  
      * There’s a tooling submission issue form on the Github that will present a template for submitting it.  
      * [The issue template](https://github.com/rustfoundation/safety-critical-rust-consortium/issues/new/choose) is just a start but we can add more fields as needed  
      * There’s another open PR for an issue template for a tooling request, an ask for a Rust tool or feature that does not yet exist  
  * PR about adding machine readable lists for all tools and compiler coverage features  
    * [PR link](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/463)  
    * This PR adds the initial list of tools that will be/are being collected with the previous PR and issue template  
    * Document is structured in a Rust file with serde serialization and deserialization. Actionable as a cargo xtask.  
    * Review of the fields, specifically which fields are optional and required  
    * The license is just one string field, what happens when a tool has multiple licenses?  
      * Just add the relevant details of any license complexities into the string  
    * Let’s bias towards just getting it merged (LTGM) and improve as we go on  
      * A good way to get more eyes on things would be to just send it on Zulip since we seem to be getting behind on Github notifications  
    * The consensus is to just get this merged and we can iterate as necessary  
  * \[todo\] Pete: Put contribution guide to coding guidelines onto arewesafetycriticalyet.org   
    * Bot that runs when CONTRIBUTION.md is updated?  
* Main topic: getting a 2026 Rust Project goal on the board for the consortium  
  * (This work could and maybe should also be done in the Rust Project Bridge Task Force? But we’re also open to soliciting feedback in the subcommittees)  
  * [Rust Goals group reached out](https://rust-lang.zulipchat.com/#narrow/channel/546987-project-goals.2F2026-workshop/topic/Safety.20Critical.20Consortium/with/558841301) to the Safey-Critical Consortium inviting us to bring a 2026 goal to the table. We want to meet them halfway on this and bring some suggestions.  
  * There [has also been feedback](https://hackmd.io/-SoPwfT6TDaHmFvGrQxSCw) from everyone about how the Rust goals are going.  
  * It seems that goals may switch from half year to full year. This better aligns with industry and companies. Q1 of each year would be a planning quarter and a call for proposals, with the other 3 quarters being largely for execution. In Q1 we would have meetings, discuss the values, but then also go find contributors or developers who can take on the feature. The work could then start whenever a champion is found and the matchmaking process is complete but we would start with planning prior to beginning execution.  
  * Is there any feedback on this process in general?  
    * No, thumbs ups in the chats  
  * Next steps are off-cadence meetings among the Rust Project Bridge Task Force to gather this feedback, both on the process and possible goals, then get approval from the consortium before bringing them to the project.  
  * Thoughts?  
    * So the idea is to have a big roadmap that we can then decompose into smaller goals? Or should the goals be small and execution-focused?  
      * Perhaps we should KISS (keep it simple, superperson). It may be premature to build a big roadmap and maybe we should just focus on the next item blocking SC adoption  
      * But perhaps we should think big but execute small? Having a large goal in mind, a long term plan, might allow us to make sure that our smaller goals are aligned.  
      * It would be good to make sure that what we’re bringing to the Project are specific goals that we know would help safety-critical adoption. We shouldn’t bring goals that are hypothetical or that we’ve developed internally in the consortium without specific requests from industry.  
      * We will bring the goals to the Project but they may or may not adopt them based on how achievable and realistic they are. It would be good to understand exactly how concrete our goals need to be for them to be adopted and successful before we bring up goals.  
        * We can go look at the goals in the past and identify how successful they’ve been in execution and adoption, to try to calibrate our internal goal process.  
      * We’ve discussed various smaller features in the coding guidelines subcommittee. Such as macros and macro expansion for safety-critical development. We can collect all of the smaller features being discussed, study them for themes and trends, then identify the best first steps to find a good concrete proposal.  
        * We could send out a survey to the consortium (and/or the broader community?) to ask specifically what people need, why they need it (what standard they’re trying to achieve). Then we can use that feedback to try to identify goals.  
        * \[todo\] Xander/Pete: draft a survey and get it distributed ASAP?  
          * Draft next week (12/01-12/05) and run the survey the week after? (12/08-12/10)  
        * Survey is a good idea, we should ask not just what but also the priority. Maybe we should prepopulate it with some of our ideas, ask respondents to rank them, and then also solicit new ideas.  
        * The State of Rust survey had some interesting options for features including “this would unblock my work”, “this would be nice to have”, or “I don’t need this”.               
  * Goal ideas could include MC/DC or others

-----

Niko, via email to some people regarding the Rust Project Goals process (Pete to verify if there’s another place this is posted or how public we can make this):

Hi everyone,

Following up on these discussions, I wanted to update all of you on the plans for Project Goals in 2026\. We are planning to change up how the program runs in some significant ways in response to what has worked well and what has not. This email summarizes the key ideas; you may also enjoy reading the [detailed notes from the project goal feedback discussions](https://hackmd.io/-SoPwfT6TDaHmFvGrQxSCw). Please feel free to reach out with any feedback in the \`\#project-goals\` stream in Zulip.

**\#\# TL;DR**

* **We'll move to an \*annual\* goal process:**  
  * We will plan flagship themes and cross-cutting goals in Q1, but smaller goals can be added at any point during the year.  
* **We'll put out a call for pre-proposals very soon to help connect people with the Rust org:**  
  * We hear from a lot of people that they don't know how to approach the Rust project, so we want to have a special step to receive "pre-proposals" from people who want to drive or sponsor work but need help interfacing with the project. This goes towards the goal of project goals as the "front door" for Rust.  
  * (An example of this was when Dioxus raised up the [High-level Rust goal](https://dioxus.notion.site/Dioxus-Labs-High-level-Rust-5fe1f1c9c8334815ad488410d948f05e).  
* **We'd like to meet with team leads (or others\!) to review how goals can/should be integrated into your team processes:**  
  * Goal owners all talk about the importance of active champions and team engagement. How can we help your team stay up-to-date, plan, balance resources?

**\#\# Annual goal process**

We will be shifting to an \*\***annual**\*\* goal process rather than the current 6-month process \-- so we will have 2026 goals, not 2026H1 and 2026H2.

***\#\#\# Q1 is for planning flagship goals, edition items***

Flagship goal planning takes place in Q1, with the goal of having the Goals 2026 RFC accepted by Mar 31 (end of Q1).

In edition years, the Q1 planning period will also be used to identify potential items for inclusion in the upcoming edition. It is not yet clear whether 2026 will be an edition year or not. There has been discussion of moving to annual editions; alternatively, we could do the preparation for Rust 2027 next year and actually have an edition release that takes place in the year it's supposed to be for (![😲][image1]). Or just wait another year.

***\#\#\# Smaller goals can be added at any time***

If you have a 2026 goal that is (a) approved by the relevant team leads and (b) "fully resourced" (i.e., you have someone to work on it, someone to do the reviews, etc), you'll be able to just open a PR against the repository at any point. Once the team leads sign off, we'll merge it in.

**\#\# Champions and goal resourcing**

I would like to get crisper on "goal resourcing". I am imagining something this.

First, every goal must have a champion and sign-off from the leads of every team involved. I'm inclined to make the champion a singular individual from the team that is "most involved" with the goal, rather than having multiple champions from multiple teams, unless there is a specific reason to have more than one.

Second, if the goal involves landing PRs, it must have a dedicated reviewer from each team that will be accepting PRs. This could be the same person as the champion.

I'd like to talk to folks about the "expectations" from a champion per team and how your team can integrate goals into your processes. For the lang team, for example, we are reviewing updates on lang-team goals once a month, and part of the job of a champion is to make sure there are updates to review, that they are complete and cover major design pivots, and that the champion is familiar enough with what's going to to answer questions.

**\#\# Focus quarterly updates on blog posts**

One open question is the best way publish updates. Having issues with updates is very useful. But the existing blog posts are not necessarily that great, since they mostly just repeat comments.

I'd be curious hear from folks, but my current tentative plan here is that we ought to do three things:

* Keep the Zulip stream and project goals for regular updates. You can also view updates collected across all the issues related to your team on the rust-project-goals website (e.g., [lang-related updates are here](https://rust-lang.github.io/rust-project-goals/lang/index.html)).  
* Quarterly blog posts covering the progress on flagship goals as well as overall process updates:  
  * The Q1 post (Jan) will cover the continuing goals and give a draft of our flagship plans.  
  * The Q2 post (Apr) will cover the accepted flagship goals.  
  * The Q3 post (July) will be a "mid-year" update.  
  * The Q4 post (Oct) will identify how things are going and which goals we expect to continue.  
* The [content team](https://github.com/rust-lang/content-team) has [expressed interest](https://rust-lang.zulipchat.com/#narrow/channel/523012-t-content/topic/Rust.20Project.20Goals.20-.20Narrative.20from.20the.20Content.20team/with/554433763) in doing interviews or in-depth posts and videos covering other goals.

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAARCAYAAAA7bUf6AAACt0lEQVQ4T62Ty08TURTGvzvTFx0rFFqMVVFLo6iJGxMNUYlGQQzGRF1oVFipMZEF/AFNiHGPkcSNcSOKceGDBBMscUFENhLdIPigolGKoDAUO6XPuZ47Y0cwsPMmZ1733N989zvnMvyHwZZjaF2hIRTbdrEiCYwyOKdY0IF4dkA5G93/75olEK2zsoP5Hc2SIgE2BibTtMgQkDwHz1Ek8uAzuSvK+bGbBZgFSXQG+6WAq+bGAxWRlwn03ttMEEqzIED9uXEcqlbQeqYUPJYOK03RawJkQLTbGwIsoEy8eJ/GgZpVYA4GiQIEYRID10lKHtAzpCTN0T+QwL6QE+6Gd8Z645K4G8rIFU675CYPXAzXb/3EmdMlWBdwWNuf/J5F130VLRd95A+HntKRHo3NllxSy0wl3Vu5XG6HVEQKCNQWjmNweAZ9TystSFPjBCZnU4g8CkInk/UkR34qDeXER+E9kOzbxuXVMhgBJDdD3fFPxuLFkNqGqPEt0k0QAvCkjvx8Hu660T+Q59u57JENJYwq09s3jz273Sj12iwl6lwOr4aSqD3oIQBtR0B+EeRwARIhJcWkhPpCKGFU3sJIf1PhXO+13kWZC0pyagbK0Q+mEu3xFi6vcZhKxJacJiSbDcMZOonMeA9sUtjoF52qIxpPJ3MXRr7CeyFuQhJ3gjF5Y9FaQ4XLhDA7Q+0x0wfDn55K6FkCpEQQhO7a67eDvhbstXRrT6hCfjuYAFCPiDhyyjRYjGcPg+CiT0QIwPAYyi6n/vaJSJpqR7WnqmpQ8tgIQA1EvtQ3frYgvZ2bzLYnyEI0BsyqXm8r5kTCkrOjtqNE8pWrjgq/AUnTebnaMY1wsx8um0Tb0aG9GcF0HM4dbcgU/rDsKRaTP9rxhU5vObnmotckJUZ9rdhpSVv0sCJkueSVvv0G8s8dIZO3h5YAAAAASUVORK5CYII=>