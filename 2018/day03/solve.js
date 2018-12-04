const fs = require("fs");

const input = fs
  .readFileSync(__dirname + "/input.txt")
  .toString()
  .split("\n")
  .map(s => s.replace(/\r$/, ""))
  .filter(s => s.length > 0);

// #3 @ 5,5: 2x2

function partA(input) {
  let fabric = new Object();

  for (const line of input) {
    let [id, at, start, size] = line.split(" ");
    let [xStart, yStart] = start
      .slice(0, -1)
      .split(",")
      .map(Number);
    let [width, height] = size.split("x").map(Number);
    for (let x = xStart; x < xStart + width; x++) {
      for (let y = yStart; y < yStart + height; y++) {
        fabric[`${x}x${y}`] = (fabric[`${x}x${y}`] || 0) + 1;
      }
    }
  }
  return Object.values(fabric).filter(v => v > 1).length;
}

function partB(input) {
  let fabric = new Object();
  let claims = new Object();

  for (const line of input) {
    let [id, at, start, size] = line.split(" ");
    let [xStart, yStart] = start
      .slice(0, -1)
      .split(",")
      .map(Number);
    let [width, height] = size.split("x").map(Number);
    claims[id] = true;
    for (let x = xStart; x < xStart + width; x++) {
      for (let y = yStart; y < yStart + height; y++) {
        if (fabric[`${x}x${y}`]) {
          claims[fabric[`${x}x${y}`]] = false;
          claims[id] = false;
        }
        fabric[`${x}x${y}`] = id;
      }
    }
  }
  return Number(
    Object.entries(claims)
      .filter(v => v[1])
      .toString()
      .split(",")[0]
      .slice(1)
  );
}

function solve() {
  console.log(`Part A: ${partA(input)}`);
  console.log(`Part B: ${partB(input)}`);
}

if (require.main === module) {
  solve();
}

module.exports = { partA: partA, partB: partB };
