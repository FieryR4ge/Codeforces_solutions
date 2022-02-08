use std::io;

fn read_line() -> String {
    let mut line = String::new();
    io::stdin().read_line(&mut line).expect("invalid input");
    line
}

fn main() {
    let t = read_line().trim().parse::<u32>().unwrap();

    for _ in 0..t {
        let mut n = read_line()
            .split_whitespace()
            .map(|number| number.parse().unwrap())
            .collect::<Vec<u32>>();

        n.sort();

        if n[0] + n[1] == n[2] || (n[0] % 2 == 0 && n[1] == n[2]) || (n[0] == n[1] && n[2] % 2 == 0) {
            println!("YES");
        } else {
            println!("NO");
        }
    }
}