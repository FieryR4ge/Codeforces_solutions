use std::io;

fn main() {
    let mut numbers = String::new();

    io::stdin()
        .read_line(&mut numbers)
        .unwrap();

    let numbers: i64 = numbers.trim().parse().unwrap();

    for _ in 0..numbers {
        let mut line = String::new();

        io::stdin()
            .read_line(&mut line)
            .unwrap();

        let words: Vec<i64> =
            line
                .split_whitespace()
                .map(|number|
                    number.parse().unwrap())
                .collect();

        let a = words[0];
        let b = words[1];

        if a % b == 0 {
            println!("0");
        } else {
            println!("{}", b - a % b);
        }
    }
}