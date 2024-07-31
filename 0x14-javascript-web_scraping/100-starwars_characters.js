#!/usr/bin/node
// Script that prints all characters of a Star Wars movie

const axios = require('axios');

// Check if the movie ID is provided as a command line argument
if (process.argv.length < 3) {
  console.error('Usage: node script.js <movie_id>');
  process.exit(1);
}

// Get the movie ID from the command line arguments
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Function to fetch character data
const fetchCharacter = async (characterUrl) => {
  try {
    const response = await axios.get(characterUrl);
    return response.data.name;
  } catch (error) {
    console.error(`[Error fetching character: ${error.message}]`);
    return null;
  }
};

// Fetch movie data and print character names
const fetchMovieCharacters = async () => {
  try {
    const response = await axios.get(url);
    const characters = response.data.characters;

    // Fetch all characters concurrently
    const characterNames = await Promise.all(characters.map(fetchCharacter));

    // Print character names
    characterNames.forEach(name => {
      if (name) {
        console.log(name);
      }
    });
  } catch (error) {
    console.error(`[Error fetching movie: ${error.message}]`);
  }
};

// Execute the function to fetch and print character names
fetchMovieCharacters();
