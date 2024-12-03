extern crate crypto;

use crypto::md5::Md5;
use crypto::digest::Digest;

fn solve(input: &str, target: &str) -> u64 {
    let mut hasher = Md5::new();
    let mut suffix: u64 = 1;
    // let mut output;
    loop {
        hasher.input_str(&format!("{}{}",input,suffix));
        let output = hasher.result_str();
        hasher.reset();
        if &output[0..target.len()] == target {
            break;
        } else {
            suffix += 1;
        }
    }
    // println!("{:?}", output);
    suffix
}

fn main() {
    let input = "ckczppom";
    println!("Part 1: {}", solve(&input, "00000"));
    println!("Part 2: {}", solve(&input, "000000"));

}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part1_1() {
        let input = "abcdef".to_string();
        assert_eq!(part1(&input), 609043)
    }

    #[test]
    fn test_part1_2() {
        let input = "pqrstuv".to_string();
        assert_eq!(part1(&input), 1048970)
    }
}