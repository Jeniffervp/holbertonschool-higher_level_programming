#!/usr/bin/node
let fs = require('fs');
let content;
fs.readFile(process.argv[2], 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  }
  content = data;
  console.log(content);
});
