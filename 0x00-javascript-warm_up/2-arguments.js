#!/usr/bin/node
const argvArray = process.argv;
if (argvArray.length === 3) {
  console.log('Argument found');
} else if (argvArray.length > 3) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
