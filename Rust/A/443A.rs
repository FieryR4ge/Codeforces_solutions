use std::collections::HashSet;
use std::io;

fn main() {
    let mut line = String::new();

    io::stdin()
        .read_line(&mut line)
        .unwrap();

    let line: String = line.trim().to_string();

    let line: String =
        line.chars()
            .filter(|x| x != &'{' && x != &'}')
            .collect();

    let words: Vec<&str> =
        line.split(", ")
            .collect();

    let mut set = HashSet::new();

    for word in words.clone() {
        set.insert(word);
    }

    if words[0] == "" {
        println!("{}", 0);
    } else {
        println!("{}", set.len());
    }
}