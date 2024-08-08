document.addEventListener("DOMContentLoaded", function() {
    // When the page is fully loaded, fetch the color from the backend
    fetch('/get-color')
        .then(response => response.json())  // Convert the response to JSON
        
        .then(data => {
            // Change the background color of the 'color-box' div using the retrieved color
            document.getElementById('color-box').style.backgroundColor = data.color;
        })
        
        .catch(error => console.error('Error:', error));  // Log any errors that occur during the fetch
});