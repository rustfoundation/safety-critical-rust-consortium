# Tooling Subcommittee Meeting on 04.04.2025 @ 4 PM GMT

| Search Key  | Description          |
| ----------- | -------------------- |
| [todo]      | Action Item          |
| [decision]  | Something decided on |
| [important] | Key information      |

## Agenda

1. Welcome new members

2. Discussion about the feedback form [State of Safety Critical Rust Adoption Survey · Issue #258 · rustfoundation/safety-critical-rust-consortium · GitHub](https://github.com/rustfoundation/safety-critical-rust-consortium/issues/258) - Xander Cesari

3. Discussion about the contents of the arewesafetycriticalyet.org website - Alexandru Radovici

4. Discuss the state of the safety critical tools table [[tooling] State of the safety critical tools by alexandruradovici · Pull Request #175 · rustfoundation/safety-critical-rust-consortium · GitHub](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/175)

## Check-in area

Please add your name, and an emoji that describes your day.

- Xander Cesari 🗒️

- Munawar Hafiz, 🙂

- Pete LeVasseur, 🏃

- Oreste Bernardi

- Alexandru Radovici 🙂

- Joel Marcey 😮‍💨

- Tony Aiello 😮‍💨

- Arnaud Fontaine 📱

Notetaker:

- Xander Cesari

## Housekeeping section

## Tasks

- Integrate survey question suggestions and feedback, create a PR for survey instead of a GiHub issue

- Get a framework for [https://arewesafetycriticalyet.org/](https://arewesafetycriticalyet.org/) website up

- Accept changes and merge ‘state of safety critical tooling’ PR

- Xander to submit notes as PR

## Meeting Minutes

- Sidenote: there’s still an open PR for the state of safety critical Rust tooling. Is that ready to be closed?

- First agenda item: PR feedback on the state of safety critical Rust adoption
  
  - Xander outlined the safety critical Rust adoption survey - the purpose, the timing, the general questions
  
  - What about timelines to certification? People looking at Rust want the same kind of timelines to certification in Rust as they would have got in C++. They might want a 6 month certification timeline that just isn’t realistic in Rust. 6-month-to-certification seems to be standard.
  
  - Whether we plan to merge any of this content to the repo we should use a PR so we can get granular feedback inline on each question etc. Then people can write suggestions on specific questions.
  
  - Add RISC-V to hardware targets.
  
  - We should be specific with tooling. For example, static analysis can be very different tools. Profiling should be a tooling mention, as well as code coverage. Also should ask for tools that may exist in Rust but users aren’t happy with.
  
  - Ask for existing tools they use in a text field so respondents can list specific tools they’re using.
  
  - Should we maybe not have specific tools but have the whole thing a text box?
  
  - In the list of ‘what is the primary blockers to using RUst in your role’, we’re missing a box which is “training”.
  
  - We could also improve the survey by asking about the features they’re after instead of just focusing on the tools. So are you looking for linting, performance profiling, code coverage, memory safety, etc?
  
  - MISRA isn’t technically a standard it’s a coding guidelines, as is AEC, cyber security coding guidelines, etc. Maybe break out to a separate question on coding guidelines.
  
  - Also the different levels of each standard are very different - ASIL B vs ASIL D are different requirements for tools and such. Maybe should ask after each one.

- Second agenda item: arewesafetyyet.org website content gathering
  
  - What should the website specifically contain? That changes the framework and layout of the website.
    
    - Use case: I am a user, a safety critical Rust developer, and now I want to know what’s available in the Rust world. So we should list various tool vendors, grouped by category. 
    
    - We could also list processes specifically to Rust, though this is difficult.
    
    - A list of consulting/training/services companies.
    
    - We should have an open PR process for adding your company or tool to the website.
    
    - The website should also promote the Safety Critical Rust Consortium as well. Copy some stuff from the README.md. Potentially list members / member companies. And the work that it is doing - e.g. Coding Guidelines.
    
    - We can make as many repos as we want but should the website have its own repo? Initial assumption was that the website would live in its own repo.
    
    - Initially thought the website would be a nicer UI for getting an update on what the safety critical consortium is doing, for people who don’t want to deal with Git or go dig into GitHub. Adding the list of tooling/companies is a nice addition though.
    
    - Might be good to just get something minimal up.
    
    - The [https://www.arewelearningyet.com/](https://www.arewelearningyet.com/) site is pretty minimal, might be a good starting place. As is [https://areweguiyet.com/](https://areweguiyet.com/) with the filtering tools by category.
    
    - But what are the categories to filter on? We’ll just have to figure it out as we go.
  
  - What technical platform?
    
    - Some of these websites are open source, could we just start with one of them?
    
    - Docs.rs seems perfect for this, it supports markdown which is the format of many meeting notes and minutes.
  
  - Let’s keep the pressure low, get something out there, and iterate as we go!

- Third item: state of the safety critical tools PR. 
  
  - [[tooling] State of the safety critical tools by alexandruradovici · Pull Request #175 · rustfoundation/safety-critical-rust-consortium · GitHub](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/175)
  
  - HighTec LLVM compiler is ASIL-D certified
  
  - Miri detects undefined behavior, can be added under Undefined Behaviour Absence
  
  - Verus may be in beta but seems useful.
  
  - Proposal to have relatively relaxed requirements for tool maturity in this list; any open source project with decent velocity should be added so that someone looking for a project to contribute to might find them.
  
  - Proptest has been explored by consortium members and seems to be useful enough to add.
  
  - Coq-of-Rust is a mathematical requirements language that Rust code can be translated into. It can be really difficult to maintain this codebase since it has to be retranslated every time changes to the Rust codebase are made. It’s really interesting but cumbersome, likely worth adding.
  
  - Maybe we should document whether a tool is commercial or open-source and if it’s open-source what the maturity level is?
  
  - Maybe we should have a procedural way to continually gather new tools? An agenda item at the beginning of the biweekly meeting or a GitHub issue process by which someone can introduce a new tool to the subcommittee?
  
  - Alexandru will make these changes and get the PR merged!

- Any other items?

## Material

Any material to read before the meeting should be included here.
