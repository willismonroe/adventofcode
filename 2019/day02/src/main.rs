use std::fs;
use std::path::Path;

fn main() {
    let input_a = get_input("input.txt");
    let mut input_a: Vec<&str> = input_a.split(",").collect();
    input_a[1] = "12";
    input_a[2] = "2";
    let input_a = input_a.join(",");
    let result_a: u32 = part_a(&input_a);
    println!("Part A: {}", result_a);
    let (noun, verb) = part_b(&input_a);
    println!("Part B: {}", (100 * noun + verb));
}

fn get_input<P: AsRef<Path>>(filename: P) -> String {
    let file_string = fs::read_to_string(filename).unwrap();
    return file_string;
}

fn part_a(input: &str) -> u32 {
    let mut tokens: Vec<u32> = input
        .split(",")
        .map(|item| item.parse::<u32>().unwrap())
        .collect();
    let mut cursor: usize = 0;
    loop {
        let token: u32 = tokens[cursor];
        // println!("{} - {}", cursor, token);
        match token {
            1 => {
                let loc = tokens[cursor + 3] as usize;
                let loc_x = tokens[cursor + 1] as usize;
                let loc_y = tokens[cursor + 2] as usize;
                tokens[loc] = tokens[loc_x] + tokens[loc_y];
            }
            2 => {
                let loc = tokens[cursor + 3] as usize;
                let loc_x = tokens[cursor + 1] as usize;
                let loc_y = tokens[cursor + 2] as usize;
                tokens[loc] = tokens[loc_x] * tokens[loc_y];
            }
            3..=98 => println!("Something went wrong: {}", token),
            99 => break,
            _ => println!("Don't know what we got here: {}", token),
        }
        cursor += 4;
    }
    return tokens[0];
}

fn part_b(input: &str) -> (u32, u32) {
    let mut noun = 0;
    let mut verb = 0;
    while noun < 100 {
        while verb < 100 {
            // println!("Checking {} and {}", noun, verb);
            let mut new_input: Vec<&str> = input.split(",").collect();
            let new_noun = noun.to_string();
            let new_verb = verb.to_string();
            new_input[1] = &new_noun;
            new_input[2] = &new_verb;
            let new_input = new_input.join(",");
            let result = part_a(&new_input);
            if result == 19690720 {
                return (noun, verb)
            }
            verb += 1;
        }
        verb = 0;
        noun += 1;
    }
    return (0, 0);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_a() {
        let input_1: String = "1,0,0,0,99".to_string();
        let input_2: String = "2,3,0,3,99".to_string();
        let input_3: String = "2,4,4,5,99,0".to_string();
        let input_4: String = "1,1,1,4,99,5,6,0,99".to_string();

        assert_eq!(part_a(&input_1), 2);
        assert_eq!(part_a(&input_2), 2);
        assert_eq!(part_a(&input_3), 2);
        assert_eq!(part_a(&input_4), 30);
    }

    // #[test]
    // fn test_part_b() {
    //     let input_1: String = "";
    //     let input_2: Vec<i64> = "";
    //     let input_3: Vec<i64> = [100756].to_vec();

    //     assert_eq!(part_b(&input_1), 2);
    //     assert_eq!(part_b(&input_2), 966);
    //     assert_eq!(part_b(&input_3), 50346);
    // }
}
