const fs = require("fs");

const input = fs
  .readFileSync(__dirname + "/input.txt")
  .toString()
  .split("\n")
  .map(s => s.replace(/\r$/, ""))
  .filter(s => s.length > 0);

function count(code) {
  const counts = code.split("").reduce((total, letter) => {
    total[letter] ? total[letter]++ : (total[letter] = 1);
    return total;
  }, {});
  return {
    threes: Object.values(counts).includes(3),
    twos: Object.values(counts).includes(2)
  };
}

function partA(input) {
  let counts = { threes: 0, twos: 0 };
  input.forEach(item => {
    let result = count(item);
    counts.threes += result.threes;
    counts.twos += result.twos;
  });
  return counts.threes * counts.twos;
}

function hDistance(codeA, codeB) {
  if (codeA.length != codeB.length) {
    console.log(`Unequal lengths: ${codeA}, ${codeB}`);
    return -1;
  }
  let distance = 0;
  for (let i = 0; i < codeA.length; i += 1) {
    if (codeA[i] != codeB[i]) {
      distance += 1;
    }
  }
  return distance;
}

const pairs = items =>
  items.reduce(
    (acc, v, i) => acc.concat(items.slice(i + 1).map(w => [v, w])),
    []
  );

function partB(input) {
  let match = [];
  pairs(input).forEach(pair => {
    if (hDistance(pair[0], pair[1]) === 1) {
      match = pair;
    }
  });
  let result = "";
  for (let i = 0; i < match[0].length; i++) {
    if (match[0][i] === match[1][i]) {
      result += match[0][i];
    }
  }
  return result;
}

function solve() {
  console.log(`Part A: ${partA(input)}`);
  console.log(`Part B: ${partB(input)}`);
}

if (require.main === module) {
  solve();
}

module.exports = { partA: partA, partB: partB };
