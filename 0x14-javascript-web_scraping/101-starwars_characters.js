#!/usr/bin/node
const request = require('request');
const dir = 'http://swapi.co/api/films/' + process.argv[2];
function doRequest (url) {
  return new Promise(function (resolve, reject) {
    request(url, function (error, res, body) {
      if (!error && res.statusCode === 200) {
        resolve(body);
      } else {
        reject(error);
      }
    });
  });
}

async function main (dir) {
  const res = await doRequest(dir);
  for (const i of JSON.parse(res).characters) {
    const res2 = await doRequest(i);
    console.log(JSON.parse(res2).name);
  }
}

main(dir);
