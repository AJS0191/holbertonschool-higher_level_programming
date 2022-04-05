#!/usr/bin/node
exports.converter = function (base) {
  function daConverter (num) {
    daNum = Number(num);
    return daNum.toString(base);
  }
  return (daConverter);
};
