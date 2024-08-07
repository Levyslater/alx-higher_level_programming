// Define the URL for the API request to fetch wind speed in San Francisco
let url = 'https://query.yahooapis.com/v1/public/yql?q=select%20wind%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22San%20Francisco%2C%20CA%22)&format=json';

// Fetch data from the API using jQuery's get method
$.get(url, function(data) {
    // Retrieve the wind speed from the API response
    let wind = data.query.results.channel.wind.speed;

    // Replace the text of the <div> with id "sf_wind_speed" with the retrieved wind speed
    $('div#sf_wind_speed').text(wind);
});

