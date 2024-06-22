#!/usr/bin/node

/* code initialize a class Square that extends from the Square class */

const orgSquare = require('./5-square');

class Square extends orgSquare {
  name = 'X';
  charPrint (c) {
    if (c != null) {
      this.name = c;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(this.name.repeat(this.width));
    }
  }
}

module.exports = Square;
