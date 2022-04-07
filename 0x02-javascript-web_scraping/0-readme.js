#!/usr/bin/node
const fs = require('fs');
const argvArray = process.argv;

fs.readFile(argvArray[2], 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
