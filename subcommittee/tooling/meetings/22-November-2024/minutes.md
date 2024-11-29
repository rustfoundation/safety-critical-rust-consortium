# Meeting 22.11.2024

## Attendees
- Tony Aiello (AdaCore)
- Arnaud Fontaine (Airbus)
- Johann Hemmann (Ferrous Systems)
- Bogdan Genis (OxidOS)
- Felix Gilcher (Ferrous Systems)
- Julius Gustavson (Volvo Cars)
- Tiago Manczak
- Jordan McQueen (Woven by Toyota)
- Orson Pessin (OxidOS)
- Sasha Pourcelot (Trust in Soft)
- Alexandru Radovici (Moderator)

## Subjects

### Expectations
The summary of interest points of this group is:
- creation of a (certification/qualification) tooling shop list
- define how these tools should be provided, two most obvious solutions being either inside the rust toolchain, either as separate tools
- what should be the priority for the develoment of these tools
- what would be a timeline for these tools
- is the borrow checker enough or do we need a 3rd party tool
- is there a need for Rust profiles so that only a subset of the libraries could be certified
- which set of libraries should the group try to provided tools for (`core`, `alloc` or `std`)
- what are the certification standards that the group should aim the tools for (ISO26262, DO-178)
- what level of compliance do we want the tools to be able to be used for (ASIL level, SIL level)
- the group might want to make sure the tools cover the overlapping of several standards
- do we consider the rust compiler in scope for these tools, meaning do we expect to be able to ask the Rust Project to implement some of them or do we want to implement some of them and sending pull requests to the compiler

The general expectation is that these set of tools should cover the Code Guidelines, developed by the coding guidelines subcommittee.



### How do we work
The group tentaively decided to meet every two weeks. Until all things are put in place, the group will keep the weekly meeting.

The group decided that most of the works should be performed asynchronously.

To encourage open discussions, the group decided to work under the [Chatham House Rule] (https://en.wikipedia.org/wiki/Chatham_House_Rule).



### Needs

Please fill out before our next meeting the type of tools that you would be interested.

- MC/DC tools
- Coding standard verifier
- Requirement tracability tools
- Tools do deal with unsafe code - verify it does not break the invariants
- Source code to obj code tracing - connect the code to the binary
- SBOM generation
- Defect management (if a comp version has some defect, used for recalls)
- Software supply verification

## Next Meeting
The next meeting will be on 29.11.2024.
