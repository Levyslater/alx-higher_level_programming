#!/usr/bin/node
/* This code prints array elements using a loop */
const myVar = ['C is fun', 'Python is cool', 'JavaScript is amazing'];

let count = 0;
while (myVar[count] !== undefined) {
  console.log(myVar[count]);
  count++;
}
