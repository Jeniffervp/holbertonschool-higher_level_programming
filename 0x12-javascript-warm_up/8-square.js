#!/usr/bin/node
const sq = parseInt(process.argv[2]);
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let a = 0; a < sq; a++) {
    console.log('X'.repeat(sq));
  }
}
