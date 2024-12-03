use std::fs;

#[derive(Debug, Clone)]
struct Present {
    width: i32,
    length: i32,
    height: i32,
}

impl Present {
    fn from_line(line: &str) -> Self {
        Present::from_vec(line.split("x").map(|x| x.parse::<i32>().unwrap()).collect())
    }

    fn from_vec(vals: Vec<i32>) -> Self {
        Present {
            width: vals[0],
            length: vals[1],
            height: vals[2],
        }
    }

    fn get_area(&self) -> i32 {
        let area = (2 * self.width * self.length)
            + (2 * self.width * self.height)
            + (2 * self.length * self.height);
        let mut smallest = vec![self.width, self.length, self.height];
        smallest.sort();
        let extra = smallest[0] * smallest[1];
        area + extra
    }

    fn get_ribbon(&self) -> i32 {
        let mut smallest = vec![self.width, self.length, self.height];
        smallest.sort();
        let ribbon = 2* smallest[0] + 2 * smallest[1];
        let bow = self.width * self.length * self.height;
        (ribbon + bow)
    }
}

fn get_input(filename: &str) -> Vec<Present> {
    let input = fs::read_to_string(filename).unwrap();
    let mut presents: Vec<Present> = [].to_vec();
    for line in input.split("\n") {
        presents.push(Present::from_line(line));
    }
    presents
}

fn part1(presents: &Vec<Present>) -> i32 {
    let mut area: i32 = 0;
    for present in presents {
        area += present.get_area();
    }
    area
}


fn part2(presents: &Vec<Present>) -> i32 {
    let mut ribbon: i32 = 0;
    for present in presents {
        ribbon += present.get_ribbon();
    }
    ribbon
}

fn main() {
    let presents = get_input("input.txt");
    println!("Part 1: {}", part1(&presents));
    println!("Part 2: {}", part2(&presents));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part1_1() {
        let present = Present::from_line(&"2x3x4".to_string());
        assert_eq!(present.get_area(), 58)
    }

    #[test]
    fn test_part1_2() {
        let present = Present::from_line(&"1x1x10".to_string());
        assert_eq!(present.get_area(), 43)
    }

    #[test]
    fn test_part2_1() {
        let present = Present::from_line(&"2x3x4".to_string());
        assert_eq!(present.get_ribbon(), 34)
    }

    #[test]
    fn test_part2_2() {
        let present = Present::from_line(&"1x1x10".to_string());
        assert_eq!(present.get_ribbon(), 14)
    }
}
