const fs = require("fs");

const input = fs
  .readFileSync(__dirname + "/input.txt")
  .toString()
  .split("\n")
  .map(s => s.replace(/\r$/, ""))
  .filter(s => s.length > 0);

function parse(line) {
  let [claim, d1, loc, size] = line.split(" ");
  loc = loc.replace(":", "");
  claim = claim.slice(1);
  let [hloc, vloc] = loc.split(",").map(Number);
  let [hsize, vsize] = size.split("x").map(Number);
  return { claim: claim, hloc: hloc, vloc: vloc, hsize: hsize, vsize: vsize };
}

function enumerate(line) {
  let claim = parse(line);
  let claims = [];
  for (let x = 0; x < claim.hsize; x++) {
    for (let y = 0; y < claim.vsize; y++) {
      claims.push(`${claim}-${x + claim.hloc}x${y + claim.vloc}`);
    }
  }
  return claims;
}

function partA(input) {
  let claims = new Set();
  let dups = 0;
  let seen = new Set();
  input.forEach(line => {
    enumerate(line).forEach(item => {
      item = item.split('-')[1];
      if (!seen.has(item)) {
        if (claims.has(item)) {
          dups += 1;
          seen.add(item);
        } else {
          claims.add(item);
        }
      }
    });
  });
  return dups;
}

function partB(input) {
  let claims = new Map();
  input.forEach(line => {
    enumerate(line).forEach(item => {
     claims[item] = claims[item] ? claims[item]++ : (claims[letter] = 1);
}

function solve() {
  console.log(`Part A: ${partA(input)}`);
  console.log(`Part B: ${partB(input)}`);
}

if (require.main === module) {
  solve();
}

module.exports = { partA: partA, partB: partB };
