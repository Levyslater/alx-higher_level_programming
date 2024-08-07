// Ensure the script runs after the DOM is fully loaded
$(document).ready(function() {
    // When the <div> with id "red_header" is clicked
    $('div#red_header').click(function() {
        // Add the "red" class to the <header> element
        $('header').addClass('red');
    });
});

