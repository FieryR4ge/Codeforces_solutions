use std::io;

fn main() {
    let mut t = String::new();
    io::stdin().read_line(&mut t).expect("Invalid input t");

    let t: i64 = t.trim().parse::<i64>().unwrap();

    for _ in 0..t {
        let mut n = String::new();
        io::stdin().read_line(&mut n).expect("Invalid input n");

        let n: i64 = n.trim().parse::<i64>().unwrap();
        let k: i64 = ((2_f64 / 3_f64) as f64 * n as f64).ceil() as i64 / 2 as i64;
        let l: i64 = n - (2 * k);

        println!("{} {}", l, k);
    }
}