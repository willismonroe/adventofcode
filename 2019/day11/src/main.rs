use intcode::{get_computer, IntCodeComputer, Signal};
use std::error::Error;
use std::fs::File;
use std::io::prelude::*;

use std::collections::HashSet;

const BLACK: i64 = 0;
const WHITE: i64 = 1;

const LEFT: i64 = 0;
const RIGHT: i64 = 1;

fn get_input() -> Result<Vec<i64>, Box<dyn Error>> {
    let mut f = File::open("input.txt")?;
    let mut s = String::new();
    f.read_to_string(&mut s)?;

    Ok(s.split(',').filter_map(|x| x.parse::<i64>().ok()).collect())
}

enum Direction {
    Up,
    Down,
    Left,
    Right,
}

struct EHPR {
    loc: (i64, i64),
    dir: Direction,
    board: Vec<Vec<i64>>,
    comp: IntCodeComputer,
}

impl EHPR {
    fn new(input: &Vec<i64>, (height, width): (usize, usize)) -> Self {
        EHPR {
            loc: (0, 0),
            dir: Direction::Up,
            board: vec![vec![BLACK; width]; height],
            comp: get_computer(&input, vec![]),
        }
    }

    fn set_location(&mut self, loc: (i64, i64)) {
        self.loc = loc;
    }

    fn paint_board(&mut self, color: i64) {
        let (x, y) = self.loc;
        self.board[y as usize][x as usize] = color;
    }

    fn get_color(&self) -> i64 {
        let (x, y) = self.loc;
        self.board[y as usize][x as usize]
    }

    fn turn_right(&mut self) {
        use Direction::*;
        self.dir = match self.dir {
            Up => Right,
            Down => Left,
            Left => Up,
            Right => Down,
        }
    }

    fn turn_left(&mut self) {
        use Direction::*;
        self.dir = match self.dir {
            Up => Left,
            Down => Right,
            Left => Down,
            Right => Up,
        }
    }

    fn turn(&mut self, dir: i64) {
        if dir == LEFT {
            self.turn_left()
        } else if dir == RIGHT {
            self.turn_right();
        } else {
            panic!("Unknown direction {}", dir);
        }
    }

    fn move_forward(&mut self) {
        use Direction::*;
        let (x, y) = self.loc;
        self.loc = match self.dir {
            Up => (x, y - 1),
            Down => (x, y + 1),
            Left => (x - 1, y),
            Right => (x + 1, y),
        }
    }

    fn turn_and_move(&mut self, dir: i64) {
        self.turn(dir);
        self.move_forward();
    }

    fn tick(&mut self) -> bool {
        match self.comp.run() {
            Signal::Halt => return false,
            Signal::ProducedOutput => {
                let paint_color = self.comp.get_output().unwrap();
                self.paint_board(paint_color);

                self.comp.run_till_signal(Signal::ProducedOutput);
                let direction = self.comp.get_output().unwrap();
                self.turn_and_move(direction);

                self.comp.feed_input(self.get_color())
            }
            _ => panic!("No"),
        }
        true
    }

    fn print_board(&self) {
        for row in self.board.iter() {
            for j in row {
                print!("{}", if *j == BLACK { ' ' } else { '#' });
            }
            println!("");
        }
    }
}

fn part1(inp: &Vec<i64>) -> i64 {
    let mut hs: HashSet<(i64, i64)> = HashSet::new();
    let mut count: i64 = 0;

    let mut robot = EHPR::new(&inp, (201, 201));
    robot.set_location((100, 100));
    robot.comp.feed_input(BLACK);

    while robot.tick() {
        if !hs.contains(&robot.loc) {
            hs.insert(robot.loc);
            count += 1
        }
    }
    count
}

fn part2(inp: &Vec<i64>) {
    let mut robot = EHPR::new(&inp, (6, 45));
    robot.board[0][0] = WHITE;
    robot.comp.feed_input(WHITE);
    while robot.tick() {}
    robot.print_board();
}

fn main() {
    let input: Vec<i64> = get_input().unwrap();

    println!("Part 1: {:?}", part1(&input));
    println!("Part 2:");
    part2(&input);
}
