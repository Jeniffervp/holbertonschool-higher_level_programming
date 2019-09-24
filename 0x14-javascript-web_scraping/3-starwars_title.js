#!/usr/bin/node
const re = require('request');
const dir = 'http://swapi.co/api/films/' + process.argv[2];
re.get(dir, function (error, response, data) {
  if (error);
  console.log(JSON.parse(data).title);
});
