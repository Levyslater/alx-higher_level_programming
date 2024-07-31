#!/usr/bin/node
// Script to get the status code of a GET request

const request = require('request');

// Check if the URL is provided as a command line argument
if (process.argv.length < 3) {
  console.error('Usage: node script.js <url>');
  process.exit(1);
}

// Get the URL from the command line arguments
const url = process.argv[2];

// Perform a GET request to the specified URL
request.get(url, function (error, response) {
  if (error) {
    // Log the detailed error object if there is an error
    console.error(`[Error: ${error.message}] {`);
    console.error(`  errno: ${error.errno},`);
    console.error(`  code: '${error.code}',`);
    console.error(`  syscall: '${error.syscall}',`);
    console.error(`  address: '${error.address}'`);
    console.error('}');
  } else {
    // Log the status code of the response
    console.log('code:', response.statusCode);
  }
});
