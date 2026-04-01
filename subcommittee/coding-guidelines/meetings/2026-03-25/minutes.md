# **Coding Guidelines Subcommittee Meeting on 2026-03-25 @ 1600 CET / 1100 EDT**

[Link](https://www.worldtimebuddy.com/?qm=1&lid=5,12,2643743,8,1850147,100,14&h=5&date=2026-3-25&sln=11-12&hf=1) to meeting time in common time zones.

| Search Key | Description |
| :---- | :---- |
| \[todo\] | Action Item |
| \[decision\] | Something decided on |
| \[important\] | Key information |

## **Agenda**

1. Solicitation of notetaker  
2. Acceptance of [Previous Meeting Minutes](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/subcommittee/coding-guidelines/meetings/2026-03-18/minutes.md)  
3. Introduction of new members  
4. Review batches for [CERT C \=\> Rust Mapping](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/336) (Pete)  
   - [\#427 \[CERT C Review Batch 1/5\] Review proposed Rust categorization](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/427)  
   - [\#428 \[CERT C Review Batch 2/5\] Review proposed Rust categorization](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/428)  
   - [\#429 \[CERT C Review Batch 3/5\] Review proposed Rust categorization](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/429)  
     * Batch A  
   - [\#430 \[CERT C Review Batch 4/5\] Review proposed Rust categorization](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/430)  
     * Batch B  
   - [\#431 \[CERT C Review Batch 5/5\] Review proposed Rust categorization](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/issues/431)  
     * Batch C  
5. Coverage of MISRA C and CERT C in 2026 (Félix / Markus)  
   - MISRA C one has a [PR up](https://github.com/rustfoundation/safety-critical-rust-coding-guidelines/pull/432) from Markus  
   - Félix wanted the review batches done first IIRC  
6. Proposals and ideas for new rules (all)  
7. Progress on ongoing tasks (all)  
8. Round table

## **Check-in area**

* David Svoboda (:  
* Douglas Deslauriers 🎨  
* Alex Celeste ☕  
* William Barsse  
* Max Jacinto ⚽  
* [Arshad Mahmood](mailto:arshadm@collabli.com)☔  
* Pete LeVasseur 🎊🦀  

**Please add your name, and an emoji that describes your day.**

**Notetaker:**

* William Barsse

For tips on how we take notes in the Safety-Critical Rust Consortium, please see the [Meeting Notetaker Role](https://github.com/rustfoundation/safety-critical-rust-consortium/blob/main/docs/notetaker-role.md) doc.

## **Housekeeping section**

* Document space: [coding-guidelines](https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/subcommittee/coding-guidelines)  
* Zulip: [safety-critical-consortium: Coding Guidelines](https://rust-lang.zulipchat.com/#narrow/channel/445688-safety-critical-consortium/topic/Coding.20Guidelines)  
* [Kanban board](https://github.com/orgs/rustfoundation/projects/1/views/3)  
  * [`contributor experience`](https://github.com/orgs/rustfoundation/projects/1/views/4) view  
  * [`coding guideline`](https://github.com/orgs/rustfoundation/projects/1/views/5) view

## **Tasks**

* Open PR for “pro-tips” concerning crate suggestions for use in an Safety Critical context.

## **Meeting Minutes**

* No objections to the previous meeting’s notes.  
* CertC to Rust mapping, proposal to break into small groups to push discussions along. No objections to the process. 3 (for now) meetings to be organized (see item 4 in Agenda above).  
* Group A  
  * [PRE32](https://wiki.sei.cmu.edu/confluence/display/c/PRE32-C.+Do+not+use+preprocessor+directives+in+invocations+of+function-like+macros): Agree.  
  * [DCL31](https://wiki.sei.cmu.edu/confluence/display/c/DCL31-C.+Declare+identifiers+before+using+them): Agree  
  * [DCL37](https://wiki.sei.cmu.edu/confluence/display/c/DCL37-C.+Do+not+declare+or+define+a+reserved+identifier): Agree  
  * [EXP37](https://wiki.sei.cmu.edu/confluence/display/c/EXP37-C.+Call+functions+with+the+correct+number+and+type+of+arguments): Agree  
  * [EXP44](https://wiki.sei.cmu.edu/confluence/display/c/EXP44-C.+Do+not+rely+on+side+effects+in+operands+to+sizeof%2C+_Alignof%2C+or+_Generic): Agree  
  * [EXP47](https://wiki.sei.cmu.edu/confluence/display/c/EXP47-C.+Do+not+call+va_arg+with+an+argument+of+the+incorrect+type): Agree  
  * [STR34](https://wiki.sei.cmu.edu/confluence/display/c/STR34-C.+Cast+characters+to+unsigned+char+before+converting+to+larger+integer+sizes): Agree \- although rust has it’s own weirdness \- if c is a char, we can do (c as i32) which in theory could result in a negative number because c is represented internally as a u32, but there is no i32::From(c).  
  * [FIO30](https://wiki.sei.cmu.edu/confluence/display/c/FIO30-C.+Exclude+user+input+from+format+strings): Agree  
  * [FIO41](https://wiki.sei.cmu.edu/confluence/display/c/FIO41-C.+Do+not+call+getc%28%29%2C+putc%28%29%2C+getwc%28%29%2C+or+putwc%28%29+with+a+stream+argument+that+has+side+effects): Agree  
  * [ENV30](https://wiki.sei.cmu.edu/confluence/display/c/ENV30-C.+Do+not+modify+the+object+referenced+by+the+return+value+of+certain+functions): Mostly Agree  
    1. This CERT C rule talks about a selection of specific C library functions. These functions are technically callable in Rust via a C FFI (unsafe).  
    2. I suppose the argument could be made that this rule applies to unsafe rust, since they are likely available on any system Rust is used. But IMO it’s equally valid to say that they are out of scope)  
  * [ENV32](https://wiki.sei.cmu.edu/confluence/display/c/ENV32-C.+All+exit+handlers+must+return+normally): Do not quite agree,  
    1. minor: the rationale should talk about [panic handler](https://doc.rust-lang.org/nomicon/panic-handler.html) explicitly since they correspond more closely with exit **handler**.  
    2. medium: The CERT rule also talks about potential clean up actions after the exit handler that could be ignored if the rule is violated.  
        In Rust, when a panic handler panics the program is aborted (as the rationale points out), this means subsequent clean up is skipped \-\> same problem  
  * [ERR34](https://wiki.sei.cmu.edu/confluence/display/c/ERR34-C.+Detect+errors+when+converting+a+string+to+a+number): Agree  
  * [INT31](https://wiki.sei.cmu.edu/confluence/display/c/INT31-C.+Ensure+that+integer+conversions+do+not+result+in+lost+or+misinterpreted+data): Agree  
  * [FLP32](https://wiki.sei.cmu.edu/confluence/display/c/FLP32-C.+Prevent+or+detect+domain+and+range+errors+in+math+functions): Agree  
  * [ENV33](https://wiki.sei.cmu.edu/confluence/display/c/ENV33-C.+Do+not+call+system%28%29): Agree  
  * [MSC41](https://wiki.sei.cmu.edu/confluence/display/c/MSC41-C.+Never+hard+code+sensitive+information): Agree  
  * [MEM31](https://wiki.sei.cmu.edu/confluence/display/c/MEM31-C.+Free+dynamically+allocated+memory+when+no+longer+needed): Agree (Based on the rationale it sounds like the rule should be reclassified from 'maybe' to 'maps to Rust')  
  * [DCL30](https://wiki.sei.cmu.edu/confluence/display/c/DCL30-C.+Declare+objects+with+appropriate+storage+durations): Agree  
  * [EXP42](https://wiki.sei.cmu.edu/confluence/display/c/EXP42-C.+Do+not+compare+padding+data): Agree  
  * [ENV31](https://wiki.sei.cmu.edu/confluence/display/c/ENV31-C.+Do+not+rely+on+an+environment+pointer+following+an+operation+that+may+invalidate+it): Agree  
* Group B  
  * [DCL36](https://wiki.sei.cmu.edu/confluence/display/c/DCL36-C.+Do+not+declare+an+identifier+with+conflicting+linkage+classifications): Agreed, linkage specification mismatches are not relevant here  
  * [DCL41](https://wiki.sei.cmu.edu/confluence/display/c/DCL41-C.+Do+not+declare+variables+inside+a+switch+statement+before+the+first+case+label): Agreed  
  * [EXP45](https://wiki.sei.cmu.edu/confluence/display/c/EXP45-C.+Do+not+perform+assignments+in+selection+statements): Agreed, rationale for preventing use of assignments does not apply  
  * [EXP46](https://wiki.sei.cmu.edu/confluence/display/c/EXP46-C.+Do+not+use+a+bitwise+operator+with+a+Boolean-like+operand): Agreed  
  * [FIO38](https://wiki.sei.cmu.edu/confluence/display/c/FIO38-C.+Do+not+copy+a+FILE+object): Agreed, this might only be relevant for FFI and doesn’t warrant a rule  
  * [FIO40](https://wiki.sei.cmu.edu/confluence/display/c/FIO40-C.+Reset+strings+on+fgets%28%29++or+fgetws%28%29+failure): Agreed  
  * [SIG30](https://wiki.sei.cmu.edu/confluence/display/c/SIG30-C.+Call+only+asynchronous-safe+functions+within+signal+handlers): Agreed, signal handling in Rust is outside of the scope of our document  
  * [SIG31](https://wiki.sei.cmu.edu/confluence/display/c/SIG31-C.+Do+not+access+shared+objects+in+signal+handlers): Agreed  
  * [ERR30](https://wiki.sei.cmu.edu/confluence/display/c/ERR30-C.+Take+care+when+reading+errno): Agreed, errno is part of libc and not relevant here  
  * [ERR32](https://wiki.sei.cmu.edu/confluence/display/c/ERR32-C.+Do+not+rely+on+indeterminate+values+of+errno): Agreed  
  * [CON30](https://wiki.sei.cmu.edu/confluence/display/c/CON30-C.+Clean+up+thread-specific+storage): Agreed, any method of creating memory leaks wouldn’t be thread-specific  
  * [CON39](https://wiki.sei.cmu.edu/confluence/display/c/CON39-C.+Do+not+join+or+detach+a+thread+that+was+previously+joined+or+detached): Agreed, the case for preventing this in unsafe code doesn’t rise to the justification of a Rule  
  * [INT32](https://wiki.sei.cmu.edu/confluence/display/c/INT32-C.+Ensure+that+operations+on+signed+integers+do+not+result+in+overflow): Agreed  
  * [INT34](https://wiki.sei.cmu.edu/confluence/display/c/INT34-C.+Do+not+shift+an+expression+by+a+negative+number+of+bits+or+by+greater+than+or+equal+to+the+number+of+bits+that+exist+in+the+operand): Agreed  
  * [CON33](https://wiki.sei.cmu.edu/confluence/display/c/CON33-C.+Avoid+race+conditions+when+using+library+functions): Agreed, but we think library functions like [std::env::set\_var](https://doc.rust-lang.org/std/env/fn.set_var.html) are worth mentioning since that is closer to the original purpose of the CERT Rule. We checked through the CERT example functions to see if any of those analogies in Rust applied, but they did not  
  * [CON41](https://wiki.sei.cmu.edu/confluence/display/c/CON41-C.+Wrap+functions+that+can+fail+spuriously+in+a+loop): Agreed  
  * [ARR37](https://wiki.sei.cmu.edu/confluence/display/c/ARR37-C.+Do+not+add+or+subtract+an+integer+to+a+pointer+to+a+non-array+object): Started to discuss, but ran out of time while discussing pointer provenance  
* Group C  
  * [INT35](https://wiki.sei.cmu.edu/confluence/display/c/INT35-C.+Use+correct+integer+precisions): Rust has both a fixed size and a precision \=\> doesn’t apply to Rust. Agreed.  
  * [STR37](https://wiki.sei.cmu.edu/confluence/display/c/STR37-C.+Arguments+to+character-handling+functions+must+be+representable+as+an+unsigned+char): Doesn’t apply to Rust. Agreed.  
  * [STR38](https://wiki.sei.cmu.edu/confluence/display/c/STR38-C.+Do+not+confuse+narrow+and+wide+character+strings+and+functions): Doesn’t apply. Agreed.  
  * [MEM33](https://wiki.sei.cmu.edu/confluence/display/c/MEM33-C.++Allocate+and+copy+structures+containing+a+flexible+array+member+dynamically): Doesn’t apply. Agreed.  
  * [FIO47](https://wiki.sei.cmu.edu/confluence/display/c/FIO47-C.+Use+valid+format+strings): Doesn’t apply, fmt patterns checked at compile time. Agreed.  
  * [SIG34](https://wiki.sei.cmu.edu/confluence/display/c/SIG34-C.+Do+not+call+signal%28%29+from+within+interruptible+signal+handlers): Doesn’t apply to Rust std, will be specific to OS Lib (out of scope). Agreed.  
  * [SIG35](https://wiki.sei.cmu.edu/confluence/display/c/SIG35-C.+Do+not+return+from+a+computational+exception+signal+handler): same as SIG34. Agreed.  
  * [CON31](https://wiki.sei.cmu.edu/confluence/display/c/CON31-C.+Do+not+destroy+a+mutex+while+it+is+locked): Doesn’t apply to safe rust though technically possible. May need a broader rule regarding using unsafe to side-step guarantees provided by safe constructs provided by the language (e.g. Mutex). More discussion needed.  
  * [MSC33](https://wiki.sei.cmu.edu/confluence/display/c/MSC33-C.+Do+not+pass+invalid+data+to+the+asctime%28%29+function): FFI could be used but std and dedicated Rust libs allow working with time without.  
    1. Note: would be interesting to have a list, or a ref to a list of crates useful/usable in a safety-critical context.  
  * [MSC38](https://wiki.sei.cmu.edu/confluence/display/c/MSC38-C.+Do+not+treat+a+predefined+identifier+as+an+object+if+it+might+only+be+implemented+as+a+macro): Doesn’t apply \- would be caught at compile time. Agreed.  
  * [MSC39](https://wiki.sei.cmu.edu/confluence/display/c/MSC39-C.+Do+not+call+va_arg%28%29+on+a+va_list+that+has+an+indeterminate+value): Doesn’t apply \- no manipulation of arguments as a data structure. Variadic macros expand all their arguments and translate to Rust code (and checked by the compiler). Agreed.  
  * [MSC40](https://wiki.sei.cmu.edu/confluence/display/c/MSC40-C.+Do+not+violate+constraints): without unsafe this doesn’t apply. Again a broad rule regarding how to use / not use unsafe could cover this. More discussion needed.  
  * [FLP34](https://wiki.sei.cmu.edu/confluence/display/c/FLP34-C.+Ensure+that+floating-point+conversions+are+within+range+of+the+new+type): definitely applies, existing clippy lints. Agreed.  
  * [FLP36](https://wiki.sei.cmu.edu/confluence/display/c/FLP36-C.+Preserve+precision+when+converting+integral+values+to+floating-point+type): same as FLP34. Agreed.  
  * [FIO42](https://wiki.sei.cmu.edu/confluence/display/c/FIO42-C.+Close+files+when+they+are+no+longer+needed): maps for ‘static lifetimes, or leaking but baseline Rust handles it automatically on Drop.  
  * [CON38](https://wiki.sei.cmu.edu/confluence/display/c/CON38-C.+Preserve+thread+safety+and+liveness+when+using+condition+variables): to be discussed further  
  * [MSC32](https://wiki.sei.cmu.edu/confluence/display/c/MSC32-C.+Properly+seed+pseudorandom+number+generators): handled by crate outside std, up to it to ensure the generator is seeded (e.g. with a typestate). To be discussed.  
  * 4 unaddressed  
* Appreciation of the “fast” review process: Teams would have liked/needed more time to evaluate and make sure the CERTC rules are well understood.  
* Format to express mapping from “foreign” coding standards to SCRC mapping discussed in outside discussion. Proposal to be presented soon.  
* Suggestion for a “pro-tips” section with for instance suggestions of commonly used, crates (eg. chrono, heapless, zerocopy, etc). \[see tasks\]  
* Topics for next time?

## **Material**

Any material to read before the meeting should be included here.  
