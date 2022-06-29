use std::io;

fn read_line() -> String {
    let mut line = String::new();
    io::stdin().read_line(&mut line).expect("invalid input");
    line
}

fn main() {
    let t = read_line().trim().parse::<i32>().unwrap();
    let s = "989".to_string();

    for _ in 0..t {
        let n = read_line().trim().parse::<i32>().unwrap();
        if n <= 3 {
            println!("{}", &s[..(n as usize)])
        } else {
            print!("{}", s);
            for i in 3..n {
                print!("{}", (i - 3) % 10);
            }
            println!();
        }
    }
}
