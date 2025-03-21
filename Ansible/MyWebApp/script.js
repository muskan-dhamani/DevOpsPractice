// Get the button element
const button = document.getElementById('colorButton');

// Array of colors
const colors = ['#FF6347', '#98FB98', '#87CEEB', '#FFD700', '#8A2BE2'];

// Function to change the background color
function changeBackgroundColor() {
    const randomColor = colors[Math.floor(Math.random() * colors.length)];
    document.body.style.backgroundColor = randomColor;
}

// Add event listener to the button to trigger the color change on click
button.addEventListener('click', changeBackgroundColor);

