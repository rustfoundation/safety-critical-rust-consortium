# Safety Critical Consortium Meeting, 10 September 2024, Montreal, Quebec, Canada

Summary of meeting [here](./summary.md).

## Logistics

10 September 2024, 9 am - 4 pm EDT
Lunch: 12:30–1:30PM EDT.

The meeting will be held on the front-end of RustConf 2024 with both an in-person and virtual component. The in-person room is limited to 25 people, so that will primarily be made up of original consortium members.
In person

Hôtel Gault, 449 Rue Sainte-Hélène, Montréal, QC H2Y 2K9, Canada
Virtual/Remote
https://meet.google.com/ihc-xuwx-ecb

## Agenda

- Plan for the day
  - Recording the meeting
  - Note taking - Jordan McQueen (thank you!)
  -  Virtual attendees asking questions
- Introductions
  - Why are you here?
  - Why do you care about safety critical applications and languages that support them?
- Governance and goals
  - Mission
  - Decision making
  - Membership
  - Sharing Confidential information
  - Goals
- Potential Work Items
- Supply Chain Management
- What’s Next?

## Meeting Prep Info

### Governance

#### Examples

- Rust’s, obviously: https://www.rust-lang.org/governance
- More than we probably need, but good: https://www.eclipse.org/org/documents/
- Interesting reading: https://widgets.weforum.org/blockchain-toolkit/pdf/consortium-governance.pdf

#### Mission Statement

What is the purpose of this consortium?

#### Goals

