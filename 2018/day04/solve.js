const fs = require("fs");

const input = fs
  .readFileSync(__dirname + "/input.txt")
  .toString()
  .split("\n")
  .map(s => s.replace(/\r$/, ""))
  .filter(s => s.length > 0);

function count(input) {
  return [...new Set(input)].map(x => [x, input.filter(y => y === x).length]);
}

function range(start, end) {
  let ret = [];
  for (let i = start; i <= end; i++) {
    ret.push(i);
  }
  return ret;
}

function sortDate(input) {
  input.sort((a, b) => {
    return new Date(a.slice(1, 17)) - new Date(b.slice(1, 17));
  });
  return input;
}

function createBarracks(input) {
  input = sortDate(input);

  let barracks = { guards: {} };

  let guard = {};

  let guardRe = /Guard #(\d{1,4})/;

  for (let line of input) {
    let [timeStamp, action] = line.split("] ");
    let timeRe = /\d{4}-(\d{2})-(\d{2}) \d{2}:(\d{2})/;
    let result = timeRe.exec(timeStamp);
    let [month, day, minute] = [result[1], result[2], result[3]];

    switch (action.slice(0, 5)) {
      case "Guard":
        let id = guardRe.exec(action)[1];
        if (id === guard.id) {
          // console.log("Same guard");
        } else if (Object.keys(barracks.guards).includes(id)) {
          // console.log("Repeat guard");
          barracks.guards[guard.id] = guard;
          guard = barracks.guards[id];
        } else {
          if (guard.id) {
            barracks.guards[guard.id] = guard;
          }
          guard = { id: id, sleep: [] };
          // console.log(`New Guard ID: ${guard.id}`);
        }
        break;
      case "falls":
        guard.falls = minute;
        break;
      case "wakes":
        guard.wakes = minute;
        let asleep = range(guard.falls, guard.wakes - 1);
        asleep.forEach(item => guard.sleep.push(Number(item)));
        guard.falls = null;
        guard.wakes = null;
        // console.log(`Slept for: ${asleep.length} minutes`);
        break;
    }
  }
  return barracks;
}

function partA(input) {
  let barracks = createBarracks(input);
  let sleepiest = Object.keys(barracks.guards).sort((guardA, guardB) => {
    return (
      barracks.guards[guardB].sleep.length -
      barracks.guards[guardA].sleep.length
    );
  })[0];
  let minutes = count(barracks.guards[sleepiest].sleep);
  minutes = minutes.sort((a, b) => b[1] - a[1]);

  return minutes[0][0] * sleepiest;
}

function partB(input) {
  let barracks = createBarracks(input);

  for (let guard in barracks.guards) {
    if (barracks.guards[guard].sleep.length > 0) {
      let minutes = count(barracks.guards[guard].sleep);
      minutes = minutes.sort((a, b) => b[1] - a[1]);
      let minute = minutes[0];
      barracks.guards[guard].sleepiestMinute = minute;
    } else {
      barracks.guards[guard].sleepiestMinute = [0, 0];
    }
  }
  let sleepiest = Object.keys(barracks.guards).sort((guardA, guardB) => {
    return (
      barracks.guards[guardB].sleepiestMinute[1] -
      barracks.guards[guardA].sleepiestMinute[1]
    );
  })[0];
  return barracks.guards[sleepiest].sleepiestMinute[0] * sleepiest;
}

function solve() {
  console.log(`Part A: ${partA(input)}`);
  console.log(`Part B: ${partB(input)}`);
}

if (require.main === module) {
  solve();
}

module.exports = { partA: partA, partB: partB };
