use std::io;

fn read_line() -> String {
    let mut line = String::new();
    io::stdin().read_line(&mut line).expect("invalid input");
    line
}

fn main() {
    let _ = read_line().trim().parse::<u32>().unwrap();

    let n = read_line().trim().parse::<String>().unwrap();

    let one = n.matches("n").count();
    let zero = n.matches("z").count();

    for _ in 0..one {
        print!("1 ");
    }

    for _ in 0..zero {
        println!("0 ");
    }
}