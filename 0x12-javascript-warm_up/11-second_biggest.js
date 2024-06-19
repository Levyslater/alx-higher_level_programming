#!/usr/bin/node
/* This code searches and prints the second largest argument passed */

const args = process.argv.slice(2).map(Number);

function secondLargest (args) {
  if (args.length <= 1) {
    console.log(0);
    return;
  }

  let max = -Infinity;
  let nextMax = -Infinity;

  for (let i = 0; i < args.length; i++) {
    if (args[i] > max) {
      nextMax = max;
      max = args[i];
    } else if (args[i] > nextMax && args[i] !== max) {
      nextMax = args[i];
    }
  }

  console.log(nextMax);
}

secondLargest(args);
