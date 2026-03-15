---
sidebar_position: 1
---

# Are We Safety Critical Yet?

## What is Safety-Critical?

Software is not inherently "safe" or "unsafe" in isolation - it becomes safety-critical when it controls actions in the physical world that could potentially cause harm to people or the environment. Whether software is safety-critical is thus determined by its operational context: specifically, whether it contributes to system hazards as established through risk analysis and system design.

**Note:** Functional safety addresses risks from unintended malfunctions. It is distinct from cybersecurity, which addresses intentional malicious attacks.

## Evaluating safety-critical readiness of “Rust”

In practice, software is considered safe by demonstrating compliance with the relevant safety standard for the target industry and application. It is worth noting that compliance is a proxy for safety: compliant systems can still be unsafe, and non-compliant systems can be safe. The standard provides a structured framework, not a guarantee.

For this analysis, safety-critical readiness is measured by how well Rust's language design, toolchain, and ecosystem enable developers to meet the requirements of the relevant safety standards when developing safety-critical applications.

## Standards-Based Evaluations

The following evaluation examines how well specific safety-standard requirements can be satisfied when using Rust, based on the following scale:

🟢 Well supported - requirement can be met with no additional effort

🟡 Achievable - requirement can be met with moderate additional effort

🔴 Gap - requirement needs substantial additional effort or qualification activity

⚪ Not impacted - requirement is not directly affected by the choice of programming language

**Note:** Safety standards generally leave room for interpretation. In standards such as ISO 26262, final compliance claims are subject to the assessor's judgment.

### ISO 26262

🟡 Achievable with moderate additional effort

Rust's core language features - memory safety, strong typing, and data race prevention - provide excellent basis for ISO 26262 compliance. However, critical gaps exist in qualified tools, control/data flow analysis, and qualified RTOS/HAL/PAC support. These require individual qualification efforts and are barriers for production use.

[Detailed Rust vs. ISO 26262 gap analysis](iso26262.md)

### IEC 61508

Analysis in preparation. Contributions welcome via [GitHub](https://github.com/rustfoundation/safety-critical-rust-consortium).

### DO-178C

Analysis in preparation. Contributions welcome via [GitHub](https://github.com/rustfoundation/safety-critical-rust-consortium).
