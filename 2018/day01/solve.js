const fs = require("fs");

const input = fs
  .readFileSync(__dirname + "/input.txt")
  .toString()
  .split("\n")
  .map(s => s.replace(/\r$/, ""))
  .filter(s => s.length > 0);

let start = 0;

function partA(input) {
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
  start = 0;
  let dup = 0;

  while (dup == 0) {
    input.forEach(item => {
      let operand = item.slice(0, 1);
      let number = parseInt(item.slice(1));
      if (operand === "+") {
        start = start + number;
      } else {
        start = start - number;
      }
      if (visited.indexOf(start) > 0) {
        dup = start;
      }
      visited.push(start);
    });
  }
  return start;
}

function solve() {
  console.log(`Part A: ${partA(input)}`);
  console.log(`Part B: ${partB(input)}`);
}

solve();
