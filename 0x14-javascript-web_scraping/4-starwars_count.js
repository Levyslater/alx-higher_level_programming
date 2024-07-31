#!/usr/bin/node
// Script that prints the number of movies where the character “Wedge Antilles” is present

const request = require('request');

// Check if the URL is provided as a command line argument
if (process.argv.length < 3) {
  console.error('Usage: node script.js <api_url>');
  process.exit(1);
}

// Get the API URL from the command line arguments
const apiUrl = process.argv[2];

// Character ID for Wedge Antilles in the Star Wars API
const wedgeAntillesId = '18';

// Counter for the number of movies Wedge Antilles appears in
let num = 0;

// Perform a GET request to the provided API URL
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(`[Error: ${error.message}]`);
  } else if (response.statusCode === 200) {
    const content = JSON.parse(body);
    content.results.forEach((film) => {
      film.characters.forEach((characterUrl) => {
        if (characterUrl.includes(`/api/people/${wedgeAntillesId}/`)) {
          num += 1;
        }
      });
    });
    console.log(num);
  } else {
    console.error(`Error: Received status code ${response.statusCode} - ${response.statusMessage}`);
  }
});
