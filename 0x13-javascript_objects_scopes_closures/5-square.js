#!/usr/bin/node
// Creates rectangle objects and prints them using 'X' character

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
