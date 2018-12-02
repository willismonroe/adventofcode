const fs = require("fs");
const solve = require("./solve");

test("Day 02 Part A tests", () => {
  expect(
    solve.partA([
      "abcdef",
      "bababc",
      "abbcde",
      "abcccd",
      "aabcdd",
      "abcdee",
      "ababab"
    ])
  ).toBe(12);
});

test("Day 02 Part B test", () => {
  expect(
    solve.partB(["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"])
  ).toBe("fgij");
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
  test("Day 02 Part A", () => {
    expect(solve.partA(aocInput)).toBe(6175);
  });

  test("Day 02 Part B", () => {
    expect(solve.partB(aocInput)).toBe("asgwjcmzredihqoutcylvzinx");
  });
});
