#!/usr/bin/node
function fact (num) {
  if (num === 1) {
    return num;
  } else {
    return num * fact(num - 1);
  }
}
const argvArray = process.argv;
const theNum = Number(argvArray[2], 10);
if (isNaN(theNum)) {
  console.log(1);
} else {
  console.log(fact(theNum));
}
