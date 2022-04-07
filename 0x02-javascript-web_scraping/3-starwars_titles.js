#!/usr/bin/node
const request = require('request')
const argvArray = process.argv;

request(argvArray[2], function (error, response, body) {
    console.log('code: ', response && response.statusCode);
    console.log('body:', body);
})
