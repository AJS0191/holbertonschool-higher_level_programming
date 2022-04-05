#!/usr/bin/node
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    if (this.height !== undefined) {
      for (let i = 0; i < this.height; i++) {
        let theString = '';
        for (let x = 0; x < this.width; x++) {
          theString += c;
        }
        console.log(theString)
      }
    }
  }
}
module.exports = Square;
