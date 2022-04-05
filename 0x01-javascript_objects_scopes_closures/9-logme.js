#!/usr/bin/node
let count = 0;
exports.logMe = function (item) {
  let log = count;
  console.log(log + ': ' + item)
  count++;
}
