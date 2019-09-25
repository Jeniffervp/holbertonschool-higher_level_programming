#!/usr/bin/node
const re = require('request');
const fs = require('fs');
re.get(process.argv[2]).on('error', function (err) {
  console.error(err);
}).pipe(fs.createWriteStream(process.argv[3]));
