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
      claims.push(`${x + claim.hloc}x${y + claim.vloc}`);
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
  let fabric = new Object();
  input.forEach(line => {
    let claim = Number(line.split("@")[0].slice(1));
    fabric[claim] = { number: claim, claims: [], overlap: false };
    enumerate(line).forEach(item => {
      fabric[claim].claims.push(item);
    });
  });
  for (let claim1 in fabric) {
    if (fabric[claim1].overlap === false) {
      for (let claim2 in fabric) {
        if (claim1 != claim2) {
          let setClaim1 = new Set(fabric[claim1].claims);
          let setClaim2 = new Set(fabric[claim2].claims);
          let intersect = new Set([...setClaim1].filter(x => setClaim2.has(x)));
          if (Array.from(intersect).length > 0) {
            fabric[claim1].overlap = true;
            fabric[claim2].overlap = true;
          }
        }
      }
    }
  }
  for (let claim in fabric) {
    if (fabric[claim].overlap === false) {
      return claim;
    }
  }
}

function solve() {
  console.log(`Part A: ${partA(input)}`);
  console.log(`Part B: ${partB(input)}`);
}

if (require.main === module) {
  solve();
}

module.exports = { partA: partA, partB: partB };
