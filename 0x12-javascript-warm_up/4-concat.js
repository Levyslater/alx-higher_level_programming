#!/usr/bin/node
/* This code concatenates the first two argument passed to a script */

const args = process.argv.slice(2);

function printArguments(args) {
    console.log(args[0] + ' is ' + args[1]);
}
printArguments(args);