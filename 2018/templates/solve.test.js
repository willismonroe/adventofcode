const fs = require("fs");
const solve = require("./solve");

const day_num = "";

test(`Day ${day_num} Part A tests`, () => {
  expect(
    solve.partA()
  ).toBe();
});

test(`Day ${day_num} Part B test`, () => {
  expect(
    solve.partB()
  ).toBe();
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
    expect(solve.partA(aocInput)).toBe();
  });

  test(`Day ${day_num} Part B`, () => {
    expect(solve.partB(aocInput)).toBe();
  });
});
