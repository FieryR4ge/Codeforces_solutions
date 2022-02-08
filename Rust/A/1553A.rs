use std::io;

fn read_line() -> String {
    let mut line = String::new();
    io::stdin().read_line(&mut line).expect("invalid input");
    line
}

fn main() {
    let t = read_line().trim().parse::<i32>().unwrap();

    for _ in 0..t {
        let n = read_line().trim().parse::<i32>().unwrap();

        println!("{}", (n + 1) / 10);
    }
}