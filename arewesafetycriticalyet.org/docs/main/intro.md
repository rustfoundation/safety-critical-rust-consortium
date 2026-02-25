---
sidebar_position: 1
---

# Are We Safety Critical Yet?

## What is Safety-Critical?

Software and electronic control units (ECUs) cannot be inherently "safe" in isolation—they pose risks only when they control actions in the physical world and could potentially cause harm to people, the environment, or financial assets. Whether software is safety-critical is therefore determined by its operational context and potential consequences.

Software is classified as safety-critical if it contributes to identifiable system hazards. The extent of this contribution is established through product lifecycle risk analysis and system design.

**Note as distinction to Cybersecurity:** Functional safety generally addresses risks from unintended malfunctions, whereas cybersecurity addresses intentional malicious attacks from outside.

## Evaluating safety-critical readiness of “Rust”

In general the software is presumed to be safe by complying to the relevant safety-standard in your industry (context!).
It should be mentioned, that compliance to a standard (like ISO 26262) is a proxy for safety, but they are not identical, as compliant systems can be unsafe, as well as non-compliant systems can be safe.

For this analysis, safety-critical readiness is measured by how efficiently Rust and its language design, toolchain, and ecosystem enables developments to meet the requirements of the relevant safety standards, when developing safety-critical applications.

## Standards-Based Evaluations

The following evaluation examines how well specific safety-standard requirements can be satisfied when using Rust as the programming language, based on a simple traffic-light scale:

🟢 Well supported with no additional effort

🟡 Achievable with moderate additional effort

🔴 Achievable with substantial additional effort or qualification activity

**Note:** Safety standards generally leave room for interpretation. In some standards (as ISO 26262) the final compliance claims are subject to the assessor.

### ISO 26262

🟡 Achievable with moderate additional effort

Rust's core language features-memory safety, strong typing, and data race prevention provide excellent basis for ISO 26262 compliance. However, critical gaps exist in qualified tools, control/data flow analysis, and qualified RTOS/HAL/PAC support. These require individual qualification efforts and are barriers for production use.

[Detailed Rust vs. ISO 26262 gap analysis analysis](iso26262.md)

### IEC 61508

TODO

### DO-178C

TODO
