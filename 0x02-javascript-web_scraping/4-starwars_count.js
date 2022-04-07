#!/usr/bin/node
const request = require('request');
const argvArray = process.argv;
const id = '18';
let count = 0;
request(argvArray[2], function (error, response, body) {
  console.error('error:', error);
  const info = JSON.parse(body);
  for (let x in info.results) {
    for (let charc in info.results[x].characters) {
      if (info.results[x].characters[charc] === 'https://swapi-api.hbtn.io/api/people/' + id + '/') {
        count++;
      }
    }
  }
  console.log(count);
  x = 0;
  charc = 0;
});
