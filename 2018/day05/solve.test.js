const fs = require("fs");
const solve = require("./solve");

const day_num = "05";

const test_input = ["dabAcCaCBAcCcaDA"];

test(`Day ${day_num} Part A tests`, () => {
  expect(solve.partA(test_input)).toBe(10);
});

test(`Day ${day_num} Part B test`, () => {
  expect(solve.partB(test_input)).toBe(4);
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
    expect(solve.partA(aocInput)).toBe(10368);
  });

  test(`Day ${day_num} Part B`, () => {
    expect(solve.partB(aocInput)).toBe(4122);
  });
});
