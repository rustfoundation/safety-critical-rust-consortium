# Examples of `unsafe` to work into chapter

The following are examples of `unsafe` code usage we could use to work into a chapter of the [Learn unsafe Rust](https://github.com/google/learn_unsafe_rust) book. These are not exhaustive, but give a starting point for something of a practicum for using `unsafe`.

## Example 1 

```rust
#![deny(unsafe_op_in_unsafe_fn)]

use std::slice::from_raw_parts_mut;

/// # Panics
///
//  Panics if mid point is not in slice
fn split_at_mut<'a, T>(slice: &'a mut [T], mid: usize)
    -> (&'a mut [T], &'a mut [T]) {
    assert!(0 <= mid && mid <= slice.len());
    
    /// SAFETY:
    ///
    /// * split_at_mut_unchecked expects 0 <= mid <= len
    /// * we just asserted that
    unsafe { split_at_mut_unchecked(slice, mid) }
}

/// # Safety (1)
///
/// * Caller needs to ensure the mid point is actually in the slice
/// * 0 <= mid <= slice.len()
// (2) `unchecked` is Rust standard lingo
// (3) unsafe functions express pre-conditions to the caller
unsafe fn split_at_mut_unchecked<'a, T>(slice: &'a mut [T], mid: usize)
    -> (&'a mut [T], &'a mut [T]) {

    // (4) It's still useful to express our pre-conditions in unsafe functions
    // as a debug_assert!
    debug_assert!(0 <= mid && mid <= slice.len());
    
    let ptr = slice.as_mut_ptr();
    let len = slice.len();
    
    // SAFETY: (5) SAFETY ARGUMENTS
    //
    // * Caller has to ensure 0 <= mid <= len
    // * (ptr, mid) , (ptr.add(mid), len-mid) don't overlap
    // * Therefore, no aliasing
    unsafe { // (6) unsafe blocks and their role
        (from_raw_parts_mut(ptr, mid), // (7) unsafe interface of libcore
         from_raw_parts_mut(ptr.add(mid), len - mid))
    }
    // (8) unsafe blocks must be reviewed with the whole module in mind
    // (9) unsafety has interplay with visibility
}

fn conjure_non_null() {
    let mut val = 4;
    let ptr = &raw mut val;
    let non_null: std::ptr::NonNull<_> =
        unsafe { std::ptr::NonNull::new_unchecked(ptr) };
}
```

## Example 2

```rust
// (10) interactions between fields
// (11) fields with interactions have to be private
// (12) seperate unsafe bits from safe bits and hide them in visibility
pub struct RawVec<T> {
    // points of allocation if cap > 0
    // should never be read on cap = 0
    ptr: NonNull<*mut T>,
    // cap >= len
    // cap represents the actual allocation
    cap: usize,
}

impl<T> RawVec<T> {
    unsafe fn set_cap(self: &mut Vec<T>, cap: usize) {
        self.cap = cap;
    }
}

pub struct Vec<T> {
    raw: RawVec<T>,
    // len <= cap
    len: usize,
}
```

## Example 3 -- Pointer Arithmetic 

In connection with [Allocation](https://rust-lang.github.io/unsafe-code-guidelines/glossary.html#allocation), operations involving pointer arithmetic, which require resorting to the unsafe keyword, are safe as long as the resulting pointers are within the bounds of the allocated memory.

This might be needed when working with a foreign function interface ([FFI](https://doc.rust-lang.org/book/ch19-01-unsafe-rust.html#using-extern-functions-to-call-external-code)), for example processing a C-style array - given by a pointer and a length.

```rust
fn safe_pointer_arithmetic() {
    let mut values = vec![1, 2, 3, 4, 5];

    // SAFETY: get a raw pointer to the start of the vector, which is valid
    // using `as_mut_ptr` as long as the vector exists and isn't reallocated.
    let ptr = values.as_mut_ptr();
    let len = values.len();

    for i in 0..len {
        unsafe {
            // SAFETY: pointer arithmetic within the bounds of the vector.
            let elem_ptr = ptr.add(i);

            // SAFETY: dereference is safe because 0 <= i < len.
            *elem_ptr *= 2;
        }
    }
}
```
