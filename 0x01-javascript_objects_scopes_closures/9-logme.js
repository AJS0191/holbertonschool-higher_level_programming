#!/usr/bin/node
let count = 0;
exports.logMe = function (item) {
  const log = count;
  console.log(log + ': ' + item);
  count++;
};
