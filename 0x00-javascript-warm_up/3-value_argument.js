#!/usr/bin/node
const argvArray = process.argv;
if (argvArray[2] !== undefined) {
  const response = argvArray[2];
  console.log(response);
} else {
  console.log('No argument');
}
