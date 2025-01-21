# Kanye Says...

A simple desktop application that displays random Kanye West quotes using the [Kanye REST API](https://kanye.rest). Built with Python and the `tkinter` library.

## Features
- Fetches random quotes from the Kanye REST API.
- Displays quotes in a beautifully designed GUI with a customizable background.
- Includes a button featuring Kanye's image to fetch new quotes dynamically.

## Requirements
- Python 3.x
- `requests` library (for API calls)
- A `background.png` image file for the app's background.
- A `kanye.png` image file for the Kanye button.

## Installation
1. Clone this repository:
   ```
   git clone https://github.com/your-username/kanye-says.git
   cd kanye-says
   ```
2. Install the required Python package:
   ```
   pip install requests
   ```
3. Place the required image files (background.png and kanye.png) in the project directory.

## Usage
- Run the program:
    ```
    python3 app.py
    ```
- Click the Kanye button to fetch a new quote.

## File Structure
    .
    ├── app.py             # The main application script
    ├── background.png     # Background image for the app
    ├── kanye.png          # Image for the Kanye button
    └── README.md          # Project documentation

## Example
When you run the application, you'll see a window displaying a random Kanye West quote. Clicking the button with Kanye's image will fetch and display a new quote.

## Resources
Kanye REST API

## Affiliation
This code is part of the Udemy course "100 Days of Code: The Complete Python Pro Bootcamp" by Dr. Angela Yu and AppBrewery.

## License
This project is licensed under the [GNU General Public Use v3 License](https://www.gnu.org/licenses/gpl-3.0.en.html).
