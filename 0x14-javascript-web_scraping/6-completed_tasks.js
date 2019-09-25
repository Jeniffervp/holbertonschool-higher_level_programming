#!/usr/bin/node
const re = require('request');
const dir = process.argv[2];
const myDict = {};
re.get(dir, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    for (const ToDo of JSON.parse(body)) {
      if (ToDo.completed === true) {
        if (ToDo.userId in myDict) {
          myDict[ToDo.userId]++;
        } else {
          myDict[ToDo.userId] = 1;
        }
      }
    }
    console.log(myDict);
  }
});
