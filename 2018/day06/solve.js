const fs = require("fs");

const input = fs
  .readFileSync(__dirname + "/input.txt")
  .toString()
  .split("\n")
  .map(s => s.replace(/\r$/, ""))
  .filter(s => s.length > 0);

function makeMap(input) {
  let lookup = [];
  for (let i = 0; i < input.length; i++) {
    let [x, y] = input[i].split(",").map(Number);
    lookup.push([x, y]);
  }
  return lookup;
}

function dist([x1, y1], [x2, y2]) {
  return Math.abs(x2 - x1) + Math.abs(y2 - y1);
}

function partA(input) {
  let lookup = makeMap(input);
  const board = {
    x: {
      min: lookup.reduce((x, y) => (x[0] < y[0] ? x : y))[0],
      max: lookup.reduce((x, y) => (x[0] > y[0] ? x : y))[0]
    },
    y: {
      min: lookup.reduce((x, y) => (x[1] < y[1] ? x : y))[1],
      max: lookup.reduce((x, y) => (x[1] > y[1] ? x : y))[1]
    }
  };

  const startPos = [board.x.min, board.y.min];
  const endPos = [board.x.max, board.y.max];

  const points = {};
  for (let y = startPos[1]; y < endPos[1]; y++) {
    for (let x = startPos[0]; y < endPos[0]; x++) {
      const coordinate = lookup
        .map(cord => [cord, dist(cord[0], x, cord[1], y)])
        .reduce((a, b) => {
          if (a[1] < b[1]) return a;
          else if (b[1] < a[1]) return b;
          else return [[null, null], a[1]];
        })[0];
      if (points[coordinate]) points[coordinate]++;
      else points[coordinate] = 1;
    }
  }
  
}

function partB(input) {}

function solve() {
  console.log(`Part A: ${partA(input)}`);
  console.log(`Part B: ${partB(input)}`);
}

if (require.main === module) {
  solve();
}

module.exports = { partA: partA, partB: partB };
