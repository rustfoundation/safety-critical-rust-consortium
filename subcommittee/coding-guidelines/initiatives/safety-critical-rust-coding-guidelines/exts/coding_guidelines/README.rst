.. SPDX-License-Identifier: MIT OR Apache-2.0
   SPDX-FileCopyrightText: The Coding Guidelines Subcommittee Contributors

==================================
Coding Guidelines Sphinx Extension
==================================

To enhance the Safety-Critical Rust Coding Guidelines, and to facilitate its
authoring, updating, and testing it easier, we developed and use a custom
Sphinx extension that adds new roles and directives. The source code of the
extension is in the ``exts/coding_guidelines`` directory.

.. contents:: In this document:

Ferrocene Language Specification Conformance
============================================

Various checks are performed against the ``:fls:`` option present in ``guideline`` directives to
ensure they are valid.

Coverage of the coding guidlines over the FLS is calculated.

Each coding guideline has its ``:fls:`` option turned into a hyperlink to the corresponding element
within the FLS to be able to navigate there directly.

Further an ``fls.lock`` file located at ``root/src/fls.lock`` is validated against the currently
deployed version of the Ferrocene Language Spec and the build is failed if there is discrepency.

Links to the Rust standard library
==================================

You can link to the documentation of items defined in the Rust standard library
(``core``, ``alloc``, ``std``, ``test`` and ``proc_macro``) by using the
``:std:`type``` role (even for types defined in other standard library crates)
with the fully qualified item path:

.. code-block:: rst

   The type needs to implement :std:`core::marker::Copy`.
