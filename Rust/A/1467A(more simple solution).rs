use std::io;

fn read_line() -> String {
    let mut line = String::new();
    io::stdin().read_line(&mut line).expect("invalid input");
    line
}

fn main() {
    let t = read_line().trim().parse::<i32>().unwrap();
    let mut answer = "989".to_string();
    answer.push_str(&"0123456789".repeat(20000));

    for _ in 0..t {
        let n = read_line().trim().parse::<i32>().unwrap();
        println!("{}", &answer[..(n as usize)]);
    }
}