#!/usr/bin/node
/* This code searches and prints the second largest argument passed */

const args = process.argv.slice(2).map(Number);

function secondLargest(args) {
    if (args.length <= 1) {
        console.log(0);
        return;
    }

    let max = -Infinity;
    let next_max = -Infinity;

    for (let i = 0; i < args.length; i++) {
        if (args[i] > max) {
            next_max = max;
            max = args[i];
        } else if (args[i] > next_max && args[i] !== max) {
            next_max = args[i];
        }
    }

    console.log(next_max);
}

secondLargest(args);
