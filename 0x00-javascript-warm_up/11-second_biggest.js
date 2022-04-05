#!/usr/bin/node
const argvArray = process.argv;
const givenArray = new Array(argvArray.length - 2);
for (let i = 2; i < argvArray.length; i++) {
  givenArray.fill(argvArray[i], i - 2);
}
const sortMe = givenArray.sort();
console.log(sortMe[sortMe.length - 2]);
