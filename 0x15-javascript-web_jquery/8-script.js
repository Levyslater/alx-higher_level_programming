// Define the URL for the API request
let url = 'https://swapi.dev/api/films/?format=json';

// Fetch data from the API using jQuery's get method
$.get(url, function(data) {
    // Retrieve the list of films from the API response
    let films = data.results;

    // Iterate over each film and append its title as an <li> element to the <ul> with id "list_movies"
    for (let film of films) {
        $('ul#list_movies').append(`<li>${film.title}</li>`);
    }
});

