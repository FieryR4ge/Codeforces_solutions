use std::io;

fn main() {
    let mut input: String = String::new();
    io::stdin().read_line(&mut input).expect("invalid input");

    let t: i32 = input.trim().parse().unwrap();

    for _ in 0..t {
        let mut input_number: String = String::new();
        io::stdin().read_line(&mut input_number).expect("invalid number");

        let mut input_str: String = String::new();
        io::stdin().read_line(&mut input_str).expect("invalid str");

        let substr: String = input_str.trim().parse().unwrap();

        if substr.starts_with("2") && substr.ends_with("020") || substr.starts_with("2020") ||
            substr.ends_with("2020") || substr.starts_with("20") && substr.ends_with("20") ||
            substr.starts_with("202") && substr.ends_with("0") {
            println!("YES")
        } else {
            println!("NO")
        }
    }
}