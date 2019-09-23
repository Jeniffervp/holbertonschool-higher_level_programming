#!/usr/bin/node
const Recta = require('./4-rectangle.js');

class Square extends Recta {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
