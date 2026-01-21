# Tooling Subcommittee Meeting on 16 December 2026 @ 4pm GMT

| Search Key | Description |
| :---- | :---- |
| \[todo\] | Action Item |
| \[decision\] | Something decided on |
| \[important\] | Key information |

## Agenda

1. AbsInt Tool Walkthrough  
2. Rust Project Goals 2026  
   1. [Investigate Clippy Extensibility for Custom Lints](https://hackmd.io/@plevasseur/r199Y_lS-l)  
      1. [Zulip Thread](https://rust-lang.zulipchat.com/#narrow/channel/257328-clippy/topic/Tentative.20Rust.20Project.20Goal.20for.202026.20-.20Clippy.20Extensibility/with/568314216)   
   2. [Implement and Maintain MC/DC Coverage Support](https://hackmd.io/@plevasseur/H1eS3KdxHWl/edit)  
      1. [Zulip Thead](https://rust-lang.zulipchat.com/#narrow/channel/546987-project-goals.2F2026-workshop/topic/mcdc-support/with/568427319)  
   3. Specify Undefined Behavior for Safety-Critical Rust  
      1. Pete still working on this doc  
      2. Meeting with RalfJ & Niko about it ahead of releasing it

## Check-in area

**Please add your name, and an emoji that describes your day.**

* tshepang  
* Pete LeVasseur ⛑️🙂  
* Oreste Bernardi ☕  
* Alexandru Radovici  
* Manuel Hatzl  
* Tiago Manczak  
* William Cunningham ☕🧥  
* Kaneko Satoshi

**Notetaker:**

* Pete LeVasseur & Oreste Bernardi

## Housekeeping section

* 

## Tasks

* \[todo\] Manuel takes the action to review AbsInt tool pull request.

## Meeting Minutes

* AbsInt Tool Walkthrough  
  * Static analysis using Abstract Interpretation (computer science formal verification technique)  
  * Today’s tool discussion:  
    * StackAnalyzer  
    * aiT WCET Analyzer  
    * TimeWeaver  
  * StackAnalyzer  
    * Works with Rust, since operates at the binary-level  
    * Computes safe upper bounds of stack usage of tasks for all inputs  
    * Uses Abstract Interpretation  
    * May be some dialing of knobs required, e.g. if recursion or dynamic calls used  
    * Typical architectures available with typical tool couplings, e.g. dSPACE TargetLink  
  * aiT \- Static WCET Analyzer  
    * Works with Rust, since operates based on compiled down, architecture-specific instructions  
    * Sends machine-level instructions through microarchitecture analysis using Abstract Interpretation  
    * Works most consistently on those processors which have reasonably specified models, with the right level of execution pessimism  
  * TimeWeaver \- Hybrid WCET Analyzer  
    * For when the processor you’re targeting doesn’t have a timing-predictable model  
    * Has both static value and worst-case path analysis based on non-intrusive instruction-level tracing  
    * Runs multiple traces and samples from them to find maximum time over all of them to build the local timing statically like aiT does  
  * Rust support?  
    * All binary-level tools support Rust, since they rely on the final linked binary  
    * Some limitations, e.g. traits might lead to an increased effort around annotation  
  * Many compilers listed, couldn’t find specifically related to Rust, how is qualification support?  
    * Qualification kits are offered for all tools  
    * In principle compiler independent of the compiler, since working with compiled binary  
    * May begin relying upon it, for bounded loops, so then have compiler-specific add-ons for generic qual kit  
    * Developed on-demand of customer, i.e. available today for Rust for the generic case  
    * Separate contracts for those on-demand services?  
      * For tool license need supported compiler to be chosen, already supported  
      * Minimal version: no minimal version for Rust compiler / LLVM backend  
  * Manual annotations  
    * Based on ELF information?  
    * Mangled versions?  
    * AbsInt has a demangler  
    * Don’t want to have user to specify addresses, so try to offer symbolic annotation scheme, even in Rust  
    * Can copy+paste into specification file, then can tweak from there  
* Comments from members in regular call:  
  * aiT tool WCET has some limitations but it is a complementary to other tools.  
  * A member commented that the tool is worth adding to the tools list.  
* Shall we ask for a pull request to the tool vendor ?  
  * Pull request assigned for review.  
  * After review  tool vendor will be asked for review  
* A member raised questions related to the definition of “undefined behaviour" in unsafe scope.  
  * Pete, Robert, Niko and Ralf will meet to understand how to address this topic.  
* 