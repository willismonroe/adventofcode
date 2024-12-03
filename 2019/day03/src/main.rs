use std::collections::HashMap;
use std::fs;

#[derive(Debug)]
struct Loc {
    wire_num: u32,
    steps: u32,
}

pub fn manhattan_d(ax: i32, ay: i32, bx: i32, by: i32) -> u32 {
    ((ax - bx).abs() + (ay - by).abs()) as u32
}

fn write_write_path(
    wire_path: &str,
    wire_num: u32,
    visited: &mut HashMap<(i32, i32), Loc>,
) -> (u32, u32) {
    let mut x = 0;
    let mut y = 0;
    let mut nearest = std::u32::MAX;
    let mut steps = 0;
    let mut fewest_steps = std::u32::MAX;

    for mv in wire_path.split(",") {
        let a = &mv[..1];
        let d = &mv[1..].parse::<i32>().unwrap();

        let dir = match a {
            "U" => (1, 0),
            "D" => (-1, 0),
            "L" => (0, -1),
            "R" => (0, 1),
            _ => (0, 0),
        };

        for _ in 0..*d {
            x += dir.0;
            y += dir.1;
            steps += 1;
            let key = (x, y);
            let loc = Loc { wire_num, steps };

            let v = visited.entry(key).or_insert(loc);
            if v.wire_num != wire_num {
                let vd = manhattan_d(0, 0, key.0, key.1);
                if vd < nearest {
                    nearest = vd;
                }
                let steps_to_here = v.steps + steps;
                if steps_to_here < fewest_steps {
                    fewest_steps = steps_to_here
                }
            }
        }
    }
    (nearest, fewest_steps)
}

fn main() {
    let input = fs::read_to_string("./input.txt").unwrap();
    let wires: Vec<&str> = input.trim().split("\n").map(|l| l.trim()).collect();

    let mut visited = HashMap::new();

    write_write_path(wires[0], 1, &mut visited);
    let (nearest, fewest_steps) = write_write_path(wires[1], 2, &mut visited);
    println!("Part A: {}", nearest);
    println!("Part B: {}", fewest_steps);
}
