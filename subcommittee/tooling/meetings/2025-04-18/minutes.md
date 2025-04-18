# Tooling Subcommittee Meeting on 18.04.2025 @ 16:00 GMT

| Search Key    | Description          |
|:------------- |:-------------------- |
| \[todo\]      | Action Item          |
| \[decision\]  | Something decided on |
| \[important\] | Key information      |

## Agenda

1. New members introduction  
2. Approval of previous meeting minutes [https://github.com/rustfoundation/safety-critical-rust-consortium/pull/263/files](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/263/files)  
3. Discussions about the arewesafetycriticalyet.org [https://github.com/rustfoundation/safety-critical-rust-consortium/pull/281](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/281)
   
   ## Check-in area
   
   **Please add your name, and an emoji that describes your day.**
* Alexandru Radovici 🙂  
* Xander Cesari 🐸  
* Pete LeVasseur 🧰  
* Oreste Bernardi   
* Tony Aiello 😮‍💨  
* Sasha Pourcelot 🍕
  **Notetaker:**
* Xander Cesari
  
  ## Housekeeping section
* Approving previous meeting notes  
  1. No objections, approved and merged
     
     ## Tasks
* Chat about arewesafetycriticalyet.org website  
* Coding guidelines subcommittee is requesting review for their draft  
  * [https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/27](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/27)  
* Discuss coding guidelines and standard libraries
  
  ## Meeting Minutes
* [www.arewesafetycriticalyet.org](http://www.arewesafetycriticalyet.org)  
  * Current website is on docs.rs  
  * Added sections for each subcommittee with AI-sourced logos  
    * Tooling section has members, mission statement, etc  
  * Added blog section for news from the consortium  
  * Added a link to GitHub  
  * Logos  
    * \[todo\] A logo was drafted between the Rust Foundation and some members; should check with [joelmarcey@rustfoundation.org](mailto:joelmarcey@rustfoundation.org) about whether that logo is available to be used on this website  
      * [https://docs.google.com/presentation/d/1eqsq-2rdUWfpgVT6XPI5zwextiPMd1ywaSuImAEkHWs/edit?slide=id.p\#slide=id.p](https://docs.google.com/presentation/d/1eqsq-2rdUWfpgVT6XPI5zwextiPMd1ywaSuImAEkHWs/edit?slide=id.p#slide=id.p)  
    * Ferrous systems made the ‘safety critical Ferrous’ logo (crab with hardhat). Is that available for broad use for all safety critical Rust? Can we use that for the subcommittee?  
      * \[todo\] [Xander Cesari](mailto:xander.cesari@pictor.us) to follow up with Florian @ Ferrous  
  * Comment: it’s okay to merge with little to no content for now and let subcommittees start to feed content in  
  * Still need to add CI/CD pipelines with some testing and preview rendering so every PR automatically merges  
  * What is the definition of a “community-approved” tools?  
    * Tools that we know of that may be helpful to safety critical users  
    * Is “required” necessary? Not every tool we’ve identified is required in all cases  
    * \[decision\] “Community-identified” may be more neutral language as we don’t really have an approval process  
  * What’s the repository for the page?  
    * It’s in the safety critical consortium as a PR right now \- [https://github.com/rustfoundation/safety-critical-rust-consortium/pull/281](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/281)  
  * Is the website or the repo going to be the landing page for people interested?  
    * If we wanted to pull in bits and pieces of what’s in the repo as markdown files in the website?  
    * Can we include markdown files from outside the folder (within the repo) on the website?  
    * \[todo\] [alexandru.radovici@oxidos.io](mailto:alexandru.radovici@oxidos.io) to look into this technically and we can ask at the consortium meeting at RustWeek  
  * The tooling mission statement wording is slightly different between the repo and the text currently on the website, comment added to the PR  
  * Are we answering the question of “are we safety critical yet”?  
    * The other ‘are we’ pages are simpler but just have a Yes/No/Maybe and a list of tools  
    * The answer for safety-critical uses is almost always “it depends” but maybe we can add a general answer to the state of the ecosystem; we have standards, we have certified tooling, we have some static analysis tools  
    * Can we list some of the successful certification stories? Companies that have certified under certain standards and to certain levels. We can solicit companies in the certification process for ‘case studies’. This would be a win for everybody: the Rust community, the consortium, and the companies certifying.  
    * \[todo\] [plevasseur@gmail.com](mailto:plevasseur@gmail.com) to talk to some companies in the ecosystem and see if they would be willing to share a testimonial for the website  
    * Could we have simple tables showing current cert status? Maybe behind tabs for each standard but something like ISO-26262 having a table with rows for each ASIL level and indications of status. So green dot means someone has certified Rust there, yellow dot means we think it should be possible with the state of the ecosystem, and red dot means we’ve identified a gap.  
      * \[todo\] [Xander Cesari](mailto:xander.cesari@pictor.us) to take a stab at drafting the table for us to brainstorm on in a future meeting  
    * Should we list something about supported versions? Some tools only apply to specific versions of programming languages. This isn’t as big of a deal within the C community that’s slow-moving and not changing very much but in the Rust community where things change fast there are some tools that might not apply to every version of Rust. This page could also help to push tool vendors to update faster.  
      * Supported version is a bit of a moving target for tool vendors. Currently the supported versions is a relatively short list but the tool vendors would absolutely build to support any needed version, making it a bit of a moving target.  
      * Especially for small companies there may be value in showing some level of version support even if we don’t list supported versions for each tool  
      * But we also need to cert the core and std library, which may be an absolute massive cost. So just supporting the compiler version doesn’t even tell the whole story.  
      * \[decision\] It may be biting off more than we can chew to get versions on the website, just getting it live and with a list of tools is a big enough task. If we can do this versioning work internally to the consortium then maybe we can versions up.  
      * A compromise might be just getting a “last updated” time stamp on either the entire tool list or on each specific tool that we have.  
* Coding guidelines and standard library  
  * Ongoing work happening at a tool vendor to understand how much work and expense is required to certify libraries to various standards.  
  * To do this, a coding standard is needed. They looked at the current output of the coding guidelines subcommittee and unfortunately it’s not yet ready to cert against. Not bad output, just not enough yet.  
  * The coding guidelines team needs to consider the deployed standard and core library. If they come up with a guideline that the base libraries don’t meet this could make certification very difficult.  
  * The point-of-view of the coding guidelines subcommittee is that the Rust code in the base libraries (standard and core) is de facto good: it’s written by people who know Rust extremely well and it’s extremely well tested. There may be code in there that’s not acceptable or suitable for safety-critical applications but we don’t expect to/hope not to find “bad” code. Coding guidelines is aware of this concern but if there are specific examples that certifiers find they should raise it in the GitHub repo. Coding guidelines is also trying to do some outreach and open lines of communication with the Rust project to have a dialogue running about this.  
  * There’s also a big difference between the core and standard libraries: most safety-critical work is happening on embedded so the core library is probably a more critical one.  
  * Forking the standard or core libraries is an option but tool vendors are motivated to upstream any changes they need to make. It gives back to the community but also it leans on the rest of the language community to continue to forward port those changes. The massive costs associated with any forking activity blow up really quickly.  
  * \[todo\] This is probably a to-do item and further discussion point for the coding guidelines subcommittee. [plevasseur@gmail.com](mailto:plevasseur@gmail.com) is already aware of this issue and will continue to discuss via coding guidelines  
  * \[decision\] There will be a discussion at the Rust Project All-Hands in May at RustWeek about this, and building some communication between the safety-critical coding guidelines world and the Rust Project  
* \[todo\]\[important\] [plevasseur@gmail.com](mailto:plevasseur@gmail.com) representing coding guidelines would like help reviewing this PR:  
  * [https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/27](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/27)
    
    ## Material
    
    Any material to read before the meeting should be included here.
    *
