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

## Read Unaligned Pointer

Pointer arithmetic, in particular, adding an offset to a pointer via [`add`](https://doc.rust-lang.org/std/primitive.pointer.html#method.add) as shown in the previous example, is useful to create an `unaligned pointer`. We may want to read from an unaligned pointer when, for example, working on a network communication protocol in a memory-constrained context.

Using the [`packed` modifier](https://doc.rust-lang.org/reference/type-layout.html#r-layout.repr.align-packed) together with [`C` *representation*](https://doc.rust-lang.org/nomicon/other-reprs.html#reprc), the order of fields in the layout of a struct as well as lowering the padding between them can be [guaranteed](https://doc.rust-lang.org/reference/type-layout.html#r-layout.repr.alignment.intro). The following code exemplifies the safe use of the unsafe [`std::ptr::read_unaligned`](https://doc.rust-lang.org/std/ptr/fn.read_unaligned.html) function.

```rust
#[derive(Debug, PartialEq)]
#[repr(C, packed)]
struct PackedHeader {
    id: u8,
    length: u8,
    checksum: u32,
}

/// Reads a `PackedHeader` from a raw byte buffer.
///
/// It is implicitly assumed that the data matches the layout and endianness
/// of `PackedHeader`.
///
/// Returns a `PackedHeader` by reading from the data with
/// `std::ptr::read_unaligned`.
unsafe fn read_packed_header(data: &[u8]) -> PackedHeader {
    // SAFETY: the data buffer must have at least the size of the
    // `PackedHeader` in bytes.
    assert!(data.len() >= 6, "Buffer is too small.");

    let id_ptr = data.as_ptr() as *const u8;
    // SAFETY: pointer arithmetic within the bounds of the buffer.
    let length_ptr = id_ptr.add(1) as *const u8;
    let checksum_ptr = length_ptr.add(1) as *const u32;

    // SAFETY: the *_ptr pointers are "valid" for reads and they
    // point to initialized data.
    let id = std::ptr::read_unaligned(id_ptr);
    let length = std::ptr::read_unaligned(length_ptr);
    let checksum = std::ptr::read_unaligned(checksum_ptr);

    PackedHeader { id, length, checksum }
}

fn main() {
    let data: [u8; 6] = [0x01, 0x02, 0x05, 0x00, 0xFF, 0xDD];

    let mut _header = PackedHeader{id: 0, length: 0, checksum: 0};
    unsafe {
        _header = read_packed_header(&data);
    }
    assert_eq!(_header, PackedHeader{id: 1, length: 2, checksum: 0xDDFF0005});
}
```
