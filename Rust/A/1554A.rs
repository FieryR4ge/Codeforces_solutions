use std::io;

fn read_line() -> String {
    let mut line = String::new();
    io::stdin().read_line(&mut line).expect("invalid input");
    line
}

fn main() {
    let t = read_line().trim().parse::<u32>().unwrap();

    for _ in 0..t {
        let _ = read_line().trim().parse::<u32>();
        let n = read_line()
            .split_whitespace()
            .map(|number| number.parse().unwrap())
            .collect::<Vec<u64>>();

        let mut max = 0;
        for i in 0..(n.len() - 1) {
            if n[i] * n[i + 1] > max {
                max = n[i] * n[i + 1]
            }
        }

        println!("{}", max);
    }
}