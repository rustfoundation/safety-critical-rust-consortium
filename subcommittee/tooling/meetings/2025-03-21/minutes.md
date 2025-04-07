# Meeting Agenda

Tooling Workgroup

| Search Key  | Description          |
|-------------|----------------------|
| [todo]      | Action Item          |
| [decision]  | Something decided on |
| [important] | Key information      |

**1\. Attendees**

* Alexandru Radovici (Moderator)  
* Pete LeVasseur, 🕵️(Notetaker)  
* Julius Gustavsson  
* Xander Cesari  
* Manuel Hatzl  
* Bogdan Genis


**2\. Agenda Items**

1. Presentation of new members (if any) of the working group  
2. In Person meeting details  
3. arewesafetycriticalyet.org \- home page discussion (Pete)  
4. Review Coding Guidelines framework (Pete)

**3\. Meeting minutes**

1. Presentation of new members  
   1. None this time  
2. In Person meeting details  
   1. Some email came out with details, more forthcoming  
3. arewesafetycriticalyet.org \- home page discussion (Pete)  
   1. Joel bought domain via Rust Foundation  
   2. Building the home page  
      1. Anything standard?  
      2. Alexandru R \- setup the framework for the home page ([https://docusaurus.io](https://docusaurus.io/)) \[decision\] \[todo\]  
      3. Alexandru R \- Solicit the Consortium for filling in content \[todo\]  
   3. Pete L considering putting coding guidelines at coding-guidelines.arewesafetycriticalyet.org  
   4. Discussion of by what metric(s) we should consider readiness for safety  
      1. Start with big regulatory frameworks: ISO 26262, DO 178  
      2. Highlight different levels on the frameworks  
      3. Some work happening in community for safety-qualifying libcore for 2+(?) participants  
      4. E.g. in Tooling we can filter for DO 178 and get some potential subset of relevant tools  
      5. Tooling, Standards, Coding Guidelines \- allows delegation of responsibilities \[decision\]  
      6. Put meeting minutes out on the website too  
      7. Pete to open issue on the Consortium repo outlining \[todo\]  
   5. Tooling \- how do we show without much noise the readiness of tools per framework and level of framework?  
      1. Use green/yellow for ready / still-in-progress?  
      2. Gaps in certain existing ones accounting of frameworks and levels  
         1. Guidelines / items exist for C, may not be applicable for Rust  
         2. Suggestion to work with assessor / auditor to get a better sense of applicability of frameworks / levels  
            1. Some initial work we can ask of new Liaison subcommittee \[decision\] \[todo\]  
               1. Does this involve some spending, even just for chatting? \[important\]  
            2. Mention of [ISO 8926](https://www.iso.org/standard/83346.html) \- Road vehicles — Functional safety — Use of pre-existing software architectural elements  
         3. Perhaps standards frameworks will also change to have caveats for memory safe languages  
4. Review Coding Guidelines framework (Pete)  
   1. Showed the framework using Sphinx, Sphinx-Needs  
   2. Showed the generated output website  
   3. Showed the needs.json  
      1. Concept discussed is that Tooling Subcommittee could own a document in order to tie together the guideline with: tool and tool configuration that supports (e.g. simplest case: turn on this clippy lint) \[todo\]  
   4. Showed the guidelines-ids.json  
      1. Discussion of removing whitespace from guidelines  
         1. Thought of after meeting: we may want whitespace at the very least for the good and bad code examples?  
5. Liaison subcommittee  
   1. Alex Celeste will serve as chair  
6. Survey safety-critical domain users of Rust for tooling usage  
   1. Try to identify if e.g. there are people that want to use Rust, but for a missing tool  
   2. Who is the audience / where do we gather feedback?  
      1. Ask Rust Foundation to reach out?  
      2. Alexandru R \- Ask Foundation \[todo\] \[decision\]  
      3. Perhaps a catch-all survey for the Consortium, e.g. Tooling, Coding Guidelines, Liaison, etc  
      4. Try to get a sense of if there’s a:  
         1. Subset  
         2. Priority  
   3. Xander \- Open a PR to have feedback for survey \[todo\] \[decision\]
