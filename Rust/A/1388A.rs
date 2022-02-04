use std::io;
use std::io::*;


fn main() {
    let mut input: String = String::new();
    io::stdin().read_line(&mut input).expect("invalid input");

    let t: i32 = input.trim().parse().unwrap();

    for i in 0..t {
        let mut input_number: String = String::new();
        io::stdin().read_line(&mut input_number).expect("invalid number");

        let number: i32 = input_number.trim().parse().unwrap();

        if number <= 30 {
            println!("NO");
        } else {
            println!("YES");
            if number.eq(&36) || number.eq(&40) || number.eq(&44) {
                println!("6 10 15 {}", number - 31);
            } else {
                println!("6 10 14 {}", number - 30);
            }
        }
    }
}