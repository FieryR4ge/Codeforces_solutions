use std::collections::HashSet;
use std::io;
use std::io::*;

fn main() {
    let mut input: String = String::new();
    io::stdin().read_line(&mut input).expect("invalid input");

    let mut counter: u32 = input.trim().parse::<u32>().unwrap() + 1;

    while counter
        .to_string()
        .chars()
        .map(|c|
            c.to_digit(10).unwrap()
        )
        .collect::<HashSet<u32>>().len() < 4 {
        counter += 1;
    }

    println!("{}", counter);
}
