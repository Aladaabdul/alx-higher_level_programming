#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  const largest = Math.max(...args.map(Number));
  console.log(largest);
}
