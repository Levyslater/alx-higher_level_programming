// Ensure the script runs after the DOM is fully loaded
$(document).ready(function() {
    // When the <div> with id "update_header" is clicked
    $('div#update_header').click(function() {
        // Update the text of the <header> element to "New Header!!!"
        $('header').text('New Header!!!');
    });
});

