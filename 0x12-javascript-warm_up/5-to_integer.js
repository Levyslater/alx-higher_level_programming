#!/usr/bin/node
/* This code prints the first argument passed to a script as an integer or 'Not a number' if it cannot be converted */

const args = process.argv.slice(2);

function printFirstArgumentAsInteger (args) {
  const firstArg = args[0];
  const integerArg = parseInt(firstArg);

  if (isNaN(integerArg)) {
    console.log('Not a number');
  } else {
    console.log('My number: ' + integerArg);
  }
}

printFirstArgumentAsInteger(args);
