# Dangling and unaligned pointers


## Pointer Arithmetic

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
