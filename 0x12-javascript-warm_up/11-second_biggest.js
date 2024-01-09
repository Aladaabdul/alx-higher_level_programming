#!/usr/bin/node

const args = process.argv.slice(2);
let largest = args[0];

if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  for (let i = 1; i < args.length; i++) {
    if (args[i] > largest) {
      largest = args[i];
    }
  }
  console.log(largest);
}
