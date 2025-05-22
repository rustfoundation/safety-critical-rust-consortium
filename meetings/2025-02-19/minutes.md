# Safety-Critical Consortium Meeting, 19 February 2025, London, United Kingdom

| Search Key  | Description          |
|-------------|----------------------|
| [todo]      | Action Item          |
| [decision]  | Something decided on |
| [important] | Key information      |

## Attendees

- Tony Aiello
- Pietro Albini
- Espen Albrektsen
- Cristiana Andrei
- Yuri Astrakhan
- Monadic Cat
- Alex Celeste
- Xander Cesari
- Sarah Dietrich
- Scott Enow
- Arnaud Fontaine
- Felix Gilcher
- Julius Gustavsson
- Arthur Hicken
- Markus Hosch
- Takeo Kondo
- Benoit Lietaer
- Pete LeVasseur
- Joel Marcey
- Jordan McQueen
- Drew Miller
- Benjamin Monate
- Walter Pearce
- Joni Pelham
- Orson Pessin
- Christof Petig
- Sasha Pourcelot
- Koppany Pozman
- Samuel Preston
- Alexandru Radovici
- Dan Slipper
- Tyler Stevens
- Zsolt Szépes
- Samuel Tardieu
- Celina Val
- Alexandru Vochescu
- Jonas Wolf

## Set up / opening discussion

Start time: 9:30am

End time: 4pm sharp

Decided not to video/audio record the meeting. [decision]

Chatham house rules? (i.e. do not attribute notes directly to individuals unless
explicitly OK) -> yes. [decision]

Reiterating our goal: support Rust for use in safety-critical software.

109 members in the consortium as of today. [important]

## Membership

Currently, it is free and low friction to join... should it be that easy? Do we
have the right tier structure, etc.? Concern with the current structure: e.g. at
200+ or 300+, will we become unwieldy?

Feedback from the group: the working groups don't feel too crowded at present.

We get some applications that don't seem legit. Concerns around declining folks.

We don't make consensus decisions, so is there any downside to letting folks in?
If there are issues, we can kick them out.

A spam filter and declining folks that don't seem legit seems totally
reasonable.

Should we have a mechanism for vibe checking / removing folks? Currently this is
just Joel.

Does Joel feel OK with this process for now / is it burdensome? -> It's OK for
now.

Litmus test for members being legit -> We should formalize this on github issue
template. [todo]

Should we a priori define what we might think a tier system would look like to
avoid surprising folks? E.g. ‘we reserve the right to "..."'

Since we don't have quorum requirements, this doesn't seem like a big issue. We
can just use the observer / contributor distinction as the "tiers" and go from
there.

The subcommittees also already create a semi-tiered structure.

One of the members commented that they enjoyed how easy it was to join and that
it enabled them to be here. Extra process may have been sufficient to cause a
different outcome here.

If in the future we get to a point where we do voting, it will be contributors
that do the voting. [decision]

Should we have some means to prove that you're a human as an entrance test?

We thought about asking for a link to e.g. github or linkedin or something, but
there are issues (anonymity, etc.)

We should have it as a roadmap item that "we may alter our membership process".

## Membership publicity

Membership is not fully public. Should we publicize the members of the
consortium?  For the subcommittees, the list is public.

Some companies are averse to publicizing that they're using Rust.

Our process is low-barrier enough that they can use a personal account or
something.

Could also have a self-service membership list via markdown table in GitHub?

Do we want to support companies that don't want to publicize their use of Rust?

[Some uncapture discussion here, but ultimately decided...] just continue what
we're doing at present.

We haven't yet had anyone use the private application process (for anonymity).

I think it's fair to state: we will try to keep your email address as private as
possible, but people will see you at meetings and such, and things can happen,
so [...].

Resolution: keep as is for time being, do not publish a list of members.
[decision]

Not being searchable is a major aspect of the anonymization process, e.g.
people can't search their company and figure out their stack via association
with the consortium.

