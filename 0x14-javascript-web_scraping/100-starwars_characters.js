#!/usr/bin/node
const re = require('request');
const dir = 'http://swapi.co/api/films/' + process.argv[2];
re.get(dir, function (error, response, data) {
  if (error);
  for (const charac of JSON.parse(data).characters) {
    re.get(charac, function (error, response, data) {
      if (error);
      console.log(JSON.parse(data).name);
    });
  }
});
