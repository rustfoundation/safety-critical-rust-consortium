# Meeting Agenda

Tooling Workgroup

| Search Key  | Description          |
|-------------|----------------------|
| [todo]      | Action Item          |
| [decision]  | Something decided on |
| [important] | Key information      |

**1\. Attendees**

* Alexandru Radovici (Moderator)  
* Alexandru Vochescu (OxidOS & moderator today)  
* Arnaud Fontaine (Airbus)  
* Tony Aiello (AdaCore)  
* Sasha Pourcelot ✨ (TrustInSoft)  
* Pete LeVasseur (Woven by Toyota, Eclipse uProtocol), 🕵️  
* Koppany Pazman (HighTec)  
* Julius Gustavsson (Volvo Cars)  
* Manuel Hatzl (Student)  

**2\. Agenda Items**

[Alexandru Vochescu](mailto:alexandru.vochescu@oxidos.io) will moderate this meeting.

1. Presentation of new members (if any) of the working group  
2. Address the comments and merge the initial version of the requirements x standards x tools mapping  document [https://github.com/rustfoundation/safety-critical-rust-consortium/pull/175](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/175)  
3. Clarify our goals after the in person meeting [Alexandru Vochescu](mailto:alexandru.vochescu@oxidos.io)please take a look at the meeting notes from the in person meeting  
4. How do we work closer with the coding guidelines [plevasseur@gmail.com](mailto:plevasseur@gmail.com)you might want to take this up?  
5. When do we meet next time?

**3\. Meeting minutes**

Notetaker: Pete LeVasseur

1. Presentation of new members (if any) of the working group  
* Manuel Hatzl \- first time attendee

  Works on the requirements traceability tool [https://github.com/mhatzl/mantra](https://github.com/mhatzl/mantra)

  that is mentioned in the list of possible safety critical tools

2. Address the comments and merge the initial version of the requirements x standards x tools mapping  document [https://github.com/rustfoundation/safety-critical-rust-consortium/pull/175](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/175)  
* Koppany Pazman \- HighTec compiler is ASIL-D certified for ISO26262  
  * ARM target is not certified yet  
  * DO 178 qualification not planned currently  
* Miri \- agree to call it an Undefined Behavior detection tool **\[decision\]**  
* [Verus](https://github.com/verus-lang/verus) \- folks generally in attendance are hearing about it for the first time  
  * **Note: Verus is a fork of Rust** \- from the 2023 paper introducing Verus: “We forked the Rust compiler to introduce additional hooks and typechecking rules. We then implemented Verus as a separate “driver” that links against the Rust compiler.” \[[https://arxiv.org/abs/2303.05491](https://arxiv.org/abs/2303.05491)\] **\[info\]**  
  * Mark as unknown with a ?, if later information obtained we can fill more in **\[decision\]**  
  * Suggest we look into it and revisit next week  
  * How to consider beta tooling?  
    * Should maybe not exclude entirely  
    * But if there are a fair amount of these tools, it could become too much a resource expenditure on the group to catalog them all  
    * Criteria (speculation / discussion)  
      * Usage in real-world projects?  
      * GitHub stars?  
      * Bar to join is low – maybe the maintainer of such a tool could join the Tooling Subcommittee and help maintain the tooling documentation **\[decision\]**  
    * Keep a Beta vs Stable label or column **\[decision\]**  
  * Reach out to Verus folks to let them come visit the group?  
* Proptest  
  * Not much input from the folks in attendance, mark with a ? for now **\[decision\]**  
  * Suggest we look into it and revisit  
  * Unsure of any standards with property-based testing requirements / mentions. In general formal methods are not considered in safety standards. **\[info\]**

3. Clarify our goals after the in person meeting [Alexandru Vochescu](mailto:alexandru.vochescu@oxidos.io)please take a look at the meeting notes from the in person meeting  
   * Quarterly Tool Report as an artifact produced by the Tooling Subcommittee  
     * Feels ambitious on timing at the moment, maybe every half-year?  
     * Timing can be flexible if needed, perhaps on an as-needed basis?  
     * Good to have some set cadence to stay accountable  
     * Current cadence \- every half year **\[decision\]**  
     * Use current format in this [PR](https://github.com/rustfoundation/safety-critical-rust-consortium/pull/175) for now **\[decision\]**  
   * Are we Safety-Critical Yet? website  
     * Let’s do it\! **\[decision\]**  
     * Website to catalog things needed for safety-critical  
     * Seems like a great idea to make it visible to wider Rust and safety-critical community  
     * Need to check on domain availability\! **\[todo\]**  
     * Would be good to hear from folks in the community doing work on cataloging  
       * Some work on-going at some members’ on various levels of cataloging for safety-critical usage  
   * Requirements / relations subcommittee  
     * Any updates?  
     * None aware of **\[info\]**  
     * Alex R. following up in next few days with Joel Marcey for formation of subcommittee **\[todo\]**  
   * Sponsorship of Safety-Critical Rust Consortium  
     * Any impact on holding the in-person meetup at RustWeek?  
       * Unclear  
     * Concern over possible “pay to play” look  
     * Scope appears as funding for the physical, in-person meetup

4. How do we work closer with the coding guidelines [plevasseur@gmail.com](mailto:plevasseur@gmail.com)you might want to take this up?  
* Cross-pollination of members between subcommittees  
  * Suggest folks attend each others’ meetings  
* Are we safety critical yet?  
  * Work together  
* Coding guidelines input for data driven prioritization  
  * If available, please feel free to share\!

5. When do we meet next time?  
* Every two weeks works **\[decision\]**

6. Roundtable  
* None
