#!/usr/bin/node
exports.esrever = function (list) {
  let reverse = [list.length];
  let counter = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    reverse[counter] = list[i];
    counter++
  }
  return (reverse)
}
