#!/usr/bin/node
exports.converter = function (base) {
  function daConverter (num) {
    let daNum = Number(num);
    return daNum.toString(base);
  }
  return (daConverter);
};
