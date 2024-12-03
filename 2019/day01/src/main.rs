use std::fs::read_to_string;

fn main() {
    let input = read_to_string("input.txt").expect("Something is wrong reading the file.");
    let masses = parse(&input).expect("Failed to parse.");
    let result_a: isize = part_a(&masses);
    println!("Part A: {}", result_a);
    let result_b: isize = part_b(&masses);
    println!("Part B: {}", result_b);
}

fn parse(input: &str) -> Option<Vec<isize>> {
    input.lines().map(|s| s.parse().ok()).collect()
}

fn part_a(input: &Vec<isize>) -> isize {
    let mut sum: isize = 0;
    for module in input {
        let result = module / 3 - 2;
        sum += result;
    }
    return sum;
}

fn part_b(input: &Vec<isize>) -> isize {
    let mut sum: isize = 0;
    for module in input {
        let mut result: isize = module / 3 - 2;
        loop {
            if result < 0 {
                // sum += result;
                break;
            }
            sum += result;
            result = result / 3 - 2;
        }
    }
    return sum;
}

// Iter.fold(init: B, f: F), .fold(0, |acc, x| acc + x)

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_a() {
        let input_1: Vec<isize> = [12].to_vec();
        let input_2: Vec<isize> = [14].to_vec();
        let input_3: Vec<isize> = [1969].to_vec();
        let input_4: Vec<isize> = [100756].to_vec();

        assert_eq!(part_a(&input_1), 2);
        assert_eq!(part_a(&input_2), 2);
        assert_eq!(part_a(&input_3), 654);
        assert_eq!(part_a(&input_4), 33583);
    }

    #[test]
    fn test_part_b() {
        let input_1: Vec<isize> = [14].to_vec();
        let input_2: Vec<isize> = [1969].to_vec();
        let input_3: Vec<isize> = [100756].to_vec();

        assert_eq!(part_b(&input_1), 2);
        assert_eq!(part_b(&input_2), 966);
        assert_eq!(part_b(&input_3), 50346);
    }
}
