const fs = require("fs");

const input = fs
  .readFileSync(__dirname + "/input.txt")
  .toString()
  .split("\n")
  .map(s => s.replace(/\r$/, ""))
  .filter(s => s.length > 0);

function paired(a, b) {
  return (a.charCodeAt(0) ^ b.charCodeAt(0)) === 32;
}

function react(input) {
  let changed = true;
  while (changed) {
    changed = false;
    for (let i = 0; i < input.length - 1; i++) {
      if (paired(input[i], input[i + 1])) {
        input.splice(i, 2);
        changed = true;
        break;
      }
    }
  }
  return input;
}

function partA(input) {
  input = input[0].split("");
  input = react(input);
  return input.length;
}

function partB(input) {
  input = input[0].split("");
  input = react(input);
  let alpha = {};
  for (let key of "abcdefghijklmnopqrstuvwxyz".split("")) {
    alpha[key] = 0;
  }
  for (let char in alpha) {
    let l = react(input.filter(c => ![char, char.toUpperCase()].includes(c)))
      .length;
    alpha[char] = l;
  }
  let shortest = Object.keys(alpha).sort((a, b) => alpha[a] - alpha[b])[0];
  return alpha[shortest];
}

function solve() {
  console.log(`Part A: ${partA(input)}`);
  console.log(`Part B: ${partB(input)}`);
}

if (require.main === module) {
  solve();
}

module.exports = { partA: partA, partB: partB };
