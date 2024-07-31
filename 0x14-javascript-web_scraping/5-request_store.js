#!/usr/bin/node
// Script that gets the contents of a webpage and stores it in a file

const request = require('request');
const fs = require('fs');

// Check if the URL and file path are provided as command line arguments
if (process.argv.length < 4) {
  console.error('Usage: node script.js <url> <file_path>');
  process.exit(1);
}

// Get the URL and file path from the command line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Perform a GET request to the specified URL
request.get(url, (error, response, body) => {
  if (error) {
    console.error(`[Error: ${error.message}]`);
  } else if (response.statusCode !== 200) {
    console.error(`Error: Received status code ${response.statusCode} - ${response.statusMessage}`);
  } else {
    // Write the response body to the specified file
    fs.writeFile(filePath, body, 'utf-8', (error) => {
      if (error) {
        console.error(`[Error: ${error.message}]`);
      }
    });
  }
});
