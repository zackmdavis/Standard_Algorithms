// somewhat literal-minded port of the code demonstrated in
// http://zackmdavis.net/blog/2013/06/huffman/

use std::cmp::Ordering;
use std::collections::{BinaryHeap, HashMap};


type Bit = bool;
const ZERO: Bit = false;
const ONE: Bit = true;

#[derive(Debug, Eq, Ord, Clone)]
struct HuffmanNode {
    character: Option<char>,
    frequency: u32,
    left: Box<Option<HuffmanNode>>,
    right: Box<Option<HuffmanNode>>
}

impl PartialOrd for HuffmanNode {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        // let's have nodes compare in reverse order by frequency, so that we
        // can use the standard library's BinaryHeap as a min-priority queue,
        // even though it's a max heap
        Some(other.frequency.cmp(&self.frequency))
    }
}

impl PartialEq for HuffmanNode {
    fn eq(&self, other: &Self) -> bool {
        self.frequency == other.frequency
    }

    fn ne(&self, other: &Self) -> bool {
        !self.eq(other)
    }
}

struct Codebook(HashMap<char, Vec<Bit>>);

impl HuffmanNode {
    pub fn codebook(&self) -> Codebook {
        let mut codes = HashMap::new();

        fn traversal(codes: &mut HashMap<char, Vec<Bit>>,
                     item: &Box<Option<HuffmanNode>>, code: Vec<Bit>) {

            fn append_bit(prior_code: &Vec<Bit>, addition: Bit) -> Vec<Bit> {
                let mut code = prior_code.clone();
                code.push(addition);
                code
            }

            if let Some(ref node) = **item {
                traversal(codes, &node.left, append_bit(&code, ZERO));
                if let Some(character) = node.character {
                    codes.insert(character, code.clone());
                }
                traversal(codes, &node.right, append_bit(&code, ONE));
            }

        }
        traversal(&mut codes, &Box::new(Some(self.clone())), vec![]);
        Codebook(codes)
    }
}


fn huffman(frequencies: &HashMap<char, u32>) -> Codebook {
    let mut priority_queue = BinaryHeap::with_capacity(frequencies.len());
    let leaves = frequencies.iter().map(|(&c, &f)| {
        HuffmanNode {
            character: Some(c),
            frequency: f,
            left: Box::new(None),
            right: Box::new(None)
        }
    });
    for leaf in leaves.into_iter() {
        priority_queue.push(leaf);
    }
    for _ in 0..(frequencies.len() - 1) {
        let left = priority_queue.pop();
        let right = priority_queue.pop();
        let new_node = HuffmanNode {
            character: None,
            frequency: left.as_ref().map_or(0, |n| { n.frequency }) +
                right.as_ref().map_or(0, |n| { n.frequency }),
            left: Box::new(left),
            right: Box::new(right)
        };
        priority_queue.push(new_node);
    }
    priority_queue.pop().unwrap().codebook()
}

impl Codebook {
    fn encode(&self, plaintext: &str) -> Vec<Bit> {
        let mut ciphertext = Vec::new();
        for character in plaintext.chars() {
            let codeword = &self.0[&character];
            ciphertext.extend_from_slice(codeword);
        }
        ciphertext
    }
}

fn main() {
    let mut frequencies = HashMap::new();
    let frequency_data = vec![
        ('A', 8167), ('B', 1492), ('C', 2782), ('D', 4253), ('E', 12702),
        ('F', 2228), ('G', 2015), ('H', 6094), ('I', 6966), ('J', 153),
        ('K', 772), ('L', 4025), ('M', 2406), ('N', 6749), ('O', 7507),
        ('P', 1929), ('Q', 95), ('R', 5987), ('S', 6327), ('T', 9056),
        ('U', 2758), ('V', 978), ('W', 2360), ('X', 150), ('Y', 1974),
        ('Z', 74), (' ', 13000), ('.', 4250), (',', 4250)
    ];
    for &(character, frequency) in &frequency_data {
        frequencies.insert(character, frequency);
    }
    let codebook = huffman(&frequencies);
    let plaintext = "I USED TO WONDER WHAT FRIENDSHIP COULD BE, \
                     UNTIL YOU ALL SHARED ITS MAGIC WITH ME.";
    let ciphertext = codebook.encode(plaintext);
    for bit in ciphertext {
        print!("{}", if bit { 1 } else { 0 });
    }
    println!("");
}
