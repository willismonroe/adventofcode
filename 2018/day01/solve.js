const fs = require("fs");

const aocInput = fs
  .readFileSync(__dirname + "/input.txt")
  .toString()
  .split("\n")
  .map(s => s.replace(/\r$/, ""))
  .filter(s => s.length > 0);

function partA(input) {
  let start = 0;
  input.forEach(item => {
    let operand = item.slice(0, 1);
    let number = parseInt(item.slice(1));
    if (operand === "+") {
      start = start + number;
    } else {
      start = start - number;
    }
  });

  return start;
}

function partB(input) {
  let visited = [0];
  let start = 0;
  let dup = 0;

  while (dup == 0) {
    for (let item of input) {
      let operand = item.slice(0, 1);
      let number = parseInt(item.slice(1));
      if (operand === "+") {
        start = start + number;
      } else {
        start = start - number;
      }
      if (visited.indexOf(start) > -1) {
        dup = start;
        return start;
      }
      visited.push(start);
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