Action items: clear wording about what the SCC will know about you, there's
nothing we can do about it, we'll make a best effort but can't guarantee that,
and to fix the issue template. [todo]

Right now, the members of subcommittees are public. Should we keep this that
way?

I think it's a reasonable barrier to entry for subcommittee members to be
roughly known (doesn't have to be broadcasted), but members at least enumerated
somewhere. [decision]

Anonymous members in subcommittees would be kind of awkward to support from a
committee chair perspective. There should be an ‘identity' that we can post on
the md table. [decision]

Contributors should be "identified" (as applied via the GH issue). [decision]

The main spreadsheet stays private for now. [decision]

## Production of work

GitHub is the defacto place for our work. Does anyone else have any other
positions?

[No dissenting opinions.]

Who are the copyright holders? With no CLA, do we actually pass that copyright?

The slide may need to be edited; it shouldn't be licensed to the foundation,
just following the same IP rules as the foundation.

Everything you contribute here is expected to be under the LICENSE of this repo.
(SCC repo.)

Everyone was OK with the above, which is the current status quo. [decision]

[5 min break]

## Coding guidelines

Large scope goal: producing the coding guidelines.

Notion of safe vs unsafe in the Rust community; not exactly overlapping
concepts, so pamphlet-style material for helping disambiguate these concepts and
giving resources / guides has been the focus so far.

Some initial work to get text down for Learn Unsafe Rust. This is a book by
Google, undertaking how do we talk about `unsafe{}` code, write `unsafe{}` code,
etc. Still in the phases of forming the group and getting our feet under us.

### Near-term priorities

- Wrap-up a few chapters of Learn Unsafe Rust. Useful mechanism to get us
  started working together.
- Scope of coding guidelines, break down tasks, estimate timelines for
  artifacts.
- Take stock of the MISRA Rust document.

Where do we want to store documents? Github. [decision]

### Standards discussion

How can we reference these other documents / standards, given that they are IP?
Can we refer to sections, numbers, etc., e.g. this rule corresponds to MISRA ABC
1.2. Should we be aiming for this? Or should it be standalone / pure?

Same problem in the tooling committee. Should we have a working group that
reaches out to those standardization bodies and communicate with them? Reach out
to ISO, DO, mention rust, work with them, etc. If Rust isn't included now, while
changes are undergoing, is this us missing a train?

Cross-referencing: Addendum documents at the backend of MISRA, MISRA references
CERT, CERT references MISRA. It would be totally normal to do that, and the WG
would be happy to provide the guidance that you need. Trademark usage may be a
workflow that we need to go through, but that permission should be granted. The
exact mapping of X -> Y is the type of thing that we would expect. If it falls
under a headline, it falls under fair use. The group should allow that. David
Wood is a good POC for that. [important]

The airline standards may be more blocked / problematic.

Should still be fair use for headlines. There will be a subjective line when you
start paraphrasing or adding context. We should avoid that. [important]

Ferrocene references the standard sections.

The foundation could buy licenses, but that would be personalized licenses.

Ferrocene has an appendix that has a table that maps the references. You only
care about it as an appendix, here's the table, you can go click the links and
do the mapping. For individual members e.g. from the Project, it may make sense
for the Foundation to help them get access to the standard.

At one point, when wanting to make the SAE JA1020 standard not too
automotive-specific, we were referencing the DO references, to cover aerospace
and automotive, it was difficult.

It would be reasonable for the foundation to ask a lawyer to get broad strokes
of "this is OK", "this is bad", "this is gray".

When we get tooling and coding guidelines... the tooling we write should
reference our guidelines. This tool enforces/validates this part of our coding
guidelines.  Our guidelines should be comparatively reasonable. In practice,
it's less of a problem for coding guidelines.

Caution against trying to rephrase the standards... The standards are very
carefully worded.

There are known examples of it being difficult to reference (quote from)
existing standards when trying to develop reference processes.

We can follow the traceability matrix style process where everything is mapped
back at the end. And furthermore, we can/should work backwards from the
requirements that actually make things safe, then map back to the standards as
references. If we miss something, we can add it in.

The mapping is additionally helpful, but the most helpful thing is how to apply
Rust safely.

Should we be doing more outreach to the safety engineering community?

We have tried including such a mapping table in 1020, and this was the part
which got the most corrections from the safety experts.

Does it require continuous maintenance?

It refers to a specific version of the standards.

What do we want to accomplish with the coding guidelines? If the goal is "write
Rust in a safe, secure way", the standards are not aspirational. Then, if you
want to use the standards, we can later provide the mapping. Any mapping we
provide is likely to be something that most people cannot use. It cannot be
pre-qualified/certified.

We have enough people with safety-critical experience to define and help folks
write Safe Rust. There's a lot of overlap between Safe Rust and safety-critical
Rust. Walter to provide some items here that are the esoteric safe Rust
knowledge. [todo]

Bold idea: most of the standards are built for C. Should we reach out to them
and have them use Rust examples? E.g. one entry/exit -> the question mark
operator.

Regarding ISO26262, Rust has been up for the next version. (2028 is the new
version.) Rust is at least a topic to be included. If we want to make contact
with them, Julius can help with that.

Rust has famously found the third path with many of these things... it would be
nice if we could find the third way for safety-critical, that is even better
that the status quo. The RustConf talk, Safety in an Unsafe world, e.g., there
are many patterns that should make certification much easier. One of our goals
should be to come up with such patterns to make safety critical much easier to
adhere to. We can use the type system to reduce the need for tools (things that
are solved with tools in C land.)

Both subcommittees need this requirement list that we can work out of. Having
that list that Rust developers can understand and also auditors can check... we
almost need this as a precondition. Should we create it at a consortium-global
level?

We shouldn't follow today's standards too closely... they aren't aligned with
what Rust brings. We should focus on the patterns mentioned, showing
aspirational uses of Rust and the type system to create safer software and
writing the guidelines.

You can work around the way the standard is written (given that it was written
with C in mind). e.g. single entry/exit, pointers, etc. Find ways to interpret
it that show that Rust solves the underlying problems, rather than a strict
reading.

This can be part of the mapping, versus the guidelines itself.

e.g. We can have entry/exit rules in Rust be waived in our guidelines, with
justification, in the mapping section.

Fear that we are not a standards org, so if they disagree with us, then it's
lawyers. Then what?

FYI: 62501-8: Rust is highly recommended (without coding standard).

Entry/exit rule actually started from assembly. In C, it has some marginal
value, so it has kind of stuck around despite ASM not being the main thing
anymore.

Should we make another sub-committee for communicating with the external
standards committees?

Entry/exit is an example of how things are a dialog. We also decided that does
not apply to C. This will be factored into 26262. If there are things that are
unreasonable, we can filter these back in and affect the standards. 26262 can be
changed.

We should look at foundational Rust libs, e.g. libcore, is it safe? Does it
violate rules/standards? If so, why? What is considered good practice in Rust
development, and why?

If we miss the deadline for the next revision of the standards, it shouldn't
mean that we are stuck. There is an addendum to 26262 about using OSS in
safety-critical. It is outside of the standard, but still, it exists and
provides guidance.

We should focus on how to prevent misuse of Rust, versus aligning tightly with
existing standards.

Better to communicate with the standards folks so we can get ahead of the ball,
versus just consuming what they wrote.

On libcore, there are exemptions for these things, and it is common practice to
do that.

Back to the top level... what is the goal for the coding guidelines
subcommittee?

Coding guidelines not tied strictly to the standard, but working backwards from
safety-critical Rust done right. Addendum with a matrix that can reference back
to the standards. Also useful patterns for safety-critical, avoiding pitfalls,
etc.

How official are we looking for these documents to be?

If someone follows our guidelines, it should be that it's a superset or at least
very meaningfully part of the certification process.

Automatable coding guidelines, automation for following safety-critical.

If we can make it faster, then people will use it.

We can have something called a Rationale (i.e., the Addendum that has been
proposed) that is a means to show evidence of compliance - allows users to
understand the why and then decide they don't care about it (if appropriate).

It is beneficial if there is a shared understanding of what a good standard when
programming Rust is. If we can establish that industry-wide, it will benefit us
all.

Do we still think we need that sub-committee for talking to standards folks?

Coding guidelines is currently the most upstream committee.

It's almost a political / social problem – to collaborate cross groups and
collaborate with the other standards groups.

Requirements could be brought up to the global consortium level. [todo]

Xander, Joel, Alex C, Orson Pessin, Sarah Dietrich, Arnaud Fontiane, Samuel
Preston volunteer for talking cross-group to other standards groups and/or
the Project. [todo]

Can we exist independently of the standards?

The goal of the group should be to eliminate the exceptions that we specify in
the addendum mapping to the other standards.

There is a bottom-up movement to use Rust, but Rust hasn't been used in 26262.

There's two views, the long-term vision... making Rust safer, and a future with
easier to attain safety-critical properties. Separately, there's the short-term
closing-the-gaps work that can be harder to get an incremental budget for. e.g.
we can work with standards to close known gaps for Rust, e.g. a sentence that
says "Rust Coding Guidelines XYZ covers this, so it is waived", etc.

The goal of the third WG is to make sure that what we do here will be usable by
our customers and the stakeholders that decide what is usable actually take us
into account, making sure that we stay relevant here. Not to be technical, but
doing the groundwork to make sure that we stay relevant to the regulators, etc.

Stamping SAE, ISO, etc. moves the needle from a branding perspective. The gap
analysis is important. Why are you resistant to Rust? We can be the clearing
house for these issues. What are the gaps in tooling, guidelines, etc.

Resistance of industries... Safety industries have things that work. If they can
be better, it requires convincing. We must show what you gain. The goal of this
consortium is to close the gap. We have to work both ways and move them towards
us as well as developing our own processes.

Intended output of Coding Guidelines Subcommittee:

- Coding guidelines, not tied to standard inline in text
- Ideally made automateable with e.g. Clippy lints
- Addendum with some rationale and a rough matrix mapping to standards
- Useful patterns for eliminating safety issues
- Pamphlet for how-to safety-critical for Rust people and how-to Rust for
  safety-critical people.

[lunch break]

## Tooling

We currently meet about once every one to two weeks.

Working on a mapping required tools to standards.

DO-178
ISO 26262
etc.

This requirements table can be brought up into a consortium-level work item.
[decision]

What are the code metrics for Rust? e.g. Cyclomatic complexity, how do we handle
macros?

Need to add more standards to the mapping: medical, industrial?

Outreach for medical expertise? Can we get folks from medical into the
consortium? [todo]

Different vendors have different ideas on what tooling should look like. To some
extent, we need to make sure we enable that competition. The Rust Project is not
necessarily incentivized the same way we are. If we always need to go through
the Rust project, do an RFC, get approval from the Rust Project team, it will
hinder our velocity. Some things will need to go upstream, but as long as we
don't require this upstream support, we should try to pursue standalone
solutions.

There are places we can come to an agreement. e.g. annotation standards (when we
touch source code, how do we expect to annotate it / how do we tell safety
tooling that it is correct). Having this agreement would unlock a lot of things.
`MC/DC` must happen in the upstream Rust project. Identifying which things must
be upstreamed and which things shouldn't would be of value.

Open question: do we develop, do we upstream, do we co-develop, do we fund? For
the tooling committee.

Guidelines for how tools should interoperate would be nice to achieve.

Non-LLVM backends?

GCC rust is still in development, not something to currently consider from a
safety-critical perspective.

Cranelift? I'm curious how it would change the landscape.

It shouldn't make such a big difference – whether we would use the codegen
backend of cranelift or llvm, it shouldn't make a large difference in the
broader ecosystem. Practically speaking, as long as the feature parity for
backends is there, it won't be an issue.

The Rust compiler currently only supports code coverage in a very unstable way,
and it is subject to radical change. We can talk to the compiler team about
this, but there's currently only one person that cares about coverage there and
they are quite busy.

How does the coverage blocker manifest? Is it due to the LLVM backend?

It's a coordination between the backend and fronted; LLVM is orthogonal and
people don't see LLVM as an issue.

The core of the issue is mainly hardware-specific. GCC supports esoteric
hardware. It's a targeting issue.

Supporting specific triples (host-target-os) is a thing that can be supported
and developed on a vendor basis.

Espressif has not been merged upstream yet; you can't just use the regular
toolchain yet.

Open Q: What are the artifacts?

Foundation funding access for initiatives?

Do we have access to that funding for Foundation Initiatives? -> qualified yes

Open Q: Can the Foundation be a vehicle for collective funding of specific
vendor services?

Even just publicizing the needs and identifying gaps can help motivate vendors
to do the work to build things.

Quarterly state of rust tooling report?

Can we make a are-we-safety-critical-yet website?

Whatever the critical gaps for upstream are, will likely be the most upstream
blockers and time lags, so if possible, we could highlight these gaps and could
help communicate these things to upstream / help implement if possible.

We need to make sure that this report does not look like we're shaming the
Project -- because The Project are our friends and allies. We want to avoid
drama and bad PR between SCC and the project, and communicating these things in
the right way is important for that goal. Important to keep in mind that these
gaps are things that we are most incentivized to care about, and the Project has
other priorities. We can help the Project make more informed prioritization
decisions by broadcasting items that are important for safety-critical.

Setting up internal rust ecosystem -> identified tooling gap / barrier to entry.
Using internal crates, docs.rs, internal toolchains, etc. Rust in a box style –
roll out all the internal toolchains/packages/etc. as an internal deployment.

It's a good idea for developer productivity and it is something that should be
pursued, but it may be a better fit under another initiative.

The problem you're going to face here is that while there may be very broad
guidelines that you can establish, you're essentially at the end of the road.
Ultimately, it's integration work, which is always case-by-case specific.

`Stable-MIR` project – something this group can help with – bringing the needs /
the demands into the project could be helpful. Knowing the needs and the
different demands could be huge. Getting the roadmap / understanding (multiple
companies), how can we connect them financially, etc. There are ways to reach
out – don't feel like you're demanding something – the Project wants to grow the
ecosystem.

Is managing software dependencies in the tooling committee?

Yes – SBOM, dependency management, cargo vet, etc.

Is it including the qualification / is the crate suitable for each standard /
checking the evidence for that qualification?

This is in the purview of the tooling committee.

Competence management is another problem for this.

cargo-vet can be used as a tracking and process tool, but it cannot provide the
artifacts that prove that.

Where you're going to fail is the written requirements list. e.g. what are the
requirements for Tokio? There is no process to gather these requirements. The
actual doing of these things is the problem, not the tooling.

All of these are rooted in ISO9001 certifications, which is an organization
certification.

We bump into this with the Rust Project – the Project is not a legal entity, so
it cannot interact with legal processes / documents.

Certification happens in the context of the system, not in isolation.

Can we standardize the storage of this dependency-tracking compliance
information? Where to put references to requirements, etc.

Standardizing this may not be that useful – each company/assessor is different
and you may not end up saving that much time.

Eclipse Score – they do not want to qualify OSS projects in isolation, but
rather they want to say "here's some OSS that has gone through a standardized
testing process" that may help end users undergo certification processes.

This is not a unique process to Rust, and we've done the standardized
requirements format before – it's pain. I don't think we should try to undergo
this.

One of the problems is, you will need a legal entity that will have lawyers that
will have very specific ideas of what to do when things go wrong.

Let's move on since we agree it's out of scope for the tooling committee.

Is there anyone here with concrete tooling needs on a specific schedule / for a
specific deadline that they could share?

Current impression: Automotive has many curiously interested parties, but they
remain curious.

There's also the chicken and egg problem – tooling is cautious because OEMs are
cautious.

There's also the bottom-to-top problem – engineers want to use it, but the
managers have deliverables, the managers have managers, etc.

Speaking of timelines, I could qualify a gazillion things, but I'm waiting on
customers that say they need this. Some issues, e.g. `MC/DC` have a dependency
on `rustc`, which implies time lags.

With the project, sometimes you can only get things done through back channels.

How can we improve that communication? How can we help enable them to help us?
How can we work with them better?

It may depend on what you want from the Rust Project. For some of these things,
it's "do the work". If there's already an invested stakeholder, you need to work
with them. There's a broad range of how you can engage there, sometimes it's
just providing a patch. Practically speaking, what helps is articulating the
need. We need `MC/DC` to build on top of it. We need specification work.
Sometimes money helps. It depends.

Can we get safety-critical representation at one of the Project's meetups?
[todo]

The Project is interested in coming to the best solutions to problems, which can
be at odds with the "here's a patch, please accept!" approach.

No matter what, having a roadmap for how to meet your goals is very useful. If
you're willing to show up and say "hey, I have these priorities, can you make
this happen?" – there is a conversation to be had and they might be able to make
things happen.

Will this also be in the purview of the new Liaison working group?

There's a deadline on May 15. We may want to align with Rust NL for the next
meeting to see if we can connect with the Project better.

How to get the Project more aware of the consortium?

The foundation can help provide a role to champion ideas.

The Project has been trying to work more closely with stakeholders lately, e.g.
RFL folks. This seems to be working, so the question is how can this be
generalized? This could be a LC item. [todo]

Bring to the table: here's what we need, here's why, here's what it enables, and
also: here's what we can do... if we can also bring the willingness to help, it
can be useful. The Project has limited time and resources, so how can we help
them help us?

The Rust Project mostly wants what we want. The problems are mostly around
timelines. (1) communicate properly with the project, and (2) the Project wants
the perfect solution, and is willing to compromise on timelines or features
rather than doing imperfect solutions.

This first order of business should be... establish our own needs. Right now,
the project may be choosing priorities without our input. If we simply provide
these properly, things may shift due to our input – not because of pressure or
anything, but just because we showed that real users care about X.

Potential action item to come up with the list of things that are needed, then
the Liaison committee can figure out how to articulate communicating these
needs.

## Evangelism

People are reluctant to pitch big projects in Rust. Then, for the smaller
projects, they typically hit one snag where there's a gap that exceeds the
budget available to close that gap.

We could be a feeder of data into some "Why Rust" evangelist groups.

Put together a questionnaire for this? [todo]

## FLS

Ferrous has committed to contributing the FLS to the Rust Project. Joint stmt to
come. There is a Rust goal for this.

How does this integrate with t-spec? In the first half of this year, we will
have a published spec in the latter half of 2025?

Yes, that is the intended goal.

Will t-spec maintain both the reference and FLS for the time being?

Yes, for the time being, but we want to merge these over time.

This is a potential success story of actively communicating with the Project. We
should invest more in pathways shaped like this in the future.

Will the two documents be synchronized? For example, Rust 2024 – what happens
there?

Practically speaking, there will probably be differences for very practical
reasons. Is the Rust Project going to commit to having an updated version of the
spec at release time? That remains to be seen.

We are going to need to find a way to trigger notifications when the content of
the reference changes so that we can update accordingly.

This is an example of where we need to show our requirements, because we have
very specific requirements here. Specifically, stability requirements.

Call for contributions of internal coding guidelines from companies to the SCC?

## Meeting End / Wrapup

Feedback: The lack of breakouts was a good thing, the unified session was useful
and there wasn't anything I wanted to miss. +1 +1 +1 +1

Was this enough time? Do we need a second day? [todo]

Initially assumed ~every 6mo cadence – RustConf, RustNL; however, currently
leaning towards meeting at RustNL... What does everyone think?

Ship it! (Rust Week / NL in May.) [decision] (Rust Week / RustNL)

Monday before the conference may be a good day? [important]

[end of meeting, 3:58pm]
