#!/usr/bin/node

const request = require('request');
const process = require('process');
const args = process.argv.slice(2);

request.get(args[0]).on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});
