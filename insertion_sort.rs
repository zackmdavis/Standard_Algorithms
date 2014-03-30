fn insertion_sort(a: ~[int]) -> ~[int] {
    let mut b = ~[];
    b.push_all(a);
    for i in range(1, b.len()) {
        let consideration = b[i];
        let mut cursor = i-1;
        while cursor >= 0 && cursor < b.len() &&
              b[cursor] > consideration {
            b[cursor+1] = b[cursor];
            cursor -= 1;
        }
        b[cursor+1] = consideration;
    }
    b
}

fn main() {
    println!("{:?}", insertion_sort(~[9, 7, 6, 5, 0, 4, 1]));
}