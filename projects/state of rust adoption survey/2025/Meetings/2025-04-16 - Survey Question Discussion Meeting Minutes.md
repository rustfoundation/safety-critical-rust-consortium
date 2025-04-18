## Safety-Critical Rust Adoption Survey Question Discussion

## Agenda

1. Question Review  
   1. Do we have sufficient demographic/persona information? Should we ask for a country/location?  
   2. Tooling  
      1. Are the tooling categories correct/inclusive?  
      2. Should we ask about other aspects of the tooling ecosystem such as debugger support, profiling, etc?  
      3. Do we need more specificity in analysis tools (formal methods, code complexity, worst-case execution time, etc)?  
   3. Standards  
      1. Are the standards and coding guidelines complete?  
      2. Is there value in asking the specific level of standards that respondents work with?  
   4. Level of adoption section: what would you ask an existing safety-critical Rust user? What would you ask a non-SC Rust user who’s considering it? What would you ask an engineer who’s not interested in using Rust?  
   5. Hardware section  
      1. Is the list of chip architectures complete?  
2. Are there any specific burning Rust topics we should ask about such as C++ interoperability, ABI stability, language specifications, etc?  
3. Is the survey a reasonable length or should we trim questions?  
4. Should there be a Call to Action at the end? Ask interested responders for an email address or something?
   
   ## Check-in Area
* Xander Cesari  
* Pete LeVasseur, ⏰  
* El Mahdi El Araby 🐌  
* Douglas Deslauriers 🙂  
* Dillon McEwan 🦥  
* Alex Celeste 😔  
* Christof Petig 🍵  
* Koppany Pazman   
* Jonas Wolf 👂  
* Vincent EckSie  
* Andrew Fernandes ☕
  
  ## Tasks
* Discuss adoption survey PR and agree on a proposed final survey  
* View PR here:  
  * https://github.com/rustfoundation/safety-critical-rust-consortium/pull/266
    
    ## Meeting Minutes
* Discussed the purpose of the survey and the impetus for creating it
  
  ### Demographic Information
* Discussed the meaning of “Industrial” would be  
  * Tried to standard IEC 61508 (check this?)  
* Suggestion to include Financial and Cryptography  
  * Decided these are mission critical and could be adding with “Other”  
* Discussed the difference between Safety / Mission critical industries  
  * There was not a discussed different set of questions for mission critical users  
  * Common understanding of safety \== “risk of bodily harm”  
* Decided to keep size of company question  
* Decided to add “Devops / Tooling” to list of roles  
* Decided to add “Cybersecurity Engineer” to list of roles
  
  ### Language Information
* Suggestion to add “Ocaml” or “Erlang”  
  * Decided to keep it under “other”  
* Decided to add prompt to description to the Languages question to prompt the reader to include exotic languages and other languages used in tooling.  
* Decided not to add more options to the switching to Rust question  
  * Instead have a text box where you can Rave about Rust  
  * Decided to cull down options below 5 questions  
* Decided to collapse “interested in Rust” and “using rust categories”  
  * The distinction and wanted answers are the same between both  
* Suggestion to add “Using C/C++ Interoperability layer”  
  * Could be added when the user selects they use C/C++  
* Decided to add “Lack of qualified tooling” to primary disadvantages of Rust
  
  ### Tooling Information
* Add to code metrics list such as “lines of code, etc.”  
  * Change name to “Source Code Metrics”  
* Suggestion to add “Worst Case Execution Time, Stack Usage, etc.” to required tools  
* Perhaps change description of required tooling to add “on a daily basis”
  
  ### Standards Information
* Asked if we need to even ask the Standard, if we know the category?  
  * Decided to keep the standards question so we can delegate to the levels  
* Decide to add “(any version, any flavor)” to the DO-178 standard  
* Weren’t sure about keeping the static analysis guidelines question  
  * Could add more though
    
    ### Hardware Information
* Add “web assembly” to the environments to deploy code  
* Suggestion to add a text box if checking “Embedded Linux” for environment  
* Distinguish between ARM m/r, and a cores
  
  ### Wrap up questions
* Move libraries questions into the tooling section  
* Suggestion to add “which crates would need to be qualified”  
* Could add link to newsletter or Consortium
