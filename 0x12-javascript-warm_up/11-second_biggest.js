#!/usr/bin/node
const maxi = process.argv;
if (maxi.length > 3) {
  console.log(maxi.sort((a, b) => b - a).slice(3)[0]);
} else {
  console.log(0);
}
