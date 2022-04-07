#!/usr/bin/node
const fs = require('fs');
const argvArray = process.argv;

fs.writeFile(argvArray[2], argvArray[3], err => {
  if (err) {
    console.error(err);
  }
});
