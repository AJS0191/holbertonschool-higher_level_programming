#!/usr/bin/node
exports.converter = function (base) {
  function daConverter (num) {
    const daNum = Number(num);
    return daNum.toString(base);
  }
  return (daConverter);
};
