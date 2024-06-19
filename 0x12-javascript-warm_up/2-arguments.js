#!/usr/bin/node
/* This code checks the number of arguments passed to a script */

const args = process.argv.slice(2);

function checkArguments (args) {
  if (args.length === 0) {
    console.log('No argument');
  } else if (args.length === 1) {
    console.log('Argument found');
  } else {
    console.log('Arguments found');
  }
}

checkArguments(args);
