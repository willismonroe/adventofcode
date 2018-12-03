const fs = require("fs");
const request = require("request-promise");

const templateDir = __dirname + "/templates/";

const session =
  "53616c7465645f5fc95845aab929d5f2a6a7ace722d692cd5f36b3767dffeaa8fa5dd4c14c3c84f13da3ab26fef23037";

const year = "2018";

function getDay() {
  let num = process.argv.slice(2);
  return ("0" + num).slice(-2);
}

function grabInput(year, day, session) {
  const url = `https://adventofcode.com/${year}/day/${day}/input`;
  console.log(`Requesting input from: ${url}`);
  let cookie = request.cookie(`session=${session}`);
  return request({ uri: url, headers: { Cookie: cookie } }).then(function(
    response
  ) {
    return response;
  });
}

function main() {
  let day = getDay();

  const newDir = `day${day}/`;

  if (!fs.existsSync(newDir)) {
    console.log(`Creating Directory: ${newDir}`);
    fs.mkdirSync(newDir);
    console.log(`Fetching input text...`);
    grabInput(year, Number(day), session).then(input =>
      fs.writeFileSync(newDir + "input.txt", input)
    );
    console.log("Copying over template files.");
    fs.copyFileSync(templateDir + "solve.js", newDir + "solve.js");
    fs.copyFileSync(templateDir + "solve.test.js", newDir + "solve.test.js");
  } else {
    console.log("Day folder already exists!");
  }
}

main();
