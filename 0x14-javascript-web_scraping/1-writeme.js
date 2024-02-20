#!/usr/bin/node

const fs = require('fs');
const process = require('process');
const args = process.argv.slice(2);

fs.writeFile(args[0], args[1], 'utf8', err => {
  if (err) {
    console.log(err);
    return;
  }
  console.log('Successful');
});
