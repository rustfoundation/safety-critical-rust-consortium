# Tooling Subcommittee Meeting on 30 May 2025 @ 4pm GMT

| Search Key    | Description          |
|:------------- |:-------------------- |
| \[todo\]      | Action Item          |
| \[decision\]  | Something decided on |
| \[important\] | Key information      |

## Agenda

1. Present new members  
2. Establish a rotating meeting time (if it is required)  
3. Procedures for accepting and submitting tools

## Check-in area

**Please add your name, and an emoji that describes your day.**

* Alexandru Radovici 🙂  
* Tony Aiello 😶  
* Xander Cesari 🍺  
* Munawar Hafiz, 🙂  
* Pete LeVasseur, 🥣  
* Manuel Hatzl 🙂  
* Oreste Bernardi🙂

**Notetaker:**

* Xander Cesari

## Housekeeping section

* ## Tasks

* 

## Meeting Minutes

* Rescheduling our meetings to be more friendly to different timezones, specifically getting an Asia/Pacific friendly timeslot  
  * Coding Guidelines has already rescheduled to have an Asia/Pacific friendly meeting time but haven’t had many meetings. Maybe we could wait to see how their timeslot goes?  
  * Could we run a casual ‘office hours’ type meeting at an Asia/Pacific friendly time to try to measure interest in that timeslot?  
  * Zulip has a poll feature, could we just poll the consortium members on who would be interested in joining from those timezones?  
  * Action: start with a poll in the Zulip tooling channel \[todo\]  
  * Action: schedule an Asia/Pacific office hours. \[todo\]  
    * 9am in Japan  
    * Maybe make it broader than just one subcommittee? A consortium-wide effort to get participation from that region  
    * [Xander Cesari](mailto:xander.cesari@pictor.us) to host since 8pm US ET time is 9am in Japan. Date will be June 9 or 10\.  
* Procedure for accepting and submitting tools  
  * Xander was developing a GitHub issue template for identifying tooling/process gaps in the Rust ecosystem. Would be relatively simple to build an issue template for “bringing a tool to the attention of the tooling subcomittee consortium”.  
    * [https://github.com/MerrimanInd/safety-critical-rust-consortium/blob/tooling\_request\_issue\_template/.github/ISSUE\_TEMPLATE/tooling\_gap.yml](https://github.com/MerrimanInd/safety-critical-rust-consortium/blob/tooling_request_issue_template/.github/ISSUE_TEMPLATE/tooling_gap.yml)  
  * Coding guidelines has already implemented something similar. Additionally there are some GitHub actions behind it.  
    * [https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/new?template=CODING-GUIDELINE.yml](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/new?template=CODING-GUIDELINE.yml)  
  * So what fields should the tooling issue have?  
    * We need to decide what the procedure should be for “vetting” tools that are submitted through this issue.  
    * [alexandru.radovici@oxidos.io](mailto:alexandru.radovici@oxidos.io) to work on drafting this procedure  
    * We should have a contact person for each tool (visible only to us, internal use)  
    * [Xander Cesari](mailto:xander.cesari@pictor.us) to draft a GitHub issue template  
    * At the last in-person meeting a list of fields/data we should know about each tool was drafted, this could be drawn   
  * Are we open to fielding issues without a point-of-contact person who owns the tool?  
    * Yes, especially if the tool is in use in safety critical development. But we would likely need to go track down the contact before posting it to the website  
* GitHub issue for identifying tooling gaps  
  * There’s a difference between identifying a gap in a process and identifying a tool that might fill it. Should these be two different templates?  
  * Very difficult to make this type of form rigid and programmatic; there will be many long-form text fields with “describe what you were trying to do”  
  * Maybe all of these issues should include a ‘process gap’ section with an optional ‘tooling suggestion’ section if the submitter feels they know exactly what tool would close the gap?

## Material

Any material to read before the meeting should be included here.

* ## Tools Information

```
Tools list  
- make a list with names of the tools  
- tool type tag:  
   - "coverage"  
     -> "mc"  
     -> "dc"  
     -> "statement"  
     -> "function"  
     -> "call"  
     -> "branch"  
     -> "test"  
   - "requirements-traceability"  
   - "qualified-compiler"  
   - "test-runner"  
   - "formal-verification"  
   - "static-analysis"?  
   - "tests-generation"  
     -> "unit"  
     -> "integration"  
 - "enforce-guidelines"  
   - "rust-safety-critical" - will it have levels? @Pete  
 - "graphical-representation"  
 - "metrics" - https://www.exida.com/blog/software-metrics-iso-26262-iec-61508 (Section 3.1)  
   - "cyclomatic-complexity"  
   - "comment-density"  
   - "number-of-paths"  
   - "number-of-goto-statements"  
   - "number-of-calling-functions"  
   - "number-of-parameters"  
   - "instructions-per-function"  
   - "function-return-points"  
   - "stability-index"  
   - "language-scope"  
   - "recursions"  
   - "other" -> describe as text  
- standard tag and level:  
 - "ISO 26262"  
     -> "ASIL A-D" + "QM"  
     -> "TCL 1-3"  
 - "DO-178C" -> "DAL A-E"  
     -> "TQL 1-5"  
 - "IEC-61508"  
   -> might not have tool level  
 - "IEC-62304"  
   -> "Class A-C"  
   -> might not have tool level  
- applicable environment? - TBD  
 - std  
 - core  
   or  
 - cloud  
 - local  
- usage level  
 - production  
 - research  
 - prototype  
- link to project  
- cost  
 - "free"  
 - "paid"  
- license  
 - "proprietary"  
 - ... open source license  
- support  
 - "community"  
 - "commercial"  
 - "none"  
- 3rd party support  
 - companies that offer 3rd party support or are willing to enhance it  
- developer is interested in providing commercial custom development  
 - yes  
 - no  
- last date when visited the project (we need a better word)  
- rust version? (does it specify a max rust version)`

`Another list for Companies building tools  
- link the tools for each company (if possible)  
- name  
- link  
- lis`t of tools (+ tags)  
```
