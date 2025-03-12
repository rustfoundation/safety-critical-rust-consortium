# 2024-12-07 Tools Subcommittee Meeting Minutes

[Introductions again for new members.]

Let’s dive into the mapping on the PR for certification levels and tools /
requirements.

We’ll need to refine the categories into properties that are more specific to do
the mapping.

Let’s discuss that.

For example, in aerospace MC/DC is required for DAL-A.

Decision Coverage, for example, is DAL-A and DAL-B.

We should do a refined mapping on specific features, e.g. MC/DC, test coverage,
SBOM, WCET, etc.

Last time we refined some needs by priority, e.g. MC/DC, coverage tools, etc.
Then, MC/DC maps to DAL-A, and so on.

OK, so we can map from features into standards requirement levels.

For automotive, in ISO26262, there is a corresponding table, for ASIL-A thru D
where they list similar properties and how enforced it is, so we can also use
that.

So, let’s list all the properties/features and start a table from that, and then
go from there?

We’re trying to find folks from the medical side of things to get representation
there.

Maybe Ferrous Systems has a mapping of some sort for this sort of thing?

How should we collaborate on this? GitHub? Google Drive?

GitHub.

OK, I’ll start a GitHub PR for this and we can start collaborating on the
characteristics table.

There’s also an approximate mapping of Safety Critical mappings across levels at
the bottom of this document:
https://en.wikipedia.org/wiki/Automotive_Safety_Integrity_Level
Of course, we’re not sure how accurate it is, but it may be useful as a starting
summary.

[New member joins and introductions happen.]

Part 6 is Coding Guidelines, Part 11 is the tools.

We may not be able to continue with the next agenda point for mapping to tools
until we complete the first mapping matrix.

Coding Guidelines is currently focused on UB / Unsafe Rust pragmatic guidelines,
practicum, etc.

Coverage should be a higher priority than traceability for Rust.

For WCET (Worst Case Execution Time), electrical aircraft command has high-level
requirements that the command should respond in less than X time. For the binary
code, you may have to ensure that the whole pass can do this in less than X. You
can split it and sum these, etc.

It’s important to have good tooling to measure this on any or all levels, WCET.

The major problem for Rust is correlating binary back to source code to identify
the unit. This is probably more challenging in Rust than in C. This is reflected
in number 6 in our minutes from the previous meeting.

This would also enable SBOM generation.

We should also make sure we map this back to the parts of the standards
documents.

It seems like the ISO26262 folks are also adding Rust into the literature?

It may be that we cannot use the maximum optimization level in order to preserve
traceability? For example, link time optimization, etc.

Let’s take an action item to investigate the above, on what the constraints
might be for preserving traceability and source to obj code tracing.

Source code to obj code tracing may be something that has to be solved at the
compiler level or at the LLVM level, e.g. offer the right feature/flag or
optimizing the debugging information.

We will schedule the next meeting for the second week in January.

Proposal: A column for what degree the property is language agnostic or coupled
to the language itself, e.g. Rust.

Is the goal of this group to develop the tools, support commercial vendors, or
to integrate it into the compiler, etc.?

We think that our first goal is to identify the MVP package of tools that we
need for safety critical, then from there, it will likely be a mix of the above,
supporting open source efforts, developing tools where necessary, and pursuing
commercial engagements.

Let’s take the above as an agenda point for the next meeting, I think it’s
important to answer it thoroughly and correctly and I don't want to rush this
discussion since we only have a minute left.
