use std::io;

fn main() {
    let mut input: String = String::new();
    io::stdin().read_line(&mut input).expect("invalid input");

    let t: i32 = input.trim().parse().unwrap();

    for _ in 0..t {
        let mut input_str: String = String::new();
        io::stdin().read_line(&mut input_str).expect("invalid str");

        let s: String = input_str.trim().parse().unwrap();

        println!("{}",s.len())
    }
}