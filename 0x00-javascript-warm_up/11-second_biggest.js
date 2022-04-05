#!/usr/bin/node
const argvArray = process.argv;
const givenArray = new Array(argvArray.length - 2);
if (argvArray[2] === undefined) {
  console.log(0);
} else if (argvArray[3] === undefined) {
  console.log(0);
} else {
  for (let i = 2; i < argvArray.length; i++) {
    givenArray.fill(argvArray[i], i - 2);
  }
}
const sortMe = givenArray.sort();
console.log(sortMe);
console.log(sortMe[sortMe.length - 2]);
