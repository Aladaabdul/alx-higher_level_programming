#!/usr/bin/node
const request = require('request');
const process = require('process');
const args = process.argv.slice(2);

const id = args[0];

const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const movie = (`${body.title}`);

  console.log(`${movie}`);
});
