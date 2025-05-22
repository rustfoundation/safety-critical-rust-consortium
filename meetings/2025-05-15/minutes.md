# Safety Critical Rust Consortium Meeting on 15 May 2025 @ 9 AM CET, Utrecht, Netherlands

| Search Key | Description |
| :---- | :---- |
| \[todo\] | Action Item |
| \[decision\] | Something decided on |
| \[important\] | Key information |

## Agenda

1. **9 AM**: Welcome and Meeting Logistics (@JoelMarcey)  
   1. Welcome New Members  
2. **9:15 AM**: Subsidizing costs of in-person meetings (@JoelMarcey)  
   1. Try to have consortium members host in cities where we have meetings?  
3. **9:30 AM**: Website for consortium information and status (@JoelMarcey)  
   1. Domain  
   2. Front matter content  
   3. Subcommittee content  
   4. Consortium information source of truth \- repo or website.  
4. **10:00 AM**: Safety Critical Survey results and discussion (@MerrimanInd)  
5. **10:30 AM**: Rust specification update (@JoelMarcey)  
   1. Ferrocene Language Specification (FLS) within Rust Project now  
   2. Utilizing the specification within our work  
6. **11:00 AM**: Subcommittee Reports  
   1. Coding Guidelines (@PLeVasseur)  
      1. Walkthrough of current progress, process of contributing: 5 mins  
      2. Safety-certifiability of `libcore` and `libstd` based on the coding guidelines: 10 mins  
         1. Upstreaming of best practices into the Rust Project as deemed feasibly to ease safety-certification.  
      3. The degree to which we should align with existing coding standards e.g. MISRA C to ease adoption: 5 mins  
   2. Tooling (@alexandruradovici)  
   3. Liaison (@AlexCeleste)  
7. **12:30 PM**: Lunch and free discussion  
8. **1:30 PM**: Breakout groups / Review Open Issues and PRs  
   1. Coding Guidelines (@PLeVasseur)  
   2. Tooling (@alexandruradovici)  
   3. Liaison (@AlexCeleste)  
   4. Specification (@JoelMarcey)  
9. **2:30 PM**: Meeting Close (@JoelMarcey)  
   1. Post-mortem  
      1. What worked well?  
      2. What can be improved?  
   2. Next meeting?  
10. **3:00 PM**: Depart

## Check-in area

**Please add your name, and an emoji that describes your day.**

* Joel Marcey 😱  
* Jonas Wolf 🙂  
* Arthur Hicken 🫨  
* Alex Celeste 😌  
* Alex Heslop 😊  
* Andrew Herridge 👍  
* Pete LeVasseur ☕🫖  
* Enow Scott 🙂  
* Xander Cesari 🪩  
* Sarah Dietrich 🙂  
* Sasha Pourcelot 🚄  
* Takeo Kondo 😄  
* Martin Becker☕  
* Tim Janus   
* Chadi Alkurdi☕  
* Jonathan Leeming 😊  
* Samuel Tardieu 😊  
* Jordan McQueen 🤡🥸  
* JF Bastien 🤡  
* Koppany Pazman  
* David Wood 👏  
* Alexandru Vochescu 🙂  
* Alexandru Radovici 🙂  
* Orson Pessin  
* Manuel Hatzl😴  
* Arnaud Fontaine   
* William Barsse  
* Christof Petig 😊  
* Tim Koval 🙏  
* Julius Gustavsson 🤩  
* Lukas Wirth  
* Markus Hosch 🚲  
* Marc Schoolderman 🚲😵‍💫  
* El Araby El Mahdi 🐌
* Gonzalo Brito 🦀 
* Benoit Lietaer🦀 

**Notetaker:**

* Christof Petig

## Meeting Minutes

* Meeting funding: New option members of the consortium could host the meeting and keep going free of charge  
  * Concern is to not introduce a paywall  
  * Looking for a company with an office in Seattle to host it  
  * \[todo\] Joel will try to find a member to host close to the chosen location  
  * Companies are used to a conference fee, so it should be more easy to get this approved  
  * Tip jar might be an option as well  
  * As many individuals joining try to sell Rust in safety to their company there might be a chicken and egg problem of the company seeing the benefits of Rust in safety already  
  * Proposal to arrange the next location at the previous meeting, trying to find someone hosting it  
