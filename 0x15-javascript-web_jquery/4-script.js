// Ensure the script runs after the DOM is fully loaded
$(document).ready(function() {
    // When the <div> with id "toggle_header" is clicked
    $('div#toggle_header').click(function() {
        // Toggle the "red" class on the <header> element
        $('header').toggleClass('red green');
    });
});

