#!/usr/bin/node
const requests = require('request')
const argvArray = process.argv;

requests(argvArray[2], function (error, response, body) {
  console.log('code: ' + response && response.statusCode);
})
