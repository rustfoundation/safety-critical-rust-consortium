# Tooling Subcommittee Meeting on 27 June 2025 @ 4pm GMT

| Search Key    | Description          |
|:------------- |:-------------------- |
| \[todo\]      | Action Item          |
| \[decision\]  | Something decided on |
| \[important\] | Key information      |

## Agenda

1. Present new members  
2. Tooling for checking for macro hygiene (Pete \- from last time) \- came from coding guidelines [meeting](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/coding-guidelines/meetings/2025-06-04/minutes.md) \- we did not finish this discussion  
3. Review the initial procedure for submitting new tools \- [tooling new submission](https://docs.google.com/document/d/1hZGU5MCx_sb_8qEhww4l-KtLYyDNdQihQP7Tgtu4QSg/edit?tab=t.0)  
4. Woven has offered some engineering work for the Tooling Subcommittee what could the do?
   
   ## Check-in area
   
   **Please add your name, and an emoji that describes your day.**
* Alexandru Radovici 😃  
* Tony Aiello 😮‍💨  
* Manuel Hatzl  
* Xander Cesari 🌶  
* Orson Pessin 🇫🇷  
* Tiago Manczak
  **Notetaker:**
* Xander Cesari
  
  ## Housekeeping section
* ## Tasks
* See \[todo\] below ⏬
  
  ## Meeting Minutes
* No new members  
* Macro hygiene discussion postponed until relevant members are on a call  
* Review procedure for submitting new tools  
  * Procedure:  
    * GitHub issue template from template  
    * Opening the issue creates a PR  
    * The PR will require two approvers to merge and will be open for 15 days  
    * Upon merging the tool will be added to the database  
  * Every 6 months we will perform a “tool cleanup”  
  * Who would be assigned to the PR?  
    * Two members of the tooling subcommittee, specifically who didn’t open the PR  
  * What should be in the assessment form that both reviewers have to fill?  
    * Most criteria should be about whether we have the correct information to track it. Do we have a point of contact? Is it maintained? Is it a commercial tool or an open source tool?  
    * This is a platform for a tool maintainer to promote the usefulness of their tool to safety-critical developers so additional info on functionality, applicability to various standards, etc is for developers to assess the tool not for the consortium to approve it.  
  * Merging PR for the GitHub issue template requesting a tool be added to the database  
* Woven has offered some engineering work for the tooling subcommittee. What might we want?  
  * Work on the website  
    * The JSON \> website database workflow for tool display  
    * Generate the table or list of tools on the website  
  * Cargo/clippy functionality to generate code quality reports: a document showing which clippy lints were suppressed, which passed, and which failed  
  * MC/DC coverage related topics: [grcov](https://github.com/mozilla/grcov) has no ability to show MC/DC coverage so would be interesting to have that functionality  
  * Upstream rustc has no support for pattern matching in MC/DC. That would be great to make progress on.  
    * \[todo\] [alexandru.radovici@oxidos.io](mailto:alexandru.radovici@oxidos.io) to ask Woven team what they’re blocked on in upstream for MC/DC  
* Other agenda items?  
  * Going once?  
  * Going twice?  
* For next time, everyone start thinking of safety-critical tools to add to the database\!
