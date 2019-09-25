#!/usr/bin/node
const re = require('request');
const dir = process.argv[2];
let count = 0;
let algo = 0;
let chara = 0;
re.get(dir, function (error, response, body) {
  if (error) {
    return console.log(error);
  } else {
    for (algo of JSON.parse(body).results) {
      for (chara of algo.characters) {
        if (chara.includes(18)) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
