const fs = require("fs");
const solve = require("./solve");

const day_num = "04";

const test_input = [
  "[1518-11-01 00:00] Guard #10 begins shift",
  "[1518-11-01 00:05] falls asleep",
  "[1518-11-01 00:25] wakes up",
  "[1518-11-01 00:30] falls asleep",
  "[1518-11-01 00:55] wakes up",
  "[1518-11-01 23:58] Guard #99 begins shift",
  "[1518-11-02 00:40] falls asleep",
  "[1518-11-02 00:50] wakes up",
  "[1518-11-03 00:05] Guard #10 begins shift",
  "[1518-11-03 00:24] falls asleep",
  "[1518-11-03 00:29] wakes up",
  "[1518-11-04 00:02] Guard #99 begins shift",
  "[1518-11-04 00:36] falls asleep",
  "[1518-11-04 00:46] wakes up",
  "[1518-11-05 00:03] Guard #99 begins shift",
  "[1518-11-05 00:45] falls asleep",
  "[1518-11-05 00:55] wakes up"
];

test(`Day ${day_num} Part A tests`, () => {
  expect(solve.partA(test_input)).toBe(240);
});

test(`Day ${day_num} Part B test`, () => {
  expect(solve.partB(test_input)).toBe(4455);
});

describe("Testing answers", () => {
  let aocInput;

  beforeAll(() => {
    aocInput = fs
      .readFileSync(__dirname + "/input.txt")
      .toString()
      .split("\n")
      .map(s => s.replace(/\r$/, ""))
      .filter(s => s.length > 0);
  });
  test(`Day ${day_num} Part A`, () => {
    expect(solve.partA(aocInput)).toBe(77084);
  });

  test(`Day ${day_num} Part B`, () => {
    expect(solve.partB(aocInput)).toBe(23047);
  });
});
