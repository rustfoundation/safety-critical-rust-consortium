# Decoding "Safety-Critical" Code

One of Rust's great strengths is that it requires [unsafe](https://doc.rust-lang.org/std/keyword.unsafe.html) code to be explicitly tagged. But when it comes to "safety-critical" code, the Rust [`unsafe` keyword](https://doc.rust-lang.org/reference/unsafe-keyword.html) "unsafe" can be easily confused with the vernacular, or "common language", meaning of the word "unsafe".

To be explicit, there are _multiple_ concepts that can be easily conflated:

* the **keyword** "unsafe", that has a very _specific and technical_ definition in Rust,
* the **concept** of "unsafe", that is usually an _imprecise_ synonym for "dangerous",
* the **concept** of "safety-critical", that implies "bad things happen if the code has bugs",
* and the **regulatory** definition of "safety-critical" that **varies** markedly by regulatory domain.

## Unsafe Code

For example, despite the fear-inducing label and _unlike_ other languages such as C or C++, code annotated as `unsafe` in Rust _cannot_ cause undefined behavior _outside of the declared unsafe scope_. That statement should not be interpreted the man that `unsafe` cannot cause far-reaching surprising or unintended consequences, because it can! What it _does_ mean is that if the programmer has been careful to _manually_ verify ["soundness"](https://doc.rust-lang.org/std/keyword.unsafe.html#unsafe-abilities), then soundness _outside_ of the `unsafe` block is maintained. Colloquially speaking, `unsafe` allows the programmer to "encapsulate" behavior that cannot be automatically checked or verfied by the compiler.

In fact, to a [first-order approximation](https://doc.rust-lang.org/nomicon/what-unsafe-does.html), the unsafe superset of safe Rust has only a small number of extra abilities:

* the ability to dereference raw pointers,
* the ability to mutate global variables, and
* the ability to access fields of `union` types.

Note that none of these are generally considered "unsafe" in other languages, even if they are considered "unwise" or indicative of poor programming practices, and may be **unavoidably necessary**, for example such as accessing low-level hardware registers in embedded programming. Consider the following _common_ embedded idiom for setting a low-level MCU clock peripheral in "C":

```c
void
da1469x_clock_sys_xtal32m_init(void)
{
    uint32_t reg;
    int xtalrdy_cnt;

    /* Number of lp_clk cycles (~30.5us) */
    xtalrdy_cnt = MYNEWT_VAL(MCU_CLOCK_XTAL32M_SETTLE_TIME_US) * 10 / 305;

    reg = CRG_XTAL->XTALRDY_CTRL_REG;
    reg &= ~(CRG_XTAL_XTALRDY_CTRL_REG_XTALRDY_CLK_SEL_Msk |
             CRG_XTAL_XTALRDY_CTRL_REG_XTALRDY_CNT_Msk);
    reg |= xtalrdy_cnt;
    CRG_XTAL->XTALRDY_CTRL_REG = reg;
}
```

Preprocessor macros, definitions, and manual `u32` bit-masking and -shifting are common patterns, and in the "C" world are usually _not_ considered unsafe.

In fact, by carefully encapsulating raw pointer dereferencing, the `unsafe` keyword allows Rust to manipulate raw peripheral memory with abstractions that provide [**strong static guarantees**](https://docs.rust-embedded.org/book/static-guarantees/index.html), making encapsulated-unsafe Rust _far safer_ --- meaning "less bug prone" --- than other programming languages. For example, in Rust, a completely type-safe and _zero-cost_ similar abstraction could be written as:

```rust
fn apply_config(&self) {
    let c = T::regs().config();
    match &self.master_clock {
        Some(MasterClock { freq, ratio }) => {
            c.mode().write(|w| w.set_mode(vals::Mode::MASTER));
            c.mcken().write(|w| w.set_mcken(true));
            c.mckfreq().write(|w| w.set_mckfreq(freq.to_register_value()));
            c.ratio().write(|w| w.set_ratio(ratio.to_register_value()));
        }
        None => {
            c.mode().write(|w| w.set_mode(vals::Mode::SLAVE));
        }
    };

    c.swidth().write(|w| w.set_swidth(self.config.sample_width.into()));
    c.align().write(|w| w.set_align(self.config.align.into()));
    c.format().write(|w| w.set_format(self.config.format.into()));
    c.channels().write(|w| w.set_channels(self.config.channels.into()));
}
```



## Safety-Critical Code

Similarly, the term "safety-critical" has no universally agreed-upon definition. As a trivial example, consider a simple reminder alarm application. Criticality depends on the context in which the application is used. If used to remind someone to water the garden, a software failure may mean wilted plants. If used to remind a critically ill patient to take lifesaving medication, a software failure may imply a trip to the hospital or worse.

Even moving to a more formal language, a bank's notion of "safety-critical" may be focused on financial loss, while an airline might be more concerned with loss of life, or a medical company would need to ensure that drug delivery occurs _exactly_ as specified. There is no "one-size-fits-all" notion of safety-critical software practices!

### A Sampling of Software Safety Standards

Here's a small sampling of some of the more common software standards that address "safety-critical" concerns across different sectors. It is by no means exhaustive or representative!

- **Industrial**
  - IEC 61508 --- This is a foundational, "umbrella" standard for functional safety of electrical, electronic, and programmable electronic safety-related systems. It's widely used across various industrial sectors.
  - IEC 62443 --- a series of standards that address security for [operational technology](https://en.wikipedia.org/wiki/Operational_technology) in [automation](https://en.wikipedia.org/wiki/Automation) and [control systems](https://en.wikipedia.org/wiki/Control_system).
  - IEC / EN 62061 --- This standard is specifically for the functional safety of machinery such as electrical, electronic and programmable electronic control systems.
- **Automotive**
  - ISO 26262 --- This standard is specifically for functional safety in road vehicles. It addresses the safety of electrical and electronic systems within automobiles.
  - ISO / SAE 21434 --- A cybersecurity standard jointly developed by [ISO](https://en.wikipedia.org/wiki/ISO) and [SAE](https://en.wikipedia.org/wiki/SAE_International) working groups that proposes cybersecurity measures for the development lifecycle of road vehicles.
  - AUTOSAR (AUTomotive Open System ARchitecture) --- an industry development partnership that develops and establishes an open and standardized software architecture for automotive electronic control units.
  - MISRA (Motor Industry Software Reliability Association) --- an organization that produces guidelines for the software developed for electronic components used in the automotive industry, but has been widely adopted in other industries, both formally and informally, as well.
- **Aerospace**
  - DO-178C / ED-12C --- The primary document by which the certification authorities such as [FAA](https://en.wikipedia.org/wiki/Federal_Aviation_Administration), [EASA](https://en.wikipedia.org/wiki/European_Aviation_Safety_Agency) and [Transport Canada](https://en.wikipedia.org/wiki/Transport_Canada) approve all commercial software-based aerospace systems.
  - DO-330 --- Describes how the tools _used_ to comply with DO-178C / ED-12C must be developed.
  - DO-326A / ED-202A --- Detail objectives for cybersecurity in avionics.
- **Medical**
  - IEC 62304 --- A standard focused on medical device software lifecycle processes. It provides a framework for developing and maintaining safe medical software.
  - ISO 13485 --- Medical Devices -- Quality Management Systems.
  - ISO 14971 --- Application of risk management to medical devices.
  - FDA [510(k)](https://www.fda.gov/medical-devices/overview-device-regulation/regulatory-controls) --- What is needed to support a submission for approval.

These standards often require rigorous development processes, documentation, testing, and risk assessment. Functional safety standards often utilize risk assessment and safety integrity levels (SILs, or ASILs for Automotive SILs) to determine the rigor of the development process that must be followed. Coding standards like those published by the MISRA organization are frequently used in conjunction with these safety standards to improve code quality and reliability. Thus "writing the software" is usually only a very small part of what "safety-critical" software programming practices need to address in order to meet a particular field's and a particular use-case's standard of care.

### Case Study: Avionics

When reading the comparatively short DO-178C / ED-12C guidance document --- a mere 144 pages, including all front and back matter! --- it is notable just _how much_ of the document deals with verification. Considerable effort is spent detailing the combination of reviews, analysis, and testing required to formally demonstrate that the output of each mandated software lifecycle process is correct with respect to its input. Specifically, of the 71 objectives required to be met for the highest assurance level, Level "A", 43 objectives apply to verification alone, regardless of what defensive programming strategies are employed.

For this reason, DO-178C / ED-12C is sometimes called a "correctness" standard rather than a "safety standard" because "safety-critical" assurance is achieved by having confidence that the software meets its detailed and complete requirements. Indeed, from DO-178C, Section 2.3, Page 12:

> Development of software to a software [design assurance] level does not imply the assignment of a failure rate for that software. Thus, software reliability rates based on software levels cannot be used by the system safety assessment process in the same way as hardware failure rates.

Taken _very_ informally, the chain of thought is that software will be "safe" if:

* the software behaves as designed, but...
* the design has to be _thorough_ and _extremely complete_, and
* that means _really, really_ tested in ways that _try hard_ to break it, and
* all of this must be _thoroughly_ documented and _traceable_.

For example, consider a common event in non-Rust languages: an invalid memory access that causes a bus fault and inadvertent CPU reset. Following the chain of thought above, we would:

* require that the software have "no unintentional restarts" --- a high level requirement
* enumerate all the things that can cause a restart, in this case, a bus fault
* determine all the things that can cause a bus fault --- one of them being an invalid memory access
* require defensive programming techniques to make invalid memory accesses difficult or impossible to write
* depending on the criticality level of the software, verify that the machine code matches the high-level language specification
* at every requirement, at every level, write positive- and negative- behavior tests to show the requirements are complete, necessary and sufficient

Notice that "safe" _does not appear in the above_. The code is "safe" as a _side-effect_ of "most definitely" conforming to a "very complete and thorough" set of specifications and requirements.

That's a very different view of "safety" than commonly assumed!

### Not Necessarily Straightforward

A last bit of emphasis regarding how important a technically-precise definition of "safety-critical" is, suppose by heroic and thorough work we had proven that our software, from the machine-code level on up, precisely matched specification, and those specifications were complete beyond reproach. No execution path unaccounted for! All possible control flows mapped and tested! We have achieved full safety criticality, right?

Right?

Not necessarily.

At this point we **may** indeed have "proven" that unintended behavior of our software is "impossible".

But what if there is a very rare, undocumented and unknown bug in the CPU hardware that is rarely or sporadically triggered? What if the bug is in the CPU low-level hardware design? Or perhaps we just got unlucky and it was a manufacturing defect in that affects only one (our) piece of silicon? Or perhaps just a stray [cosmic ray](https://en.wikipedia.org/wiki/Cosmic_ray#Effect_on_electronics) was at the wrong place at the wrong time?

Although they are "hardware" events, our software may indeed need to handle these types of issues _even if the hardware follows its own hardware-specific "safety-critical" standards!_

At the highest levels of criticality, "safety-critical" coding practices might be summarized as:

* write software such that "surprising" things are impossible, but
* handle the impossible cases too... just in case.

Always remembering that ["dead code" should usually be removed](https://stackoverflow.com/a/15700228)... _(but that's a discussion worthy of a separate, new discussion all on its own...)_

## Recommendations

* Always keep in mind the _specific_ definitions of "unsafe" and "safety-critical" that you're working with
* Remember that "safety-critical" coding doesn't _have_ to be a bad experience... but it probably will be "thorough"
* Your tools can greatly help or hinder you meeting functional or documentation or verification goals, and this is one of the areas that Rust strives to be firmly on the "good helper" side
