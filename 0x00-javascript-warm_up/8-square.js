#!/usr/bin/node
const argvArray = process.argv;
const theNum = Number(argvArray[2], 10);
if (isNaN(theNum)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < theNum; i++) {
    let theString = '';
    for (let x = 0; x < theNum; x++) {
      theString += 'X';
    }
    console.log(theString);
  }
}
