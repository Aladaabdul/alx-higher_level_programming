#!/usr/bin/node

const fs = require('fs');
const process = require('process');
const args = process.argv.slice(2);
const request = require('request');

const url = args[0];
const file = args[1];

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  fs.writeFile(file, body, 'utf-8', error => {
    if (error) {
      console.log(error);
    }
  });
});
