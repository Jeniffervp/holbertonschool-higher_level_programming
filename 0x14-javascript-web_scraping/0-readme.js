#!/usr/bin/node
const fs = require('fs');
let content;
fs.readFile(process.argv[2], 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    content = data;
    console.log(content);
  }
});
