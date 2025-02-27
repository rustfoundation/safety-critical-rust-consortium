## Meeting Minutes

* Acceptance of previous meeting minutes  
  * Quickly reviewed \- not merged to Github so needs to be merged  
  * Minutes were accepted  
* Reviewed housekeeping rules  
  * No recordings, no AI transcriptions, use Chatham House Rule for notes, limit invites to members  
  * Agreed, no objections  
* `unsafe` Formulate Chapter Material Task Force \- report (Markus, Jonas, Pete)  
  * ABI & FFI  
    * Open PR182 for the FFI and ABI, comments are welcome  
    * Ongoing   
      * Started work on calling conventions  
      * What are sources of unsafe  
    * Propose another document  
      * Start of coding guidelines doc  
      * Would be the starting point for rules  
        * Could give guidelines on when a function needs to be unsafe  
        * Could then become a clippy rule  
      * Try to make a template for one rule  
      * Maybe also scaffold out the overall layout of the guidelines  
      * Need a mapping to SAE and MISRA, we cannot use those guidelines directly  
      * Learn unsafe Rust is a specific document, rules should be in a more general location.  
  * Intrinsics  
    * Some work done, teaching material needs work.   
    * Currently a guideline, explaining where to find intrinsics, will be reoriented to become teaching material  
  *   
* `unsafe` Practicum Chapter Task Force \- report (Joni)  
  * Intro chapter to learn unsafe Rust  
  * Author not in call, so no update  
  * **TODO:** Pete \- follow up offline  
* Safety Pamphlet \- progress (Andrew Fernandes)  
  * Thinking has been done, not so much writing  
  * unsafe as Rust keyword vs unsafe as “don’t do this” vs Safgety Critical  
  * DO-178 goes to lengths to reiterate that this is *not* a safety critical standard \- it only lists objectives  
  * Struggling to decide how to map the objective to Rust guidelines  
  * Round the table  
    * Expectation is to solve the ambiguity \- what does Rust unsafe mean vs Safety critical safe \- a clear definition would be useful  
    * Maybe some typographical standard could help  
    * This is maybe “what are we covering in the coding guidelines” \- answering this question is helpful to define the scope for the coding guidelines  
    * Would like some headlines for what areas other than unsafe do we need to think about  
      * Could be broad \- then decide what to tackle and what to not tackle  
      * Types of arithmetic  
    * A use case is “I am writing a application for some specific guideline” \- I would like to have a guideline to understand what do I need to do in Rust for that particular standard.  
      * Is the pamphlet enough, or is that covered somewhere else  
      * Maybe we need to write what is *not* covered by the pamphlet  
    * Useful to talk to multiple audiences, some from Safety Critical Aero / Auto \- vs wrote a lot of Rust, new to SC. Be a bridge into SC  
      * Talk about what SC means, where does Rust fit and how  
      * After reading the pamphlet, you should understand how Rust and SC fit together  
    * There are many layers around safety  
      * Software vs Hardware vs Language  
      * Maybe at some point \- could also elaborate on this  
  * Will start simple  
    * Get something in today, to get discussions started  
    * Probably be called something other than Safety Pamphlet  
* GitHub board walkthrough \- prioritization, way of work, wrap-up of Learn unsafe Rust contributions (Pete)  
  * Priorities P0-P3  
    * P0: Need to ship  
    * P1-2: Need to ship, but not critical  
    * P3: Should do, can wait  
  * Reviewed the current content of the board  
  * XL issues will need to broken into smaller chunks. Work will be tracked on smaller work items.  
  * Current prioritization makes sense and was approved  
  * [https://github.com/rustfoundation/safety-critical-rust-consortium/issues/188](https://github.com/rustfoundation/safety-critical-rust-consortium/issues/188)   
    * Plan is to start with the Rust lang book \- then add safety guidelines for each chapter in the language book  
      * Goal is not to make it certifiable \- but to make it a starting point for someone in the industry to use the guidelines as a start point for certification arguments  
      * Need to be careful of not restricting the language *to* much  
      * Need to communicate intent \- that some feature is not recommended for safety, it can still be perfectly good in a “normal” application  
      * The guidelines would be the reference. Pamphlet and “learn unsafe Rust” is for understanding and would reference the guidelines.  
      * Should be small sample and rationale in the guideline  
    * Chapters start empty / or with a TBD.  
      * Then add sections wherever safety critical aspects need to be considered  
    * Proposal: Use the reference instead of the book  
      * Accepted as a good idea, then some discussions back and forth  
      * More people are familiar wth book than reference  
      * Need to devide  
    * Final goal should be complete as a certification input  
      * Agreed \-  as a stretch goal  
      * Initial goal is to have *something* published  
    * Do we categorize guidelines Ilke MISRA mandatory / recommend / etc  
      * Undecided  
    * Reviewed the definition of the issue  
      * Book vs Reference  
        * Opinions are divided  
      * Chapters:  
        * Could be like book  
      * Conclusion:  
        * Guidelines should cover Language Reference  
        * Chapters could be like book

**Action items:**

- Pete \- follow up offline on “`unsafe` Practicum Chapter Task Force \- report (Joni”  
- Pete \- break down XL issue \#188 into smaller issues.  
  Then Zulip request votes on most important / painful topics  
  Initial list create by Pete, everyone can add