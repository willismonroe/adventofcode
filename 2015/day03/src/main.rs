use std::collections::HashMap;
use std::fs;

fn get_input() -> String {
    let input = fs::read_to_string("input.txt").unwrap();
    input
}

fn parse_input(input: &str) -> HashMap<(i32, i32), u32> {
    let mut houses: HashMap<(i32, i32), u32> = HashMap::new();
    let mut x = 0;
    let mut y = 0;
    houses.entry((x, y)).or_insert(1);
    for c in input.chars() {
        match c {
            '^' => y += 1,
            '>' => x += 1,
            'v' => y -= 1,
            '<' => x -= 1,
            _ => panic!("Unexpected character"),

        }
        houses.entry((x, y)).or_insert(1);
    }
    houses
} 

fn part1(input: &str) -> u32 {
    let houses = parse_input(&input);
    houses.len() as u32
}

fn part2(input: &str) -> u32 {
    let input1: String = input.chars().step_by(2).collect();
    let input2: String = input.chars().skip(1).step_by(2).collect();
    
    let mut houses = parse_input(&input1);
    houses.extend(parse_input(&input2));
    houses.len() as u32
}

fn main() {
    let input = get_input();
    println!("Part 1: {}", part1(&input));
    println!("Part 2: {}", part2(&input));
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part1_1() {
        let input = ">".to_string();
        assert_eq!(part1(&input), 2)
    }

    #[test]
    fn test_part1_2() {
        let input = "^>v<".to_string();
        assert_eq!(part1(&input), 4)
    }

    #[test]
    fn test_part1_3() {
        let input = "^v^v^v^v^v".to_string();
        assert_eq!(part1(&input), 2)
    }

    #[test]
    fn test_part2_1() {
        let input = "^v".to_string();
        assert_eq!(part2(&input), 3)
    }

    #[test]
    fn test_part2_2() {
        let input = "^>v<".to_string();
        assert_eq!(part2(&input), 3)
    }

    #[test]
    fn test_part2_3() {
        let input = "^v^v^v^v^v".to_string();
        assert_eq!(part2(&input), 11)
    }
}