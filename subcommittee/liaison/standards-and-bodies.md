# Standards and Bodies Contacted

This is a list of standards, standard bodies, and organizations that the Liaison Subcommittee
is either in contact with, or has agreed to try to get into contact with, for collaboration.

## Standards

### IEC 61508

Parent standard for ISO 26262 not solely focused on automotive.
While task-based, this is not language agnostic and requires that the source is checked against language-specific guidelines, so upstreaming a process for incorporating Rust is needed.

### ISO 26262

(Automotive) Functional safety standard for automotive, derived from IEC 61508. Same concern as for the parent.

### DO-178C

Certification standard for aerospace software systems. This is task-based and generally language-agnostic.

### TR 24772 Programming language vulnerabilities

There is a general document, and language-specific documents for both ISO and non-ISO programming languages.

There is no document for Rust, which would out the applicability of the generic vulnerabilities and how they are avoided by the language, at this time.

See WG23 below for management of this.

## Bodies

### Linux Foundation

The Rust Foundation has an existing liaison to the Linux Foundation. Marcey to find out who is best suited to contact for this. Linux Foundation participates in ISO 26262 and IEC 61508.

### Red Hat

Red Hat participates in ISO 26262 development and can provide guidance for participation.

### ELISA

Enabling Linux in Safety Critical Applications. Separate contact from the Linux Foundation.
Runs the Automotive Grade Linux group.

### ISO (general)

National bodies such as INCITS, BSI, etc. are the vector for interaction with ISO.

Members who are a member of a national body should reach out to gauge interest for involvement.

### ISO WG23 Language Vulnerabilities

Perforce has existing members in WG23: Celeste to contact the core and study groups to establish whether a Rust document is wanted at this time. The WG did express an interest in developing a Rust document in 2019 but has not made any progress on this on their own. There is no Rust SG within the WG right now.

### MISRA

MISRA participates in ISO 26262 and IEC 61058 and can provide some guidance for how Rust can move towards compatibility with these. (Addendum 6 is designed to provide a first pass identification of issues that may affect 26262 and 61508.)

### Enduring Security Framework

The ESF has not met since December and has been pulled from the US Government's funding and websites. A publication was released but is unlikely to be followed up.

It may be possible to encourage other national bodies such as BSI to take over this work as equivalent security concerns apply to all states.
