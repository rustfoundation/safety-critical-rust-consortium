# Tooling Subcommittee Meeting on 13 June 2025 @ 4pm GMT

| Search Key | Description |
| :---- | :---- |
| \[todo\] | Action Item |
| \[decision\] | Something decided on |
| \[important\] | Key information |

## Agenda

1. Present new members  
2. Review the Issue template for submitting new tools \- [https://github.com/rustfoundation/safety-critical-rust-consortium/pull/337](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/337) \- rendered version [https://github.com/rustfoundation/safety-critical-rust-consortium/blob/8bf4f8fe3b63a424c513630a1066335db6c45966/.github/ISSUE\_TEMPLATE/submit\_tool.yml](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/8bf4f8fe3b63a424c513630a1066335db6c45966/.github/ISSUE_TEMPLATE/submit_tool.yml)   
3. Review the initial procedure for submitting new tools \- [tooling new submission](https://docs.google.com/document/d/1hZGU5MCx_sb_8qEhww4l-KtLYyDNdQihQP7Tgtu4QSg/edit?tab=t.0)  
4. Review the initial procedure for deleting a tool \- [tooling new submission](https://docs.google.com/document/d/1hZGU5MCx_sb_8qEhww4l-KtLYyDNdQihQP7Tgtu4QSg/edit?tab=t.0)  
5. Tooling for checking for macro hygiene (Pete) \- came from coding guidelines [meeting](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/coding-guidelines/meetings/2025-06-04/minutes.md)

## Check-in area

**Please add your name, and an emoji that describes your day.**

* Oreste Bernardi??  
* Alexandru Radovici ??  
* Tiago Manczak ??  
* Pete LeVasseur, ??  
* Arnaud Fontaine ??  
* Sasha Pourcelot ??  
* Xander Cesari ?

**Notetaker:**

* Pete LeVasseur, ??

## Housekeeping section

* 

## Tasks

* See \[todo\] below ?

## Meeting Minutes

1. Present new members  
   1. Everybody here is known\!  
2. Review the Issue template for submitting new tools \- [https://github.com/rustfoundation/safety-critical-rust-consortium/pull/337](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/337)  
   1. Goal of PR: Transcribe items we brought up in last meeting to help capture tools coming in  
   2. Goal today: review and see if we need add / modify  
      * Suggestion: Entry for whether the tool has been used in some safety-critical context, which one and which level  
        * More of this information will be captured in the pull request when adding the tool and reviewed  
        * We could make use of [Pull Request Templates](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository) for follow-up?  
        * If itÕs a user could have Ònot sureÓ or similar on the drop down for the GitHub issue template  
          1. The kinds of information weÕd have in the table should probably be publicly available such as license and so on  
        * Idea: x0rw has [started](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/122) this concept in the coding guidelines  
      * \[decision\] Remaining fields to add \[todo\] Xander Cesari to update  
        * Name & email of maintainer  
        * License  
        * Platform support  
        * Multiple categories per tool (some tools have multiple features especially commercial)  
          1. Fixed dropdowns with  
          2. Text field  
          3. ?  
        * Checkbox: Industry  
        * Checkbox: Standard and to which level  
          1. Depending on the industry the tool itself may also need to be safety-qualified  
        * Checkbox: References if already in use for safety-critical industry to fulfill requirements of a certification process / assessment process  
3. Review the initial procedure for submitting new tools \- [tooling new submission](https://docs.google.com/document/d/1hZGU5MCx_sb_8qEhww4l-KtLYyDNdQihQP7Tgtu4QSg/edit?tab=t.0)  
   1. \[todo\] Make a PR opened right away from the issue submitted via the GitHub issue template  
   2. \[important\] ÒOne way doorÓ from issue \=\> PR, modifications made on PR will not reflect back to issue  
   3. \[decision\] Emphasize that we want to keep the process as async as possible  
      * Collect comments async on the PR  
      * Allow people to come and present about in the meeting as optional, as-needed step  
      * Have a Òlast callÓ label to signal last chance to raise objection via a Request Changes  
   4. \[todo\] Alexandru Radovici to move the [tooling new submission](https://docs.google.com/document/d/1hZGU5MCx_sb_8qEhww4l-KtLYyDNdQihQP7Tgtu4QSg/edit?tab=t.0) over to a Markdown file in the repo  
4. Review the initial procedure for deleting a tool \- [tooling new submission](https://docs.google.com/document/d/1hZGU5MCx_sb_8qEhww4l-KtLYyDNdQihQP7Tgtu4QSg/edit?tab=t.0)  
   1. Safety-critical moves a little slowly Ð is 3 months too soon?  
   2. \[important\] Rust tooling early on in the ecosystem could be moving fast  
   3. \[decision\] Interrupt-driven for modifications provided to us by e.g. maintainers  
   4. \[decision\] Regularly-scheduled clean-up of the tooling list every 6 months  
5. Tooling for taking Rust crate and outputs expanded macro version (Pete) \- came from coding guidelines [meeting](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/coding-guidelines/meetings/2025-06-04/minutes.md)  
   1. Seemed useful to make sure things are interoperable due to different levels of macro hygiene  
      * Not possible as the macro is treated as if in the edition it was written in  
      * Does not seem reasonable to have cross-edition macro ability to check this  
      * Not really possible to have a tool that works like a C preprocessor in Rust due to Rust editions  
      * Procedural macros \=\> can have differing levels of hygiene so the problem exists there too  
      * Declarative macros \=\> partially hygienic so the problem exists  
      * Suggestions for coding guidelines to recommend writing macros in a way that allows easy inspection of the generated code to e.g. determine unit test coverage  
        * Yes Ð makes sense. Forbid calling something which could change hygiene  
        * Different edition from the rest of the crate. Not really fixable.
