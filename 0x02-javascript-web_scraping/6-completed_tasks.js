#!/usr/bin/node
const request = require('request');
const argvArray = process.argv;
let taskArray = [];
let thisReturn = {}

request(argvArray[2], function (error, response, body) {
    for (obj in JSON.parse(body)) {
	let count = 0;
	if (JSON.parse(body)[obj]['completed'] === true) {
	    taskArray.push(JSON.parse(body)[obj]['userId']);
	}
    }
    let x = 0;
    while (x < 500) {
	let counter = 0;
	for (y in taskArray) {
	    if (taskArray[y] === x) {
		counter++;
	    }
	}
	if (counter !== 0) {
	    thisReturn[x.toString()] = counter;
	}
	x++
    }
    console.log(thisReturn);
});
