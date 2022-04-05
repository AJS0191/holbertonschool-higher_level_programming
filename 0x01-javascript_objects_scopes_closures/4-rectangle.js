#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (this.height !== undefined) {
      for (let i = 0; i < this.height; i++) {
        let theString = '';
        for (let x = 0; x < this.width; x++) {
          theString += 'X';
        }
        console.log(theString);
      }
    }
  }

  rotate () {
    let holder = this.height;
    this.height = this.width;
    this.width = holder;
    }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
module.exports = Rectangle;
