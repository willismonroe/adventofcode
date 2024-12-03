use std::fs;

const EXP: [i64; 6] = [100_000, 10_000, 1000, 100, 10, 1];

fn convert_to_array(n: i64) -> [i8; 6] {
    assert!(n >= 0);
    assert!(n <= 999_999);
    let mut x = n;
    let mut d = [0i8; 6];
    for i in 0..6usize {
        let m = EXP[i];
        d[i] = (x / m) as i8;
        x %= m;
    }
    d
}

fn check_pw(num: i64) -> bool {
    let digits = convert_to_array(num);
    let mut last: i8 = -1;
    let mut has_double = false;
    for &d in &digits {
        if d < last {
            return false;
        }
        if d == last {
            has_double = true;
        }
        last = d;
    }
    has_double
}

fn check_pw_two(num: i64) -> bool {
    let digits = convert_to_array(num);
    let mut last: i8 = -1;
    let mut digit_count = 1;
    let mut has_double = false;
    for &d in &digits {
        if d < last {
            return false;
        }
        if d == last {
            digit_count += 1;
        } else {
            if digit_count == 2 {
                has_double = true;
            }
            digit_count = 1;
        }
        last = d;
    }
    if digit_count == 2 {
        has_double = true;
    }
    has_double
}

fn count_passwords<F>(start: i64, end: i64, check: F) -> usize
where
    F: Fn(i64) -> bool,
{
    (start..=end).filter(|&n| check(n)).count()
}

fn main() {
    let input = fs::read_to_string("./input.txt").unwrap();
    let mut min_max = input.split("-").map(|i| i.parse::<i64>().unwrap());
    let min: i64 = min_max.next().unwrap();
    let max: i64 = min_max.next().unwrap();
    let result1 = count_passwords(min, max, check_pw);
    println!("{}", result1);
    let result2 = count_passwords(min, max, check_pw_two);
    println!("{}", result2);
}
