use std::io;

fn main() {
    let mut t = String::new();

    io::stdin().read_line(&mut t).expect("Invalid input t");
    let t: i64 = t.trim().parse::<i64>().unwrap();

    for _ in 0..t {
        let mut parameters = String::new();
        io::stdin().read_line(&mut parameters).expect("Invalid input parameters");

        let parameters: Vec<i64> = parameters
            .split_whitespace()
            .map(|number|
                number.parse().unwrap()
            )
            .collect();

        let w = parameters[0];
        let h = parameters[1];
        let n = parameters[2];

        let mut parts = 1;
        let mut square = w * h;

        while square % 2 == 0 {
            square /= 2;
            parts *= 2;
        };

        let answer = if parts >= n {"YES"} else {"NO"};

        println!("{}", answer);
    }
}