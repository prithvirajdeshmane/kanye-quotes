from tkinter import *  # Import all classes and functions from the tkinter library for GUI creation.
import requests  # Import the requests library to handle HTTP requests.

# Define the API endpoint for retrieving Kanye West quotes.
api_url = "https://api.kanye.rest/"

# Function to fetch and display a quote from the Kanye REST API.
def get_quote():
    res = requests.get(api_url)  # Send a GET request to the API.
    res.raise_for_status()  # Raise an error if the request was unsuccessful.
    data = res.json()  # Parse the JSON response into a Python dictionary.
    # Update the text of the canvas element with the new quote.
    canvas.itemconfig(quote_text, text=data['quote'])

# Create the main application window.
window = Tk()
window.title("Kanye Says...")  # Set the title of the window.
window.config(padx=50, pady=50)  # Add padding around the window.

# Create a canvas widget to display the background and quote.
canvas = Canvas(width=300, height=414)  # Set the size of the canvas.
background_img = PhotoImage(file="background.png")  # Load the background image.
canvas.create_image(150, 207, image=background_img)  # Add the background image to the canvas.
# Add a text widget to the canvas for displaying the quote.
quote_text = canvas.create_text(150, 207, width=250, font=("Arial", 20, "bold"), fill="white")
canvas.grid(row=0, column=0)  # Position the canvas in the grid layout.

# Create a button with an image of Kanye West to fetch new quotes.
kanye_img = PhotoImage(file="kanye.png")  # Load the button image.
# Create the button and associate it with the get_quote function.
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)  # Position the button below the canvas.

get_quote()  # Fetch and display the first quote when the application starts.

# Run the Tkinter event loop to keep the application running.
window.mainloop()