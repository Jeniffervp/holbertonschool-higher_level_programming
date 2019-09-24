#!/usr/bin/node
const re = require('request');
re.get(process.argv[2], function (error, response) {
  if (error) {
    console.error('code: ', error);
  } else {
    console.log('code: ', response.statusCode);
  }
});
