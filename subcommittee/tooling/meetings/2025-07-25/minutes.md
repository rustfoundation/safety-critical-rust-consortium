# Tooling Subcommittee Meeting on 25 July 2025 @ 4pm GMT

| Search Key    | Description          |
|:------------- |:-------------------- |
| \[todo\]      | Action Item          |
| \[decision\]  | Something decided on |
| \[important\] | Key information      |

## Agenda

1. Solicitation of notetaker  

2. Review [last time’s meeting minutes](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/tooling/meetings/2025-06-27/minutes.md)  

3. Present new members  

4. Chat about a first safety-critical standard which need be applied (Pete)  
   
   1. ISO 26262?  
   2. DO 178C?  
   3. Some sort of NASA standard?  
   4. Rail safety critical?  
   5. Who would like to lay out the path to safety-certify code and required tooling?  

5. Chat about safety-critical tools to add to the database in support of ISO 26262 (Pete)  

6. Review the initial procedure for submitting new tools \- [tooling new submission](https://docs.google.com/document/d/1hZGU5MCx_sb_8qEhww4l-KtLYyDNdQihQP7Tgtu4QSg/edit?tab=t.0) (Pete)  

7. Update from Woven by Toyota on MC/DC support upstream (Pete)  
   
   1. [Why MC/DC?](https://hackmd.io/@i-aMA8ZOS92HAYpU8f_8eg/S1-KTICmee/edit)  
   
   2. [Notes](https://hackmd.io/@i-aMA8ZOS92HAYpU8f_8eg/rkIRw0wXlx/edit) of Woven by Toyota implementors
      
      ## Check-in area
      
      **Please add your name, and an emoji that describes your day.**
* Pete LeVasseur 🛬  

* Xander Cesari 🪐  

* Stephen Hedrick ⚡️  

* Tiago Manczak  

* Arnaud Fontaine 😀  

* Oreste Bernardi
  **Notetaker:**

* Xander Cesari
  
  ## Housekeeping section
  
  ## Tasks

* See \[todo\] below ⏬
  
  ## Meeting Minutes

* Approving last meeting’s minutes  
  
  * SC Tooling Issue template was approved and merged  
    * [https://github.com/rustfoundation/safety-critical-rust-consortium/pull/337](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/337)  
  * SC Tooling Request issue template is still open and in draft  
    * [https://github.com/rustfoundation/safety-critical-rust-consortium/pull/336](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/336)  

* Following up on a discussion topic from last in-person meeting, we would like to look at the process of certifying software for a safety-critical standard and map out the tooling and standards required.  
  
  * Which standard to start with?  
    * ISO-26262  
    * DO-178C  
      * Likely a very difficult standard to start with and not the first standard to adopt  
    * We should pick the standard/industry where Rust is a first mover. Most likely automotive but if there’s an aero/space/defense standard that’s moving fast we should go there.  
  * Who can start on this?  
    * [Xander Cesari](mailto:xander.cesari@pictor.us) will be doing a similar project for some marketing efforts (running through a simulated cert process in Rust with some tooling) so about 60-80% of his work will likely overlap.  
    * In standard ISO-26262 processes they don’t point to specific tools, the standard is process-oriented and this often drives specific tools or manual processes. So there are many paths to certification.  
    * The process of certifying a tool itself for ISO-26262 is a further stretch goal, this should focus on the product focused process.  
    * Artifact output will be a page on the website and in the writing of this page identify any gaps in the process.  
    * Target ASIL D but highlight lower safety level requirements as well.  
    * Oreste has some templates and documentation that may be publicly shareable.  
    * Eclipse S-CORE may have some process documentation for using Rust in safety critical contexts. [tiago.manczak@infineon.com](mailto:tiago.manczak@infineon.com) to look for links and add them.  
    * [https://github.com/eclipse-score](https://github.com/eclipse-score) \- main github repo  
    * [https://eclipse-score.github.io/process\_description/main/process\_areas/tool\_management/index.html](https://eclipse-score.github.io/process_description/main/process_areas/tool_management/index.html) \- tool management process description  
    * [https://eclipse-score.github.io/process\_description/main/process\_areas/tool\_management/guidance/tool\_management\_checklist.html](https://eclipse-score.github.io/process_description/main/process_areas/tool_management/guidance/tool_management_checklist.html) \- checklist (suggestion: we could prepare such checklist for the SCORE project for the tools we are listing)  
    * Might be interesting to “upstream” some of these blueprints/processes to orgs like SOAFEE or Eclipse SDV after we develop them internally. This could use the Eclipse Trustable Software Framework.  

* Who came with ideas for safety-critical tools to add to the database?  
  
  * Tools  
    * Pete  
      * TrustInSoft tool \- static analysis  
      * HighTec Compiler  
      * Kani  
    * Arnaud  
      * Ferrocene Compiler  
      * Mantra requirement tracing  
      * Verifast  
      * creusot  
    * Oreste  
      * OpenFastTrace \- requirements tracing  
      * Lautherbach debugger  
      * UDE Pls debugger  
      * Reqtify \- [https://www.3ds.com/products/catia/reqtify](https://www.3ds.com/products/catia/reqtify)  
    * Stephen  
      * Sphinx Needs \- requirements tracing  
      * AdaCore GNAT Pro for Rust  
      * Clippy  
    * Xander  
      * OxidOS RTOS \- OS / Libraries  
      * [Rapita](https://www.adacore.com/press/rapita-embraces-rust-via-adacore-partnership)  
      * OSS tooling  
        * Cargo extensions (deny, audit, etc)?  
  * Editor (Safety Evaluation as a part of the process is done. May not be included explicitly in DB, but could be highlighted as a step that need be done.)  
    * RustRover  
    * VSCode  
    * ?  
  * OS / libraries  
    * OxidOS RTOS  
  * Note that target audience for this website is existing safety-critical developers who know software and some SC processes but want to learn the state of the Rust ecosystem  
  * Task: submit Github issue using the Tool template adding these tools to the database  
    * [https://github.com/rustfoundation/safety-critical-rust-consortium/issues/new?template=submit\_tool.yml](https://github.com/rustfoundation/safety-critical-rust-consortium/issues/new?template=submit_tool.yml)  
  * Submitted an issue live to dogfood the process  

* MC/DC at Woven by Toyota  
  
  * The Woven by Toyota team working on MC/DC was an internship program and they won’t be able to finish it in time. So they’re switching over to a project that’s completable in the scope of their internship. Most likely their work won’t get merged but they have some interesting work done.  
  * There are still some interesting question marks in the Rust ecosystem about how Rust and MC/DC overlap.  
  * This may be an opportunity for the Consortium to highlight the Rust MC/DC gap and try to find someone to continue the work.
