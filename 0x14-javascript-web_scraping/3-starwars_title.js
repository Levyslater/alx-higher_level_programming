#!/usr/bin/node
// Scriptthat prints the title of a Star Wars movie where the episode number matches a given integer

const request = require('request');

// Check if the episode number is provided as a command line argument
if (process.argv.length < 3) {
  console.error('Usage: node script.js <episode_number>');
  process.exit(1);
}

// Get the episode number from the command line arguments
const episodeNumber = process.argv[2];

// Construct the URL for the Star Wars API
const url = 'https://swapi-api.alx-tools.com/api/films/' + episodeNumber;

// Perform a GET request to the Star Wars API
request.get(url, (error, response, body) => {
  if (error) {
    // Log the detailed error object if there is an error
    console.error(`[Error: ${error.message}] {`);
    console.error(`  errno: ${error.errno},`);
    console.error(`  code: '${error.code}',`);
    console.error(`  syscall: '${error.syscall}',`);
    console.error('}');
  } else if (response.statusCode === 200) {
    // Parse the response body and print the movie title
    const content = JSON.parse(body);
    console.log(content.title);
  } else {
    // Log the status code and status message if the response is not successful
    console.error(`Error: Received status code ${response.statusCode} - ${response.statusMessage}`);
  }
});