- What specific, measurable goals does the consortium want to achieve?
- What is our timeline?
- Possible proposed goals
  - BHAG (Big Hairy Audacious Goal): Make and keep rustc the safest open source compiler
  - Create industry-standard best practices and tools: how do I write code in Rust, using rustc and other tools, to meet my product’s safety goals. For example, I want to ship ASIL-B software in vehicles following ISO 26262.
  - Forming and holding relationships with other players in the Rust safety scene
    - The Rust Project
    - Eclipse Rust SiG
    - MISRA
    - [AUTOSAR Working Group - Safety](https://www.autosar.org/news-events/detail?tx_news_pi1%5Baction%5D=detail&tx_news_pi1%5Bcontroller%5D=News&tx_news_pi1%5Bnews%5D=139&cHash=b332c8babc7aad27723ab939f9723fc6)
    - SAE JA 1020 [(SAfEr Rust Task Force)](https://standardsworks.sae.org/standards-committees/safer-rust-task-force)
  - Deduplication of efforts
  - Discuss safety related topics
  - Coding and Style recommendations, with potential integration into mainline Rust
  - Proposals and RFCs for mainline Rust changes or additional tools
  - Find intersections between safety- and non-safety related concerns on Rust
    - E.g. timing analysis is very important in safety, but has a lot of other places where it makes sense

#### Roles and Responsibilities

- Do we need formal titles like chair, secretary, etc.?
- What’s the leadership structure of the group?

#### Decision making process

Consensus, voting, quorum?

#### Membership

- How do we handle who can be members of the consortium?
- Only accessible to Foundation members?
  - De-facto not in effect currently
  - Might be seen as pay to play
  - Could lead to formation of other groups
  - Is the safety group a good measure to recruit new members for the Rust Foundation?
- Open to all?
  - Gives a lot legitimacy to the group
  - Enables easier changes in the Roster
  - Avoids a situation where a contributing member needs to leave if their company leaves the Foundation - that can be quite hazardous to projects.
- Do we limit membership numbers?
- What is the benefit for people to join the consortium? Why would they do it?
- How much time commitment is it for members? What do members actually have to do? What is their responsibility?

#### Meeting Structure

How often, virtual/in-person, minutes publishing?

#### Communication Channels

Zulip, email, anything else?

#### Code of Conduct

- Do we want an official code of conduct for the consortium?
- How do we handle conflict resolution?

#### Confidential Information

- How do we handle the sharing of IP and Confidential information?
- Do we need a formal process across all the members for this?

#### Uncategorized Items

- What is the exact relationship between this group and the Rust project?
- Which standards will be covered?
  - MISRA?
  - ISO26262?
  - IEC61508
  - DO-178C
  - IEC 62304
  - EN 50128
  - A/SPICE-process?
- Will we engage in standards drafting (e.g. sending delegates)?
- What is our working style?
  - Open Source Licensing, Apache 2.0/MIT style licensing.
  - Only discuss topics applying to open codebases and impacting Rust codebases
  - Preferably work on https://github.com/rust-lang or https://github.com/rustfoundation, to bring the topic of safety to the main Rust project


## Write-in questions

1. Can someone link to the Zulip channel? 
    https://rust-lang.zulipchat.com/#narrow/stream/445688-safety-critical-consortium/
2. Can the coding guidelines standard live in the Rust Foundation?

## Meeting Minutes

### Attendees

#### In-Person

- Joel Marcey (Rust Foundation)
- Walter Pearce (Rust Foundation)
- Tony Aiello (AdaCore)
- Filip Gajowniczek (AdaCore)
- Fabrice Derepas (Trust-in-soft)
- Daniel Frasinelli (Veecle)
- Erik Jonkers (Tweede Golf)
- Julius Gustavasson (Volvo)
- Frederic Ameye (Ampere)
- David Sankel (Adobe)
- Jordan McQueen (Woven by Toyota)
- JF Bastien (Woven by Toyota)
- Florian Gilcher (Ferrous Systems)
- Peter LeVasseur (Eclipse uProtocol)
- Alexandru Radovici (OxidOS)
- Alexandru Vochescu (OxidOS)
- Orson Pessin (OxidOS)
- Nick DeMarco (Adobe)
- Zsolt Szepes (HighTec EDV)
- Koppany Pazman (HighTec EDV)

#### Virtual

- Alex Celeste (Perforce)
- Arnaud Fontaine (Airbus)
- Benoit Lietaer (SpaceApps)
- Christof Petig (Aptiv)
- Daniel Windham (Atlas Computing)
- Jeffrey Marshall (Lynx)
- Kyle Heins (Cognizant)
- Lachezar Lechev (Lechev.space)
- Rizet Nadege (AMPERE)
- Sameer Gupta (NixOS)
- Samuel Tardieu (Telecom Paris)
- Yuta Matsuyama (Techfund)


### Notes

Starting with introductions. In person.

- Joel Marcey director of technology at Rust Foundation, helping manage consortium. Not leading, just managing. Care about safety to ensure Rust progresses to be able to be utilized in as many areas as possible.
- Walter Pierce, security at Rust Foundation. Shepherd, help out. Former life did 15 years of consulting in safety spaces, automotive and power.
- Tony Aiello, AdaCore. Product manager for Rust product. Want to see success in high integrity market. Interested in high integrity languages, started with Ada.
- Filip Gajowniczek, AdaCore, interested in safety-critical dev, technical account mgr, works w/ feds and gov’t customers, interested in representing those customers.
- Fabrice Derepas, Trust in Soft founder, researcher, nuclear industry, started > 10 years ago, interested in formal methods for software dev processes, works with phones, IOT, watches, etc. Today, mostly using C/C++ on firmware, hypervisor, etc., but recently switching to Rust, wanting to develop a new frontend with aims of formal methods.
- Daniel Frassinelli, from Veecle, is looking at starting a safety-critical team internally, developing a Rust runtime for automotive and safety critical usage. Interested in understanding next steps.
- Erik Jonkers, Tweede golf, based in NLD, not yet active in safety-critical apps, but recently started rust implementations (OpenADR) in the energy domain, participation here is forward-looking.
- Julius Gustavsson, system architect and team lead at Volvo Cars, developed ECU from scratch in Rust, now in production. Polestar 3 and EX90. First test run for Rust. Only QM so far but looking to expand our efforts to ASIL levels as well.
- Frédéric Ameye, Ampere (Renault), car maker, pushed Rust for QM in many places. Envisioning future more Rust in safety ECUs. Include Autosar or other RTOS. Just starting on this journey.
- David Sankel, from Adobe, Principal Scientist, acrobat, creative software, active in C++ standardization, focused on safety (security)
- Jordan McQueen from Woven by Toyota, helped introduce Rust at AWS. Background in security and distributed systems. Interested in safety critical adoption in automotive. Find ways to collaborate. Certification, ISO26262.
- JF Bastien from Woven by Toyota, chair evolution of C++ language, likes languages, not married to C++. Looking to find a path forward to make Rust a realistic choice for safety-critical. Sad about the C/C++ safety status. Expensive and slow, but it works. Hope here is to collectively find a way to do safety well in Rust, but also while helping other communities. Hoping to lead by example here.
- Florian Gilcher, from Ferrous Systems, RF, started conversation with safety critical rust 5 years ago, qualified the Rust compiler for ISO26262, totally open source including safety materials, not interested in subsetting the language – all safety changes should be upstreamed to rustc. Eclipse Rust SiG lead.
- Peter LeVasseur, representing eclipse uProtocol, working for 9-10 mos or so, incubated within GM, the idea being that software together in the vehicle is difficult, having an STD framework to connect in-vehicle to cloud, mobile, etc. helps alleviate this pain, supporting multiple protocols, worked on apps teams and automotive for a decade, interested in solving this problem.
- Alex Radovici, Oxidos, background in OS and compilers, building alternative to AUTOSAR classic, looking to avoid duplication of safety-critical code, interested in open source, wants to share work here.
- Alex Vochescu, Oxidos, CS background, architecture, also automotive, interested in use cases for Rust in automotive. 

Online:

[Virtual folks were muted and video off, some troubleshooting to fix ongoing.]

Will follow-up with virtual intros after troubleshooting audio.

What do we want to do? -> variety of interest from the attendees.

Why is this WG in the foundation instead of in the project? (This question will come up, we should have a clear answer.)

Florian: What are our shared pain points?

Safety critical applications follow standards, and if someone is injured, there is an investigation and legal liabilities. Individual companies can solve these issues on their own, but there’s value in collaborating on inter-validated solutions.

Project is more focused on the language itself, but the foundation may have a broader scope: tooling, standard, [...]. The Linux Foundation is not just about Linux. E.g. Open SSF is an initiative very separate from Linux, but very compelling.

Being in the foundation lets us look outside the project, and be a more neutral arbiter. The foundation’s mission is to support the project, but also to support the ecosystem and community.

Very broad questions about things that are implicit knowledge for some. E.g. how to properly implement, validate, review unsafe code. We don’t have good manuals for unsafe code. What should you do, not do, etc. e.g. for ISO26262, review guidelines for rust code. This can possibly be written in a way to transcend specific regulatory standards. 

Coding guidelines are valuable. -> divergence between different uses?

You cannot write certified C/C++ without deviations, generally speaking.

If we want to create Rust guidelines, we may need to be more prescriptive for safety-critical contexts.

AUTOSAR/MISRA mistake -> didn’t work with tooling vendors early on. Unprovable rules, etc. Implementable is an important quality of rules.

When you push Rust in safety-critical environments, people ask “what about MISRA/AUTOSAR, etc.” -> Therefore I started looking at SAE JA1020(?). We need guidelines on how to use Rust in a safety-critical environment to flatten the adoption costs. Need to join the [Safer Rust Task Force](https://standardsworks.sae.org/standards-committees/safer-rust-task-force) to get access to the JA1020 draft.

Why outside the project? -> The Project is a research project, but in safety-critical, we use a subset of the language. In safety critical space, we need to not fail. The safety-critical space is very narrow compared to the general software space.

We can get access for folks here to SAE JA1020.

[continuing virtual intros]

- Christof Petig, co-chair of J1020, work at Aptiv, looking to introduce Rust to the industry, was looking for a highly-credible framework for coding guidelines -> therefore SAE (credibility > visibility)
- Alex Celeste, tool vendor, Perforce, Helix QAC, MISRA-C WG, interested in exploring into Rust, interested in contributing to rules recommendations.
- Arnaud Fontaine, working at Airbus, sanitizers, joined last year, author of the [ANSSI rules](https://github.com/ANSSI-FR/rust-guide), SAE taskforce (?), working on the public secure guidelines, as of today not ready for safety critical development, but making progress [...]
- Daniel Windham, Atlas Computing, formal methods/verification, how can we speed up verification in rust? Want to help folks not spending 99% of their time formally validating, interested in tech transfer of formal methods within Rust.
- Jeff Marshall, Lynx, builds hypervisor, RTOS, interested in Rust internally, customers also writing Rust / want to write Rust – how do we get to Rust being a credible replacement?
- Kyle Heins, Cognizant (was Belcan, acquired) – aviation sector, DO178B, how can we leverage or encourage adoption in aviation?
- Lachezar Lechev, Lechev.space, Aerospace Industry, Co-founder, looking at increasing Rust adoption.
- Samir Gupta, NixOS, embedded Rust operating systems, curious about leveraging rust for secure OSes.
- Samuel Tardieu, Autonomous Critical and Embedded Systems (ACES) team at Telecom Paris, engineering school and public research center in France, formal methods for software and hardware design, we use Rust a lot, also teaching. Interested in Rust certification and research.
- Fabrice: Coming from C/C++, the standard is useful. If someone dies, we want to know why. Interested if the compiler is correct / following the norm. If the specification is embedded in the compiler itself, we have to understand the complete toolchain. OK, we don’t have a standard, but under the foundation, we have a community and it can act as an umbrella that we all operate under.

Joel: Do we need a spec?

Florian: All standards require that the requirements are written down. The least is to have a language reference from each compiler version.

The point of the original specification is to specify the rustc compiler.

JF: In C/C++ the stdlib is also specified. Do we also want to do that for libcore? This doesn’t scale to crates, so we need to find a way to manage that.

David: Having a specification is not a prereq for us (Adobe), but it is useful for failure analysis in terms of where in the chain did this fail? Not a show stopper, but it is plus alpha. At Adobe, “what’s our safety plan?” -> our plan cannot be “just use Rust”. If we use a vulnerable crate, this is another vector for attacks. C/C++ is very painful to update third party deps, so it’s effectively a new vector. If we have recommended processes / guidelines to solve the safety problem, that’s a useful outcome that would make a difference for us in terms of “what’s our safety plan?”

Tony: We need a specification of the language or of rustc. Absent a statement of what the tool is supposed to do, I don’t see how we can have qualification. Any SC process, e.g. 26262, demands qualified tools. Having a specification is essential.

Daniel: It’s not just the language, what Rust is trying to do is replace 35-40 years of processes, learning, etc. in the span of 5 years. How do you manage deps, how do you deploy OSS, pull OSS, etc. – so many questions, but still open. Identify all the different components required (important one is spec), and prioritize and create a plan of execution for all of these initiatives.

Florian: Suggest to split off supply chain mgmt and follow-up as agenda point.

Goals of the specification? A good high-quality specification allows you to re-engineer the tool. There’s pushback on the spec because of the possibility to create a competing compiler(?).

Problem: proliferation of specification work. (at least 2 such projects)

Message back to project: Is the specification team in the Rust project that people are putting this in jet engines? We need a committed and hard timeline for the spec. The officiality carries weight, and there are safety-critical use cases that are downstream.

Alex: It’s a research project, so they won’t commit to a timeline. The spec may or may not be sufficient for safety critical. We shouldn’t expect this from the project. They need to cover all the use cases, push the language further, consensus-oriented. We are the small users, we need the spec, we are the ones putting it into jet engines.

Tony: AdaCore is not trying to rebuild rustc. Back to the spec: I’ve heard from folks that until Rust is an ISO standard, we can’t use it, but I would prefer we do not go that route. I suggest we take this spec development seriously, and even if it isn’t ISO, it should have credibility and be adopted/supported. It should be possible to build a second compiler, but not necessary.

Florian: rustc and rust-analyzer are already effectively separate compilers. -> the multiple compiler problem already exists.

David: It’s essential that the folks changing the language are also working on the specification. Therefore, it seems to imply it needs to be a part of the project if it’s going to be a successful specification.

Joel: Perhaps the spec can live outside the project, but we 100% need folks working on the language involved.

ISO standard X -> what we need is confidence in the tools, how the highest safety standards are working, deterministic computation, testing, this is where the confidence comes in, not from the standard. You don’t need an ISO standard, only confidence.

Florian: Agreed. This is probably the room with most people experienced with ISO standards. The Rust Project is impressive and big, false respect -> they think the Project can solve everything, but this leads to misunderstood needs, it will not do the endeavor any good if we’re too laissez faire about how the specification is developed.

David: ISO Specification -> spoke to Bjarne about this -> “Why did you make it ISO?” -> He said it was very easy; Boeing and others required ISO. These days, there are other options. JTC is a combo of ISO and IEC; very antiquated. There are many ways to get in. There are more modern standardization bodies, so we shouldn't focus on ISO. The real question is “do we make a standard?”

Joel: We should work backwards from the requirements of the industry members here. What are the bare minimum requirements to use Rust in safety critical? Can we have a uniform usage of this? How do we get there?

Tony: From the perspective of A&D, customers need an ecosystem of tools -> compiler, coding standard, checker for the standard, clippy, MC/DC, static analysis, etc. Many industry players, e.g. aerospace, haven’t gotten past “can we instantiate this whole toolchain in Rust?” Anything we can do in this room to chip away at these problems -> ++. We want to give our customers tools that we have confidence in that they do what they’re supposed to do, supply chain mgmt solved, etc.

Florian: “Is the rust compiler a form of formal verification?” is a question I’ve always wanted an answer for. 

JF: “What do we need” -> the answer will be different per industry. For example, defect management. You might ship code from 2-3 years old toolchain. Later, defects may be found. You can go to your toolchain provider to understand your defect posture. Managing these defects is pretty onerous. We should collaborate on this. Look at all the defects, collaborate on impact and analysis. This doesn’t seem appropriate for the project. Having people understand how rustc/etc. works and analyze the impact of incoming defects. CVEs exist, but are sort of useless. As a user of the tools, I need someone to manage the defects.

Florian: The compiler toolchain vendor use cases are a very specific one. May be worth a specific WG.

JF: AFAIK, you don’t need ISO for the specification/standard. This may depend on the industry, however. If we need an actual standard, it may be useful leaving that door open. I don’t recommend ISO, but IEEE seems reasonable. Until we have a concrete requirement, we shouldn’t go down the standardization path.

Tony: Vendor lock-in is a common talking point here, but rushing towards a standard seems unneeded.

Florian: Is anyone aware of any place where ISO is mandated? Other than one, I am not aware of any. (Japanese gov’t -> language use.) Historically speaking, C/C++ got standardized because of competing implementations and to find a common ground. [non sq] How do we guide users in those specific environments – groups of hundreds implementing software at a consistent quality. 

Daniel: ISO may not be important, but an alternative approach to solve the same goal is. V model.

Alex: Knowing a timeline for when the full V model will be applicable to rust is difficult.

Joel: Maybe if we just combine all the work of everyone in this room, we’re already pretty close?

Walter: The Foundation gives the method to get around NDAs, share the information. This is the place we can funnel info and setup projects.

Fred: From a security perspective, real vs non-real security. If we don’t have a credible organization stamp, it may be difficult to push (from a company perspective).

Alex: If we have the timelines and clear steps, an assessor can certify that.

Joel: ISO stamp is a C-suite pleaser. The consortium community-based approach is a paradigm shift.

Florian: I know there’s a frequent want for Foundations to do that work themselves; the biggest problem I see is the misunderstanding that qualification is just all the paperwork. Liability is also key – if the Rust Foundation accepts that liability and goes bust, we’ve all got a problem. The RF should remain liability free.

Tony: It’s really expensive to qualify a compiler, and maintain it. New version, use cases, new switches, etc. – very expensive. Transferring that burden to the RF seems unreasonable. We should find the points of commonality that should exist at the RF that are undifferentiated heavy lifting so that we can all be more efficient. You don’t want a situation where Volvo is stuck on some funky subset of Rust toolchain. We should work off the same spec, understand/agree what the language means.

JF: In C++, there’s the problem where what set of CLI flags you end up using subset the language, and is not standardized cross-vendor. E.g. -fnoexpections vs not. Your vendor decides what you get to use. We should avoid that. What to subset – we should agree on that. Defect management gets easier if we get this right.

Florian: Rust considers compiler flags as part of its interface. Divergence from there needs to be discussed, particularly divergence from the Rust language makes you lose the trademark. There’s already a tighter package there, needs to be discussed.

Arnaud: In aviation, we are responsible to convince the authorities. We are doing the job with some help. We can rely on AdaCore, e.g. if they have some qualification, we can use some prepared kits from vendors, recommendations -> everyone can benefit from this, reuse it. You cannot sell a qualified toolchain. You cannot just put a stamp. It doesn’t mean that it is qualified for everyone forever, it’s a case-by-case qualification process.

[10m break]

Joel: Icebreaker: Would be interesting to know from some of the end users – what are the gaps in Rust that prevent you from actually using it in your software?

Alex: Yes, Rust is great, memory safe, it’s fantastic, but… we have existing software (C headers, libs, etc.) – interoperability is one of the first questions. We did a POC and yeah, you can interop with vendor-specific libraries, but this is at a POC level. Having guidelines for interop and unsafe rust would be good here.

Joel: Rust-C interop initiative is being spun up now.

Joel: There are a lot of sub initiatives (security, interop, spec work) that kind of fold into this one.

JF: line coverage and MC/DC coverage. We have to know the code that we write is being executed, so having these tools is important. Defect management. The specification is ~kindof required. You could probably get away without it, but that’s not a good idea. The spec covers the language, we probably want to cover parts of the library… You also want a spec for the tool itself. E.g. static analysis tool X produces output Y and you use it like this.

Julius: Same things, but also preface that we’ve only been doing QM so far. We have yet to do an in depth investigation on what exactly is lacking for tool qualification. Documentation Generation, SBOM, supply chain mgmt would be nice to have in place as a common good. Cargo, out of the box will generate a SBOM but it will have more than you actually end up shipping / have linked in the final binary.

Walter: Cargo doesn’t do LTO / dead code analysis. If we could do SBOM after LTO, this would fix that.

JF: We talk about tooling, static analysis, etc. – we want to create an ecosystem, but we may want to standardize the interfaces for some of this. E.g. the meta usage of the tool. In C++, you always need deviations in MISRA for example, how you specify this is not standardized – every tool does it its own way. At a minimum if we had a standardized method of deviation, that would be useful.

Julius: We shouldn’t forget that we are doing this QM component, just following the standard cargo toolchain, at a standard Rust level, the quality is not comparable to e.g. ASIL-certified things. The quality is so much higher, there is no comparison. Rust found a third path towards safety and quality – we should find similar ways in this safety critical consortium. We should not blindly follow what was done before, what is plaguing C/C++, but forge a new path, motivate why these processes are actually needed, focus on higher order bits.

Tony: Certification of the standard library. Cost is high. Much more nebulous thing: fear of being the first mover. esp. in aerospace and defense.

Fred: There is a need from big companies to announce plans to do more safety critical work in Rust. We will go into Rust for safety-critical to ASIL-D, even have a strategy to make it mandatory in some places by 2028.

JF: Something else we need, a workforce that knows how to do this stuff. (Rust programmers in a safety critical setting.) Training, growing the workforce.

Walter: The #1 question is, where is the education pipeline?

JF: In the safety industry, you have to show you have a safety mindset. Part of that is assessment of your workforces’ skills, have continuous training, etc. This isn’t necessarily a consortium requirement, but maybe some guidance or syllabus of training materials for safety.

Florian: A syllabus is much more important in the beginning, having a consistent program.

Fred: From our experience, starting with a few people, after making Rust mandatory in some parts, 150 people were trained in Rust, and some of them did not like switching, but ended up really liking it. Training is no longer an issue. There are many companies doing training with high quality experts, and so on. The business objective of going into Rust is clear. I was contacted by another company that thought they would lose business by not going into Rust. Training hasn’t been a blocker in my experience.

Julius: Same here.

Florian: Convincing engineers versus convincing managers of a six-figure investment are very different things.

Alex: We introduced Rust in the University 3 years ago. Embedded, OS, etc.

Fred: We worked on a business plan for Rust at Rust Netherlands. It’s difficult to measure the gains from increased productivity and lower defect rates.

Florian: One of the problems, Lars going on stage recently, cost savings, efficiency, time to market is not a concrete selling point. We need to make it very tangible why Rust achieves these. Reverse Mexican standoff – everyone waiting for results from other groups.

Fred: Need to improve marketing of gains for safety-critical Rust.

Alex: Unless someone manages to create these tools, e.g. this consortium, it’s more expensive. It’s a higher cost for us to convince assessors. For example, in MISRA, it says one entry one exit. Rust question mark -> 😞. We need to deduplicate this work and amend the standard or fix these issues as applied to Rust.

Florian: The initial Rust projects going through certification will be wildly expensive.

Tony: Starting with QM and slowly climbing up the ladder is a good approach. Creating a plan for Rust strategy and rollout is useful because it allows us to proactively invest in accordance with your timeline.

Alex: We need to go together to fix the applications of these standards to Rust. If we go alone, the small companies cannot talk to ISO and OEMs to fix these issues. If we go together with a unified plan, it will be more efficient.

Tony: Were it to happen, that would be a fantastic result. With Spark, we had an ASIL-D experience with a customer that is going to show cost savings. It may be better for OEMs to quasi-individually adjust their processes. 

Alex: My personal opinion is that most automotive OEMs will not do this.

Julius: It’s been an uphill battle, but we’re starting to get data – fault reports, getting team members up to speed w/o impacting quality – everything is adding to the idea that there’s a huge opportunity on warranty and maintenance costs. Management is starting to notice this.

JF: In trying to find that list of things that are needed, you said you’re trying to target a smaller ECU now… did you have issues with code size, architecture support, etc?

Cortex M4

Julius: Code size… it fits… 😂

Florian: Toolchain vendors more open to giving support if there are multiple OEMs that are committed or speaking as a group. Perhaps we can use this group as a speaking platform.

Peter: Case study of a C++ codebase -> on the order of 15% of the bugs would be eliminated by Rust. This group can publish these kind of studies to improve the messaging.

Alex: The project and community has done a good job of communicating this. The big issue is certification. It’s a complete blocker. The scope of this consortium to help here as opposed to popularizing Rust.

Joel: Popularization can be a second-order effect of safety work we do.

Fred: On the cost of qualification, there will be a transition plan – on the same ECU, AUTOSAR-based C and Rust code. This will have a cost of two toolchains. We are thinking about how we want to mitigate this. Qualification of both toolchains.

Model-based design… there seems to be a trend for this to be replaced by code written by humans. (Simulink and Matlab talent pool is small.) With Rust, there should be less things to prove here.

David: We’ve talked about spec, coding guidelines, qualifications… perhaps we should focus on coding guidelines? It seems like that would fill a huge gap.

JF: Not MISRA.

Florian: 1020 is a good document, not by any means complete…

On MISRA… a number of people from MISRA has been reached out… bad experience with MISRA C++ and its community.

Eclipse Rust is interested in contributing to this. We have a little plan about an unsafe document that we could discuss in the future.

JF: If we focus on getting a coding standard out there, and link all the other things into it, that’s a nice start I think. Start somewhere; we have a long shopping list.

Joel: Some things on this shopping list may already be completed by some of the people in this room. We definitely want to tackle something that feels tenable. Specification … maybe not first.

Walter: +1 to coding guidelines. E.g. you must do SBOMs, you must do … X

Julius: Regarding coding guidelines… has there been any study on each of these MISRA rules in 1020, should they actually apply to rust? We shouldn’t do these just because they’ve always been done this way.

Florian: One of the things I’ve been trying to get anyone who writes coding guidelines… do not transfer MISRA to rust. Guidelines will help to have a standardized mechanism for creating and applying lints. Even outside of safety critical, this has huge boons.

Alex: We did an applicability of MISRA C to Rust study -> how many of the rules apply? Of the 200(?) or something rules, about 200 cannot be applied, leaving ~90(?) rules remaining.

We started at looking ISO26262, going through each and every recommendation and trying to map it to Rust and make sense of it, DO-178 and DO-332, [...]

David: It sounds like we’ve already done a lot of work on these coding guidelines, it would be good to collect that into a body of knowledge in this group and action it.

How to get our coding guidelines document going?

Florian: Some companies has internal guidelines on this -> e.g. Google. Instead of starting fresh, can we get a large company to disclose theirs and build from that rather than start from scratch?

Joel: Three potential sources: Google, MISRA, and JA1020. Could we use those three sources and become the umbrella + add to it? How do we get started?

David: Call for volunteers to review and contribute and go from there.

[Volunteers’ names collected.]

Circling back: What’s the mission of the consortium? Do we need a mission?

David: When you need a mission, you really need it. +1 for having a mission.

JF: What’s the mission of the Rust Foundation?

Joel: Originally, to support the project. Now: to support the project, ecosystem, and supporting the maintainers.

JF: Folks in the consortium may not be aligned with the RF mission. To me, Rust is a means to an end.

Joel: Nurturing the ecosystem is a direct fit for the consortium.

David: It’s not about growing usage of Rust -> improve the suitability of Rust for safety critical use.

JF: (Purely hypothetically) I wouldn’t want this group to go to the US Gov and mandate Rust usage. I want the mission to further making Rust be the best tool for the job.

Fabrice: We need to aggregate and synchronize what we are doing.

JF: The way I pitched it before is to look at what other languages have done and speed run it. C++ etc. is messy because it’s been accreted over many many years. We can speed run that here in rust.

Joel: Any other comments on mission?

JF: We can’t be imposing on the Rust Project, things that are unreasonable to ask.

Joel: Given this list of things to improve suitability of Rust in safety critical, one of our questions is “who’s going to pay for it?” 

Florian: Coming back to “too much respect for the Rust project”, if we send an engineer to the Rust Project, we need a commitment that their time will be well used. For example, if we want to contribute things to the compiler, we should have a reasonable expectation that the changes will be received and integrated.

Joel: That’s going to be a challenge.

Florian: It would be useful to pick something where we need to work with the project to develop the relationship. It’s to our benefit to have a strong stance on our side when something needs doing.

Joel: Question to folks in the room. What’s your timeline for rust safety-critical readiness?

Alex: Yesterday.

Florian: It’s becoming an observed issue that Rust is moving too slow in this space. I think the project is making some decisions that will further delay this. Rewriting the spec, for example.

Alex: Personal opinion here, if we really want to see Rust in this industry, we need to move now.

David: Two things. 1) Would be useful to set a timeline for the coding guidelines. 6 months or something, for clear expectations. 2) Specification of the language. We need clarity from the specification folks what their timeline is. Is a year unreasonable?

Joel [on the specification team]: I can give you an answer you won’t be happy with. We’re trying to convert the Rust reference into the specification at present. The goal is to rename (metaphorically) the reference to the spec this year. I’m not sure if we’ll meet that EOY goal, but once it’s hit, enter maintenance mode.

Alex: Why not use an existing spec? e.g. ferrous

Joel: Three options.

Ferrocene Spec, seemed obv/clear choice.
Re-tool the reference into the spec.
Write a spec from scratch.

Started with 3, but realized it was going to be long. Consensus from the t-spec team was that people would be more amenable to using the reference as a base.

This is the first time where the end goal isn’t an improvement to the project in and of itself. The spec impacts many entities outside of the project.

Florian: From our side, we have not felt that this was not a very technical decision. Several experienced tech writers have held off from participating in that project for this reason. It is unclear if the spec the rust project is currently writing will be of use to us. We are currently the only users of a rust spec. I’m surprised the project doesn’t engage more with us.

David: Taking the rust reference manual and evolving it into a spec seems reasonable. The timeline is not unreasonable – even slipping by 6 months, that’s not unreasonable.

Joel: I’m speaking as a member of the t-spec team. The ferrocene spec is a guide into what we’re going to be doing with the spec. We want to get to parity with the ferrocene spec. We’re trying to utilize format and structure to be the path forward.

Joel: Could we as a consortium, put pressure to change tactics? It’s not too late.

Alex: Could we use the FLS as the spec until the project produces and later swap?

Joel: We could do that, and if we do, the t-spec team would have to adapt to that reality.

Walter: 

Florian: 

Joel: We need to do what’s best for this consortium. We don’t need to be beholden to what t-spec is doing.

Fabrice: We are using FLS, then maybe hopefully in 2-3-4 years, we can transition to another spec.

David: With the t-spec team, how far along are they actually right now?

Joel: T-spec team formed, but didn’t have a lot of time to invest. The foundation hired someone to get involved. Started couple of months ago w/ the hired help.

David: It’s essential that we have a spec that the project is committed to.

Joel: We can bring this to the leadership council.

Florian: Just because it’s called the FLS, it was to avoid clash with the Rust name. There’s undeniable costs to anyone already using that to switch over… we should ask the question: how much cost do we inflict on the ecosystem by not adopting this now?

Alex: We should talk to the team and see if they can adopt that. We want to work with them and not against them. As an industry user, I really need this.

Arnaud: Is there a specific use for the t-spec team’s spec?

Joel: There was an RFC written to cover this: (https://rust-lang.github.io/rfcs/3355-rust-spec.html) (1) have an official spec for rustc, (2) have a document that could be used in safety-critical industries.

David: One way we can resolve this is to have this body make a recommendation to the leadership team on what to do here. I think we’re not ready to do that yet, we can invite the t-spec team and ferrocene to get informed on this, then make a recommendation to the leadership team because we need to make a decision.

Florian: We won’t make that argument as the Ferrocene project; we’re just going to use and maintain it until we can replace it.

Joel: It feels like we’re either neutral or positive to recommending the FLS as the base for the consortium. We can take that to t-spec and try to figure out how to go forward.

Alex: I don’t think we should immediately go to the leadership council.

Joel: I meet with t-spec every thursday. I’m going to bring the consortium’s perspective to the next meeting, have a heartfelt meeting and see where it goes.

David: We can form an opinion in this body, if we’re well informed.

Alex: Agreed.

JF: My understanding from being a part of one of the t-spec meeting is that FLS isn’t mechanized and doesn’t cover everything, which is another part. Instead of saying let’s take the Ferrous spec, make it the Rust spec, they wanted to start from scratch. Now, it sounds like they’re taking the reference. What’s the output of taking the reference? English language or mechanized?

Joel: Mechanized with annotations.

JF: Mechanized is doable, but very difficult. Their goal is too broad. We have a thing today.

Joel: They don’t see the urgency. We’re not necessarily beholden to a timeline.

JF: That’s where Alex is right; it’s a research project. /We/ are talking about production. These two things are at odds, but reconcilable.

Florian: We have asked about an example of those inconsistencies, but have not been shown anything tangible yet. Also, [Compile time reflection discussion.] We are here to bring rust into production, and we’re already missing windows. e.g. The FDA is reserving the right to refuse memory safety [...?]

Joel: As a practical matter, the FLS is going to bring us to something sooner.

Peter: Why is there a disconnect with urgency?

[More or less, lack of connection to industry and/or shipping to prod.]

JF: FLS has already been around a good chunk of Rust 1.0’s lifetime. Writing a spec is a good amount of work.

Alex: We still have about an hour, but we should decide on action points.

JF: I don’t want to do anything that would deter participation from other OEMs. I want this to be an open group.

Walter: We can use the Foundation as an anon filter for PR that you cannot publish publicly as your company.

JF: Two things IP-wise to address. If we create a Coding Guidelines, we need IP contribution rules (copyright, patents, etc). For documentation, Linux Foundation recommended Community Specification license or OWFA v0.9 (not 1.0). This type of concern is for example covered by ISO when contributing to C++ standards.

Alex: We desperately need the outcome for the spec. -> action items?

Joel: (1) mission (2) coding guidelines document together (3) resolve the spec problem.

Other action items?

JF: Tooling roadmap / shopping list? e.g. MC/DC, defect management, [...]

Alex: Seconded.

Jordan: Training syllabus?

Tony: Opportunities for different profiles for the standard library / runtime. We have libstd, libcore, which are both large; libstd requires an OS, but some parts may be separable. UTF-8. Look at common use cases, functionality they would need, and chunking them out. There’s a vendor I’m working with talking about certification – if I can reduce the scope of the standard library, I can reduce the cost.

Florian: I agree, however, the stdlib is a facade in rust, and it’s a long-standing issue on how to compartmentalize it more. It’s waiting on someone to actually instigate. Document workspace and code workspace.

JF: i.e. how do we contribute?

Florian: If we follow the route for asking other companies to contribute their artifacts, the IP issue becomes front and center since their lawyer will ask about it.

Joel: Is it an action item to create subcommittees? I can take that: create subcommittees, assign responsibilities, ask about membership.

JF: Async work didn’t work on the charter, will it work in the future?

Tony: Sub-committees may have better results. I would contribute more on select subcommittees. Nebulous 

JF: Is supply chain an actual safety thing? Versus security.

Walter: We should ask if there are unique supply chain issues to safety and go from there.

Tony: I think supply chain issues are super important.

Walter: There are many initiatives here. Google has cargo-vet, crates.io has work, openssf, etc. all discussing how do we do sustainability and such.

Erik: One of the issues we see is that when we sync crates to our repo, we fall behind over time.

Arnaud: The problem for crates.io is not safety problems; I am more concerned about the crates used to build the toolchain is of confidence on a long-term basis.

JF: I don’t think supply chain should be in this group; we should be a user of it. We should do something similar to what the LF does with security. We have a fund of money they allocate to base infrastructure security, funding them. The issue is, they have to figure out what’s important for security. I think we’ll have a similar world here on the safety side. Not necessarily crates, but similar projects – we may want to have open-source safety projects we’d want out there. We’d need something like the foundation as an anonymizer – I care about this crate, about this project, the RF anonymizes it, then helps drive investment into these projects at scale. We can’t go to an open-source Rust project and say “you’re safety critical now”, until they actually are. If some of those projects are really safety critical, we may want to change their development process at some point. This could be an important role for the foundation where it becomes an anonymizer. But this is for later, not next year.

Florian: It may be hard to bolt on more responsibilities to this consortium.

JF: It could live in LF too.

Walter: Any other action items? How are we going to meet, frequency?

Joel: It seems like we almost have to work async, given time zone differences. Big meetings like this will probably be far and few between.

Walter: Maybe yearly meetings at RustConf and quarterly whole group virtual meetings? Sub-committees can be decided separately.

David: I would recommend starting with virtual meetings versus async, because there's a risk of losing the momentum that got created here. I’ve seen async fail many times.

Jordan: I like piggy-backing on the conferences.

Joel: The sub-committees can decide their own meeting cadences.

Tony: We should leave the room with sub-committees and chairs.

[Coding Guidelines committee members decided.]

[Tooling committee members decided.]

[Profile committee -> moved into tooling committee for the time being.]

David: It sounds like a group-wide thing.

[Spec committee decided to be a global static.]

Joel: Are there any other subcommittees?

Joel: Should we open the chat to the world?

David: Prefer to keep private for now.

Florian: We should decide the preconditions for membership. We can push the chat room restrictions later.

JF: It can’t be a group that you can’t join. We should have common sense entry eligibility.

Florian: Membership may be difficult for some companies.

JF: Governance structure -> if someone wants to join, they can join, but they can’t derail.

Walter: Start a GitHub org?

Jordan: After standing up the GitHub org, we can determine the IP contribution rules? Can we just discuss that on Zulip?

Walter: Yeah, we can do that async.

Joel: RustConf and RustNation are the conferences Rust Foundation members go to. Next meeting, RustNation in UK? March.

👍

Florian: Rust AllHands is next year. Would that also be appropriate? Just putting it out there. For the Rust Project and getting more rapport?

[Decided for ^ to not necessarily be a full group meeting, but those attending can reach out to project folks on behalf of RSC.]

### Subcommittees

#### Coding Guidelines

Look at MISRA, JAE1020, and MISRA C applicability to Rust (from Alex C)

- Walter
- Joel
- Alex V.
- Florian
- Peter
- Erik
- Jordan
- Christof
- Alex C.

#### Education

Training syllabuses and curriculum

- Alex R.
- Florian
- Filip
- Walter

(This may be subsumed by the coding guidelines committee)

#### Tooling

This includes standard library profiling as well.

- Tony
- Jordan
- Febrice
- Aranud
- Daniel
- Fred
- Julius
- Alex V
- Orson

