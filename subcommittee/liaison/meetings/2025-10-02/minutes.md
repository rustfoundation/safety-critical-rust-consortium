# **Liaison Subcommittee Meeting on 2025-10-02 @ 1600 BST / 1700 CEST / 1100 EDT**

[Link](https://www.worldtimebuddy.com/?qm=1&lid=14,12,1850147,5&h=14&date=2025-10-2&sln=16-17&hf=1) to meeting time in common time zones.

| Search Key | Description |
| ----- | ----- |
| \[todo\] | Action Item |
| \[decision\] | Something decided on |
| \[important\] | Key information |

## **“ISO26262 and Rust”**

## **Agenda**

1. Solicitation of notetaker  
2. Introduction of speaker  
3. Broad scope introduction:  
   * What is functional safety?  
   * What are the basics of achieving functional safety for a product?  
     * Including ASILs  
   * How tools can assist  
     * Why they need to be certified  
4. Question and answers  
5. Round table

## **Check-in area**

**Please add your name, and an emoji that describes your day.**

* Andrew Fernandes ☕  
* Tshepang 🙂  
* Samuel Wright  
* Oreste Bernardi 🛟  
* Douglas Deslauriers 😷  
* Pete LeVasseur 🚗🦺  
* Car  
* Joni Pelham ✈️ safety   
* José Rui Simões 🚘  
* Sabah Kabbou ![Veste de sécurité][image1]![Automobile en approche][image2]  
* John Vishnefske🚀   
* Félix Fischer ☕  
* Xander Cesari 🍳  
* Will Cunningham ☕  
* Ana Hobden  
* Christof Petig 🚲  
* Manuel Hatzl  
* Max Jacinto 🍀  
* Olivier PHILIPPE 🚘  
* Samuel Preston 🐱‍🐉  
* Orson Pessin🍺  
* David Wood 🦀  
* Tiago Silva ☕  
* Nicholas R. Smith ⚡🔌  
* Niko Matsakis 🎃  
* Alex Celeste ☕  
* Gideon Mueller  
* David VomLehn 🚀  
* Daniel Szucs 🌀👽

**Notetaker:**

* Alex Celeste ☕

For tips on how we take notes in the Safety-Critical Rust Consortium, please see the [Meeting Notetaker Role](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/docs/notetaker-role.md) doc.

## **Tasks**

* Search for the \[todo\] markers

## **Meeting Minutes**

* Solicitation of notetaker (Alex); introduction of Jill Britton  
* Jill to introduce herself and the talk: starting at a basic level in order to ensure level field  
* Starting with What is meant by Functional Safety  
  * Protective measures between system, users, and hazards caused by failure of system  
  * Many industry-specific standards:   
    * IEC 61508 is the parent ISO standard for functional safety, with industry-specific child standards:  
      * ISO 26262 for Automotive, well-known, main subject of this presentation  
      * IEC 62279 for rail  
      * IEC 61511 for industrial processes  
      * IEC 61513 for nuclear power plants  
      * IEC 62061 for other machinery  
    * DO 178B/C \- Aerospace, independent of ISO  
  * Same fundamental core used for analysis of all of these except Aerospace: software and tools used must be shown to be safe to a similar end  
  * *Anything* used in development is a “tool”  
* How we go about achieving FS  
  * Using ISO 26262 as an example (because the basics are the same) \- find *evidence* that the requirements of a Standard have been followed  
    * “Principle” is a statement of a requirement; ASILs list whether a requirement is highly recommended, recommended, or not applicable  
    * Most such standards are language-oriented and look like they were designed by C users (because they were)  
      * *“No unconditional jumps”* and  
      * *“Restricted use of pointers”*, for example  
    * Many asterisks on certain requirements: justifications can be provided for different approaches to meeting or not meeting  
    * These requirements apply to a product rather than to a tool, e.g. a braking system in automotive meets these in order to certify compliance; a tool does not comply to the standard, but helps users write product code which complies  
    * “The language handles this automatically” can be one piece of evidence of meeting a requirement, but there must be some kind of evidence  
  * Safety Integrity Level / ASIL applies to most of these standards, ranked by criticality: D for a braking system, B for something less critical  
    * Safety standards *do not* specify a particular language (do not mandate C despite history)  
    * MISRA etc exist to mitigate insufficiencies of the language \- these would not be needed if the insufficiencies did not exist at all  
    * Static analysis is recommended (but not compulsory) in order to both:  
      * Automate compliance with Guidelines, *and*   
      * To check quality of the code  
    * Standards *do not* mandate full compliance to Guidelines  
    * You don’t have to enforce guidelines that are not relevant, but in that case, **you do have to prove they are not relevant**  
      * “Strong typing” is an example of a requirement that can easily be determined to be provided by a language because it is usually a language feature.  
* How tools can assist  
  * Compilers, static analysis tools, and similar; are *certified* to meeting FS requirements  
  * Users need to provide the evidence tables of meeting the process: certifying the tooling means the user does not need to re-demonstrate the process requirement is being met; a product developer *can* re-do this for any tool including a non-certified tool, but would have to prove it fulfils the process requirement  
    * Tools are classified within 26262 according to impact and error detection, giving a “tool confidence”: a static analysis tool cannot introduce errors, but may miss existing ones, and these are reflected in the impact and detection  
    * Users can add additional checking to make up for any deficiencies \- the individual tool will remain at the given TD level, but the overall system will become more robust. Using two tools is a common practice though is still not mandatory  
    * “Confidence through use” is one possible measure of tool quality  
  * To certify a tool: need a certification body, usually TUV or similar, who will need to assess it if new, or examine what has changed  
    * For instance: for a static analysis tool, the whole tool could be assessed, or just some of the checkers  
    * Certification applies to a specific version, although there is some flexibility for point-releases  
    * Requires evidence of testing that the tool behaves as documented  
    * Creation of a Safety Manual  
    * “Are these manual processes or can they be automated e.g. by CI/CD?” recording this is exactly what the documentation should include \- this is how “we” do it and are recorded as doing so; how *the user* runs it is up to them to integrate  
    * In Aerospace: lower toolchain qualification for a tool that is operated by a human running a checklist, higher threshold for an automated tool \- so that human signoff remains a part of the process (this can be counterintuitive to the mindset of a software engineer, and where the appropriate level of automation is)

## **Questions**

* What parts of the language should a Guidelines document talk about?  
  * Every part? Can we explicitly not consider parts of the language during Guidelines development?  
    * Yes\! **Subsetting**[^1] is encouraged  
* Safety elements out of context?  
  * \[conversation moved on\]  
* When an element has changed how much needs to be re-certified?  
  * Depends very much on the part of the system that is being modified (colour of vehicle vs. new engine)  
  * For example, QAC was re-certified after adding support for MISRA C++  
* Automated tests \- what matters is not *how* but the result of the test? Could it happen that different approaches that result in testing incorrectly give wrong results (e.g. difference between development and production)? Does there need to be validation for the test cases themselves to ensure consistency of results? AN audit system associated with testing?  
  * There is a requirement in DO to split responsibility between writer of test cases and requirements for them, ensuring multiple pairs of eyes  
  * Need to specify the configuration very tightly \- should not be able to be different from production if that is what is to be tested  
  * Needs to be repeatable  
* State of the art and of acceptance in the safety community? Not all guidelines are the same \- say an original set of guidelines for C that are *not* MISRA and are homegrown \- is this accepted by the community? Can it fulfil the ISO requirement?  
  * If you write your own guidelines, they need to help to meet the listed requirements  
  * It is OK to write new guidelines but they need to explain evidence for how they help with that; something someone has already written will already demonstrate this  
* Assessors like TUV-SUD are not a government agency \- they are a third-party; DO-178 is government-regulated (FAA et al) and is mandatory for aircraft at all  
  * You do need to meet ISO26262 to put a vehicle on the road, but the auditing of that fact is independent  
  * DO-178C is itself recommended *by* the FAA; the FAA accredits designated representatives who approve your process \- it is theoretically possible to not follow DO-178C although not very feasible  
* As this applies to Rust and use in Safety Critical?  
  * The important thing remains to know what its limitations are and where they are, you still need the solid background, still need support from the community and integration into the pipeline  
* Rust is thinking a lot about language specification at the moment, where does a language Standard fit in, and how does its evolution over time affect this process?  
  * This will need an entire separate hourlong meeting\!  
  * \[TODO\] follow up on this  
* “Has anyone found openly available examples of Safety Manuals and accompanying documents? In my experience that is usually NDA'd”  
  * https://public-docs.ferrocene.dev/main/safety-manual/index.html

## **Additional links**

* Article with flowchart, explaining how a tool becomes determined to be at a certain ISO 26262 Tool Confidence Level: [ISO 26262 tool qualification \- When and how to perform it](https://www.btc-embedded.com/when-and-how-to-qualify-tools-according-to-iso-26262/)  
* [Ferrocene Documentation › Safety Manual](https://public-docs.ferrocene.dev/main/safety-manual/index.html)  
  

[^1]:  **Subsetting** a language here means to define and use a specific subset of a larger language. Safe Rust is a subset of Unsafe Rust. MISRA C, for example, specifically asks users to subset C in order to more easily (and decidably) satisfy their safety requirements.

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAC4UlEQVR4Xn2U30tTYRjHLeg/6CqLSOgHtUCbPxtTR+rmnNbcZrP0KMtpRqVYuDLtooIo6MKCyIvoqoSomyDKq0IpHTp/EGgm/shKBKVmhEVz59v7PNtx5+js4st7znk/7+d5zst5T4K50ZagzszVhi00Bp1Zm/8XNauO5mbRfXzTRKulZWxkcnRasgwMG6XeIUN1b8BQ9V6dIbvZTwweFDxR5HGFlNCVxNCY/zfw2I05qRyj6V58SKvFcJoXfXoPXmTqIfuSMD38F3h4FBsKqbtP9y5uJZiFAiapIhxIrcGbFAnfapNYONkfBu5bgacVdvWra7qb9JkWcDk5Imw3A51e7kzp7tmeMiy36GRiWHj7CPDcg7gdUpWfF/aB4Im+lQjccRKBlDIW9hyqwqOdRTyvCMPXcrho0OvRa4S0D4oMvsOR6q1G4I6TF9HrvtSdwETJDp7XMHfLWboqpL2j7kKNB1bhqX5Erm+Ucpe0d9RdqG4v0GTUMPJ1G0vlzqpd1Bh3N37J+hpnDUBzHi9gmBa2ljA8J+nRbdiNcL0uvI7x2SKF2+09LKQOp+rMgyxssoBGhvm+mGHqfj5/G1CTEYexRArftA6RKyYkuD4fqMvGzAB4xPlCoM3Jr8rCikzBFPIcCxXGZ48jZFgIPTkRoRhxWlT2udYL1Qzdk7BNJaRjBreYrBTtV0ZhMeKUEDa5sCLpMG/cDjiyxLM4zDmR5qLBOEKxwe4o7M6LL2QmL8pEhWdcWmFX57vAx7d/MOsHh+Cv0XwfB750B9F1qwsjr5ZkNUOjwvyYl2PCWYcpgNxkGcXidKyN6Chk2Y/Fg4nYmLHQVkSE9O18dpr7kSu+Kas4WrYSbTwulXADptwRE9IpCTrMHbKhAMgWkya7NqXH8Cs3GQsZJjCzdp4iipCDXKtneSld6ljWS/7lVGkslurRKXeDiyoTR9f0TMOINbRW+S9q/jZrf5bK83jXSmiN+vk/0ICjr06GXDcAAAAASUVORK5CYII=>

[image2]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAB7klEQVR4XmNwL/BhoCbGEKAUYwhQijEEKMUYApRiDAFKMYYADE/ydmdEFyNGDkMAhC/5+jJdMXM58d3M4/83M3cw/mziBse/3EJPgNSg68NpYPaUMyyKc///k5/1/z8My039B8cgOXQ9OA0EGWay5d9i9c3//yuvx41BakBq0fVjGKgia5ftcf//f4+bEOx2BRW7XkBgkFp0/RgGmk3f+tnr4///3l///wfRIOzxDgm/hGKgpSC16PrhjI25HcyXvAp0X5kF/39uHf4fRr9xiPr/yR6C3zvEgPkgORAN4oP0gPRiGAjCf+4Vv/3zIOH/R838/6/OfPv/3L3sv7ygNxhrcLv+l+c2+/8joun/q5u///9zzv//5Urwf5AerC4E4f/vi////5X6/65s9f/3rz/9v+rb919JK/S/uorvfzV5t/9SfLr/Pxcu+w8CX4y6gWQhGOM08Jh587/Lyh3/L+v2/IfRzwwn/n9uNu3/O8vZYAxig8ReO84E8x9a9uI2UEXU5n9L3GIUXBs5+//snnW/QbgjZdl/GO7JWg7GRqouuA0EhZEOp+d/eV6jD8jiUxs3bgNhZDElfov3ILWgYMBqICgrOWslhtoIxW73Vsh2QFaEDXvL59mD1IL0IGdDFEX6qv7MMIxuADrGpRYAivZitRBTt4cAAAAASUVORK5CYII=>