document.addEventListener("DOMContentLoaded", function() {
    // When the page is fully loaded, fetch the colors from the backend
    fetch('/get-colors')
        .then(response => response.json())  // Convert the response to JSON
        
        .then(data => {
            // Change the background colors of the three elements using the retrieved colors
            document.getElementById('color-box-1').style.backgroundColor = data.color1;
            document.getElementById('color-box-2').style.backgroundColor = data.color2;
            document.getElementById('color-box-3').style.backgroundColor = data.color3;
        })
        
        .catch(error => console.error('Error:', error));  // Log any errors that occur during the fetch
});
