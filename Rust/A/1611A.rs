use std::io;

fn read_line() -> String {
    let mut line = String::new();
    io::stdin().read_line(&mut line).expect("invalid input");
    line
}

fn main() {
    let mut input: String = String::new();
    io::stdin().read_line(&mut input).expect("invalid input");

    let t: i32 = input.trim().parse().unwrap();

    for _ in 0..t {
        let mut input_str: String = String::new();
        io::stdin().read_line(&mut input_str).expect("invalid str");

        let s: String = input_str.trim().parse().unwrap();

        let first_digit: i32 = s.chars().next().unwrap() as i32;
        let last_digit: i32 = s.chars().last().unwrap() as i32;

        if last_digit % 2 == 0 {
            println!("0");
            continue
        }
        if first_digit % 2 == 0 {
            println!("1");
            continue
        }

        let count_2 = s.matches('2').count();
        let count_4 = s.matches('4').count();
        let count_6 = s.matches('6').count();
        let count_8 = s.matches('8').count();

        if count_2 > 0 || count_4 > 0 || count_6 > 0 || count_8 > 0 {
            println!("2");
            continue
        }
        println!("-1");
    }
}