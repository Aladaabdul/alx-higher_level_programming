#!/usr/bin/node

const fs = require('fs');
const process = require('process');
const args = process.argv.slice(2);

fs.readFile(args[0], 'utf8', (err, data) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(data);
});
