fn swap (a: ~[int], p: int, q: int) -> ~[int] {
    let mut b = a;
    let temp = b[p];
    b[p] = b[q];
    b[q] = temp;
    b
}

fn partition(a: ~[int], p: int, r: int) -> (int, ~[int]) {
    let mut b = a;
    let x: int = b[r];
    let mut i: int = p-1;
    for j in range(p, r) {
        if b[j] <= x {
            i = i+1;
            b = swap(b, i, j);
        }
    }
    b = swap(b, i+1, r);
    (i+1, b)
}

fn quicksort (a: ~[int], p: int, r: int) -> ~[int] {
    if p < r {
        let first = match partition(a, p, r) {
            (q, partitioned) => (q, quicksort(partitioned, p, q-1))   
        };
        let sorted = match first {
            (q, left_sorted) => quicksort(left_sorted, q+1, r)
        };
        sorted
    } else {
        return a;
    }
}

#[test]
fn test_swap() {
    let a: ~[int] = ~[1, 2];
    let b = swap(a, 0, 1);
    if b[0] != 2 || b[1] != 1 {
        fail!("that didn't work");
    }
}

#[test]
fn test_partition() {
    let a: ~[int] = ~[2, 8, 7, 1, 3, 5, 6, 4];
    let partitioning = partition(a, 0, 7);
    match partitioning {
        (3, _unused) => (), // OK
        _ => fail!("it should have partitioned at index 3")
    }
}

#[test]
fn test_sorted() {
    let a: ~[int] = ~[7, 8, 9, 1, 2, 11, 5, 12, 3, 4, 6, 0, 10];
    let sorted = quicksort(a, 0, 12);
    println!("sorted {:?}", sorted);
    for i in range(0, 11) {
        assert!(sorted[i] <= sorted[i+1]);
    }
}
