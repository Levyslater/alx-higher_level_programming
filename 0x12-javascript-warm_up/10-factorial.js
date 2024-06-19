#!/usr/bin/node
/* This code computes and prints the factorial of n passed as an argument */

const args = process.argv.slice(2);

function firstargasint (args) {
  const firstArg = args[0];
  const integerArg = parseInt(firstArg);

  if (isNaN(integerArg)) {
    console.log(1);
    return;
  }

  function factorial (n) {
    if (n === 0 || n === 1) {
      return 1;
    }
    return n * factorial(n - 1);
  }

  console.log(factorial(integerArg));
}

firstargasint(args);
