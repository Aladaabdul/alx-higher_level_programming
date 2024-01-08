#!/usr/bin/node

const process = require('process');
const args = process.argv.slice(2);
const number = parseInt(args[0]);

if (isNaN(number)) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < number; i++) {
    console.log('C is fun');
  }
}
