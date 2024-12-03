use std::collections::HashMap;
use std::fs;

// https://github.com/galenelias/AdventOfCode_2015/blob/master/src/Day5/mod.rs

// fn vowels(input: &str) -> u8 {
//     let mut vowel_map: HashMap<char, bool> = HashMap::new();
//     for c in input.chars() {
//         match c {
//             'a' => {
//                 vowel_map.entry(c).or_insert(true);
//             }
//             'e' => {
//                 vowel_map.entry(c).or_insert(true);
//             }
//             'i' => {
//                 vowel_map.entry(c).or_insert(true);
//             }
//             'o' => {
//                 vowel_map.entry(c).or_insert(true);
//             }
//             'u' => {
//                 vowel_map.entry(c).or_insert(true);
//             }
//             _ => {}
//         };
//     }
//     vowel_map.len() as u8
// }

fn get_input() -> Vec<String> {
    let input = fs::read_to_string("input.txt").unwrap();
    let mut output: Vec<String> = vec![];
    for line in input.split("\n") {
        output.push(line.to_string());
    }
    output
}

fn vowels(input: &str) -> bool {
    let mut count: u8 = 0;
    for c in input.chars() {
        match c {
            'a' | 'e' | 'i' | 'o' | 'u' => count += 1,
            _ => {}
        }
        if count > 2 {
            return true;
        }
    }
    false
}

fn double_letter(input: &str) -> bool {
    let mut prev: char = 'A';
    for c in input.chars() {
        if c == prev {
            return true;
        }
        prev = c;
    }
    false
}

fn no_banned_pairs(input: &str) -> bool {
    if input.find("ab") == None
        && input.find("cd") == None
        && input.find("pq") == None
        && input.find("xy") == None
    {
        return true;
    }
    false
}

fn nice(input: &str) -> bool {
    // let mut nice_vowels: bool = false;
    if vowels(&input) && double_letter(&input) && no_banned_pairs(&input) {
        return true;
    }
    false
}

fn main() {
    let input = get_input();
    println!(
        "Part 1: {}",
        input
            .clone()
            .iter()
            .filter(|s| nice(s))
            .count()
    );
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part1_1() {
        let input = "ugknbfddgicrmopn".to_string();
        assert_eq!(nice(&input), true)
    }

    #[test]
    fn test_part1_2() {
        let input = "aaa".to_string();
        assert_eq!(nice(&input), true)
    }

    #[test]
    fn test_part1_3() {
        let input = "jchzalrnumimnmhp".to_string();
        assert_eq!(nice(&input), false)
    }

    #[test]
    fn test_part1_4() {
        let input = "haegwjzuvuyypxyu".to_string();
        assert_eq!(nice(&input), false)
    }

    #[test]
    fn test_part1_5() {
        let input = "dvszwmarrgswjxmb".to_string();
        assert_eq!(nice(&input), false)
    }
}
