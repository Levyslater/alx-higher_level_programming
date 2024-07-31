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
const fetchCharacter = (characterUrl, callback) => {
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
    return;
  }

  try {
    const movieData = JSON.parse(body);
    const characters = movieData.characters;

    // Process each character URL
    characters.forEach((characterUrl) => {
      fetchCharacter(characterUrl, (name) => {
        if (name) {
          console.log(name);
        }
      });
    });
  } catch (parseError) {
    console.error(`[Error parsing movie data: ${parseError.message}]`);
  }
});
