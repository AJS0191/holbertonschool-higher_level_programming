#!/usr/bin/node
const argvArray = process.argv;
if (argvArray.length > 2) {
  const response = argvArray[2];
  console.log(response);
} else {
  console.log('No argument');
}
