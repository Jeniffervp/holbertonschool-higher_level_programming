#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  for (let ocur = 0; ocur < list.length; ocur++) {
    if (list[ocur] === searchElement) {
      counter++;
    }
  }
  return counter;
};
