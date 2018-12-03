const fs = require("fs");

const aocInput = fs
  .readFileSync(__dirname + "/input.txt")
  .toString()
  .split("\n")
  .map(s => s.replace(/\r$/, ""))
  .filter(s => s.length > 0);

function partA(input) {
  return input.reduce((acc, change) => acc + Number(change), 0);
}

function partB(input) {
  let start = 0;
  let seen = new Set();

  while (true) {
    for (let item of input) {
      seen.add(start);
      start += Number(item);
      if (seen.has(start)) {
        return start;
      }
    }
  }
}

function solve() {
  console.log(`Part A: ${partA(aocInput)}`);
  console.log(`Part B: ${partB(aocInput)}`);
}

if (require.main === module) {
  solve();
}

module.exports = { partA: partA, partB: partB };
