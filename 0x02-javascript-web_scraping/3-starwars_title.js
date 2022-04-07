#!/usr/bin/node
const request = require('request')
const argvArray = process.argv;

request('https://swapi-api.hbtn.io/api/films/' + argvArray[2], function (error, response, body) {
    console.log(JSON.parse(body)['title']);
})
