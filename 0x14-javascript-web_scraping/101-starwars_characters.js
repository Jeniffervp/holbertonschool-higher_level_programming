#!/usr/bin/node
function doRequest(url) {
  return new Promise(function (resolve, reject) {
    request(url, function (error, res, body) {
      if (!error && res.statusCode == 200) {
        resolve(body);
      } else {
        reject(error);
      }
    });
  });
}

// Usage:

async function main(dir) {
  let res = await doRequest(dir);
  console.log(res);
}

const re = require('request');
const dir = 'http://swapi.co/api/films/' + process.argv[2];
main(dir);
