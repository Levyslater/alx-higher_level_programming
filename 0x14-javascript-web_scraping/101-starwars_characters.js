#!/usr/bin/node
// Script that prints all characters of a Star Wars movie

const request = require('request');

// Check if the movie ID is provided as a command line argument
if (process.argv.length < 3) {
  console.error('Usage: node script.js <movie_id>');
  process.exit(1);
}

// Get the movie ID from the command line arguments
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Function to fetch character data
const fetchCharacterName = (characterUrl, callback) => {
  request.get(characterUrl, (error, response, body) => {
    if (error) {
      console.error(`[Error fetching character ${characterUrl}: ${error.message}]`);
      callback(null);
      return;
    }
    try {
      const characterData = JSON.parse(body);
      callback(characterData.name);
    } catch (parseError) {
      console.error(`[Error parsing character data: ${parseError.message}]`);
      callback(null);
    }
  });
};

// Fetch movie data and print character names
request.get(url, (error, response, body) => {
  if (error) {
    console.error(`[Error fetching movie: ${error.message}]`);
    process.exit(1);
  }

  try {
    const movieData = JSON.parse(body);
    const characters = movieData.characters;

    // Track the number of pending requests
    let pendingRequests = characters.length;

    // Process each character URL
    characters.forEach((characterUrl) => {
      fetchCharacterName(characterUrl, (name) => {
        if (name) {
          console.log(name);
        }
        pendingRequests -= 1;
        if (pendingRequests === 0) {
          process.exit(0);
        }
      });
    });
  } catch (parseError) {
    console.error(`[Error parsing movie data: ${parseError.message}]`);
    process.exit(1);
  }
});