* Official web site [https://arewesafetycriticalyet.org](https://arewesafetycriticalyet.org), more TLDs secured  
  * Initial content work in progress  
  * Pull request from the main repo  
* Survey results  
  * See presentation or details  
  * \[todo\] “How to sell Rust within your company“ slide deck, technical briefs for management  
  * Walk through of the process of certify a project  
    * Point to existing tools which help you in the qualification, with roadmap of upcoming certifications  
    * Woven might be able to provide some success stories soon  
    * Sharing experience from projects would help bootstrap projects, like eclipse SDV blueprint projects  
    * Outreach could become part of the liaison subcommittee  
  * SAE JA 1020 reached more than 80% approval; going to the next phase\!  
  * Ideas for the next one: More specific on the tool selection  
* Rust Specification  
  * Priority should be on completing the spec before adding new RFCs  
  * Cross referencing or mapping between FLS and Reference would help a lot to harmonize  
  * Ferrocene will continue to upstream their changes into the FLS, but a hand over of responsibility is in planning  
  * A yearly cadence is planned to sync (editions feel too coarse, releases too frequent)  
  * We should aim for close synchronization between the compiler and the spec  
  * Conformance test suite exists within the public ferrocene repository, traceability is being worked on  
    * [CodeThink](https://www.codethink.co.uk/) presented a helpful framework to the [Eclipse SDV WG](https://sdv.eclipse.org/)   
      * Eclipse Foundation has chosen to accept the [Trustable Software Framework](https://fosdem.org/2025/schedule/event/fosdem-2025-6204-the-trustable-software-framework-a-new-way-to-measure-risk-in-continuous-delivery-of-critical-software/) (TSF) from CodeThink as a first candidate into their [Eclipse Foundation Functional Safety Process](https://blogs.eclipse.org/post/dana-vede/introducing-development-process-safety-critical-applications)  
      * [Eclipse uProtocol](https://uprotocol.org/) through contributions from Daniel Krippner, Kai Hudalla of ETAS have volunteered to be a pilot project for the TSF in the Eclipse SDV WG  
  * Because people contributing a feature to Rust might not be skilled enough at wording the specification there is hesitation to require it to not slow down Rust evolution  
    * Stabilization could reasonably require a specification update link  
    * A checkpoint would help a lot  
    * Please avoid repeating the mistakes seen in other languages  
    * Spec team benefits from more helping hands for synchronization  
    * The meetings are open to the public  
* Coding guidelines update  
  * Coding guidelines will move to the new web site  
  * Keep in mind that it is too immature yet to rely on for projects  
  * Goal is to use the guidelines for qualification of crates and receive feedback  
  * The current MISRA document encourages using them in a not-helpful way (ticking boxes), we should strive for a document which makes it easy to use in the intended way. The compliance document explicitly asks to come up with a strategy for deviation but organizational culture leads to short cuts.  
  * Coding guidelines should strive to become a clippy lint to keep the safety flavor and the normal flavor of Rust close  
  * Clippy confirming that it checked would help confirming that the process was run, because it is so common to have zero complaints in good quality code  
* Tooling  
  * We don’t need another C certification process, the strength of Rust should be obvious  
  * More automation by tools should make compliance with guidelines less critical  
  * Showcasing tools not recommending (not introduce requirements)  
  * We need to define a process that is shorter and saves money while still providing a superior quality  
  * Do we need a bar to get a tool listed? Perhaps a long list of tools with a low bar to get a tool mentioned would also help. We don’t want to have hardly maintained tools on the list.  
    * How to get to a state of the art recommendation for tool usage?  
    * Eclipse summit feed-back on what slows down FLOSS projects focused on safety: One is the cost to access standard documents, the second is costly access to tooling. The ability to also use the tools free of charge for non-commercial projects is critical.  
    * Proven in use argument for tools might be an option for open source projects  
    * Documenting the safety argumentation is important to enable tool usage on projects  
    * The tool group could provide an initial assessment about the safety value of a tool, a tool qualification likely requires a commercial body, a statement on the maturity for qualification helps  
    * An evaluation license could help with vetting proprietary tools, a tool vendor is not expected to lie about the capabilities of a tool, anonymous testimonials might be additional evidence of its usefulness  
    * Open source tools might need a careful checking to verify claims, how to synchronize with the lifecycle of the tool, a contact person can help  
    * The companies using a tool have a high incentive to maintain the accuracy of an entry in the list, the tool author less so  
    * The ease of integration with the Rust ecosystem is another interesting metric  
    * The process should be time boxed (two to four weeks?) We should expect some bogus requests  
    * PR template and the review process fit well for tools inclusion  
  * There will be a new issue to add a recommended clippy preset for safety qualification, likely per integrity level  
    * Corporate interest from the SCRC could fund clippy  
  * A collection of process steps from C/C++ which are no longer necessary on Rust pools the knowledge across the industry   
  * Collecting the state of the art per industry needs volunteers, this is meant to be iterative, documenting existing practices is needed  
    * A responsible person per industry to coordinate the creation of the document, not do the work, would be needed. We need to prevent establishing a copy of the C process for Rust.  
  * \[decision\] Rotating time slots would make sure that Asia, Europe and Americas have equal opportunity  
* Liaison  
  * ISO is moving towards becoming less C specific  
  * AUTOSAR has a document describing Rust applications for adaptive platform, the focus is currently on enabling Rust for classic platform.  
* Next meeting  
  * Euro Rust is in October, Attendance at RustConf Seattle seems to be low, Oxidize is very close to RustConf in time  
  * Another option would be a virtual meeting, as there have already been two meetings this year  
  * \[todo\] Joel to create a poll to try to determine next meeting logistics  
* \[decision\] A monthly or quarterly meeting (?) could satisfy the needs for the people on the consortium which aren’t part of a subcommittee and would like to get a regular update  
* MISRA and CERT  
  * MISRA restricts the language to a subset that can be analyzed for safety, thus it needs a deviation process. This enables the usage of these overly broad rules.  
  * CERT came later and avoid false positives of the rules, false positives by the tools is another complication  
  * In CERT a deviation process should be rare  
  * We need to decide whether to go more towards a set of rules (like MISRA) or an iterative improvement process (like CERT), or find a more middle ground (if possible)  
  * The impulse to achieve limited liability is different from high quality code  
  * CERT worked hard to avoid flagging correct code  
  * CERT aimed towards avoiding theoretical rules which have little weight in practical security  
  * Neither of the standard guarantees correctness, this is created by the process part of safety standards  
  * Collecting data whether a rule is helpful is difficult  
  * The approval of deviations process is very costly, as it requires higher approval and proper scoping and tracking  
  * Actionable priority is preferred to binary decisions, like fix all complaints of a tool.  
  * As we don’t have data a lightweight deviation process would be better in the beginning.  
  * A crater run to check practicability of a rule is attractive  
* How do we streamline the qualification path and make it less costly?  
  * Part of 26262 is coding standard, avoiding the parts which lead to mistakes  
  * As most of the mistakes are impossible in Rust, the qualification should be easier  
  * As we want the tools qualified, we need to pool resources  
    * The Rust foundation could raise money from the companies which would have to pay for these reports  
  * The type system helps with correctness, which is common in Rust but unusual in C++  
    * Formal methods are a resource to improve quality, but they might be hard to use

## Material

Any material to read before the meeting should be included here.

* Meeting presentation: [https://docs.google.com/presentation/d/1bUCP6hYtyLq3jeOgxWRv-El1Babite7o9QNXVpjdgr0/](https://docs.google.com/presentation/d/1bUCP6hYtyLq3jeOgxWRv-El1Babite7o9QNXVpjdgr0/)
