// Ensure the script runs after the DOM is fully loaded
$(document).ready(function() {
    // When the <div> with id "add_item" is clicked
    $('div#add_item').click(function() {
        // Define the new <li> element to be added
        let element = '<li>Item</li>';
        // Append the new <li> element to the <ul> with class "my_list"
        $('ul.my_list').append(element);
    });
});

