#!/usr/bin/node
const argvArray = process.argv;
const theNum = Number(argvArray[2], 10);
if (isNaN(theNum)) {
  console.log('Not a number');
} else {
  console.log(theNum);
}
