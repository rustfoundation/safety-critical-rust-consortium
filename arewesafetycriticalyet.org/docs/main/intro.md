---
sidebar_position: 1
---

# Are We Safety Critical Yet?

## What is safety-critical?

A piece of software or a standalone ECU cannot be 'safe' in isolation because they cannot inherently cause physical harm. Hazards arise only when these elements control or take action in the environment (real world) and are e.g. capable of injuring people or environmental/financial damage. Therefore, if something is safety-critical is defined by it’s context.

If the software does contribute to a hazard, it is deemed safety-critical. The contribution of the software to these hazards is determined/designed through the overall product life cycle.
Note to delimit from Cybersecurity: Functional Safety generally stems from malfcuntions, while Cybersecurity stems from malicious outside actors.

## How to judge safety-critical readiness of “Rust”?

In general the software is presumed to be safe by conforming to the relevant safety-standard in your industry (context!).
It should be mentioned, that conformity to a standard (like ISO 26262) is a proxy for safety, but they are not identical, as conform systems can be unsafe, as well as non-conforming systems can be safe.

For this context safety-critical readiness is judged by how well the requirements of the specific standards can be achieved when using Rust as programming language to implement safety-critical software. This includes the language itself, the toolchain as well as overall ecosystem.

## Readiness in terms of standards

In the following the safety-critical readiness is judged by looking at the specific requirements of relevant industry standards and how well an organization can conform to them when using Rust. For example there might some direct requirement that a programming language has to conform to e.g. a strong typing system. This directly is required by Rust. There might are also indirect requirements, e.g. that certain test coverage metrics need to be achieved - here we would judge how well the existing toolchain, ecosystem etc. can be used to satisfy these requirements.

We will be using the following scale:
🟢 Well supported with no extra effort
🟡 Possible with some manual extra effort
🔴 Possible with high manual extra effort

Note: Additionally it has to be stated, that there is always room for interpretation in those standards. In some standards an assessor will have to judge at the end of the development lifecylce, if conformity to the standard can be claimed.

### ISO 26262

🟡 Possible with some manual effort
TODO: add executive summary

See detailed explanation:
[ISO 26262 vs. Rust detailed gap analysis](iso26262.md)

### IEC 61508

TODO

### DO-178C

TODO
