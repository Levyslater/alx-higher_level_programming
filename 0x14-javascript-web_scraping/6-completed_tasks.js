#!/usr/bin/node
// Script that computes the number of tasks completed by user ID

const request = require('request');

// Check if the URL is provided as a command line argument
if (process.argv.length < 3) {
  console.error('Usage: node script.js <url>');
  process.exit(1);
}

// Get the URL from the command line arguments
const url = process.argv[2];

// Perform a GET request to the specified URL
request.get(url, { json: true }, (error, response, body) => {
  if (error) {
    console.error(`[Error: ${error.message}]`);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Error: Received status code ${response.statusCode} - ${response.statusMessage}`);
    return;
  }

  const tasksCompleted = {};

  // Process the response body to count completed tasks by user ID
  body.forEach((todo) => {
    if (todo.completed) {
      if (!tasksCompleted[todo.userId]) {
        tasksCompleted[todo.userId] = 1;
      } else {
        tasksCompleted[todo.userId] += 1;
      }
    }
  });

  // Log the result
  console.log(tasksCompleted);
});
