const fs = require("fs");
const solve = require("./solve");

const day_num = "";

test(`Day ${day_num} Part A tests`, () => {
  expect(solve.partA(["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"])).toBe(
    4
  );
});

test(`Day ${day_num} Part B test`, () => {
  expect(solve.partB(["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"])).toBe(
    3
  );
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
    expect(solve.partA(aocInput)).toBe(116491);
  });

  test(`Day ${day_num} Part B`, () => {
    expect(solve.partB(aocInput)).toBe(707);
  });
});
