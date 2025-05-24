# Friendship Bracelet Visualizer

A web-based tool designed to help friendship bracelet makers visualize their bracelets with the colors they'd like to use before creating the physical bracelet.

## Features

- **Color Visualization**: Preview how different color combinations will look in your bracelet patterns
- **Pattern Selection**: Choose from various friendship bracelet patterns

## Getting Started

### Prerequisites

To run this project locally, you'll need:
- A modern web browser (Chrome, Firefox, Safari, or Edge)
- Basic understanding of HTML, CSS, and JavaScript for development

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/zcoder365/FriendshipBraceletVisualizer.git
   ```

2. **Navigate to the project directory**
   ```bash
   cd FriendshipBraceletVisualizer
   ```

3. **Open in browser**
   ```bash
   # Simply open the index.html file in your preferred browser
   # Or use a local server for development
   python -m http.server 8000  # Python 3
   # OR
   python -m SimpleHTTPServer 8000  # Python 2
   ```

4. **Access the application**
   - If using a local server: Navigate to `http://localhost:8000`
   - Otherwise: Open `index.html` directly in your browser

## How to Use

1. **Select a Pattern**: Choose from the available friendship bracelet patterns
2. **Choose Colors**: Pick colors from the palette that match your available threads
3. **Preview**: View the complete bracelet visualization

## Project Structure

```
FriendshipBraceletVisualizer/
├── README.md
├── static/
│   └── styles.css          # Main stylesheet for layout and design
├── templates/
│   ├── index.html          # Where you enter your colors
│   ├── results.html        # View the results of the colors you entered
│   └── template.html       # The template that the other HTML pages extend/add to
├── main.py                 # The main file that runs the program
└── README.md               # This file
```

## Code Logic Overview

### Core Components

**Pattern Engine** (`patterns.js`):
- Contains algorithms for generating different bracelet patterns
- Handles mathematical calculations for knot positions and string arrangements
- Supports various pattern types: chevron, diamond, candy stripe, alpha patterns

**Color Management** (`colorPicker.js`):
- Manages color selection and application to pattern elements
- Provides color palette functionality with hex color support
- Handles color validation and conversion between different color formats

**Visualization Engine** (`visualizer.js`):
- Renders the bracelet pattern using HTML5 Canvas or SVG
- Calculates proper scaling and positioning for realistic bracelet appearance
- Handles real-time updates when colors or patterns change

**Main Application** (`main.py`):
- Coordinates interactions between different components
- Manages application state and user interactions
- Handles event listeners for user input (clicks, color changes, pattern selection)

## Supported Patterns

- **Chevron**: Classic V-shaped pattern
- **Candy Stripe**: Diagonal stripes

## Technology Stack

- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Graphics**: HTML5 Canvas API or SVG for pattern rendering
- **Styling**: CSS Grid/Flexbox for responsive layout
- **No external dependencies**: Pure vanilla JavaScript implementation

## Browser Support

- Chrome 60+
- Firefox 55+
- Safari 11+
- Edge 79+

## Acknowledgments

- Inspired by traditional friendship bracelet making techniques
- Color theory and pattern algorithms based on mathematical knot theory
- Thanks to the friendship bracelet community for pattern inspiration

**Happy bracelet making!** 🌈✨