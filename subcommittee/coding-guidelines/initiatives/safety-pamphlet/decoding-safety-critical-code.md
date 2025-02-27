# Decoding “Safety-Critical” Code

One of Rust’s great strengths is that it requires [unsafe](https://doc.rust-lang.org/std/keyword.unsafe.html) code to be explicitly tagged. But when it comes to “safety-critical” code, the Rust [`unsafe` keyword](https://doc.rust-lang.org/reference/unsafe-keyword.html) “unsafe” can be easily confused with the vernacular, or “common language”, meaning of the word “unsafe”.

To be explicit, there are _multiple_ concepts that can be easily conflated:

* the **keyword** “unsafe”, that has a very _specific and technical_ definition in Rust,
* the **concept** of “unsafe”, that is usually an _imprecise_ synonym for “dangerous”,
* the **concept** of “safety-critical”, that implies “bad things happen if the code has bugs”,
* and the **regulatory** definition of “safety-critical” that varies markedly by regulatory domain.

## Unsafe Code

For example, despite the fear-inducing label and _unlike_ other languages such as C or C++, `unsafe` Rust [_cannot_ cause undefined behavior](https://doc.rust-lang.org/std/keyword.unsafe.html#unsafe-abilities). In fact, to a first-order approximation, the the unsafe superset of safe Rust has only three main extra abilities:

* the ability to dereference raw pointers,
* the ability to mutate global variables, and
* the ability to access fields of `union` types.

Note that none of these are generally considered “unsafe” in other languages, even if they are considered “unwise” or indicative of poor programming practices, and may be unavoidably necessary such as accessing low-level hardware registers in embedded programming.

In fact, by carefully encapsulating raw pointer dereferencing, the `unsafe` keyword allows Rust to manipulate raw peripheral memory with abstractions that provide [**strong static guarantees**](https://docs.rust-embedded.org/book/static-guarantees/index.html), making encapsulated-unsafe Rust _far safer_ — meaning “less bug prone” — than other programming languages.

## Safety-Critical Code

Similarly, the term “safety-critical” has no universally agreed-upon definition. As a trivial example, consider a simple reminder alarm application. Criticality depends on the context in which the application is used. If used to remind someone to water the garden, a software failure may mean wilted plants. If used to remind a critically ill patient to take lifesaving medication, a software failure may imply a trip to the hospital or worse.

Even moving to a more formal language, a bank’s notion of “safety-critical” may be focused on financial loss, while an airline might be more concerned with loss of life, or a medical company would need to ensure that drug delivery occurs _exactly_ as specified. There is no “one-size-fits-all” notion of safety-critical software practices!

### A Sampling of Software Safety Standards

Here's a small sampling of some of the more common software standards that address “safety-critical” concerns across different sectors. It is by no means exhaustive or representative!

- **Industrial**
  - IEC 61508 — This is a foundational, “umbrella” standard for functional safety of electrical, electronic, and programmable electronic safety-related systems. It's widely used across various industrial sectors.
  - IEC 62443 — a series of standards that address security for [operational technology](https://en.wikipedia.org/wiki/Operational_technology) in [automation](https://en.wikipedia.org/wiki/Automation) and [control systems](https://en.wikipedia.org/wiki/Control_system).
  - IEC / EN 62061 — This standard is specifically for the functional safety of machinery such as electrical, electronic and programmable electronic control systems.
- **Automotive**
  - ISO 26262 — This standard is specifically for functional safety in road vehicles. It addresses the safety of electrical and electronic systems within automobiles.
  - ISO / SAE 21434 — A cybersecurity standard jointly developed by [ISO](https://en.wikipedia.org/wiki/ISO) and [SAE](https://en.wikipedia.org/wiki/SAE_International) working groups that proposes cybersecurity measures for the development lifecycle of road vehicles.
  - AUTOSAR (AUTomotive Open System ARchitecture) — an industry development partnership that develops and establishes an open and standardized software architecture for automotive electronic control units.
  - MISRA (Motor Industry Software Reliability Association) — an organization that produces guidelines for the software developed for electronic components used in the automotive industry.
- **Aerospace**
  - DO-178C / ED-12C — The primary document by which the certification authorities such as [FAA](https://en.wikipedia.org/wiki/Federal_Aviation_Administration), [EASA](https://en.wikipedia.org/wiki/European_Aviation_Safety_Agency) and [Transport Canada](https://en.wikipedia.org/wiki/Transport_Canada) approve all commercial software-based aerospace systems. 
  - DO-330 — Describes how the tools _used_ to comply with DO-178C / ED-12C must be developed.
  - DO-326A / ED-202A — Detail objectives for cybersecurity in avionics.
- **Medical**
  - IEC 62304 — A standard focused on medical device software lifecycle processes. It provides a framework for developing and maintaining safe medical software.
  - ISO 13485 — Medical Devices – Quality Management Systems.
  - ISO 14971 — Application of risk management to medical devices.
  - FDA [510(k)](https://www.fda.gov/medical-devices/overview-device-regulation/regulatory-controls) — What is needed to support a submission for approval.

These standards often require rigorous development processes, documentation, testing, and risk assessment. Functional safety standards often utilize risk assessment and safety integrity levels (SILs, or ASILs for Automotive SILs) to determine the rigor of the development process that must be followed. Coding standards like those published by the MISRA organization are frequently used in conjunction with these safety standards to improve code quality and reliability. Thus “writing the software” is usually only a very small part of what “safety-critical” software programming practices need to address in order to meet a particular field’s and a particular use-case’s standard of care.

### Case Study: Avionics

When reading the comparatively short DO-178C / ED-12C guidance document — a mere 144 pages, including all front and back matter! — it is notable just _how much_ of the document deals with verification. Considerable effort is spent detailing the combination of reviews, analysis, and testing required to formally demonstrate that the output of each mandated software lifecycle process is correct with respect to its input. Specifically, of the 71 objectives required to be met for the highest assurance level,  Level “A”, 43 objectives apply to verification alone, regardless of what defensive programming strategies are employed.

For this reason, DO-178C / ED-12C is sometimes called a “correctness” standard rather than a “safety standard” because “safety-critical” assurance is achieved by having confidence that the software meets its detailed and complete requirements. Indeed, from DO-178C, Section 2.3, Page 12:

> Development of software to a software [design assurance] level does not imply the assignment of a failure rate for that software. Thus, software reliability rates based on software levels cannot be
> used by the system safety assessment process in the same way as hardware failure rates.

