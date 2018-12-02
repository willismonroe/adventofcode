const fs = require("fs");
const solve = require("./solve");

test("Day 01 Part A tests", () => {
  expect(solve.partA(["+1", "+1", "+1"])).toBe(3);
  expect(solve.partA(["+1", "+1", "-2"])).toBe(0);
  expect(solve.partA(["-1", "-2", "-3"])).toBe(-6);
});

test("Day 01 Part B test", () => {
  expect(solve.partB(["+1", "-1"])).toBe(0);
  expect(solve.partB(["+3", "+3", "+4", "-2", "-4"])).toBe(10);
  expect(solve.partB(["-6", "+3", "+8", "+5", "-6"])).toBe(5);
  expect(solve.partB(["+7", "+7", "-2", "-7", "-4"])).toBe(14);
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

  test("Day 01 Part A", () => {
    expect(solve.partA(aocInput)).toBe(479);
  });

  test("Day 01 Part B", () => {
    expect(solve.partB(aocInput)).toBe(66105);
  });
});
