// Define the URL for the API request
let url = 'https://swapi.dev/api/people/5/';

// Fetch data from the API using jQuery's get method
$.get(url, function(data, status) {
    // Replace the text of the <div> with id "character" with the name from the API data
    $('div#character').text(data.name);
});

