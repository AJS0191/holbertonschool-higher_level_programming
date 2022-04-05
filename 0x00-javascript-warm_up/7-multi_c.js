#!/usr/bin/node
const argvArray = process.argv;
const theNum = Number(argvArray[2], 10);
if (isNaN(theNum)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < theNum; i++) {
    console.log('C is fun');
  }
}
