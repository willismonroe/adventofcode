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

function manDist(p1, p2) {
  return Math.abs(p1[0] - p2[0]) + Math.abs(p1[1] - p2[1]);
}

function partA(input) {
  let lookup = makeMap(input);
  let grid = [];
  let maxX = Math.max(...lookup.reduce((acc, val) => acc.concat(val[0]), []));
  let maxY = Math.max(...lookup.reduce((acc, val) => acc.concat(val[1]), []));
  for (let x = 0; x <= maxX; x++) {
    grid.push([]);
    for (let y = 0; y <= maxY; y++) {
      let distances = [];
      for (let i = 0; i < lookup.length; i++) {
        distances.push([i, manDist(lookup[i], [x, y])]);
      }
      distances.sort((a, b) => a[1] - b[1]);
      if (distances[0][1] === distances[1][1]) {
        grid[x].push("X");
      } else {
        grid[x].push(distances[0][0]);
      }
    }
  }
  let top = grid[0];
  let bottom = grid[grid.length - 1];
  let left = grid.map(row => row[0]);
  let right = grid.map(row => row[row.length]);
  let edges = new Set([...top, ...bottom, ...left, ...right]);
  console.log(edges);
  for (let x = 0; x < grid.length; x++) {
    for (let y = 0; y < grid[x].length; y++) {
      if (edges.has(grid[x][y])) {
        grid[x][y] = "X";
      }
    }
  }
  grid = grid.flat();
  let counts = {};
  for (let i = 0; i < grid.length; i++) {
    let num = grid[i];
    counts[num] = counts[num] ? counts[num] + 1 : 1;
  }
  console.log(counts);
  let largest = Object.keys(counts).sort((a, b) => {
    return counts[a] - counts[b];
  })[Object.keys(counts).length - 2];
  return counts[largest];
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
