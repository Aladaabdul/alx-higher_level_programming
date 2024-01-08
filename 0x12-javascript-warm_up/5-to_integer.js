#!/usr/bin/node

const process = require('process');
const args = process.argv.slice(2);
const number = parseInt(args[0]);

if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${number}`);
}