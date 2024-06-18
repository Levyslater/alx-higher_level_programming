#!/usr/bin/node
/* This code prints addition of two numbers  */

const args = process.argv.slice(2);

function add(a, b) {
    console.log(parseInt(a) + parseInt(b));
}

add(args[0], args[1]);