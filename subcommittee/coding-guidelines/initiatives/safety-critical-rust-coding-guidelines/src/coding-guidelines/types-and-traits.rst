.. SPDX-License-Identifier: MIT OR Apache-2.0
   SPDX-FileCopyrightText: The Coding Guidelines Subcommittee Contributors

.. default-domain:: coding-guidelines

Types and Traits
================

.. guideline:: Avoid Implicit Integer Wrapping
   :id: gui_xztNdXA2oFNB
   :status: draft
   :fls: fls_cokwseo3nnr
   :tags: numerics
   :category: types
   :recommendation: required

   Code must not rely on Rust's implicit integer wrapping behavior that occurs in release builds. 
   Instead, explicitly handle potential overflows using the standard library's checked, 
   saturating, or wrapping operations.

   .. rationale:: 
      :id: rat_kYiIiW8R2qD1
      :status: draft

      In debug builds, Rust performs runtime checks for integer overflow and will panic if detected.
      However, in release builds (with optimizations enabled), integer operations silently wrap
      around on overflow, creating potential for silent failures and security vulnerabilities.
      
      Safety-critical software requires consistent and predictable behavior across all build
      configurations. Explicit handling of potential overflow conditions improves code clarity,
      maintainability, and reduces the risk of numerical errors in production.

   .. bad_example:: 
      :id: bad_ex_PO5TyFsRTlWv
      :status: draft
   
       .. code-block:: rust
   
         fn calculate_next_position(current: u32, velocity: u32) -> u32 {
             // Potential for silent overflow in release builds
             current + velocity
         }

   .. good_example:: 
      :id: good_ex_WTe7GoPu5Ez0
      :status: draft
   
       .. code-block:: rust
   
         fn calculate_next_position(current: u32, velocity: u32) -> u32 {
             // Explicitly handle potential overflow with checked addition
             current.checked_add(velocity).expect("Position calculation overflowed")
         }

