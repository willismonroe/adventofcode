use std::fs;

fn part1(directions: &String) -> i32 {
    let mut output: i32 = 0;
    for dir in directions.chars() {
        match dir {
            '(' => output += 1,
            ')' => output -= 1,
            _ => break 
        }
    }
    output
}

fn part2(directions: &String) -> u32 {
    let mut output: i32 = 0;
    for (i, dir) in directions.chars().enumerate() {
        match dir {
            '(' => output += 1,
            ')' => output -= 1,
            _ => break 
        }
        if output < 0 {
            return (i + 1) as u32
        }
    }
    0
}

fn main() {
    let input = fs::read_to_string("input.txt").unwrap();
    let dir = part1(&input);
    println!("Part 1: {}", dir);

    let idx = part2(&input);
    println!("Part 2: {}", idx);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part1_1() {
        assert_eq!(part1(&"(())".to_string()), 0)
    }

    #[test]
    fn test_part1_2() {
        assert_eq!(part1(&"()()".to_string()), 0)
    }

    #[test]
    fn test_part1_3() {
        assert_eq!(part1(&"(((".to_string()), 3)
    }

    #[test]
    fn test_part1_4() {
        assert_eq!(part1(&"(()(()(".to_string()), 3)
    }

    #[test]
    fn test_part1_5() {
        assert_eq!(part1(&"))(((((".to_string()), 3)
    }

    #[test]
    fn test_part1_6() {
        assert_eq!(part1(&"())".to_string()), -1)
    }

    #[test]
    fn test_part1_7() {
        assert_eq!(part1(&"())".to_string()), -1)
    }

    #[test]
    fn test_part1_8() {
        assert_eq!(part1(&")))".to_string()), -3)
    }

    #[test]
    fn test_part1_9() {
        assert_eq!(part1(&")())())".to_string()), -3)
    }

    #[test]
    fn test_part2_1() {
        assert_eq!(part2(&")".to_string()), 1)
    }

    fn test_part2_2() {
        assert_eq!(part2(&"()())".to_string()), 5)
    }
}