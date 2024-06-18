#!/usr/bin/node
/* This code prints the first argument passed to a script */

const args = process.argv.slice(2);

function printArguments(args) {
    if (args[0] === undefined) {
        console.log('No arguments');
    } else {
        console.log(args[0]);
    }
}

printArguments(args);
