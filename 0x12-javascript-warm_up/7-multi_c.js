#!/usr/bin/node
/* This code prints a string n times where n is passed as an argument */

const args = process.argv.slice(2);

function printFirstArgumentAsInteger (args) {
  const firstArg = args[0];
  const integerArg = parseInt(firstArg);

  if (isNaN(integerArg)) {
    console.log('Missing number of occurrences');
  } else {
    for (let i = 0; i < integerArg; i++) {
      console.log('C is fun');
    }
  }
}

printFirstArgumentAsInteger(args);
