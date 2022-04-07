#!/usr/bin/node
const request = require('request');
const argvArray = process.argv;
const fs = require('fs')

request(argvArray[2], function (error, response, body) {
    fs.writeFile (argvArray[3], body, err => {
	if (err) {
	    console.error(err);
	    return
	}
    })
});
