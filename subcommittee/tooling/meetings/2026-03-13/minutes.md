# Tooling Subcommittee Meeting on 13 March 2026 @ 3pm GMT

| Search Key | Description |
| :---- | :---- |
| \[todo\] | Action Item |
| \[decision\] | Something decided on |
| \[important\] | Key information |

## Agenda

1. Solicitation of notetaker  
2. Review [last time’s meeting minutes](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/580)  
3. Present new members  
4. Presentation of *mutation project work* by Zalan Balint Levi  
5. Tools-list website page PR [https://github.com/rustfoundation/safety-critical-rust-consortium/pull/578](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/578)  
6. Category discussion for mutest-rs tool: test-runner \=\> testing, or new category?  
   See: [https://github.com/rustfoundation/safety-critical-rust-consortium/issues/571](https://github.com/rustfoundation/safety-critical-rust-consortium/issues/571)  
7. Samuel Wright asks if we have “help wanted“ topics for the SCRC newsletter

## Check-in area

**Please add your name, and an emoji that describes your day.**

* Pete LeVasseur 🖖  
* Zalán Bálint Lévai 🤩  
* Oreste Bernardi 🪻  
* Arnaud Fontaine 😀  
* Manuel Hatzl  
* Tiago Manczak  
* Alexandru Radovici 🙂

 **Notetaker:**

* Pete LeVasseur

## Housekeeping section

## Tasks

* 

## Meeting Minutes

* Accepted last time’s meeting minutes  
* Intro of new members  
  * Zalán 👏  
  * Kartik 👏  
* Presentation of *mutation project work* by Zalan Balint Levi  
  * Zalán \- PhD student, working on mutation testing project last four+ years  
  * Bugs slip past, due to e.g. happy path, forgetting some edge case  
    * Coupling between tests and code happens  
  * Tests “good” only if they: capture all requirements, actually fail if code changes now violate requirements  
  * Mutation testing: changing the code in deliberate ways to make faulty program behaviors to search for where we’ve not yet covered in testing  
  * Mutations: small, subtle changes which mimic mistakes of experience developers  
    * Tests should ideally reject faulty behavior caused by mutations  
  * What about code coverage?  
    * Function completely covered by tests example of bitwise arithmetic of configurations  
    * However, no one checked if configuration was correctly checked; mutation mimics this subtle kind of error in programming  
  * Safety-critical standards do mention kinds of mutation testing:  
    * IEC 61508: Error Seeding for SIL 2-4 (Part 3, Annex B, Table B.2)  
    * ISO 26262: Fault Injection Testing for ASIL A-D, “Coding Mutations” method (Part 6, Table 8\)  
  * Using mutation testing on dependencies  
    * More confident about any given dependency  
    * Gives higher confidence in usage and choice of particular dependency when there are multiple options  
    * Could be used to convince relevant leadership about dependency of particular dependency due to mutation testing as a quantitative measure  
  * mutest-rs intro  
    * Build on rustc for compiler analysis and only for “interesting” mutations that are not caught by the compiler  
    * Call graph from test functions to “program” functions; only run relevant tests for each mutation which impacts it  
      * Helps make this faster  
    * Performing code mutations in Rust requires foresight; e.g. some may impact unsafe  
  * Performance of mutest-rs  
    * alacritty \- 79 tests; 1,808, \~60 seconds; with more threads \~11s, with some experimental features \~6s  
    * (more testing results shown, couldn’t keep up 😅)  
  * Using [mutest-rs](https://mutest.rs/)  
    * `cargo mutest run` like you would `cargo test`  
    * Web-based inspector `cargo mutest inspect`  
  * Why mutation testing for safety-critical?  
    * Changes to code will be in spaces where changes could have large impact  
    * Mutation testing can help find those gaps when changing code  
  * Future work  
    * Improving reliability by working with Rust Compiler Team  
    * Take what’s been learned on Rust analysis and code generation to other fields, e.g. for MC/DC tooling  
  * Q\&A:  
    * How can we define the single most common mutation errors? Statistics? Database?  
      * Mutation testing as a discipline is not new; dates back to work from the late 1980s  
      * Different domains, programming languages make things different, but there’s a consensus on more procedural programming languages on what’s most common and useful  
      * Part of the research is focused on analyzing which pieces apply to Rust; in lieu of such a database for Rust much of the work is building that database  
        * \~18 operators  
        * Swapping operators; e.g. addition to subtraction but need to do this in a Rust-aware way to note that some are not possible depending on the types  
        * Can enable/disable parts of the mutation testing framework; possible to scope this to areas of interest for your safety-critical setting  
        * Can also define own operator implementations; part of the design goals to enable extension if say some certain pattern happens  
          * If e.g. something is challenging to encode in the Rust programming language semantics  
          * E.g. “please don’t do this” to the team can be turned into one of these things to check via mutation testing to simulate those sorts of faults  
    * How deterministic is mutest-rs? Run twice, will you get the same result?  
      * Everything about mutest-rs is deterministic; even things like storing things in a hashmap doesn’t change the order of mutations  
      * Internal mechanisms have been implemented as a part of the design goal  
      * Tests themselves may not be deterministic  
        * In surveys across Rust open source repos hasn’t turned this issue up much in practice  
        * But if there are flaky tests, this can show up as noise in mutation testing  
  * Demo of mutest-rs  
    * Run on alacritty  
    * Took \~18 seconds in this case  
    * Get Rust Compiler-style warnings and errors with helpful guidance on how to proceed  
      * Get mutations for pieces of code under test  
    * Get a breakdown of particular mutation operators  
      * arg\_default\_shadow: tests whether dealt with a function argument at all; if not used clearly able to tell not exploring any code paths based on that  
      * Get listing of number of mutations  
      * Notes which were undetected  
    * Web-based inspector tool  
      * Shows pane / sidebar forms almost a todo list of what needs to be done and investigated  
      * Can click on test cases and get more details  
      * Able to see all the traces through the program, pieces of functions and hops through program which were exercised  
        * Works with macro expanded code, since built on top of compiler  
    * Q: Is there any study / mention in safety-critical standards on how to attach mutations to parts of programs or traceability guidance? Requirements traceability? E.g. “I’m violating this here, on this part of code, and these tests are relevant for this tests which were supposed to test these requirements.”  
      * Aware of two for Rust  
        * [tracey](https://crates.io/crates/tracey)   
        * [mantra](https://docs.rs/mantra/latest/mantra/)  
          * mantra is looking at statement coverage of tests already. so would already be based on the call graph  
    * Q: “Is my mutation enough?” Concern on if there’s metrics for the mutation. For safety-critical not so important, but understands that it’s not possible to mutate everything.  
      * If needs are specific/tailored you can turn things off and disable them  
      * Seeing how things break down per test is important to see “what value” there is per test  
      * e.g. on Alacritty there are a few tests which seem at surface-level that are not high value; may be able to prune or consolidate test suite based on these signals  
        * Writing tests is good, but also removing them can be as well  
    * Q: Combined into a binary and run, right? How does this work with unit and integration tests? Mutating source, building?  
      * Large engineering challenge to get integration test support working, since these are separate compilation units  
      * mutest-rs works as a replacement for rustc under the hood to produce binaries for mutation testing  
      * Unit testing is simple  
      * Integration testing becomes more complex; try to make use of as much of Cargo’s facilities as possible  
        * When modified compiler is run against integration test, start building reachability analysis via call graph across crates  
        * Use mapping and stable definition references, go back to original library writing test for and create “meta mutant” that’s a single dedicated library that attaches to this specific integration test suite  
        * End up reflectively analyzed in the library with dedicated, mutated one  
        * Honors that integration tests are separate compilation units  
        * If unit tests \+ 3 x integration tests, end up with 4 x final compilation units, just like normal  
    * Q: How does the packaging work for unit tests?  
      * Generated all up-front, then generates a single large piece of program with all the branching built in  
      * Allows for influencing which paths are taken at run time, just like the generated binary done normally for cargo test  
    * Q: Lots of combinations, which seems to make the analysis complex as mutants are created. Does it hurt debug cycles by combining together into a single binary for the mutation testing?  
      * When these are combined, it’s a fundamental constraint to toggle only one mutated code path to run at a time  
      * Imagine that there’s an internal switchboard of sorts, which allows for toggling of one switch at a time  
        * One test, one path, one mutation  
        * Create effectively a match expression which branches for each and every mutation including original behavior to allow for switching easily  
    * Q: How are teams in “real life” using this? Running locally to find more tests? CI for gatekeeping?  
      * Want to hear everyone’s experiences  
      * Been developing for \~4 years  
      * Part of it is that research is being built on top of Rust itself, but also building it for practical usage  
      * Always has been publicly available; only soft-launched this recently, e.g. since Rust Nation UK 2026 in talking with people  
      * Cannot give detailed answer; need to have others make use of it to gather up those experiences  
      * Gave a talk at Rust Manchester \~2 weeks ago covering similar topics and had people since then running against mutest-rs  
        * Some initial use in cryptography and some initial use showed useful here  
      * Really wants to have people to submit feedback, whether public or private  
      * Jon Gjengset offered up feedback on “build trophy case of issues discovered” to showcase usefulness  
* Samuel Wright asks if we have “help wanted“ topics for the SCRC newsletter  
  * Pete: I’ll make a Zulip topic to gather this up a bit  
* Tools-list website page PR [https://github.com/rustfoundation/safety-critical-rust-consortium/pull/578](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/578)  
  * Let’s all review and leave comments as needed so we can merge at the latest by next meeting in two weeks  
* Category discussion for mutest-rs tool: test-runner \=\> testing, or new category?  
  See: [https://github.com/rustfoundation/safety-critical-rust-consortium/issues/571](https://github.com/rustfoundation/safety-critical-rust-consortium/issues/571)  
  * For mutest-rs we’ll probably try to revise how we categorize and then if needed to a follow-up PR
