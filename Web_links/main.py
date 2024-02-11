"""
This Python script serves as a versatile tool for creating and managing shortened URLs using various URL shortening services. 
It begins by importing necessary modules, including 'requests' for making HTTP requests and 'json' for handling JSON data. 
Additionally, it utilizes a custom GUI module, 'customtkinter', 
for constructing the graphical user interface (GUI), and 'PIL' for image processing.
 
API keys for services like Bitly, Rebrandly, and TinyURL are imported from an external script. 
The script defines functions for shortening URLs with TinyURL, Bitly, and Rebrandly, leveraging their respective APIs.
A GUI interface is then created using customtkinter, facilitating user interaction for URL shortening. 

Users can input a long URL, click a button to generate shortened links, and view the results displayed in designated output boxes.
The script encapsulates its functionality within a class named 'CustomWindowApp', ensuring modularity and ease of maintenance. 
Finally, the script executes the GUI application within a main loop, allowing users to interact seamlessly with the interface.
"""


# Importing the requests module for making HTTP requests
import requests

# Importing the json module for working with JSON data
import json

# Importing a GUI module named customtkinter 
# renaming it as ctk for convenience
import customtkinter as ctk
 
# Importing the Image class from the PIL module
from PIL import Image

# Importing API keys from a separate python script named api_keys
# you would need to create a new file named api_keys.py and define the API keys as variables
# they can be gotten from the repective web link services, with the help of their user accounts
from api_keys import bitly_api_key, rebrandly_api_key, tinyurl_api_key

# Function to create a short URL using the TinyURL API
def tinyurl(url):
    
    # Constructing the URL for the TinyURL API endpoint with the provided URL
    request_url = f'https://tinyurl.com/api-create.php?url={url}'
    
    # Sending a GET request to the constructed URL
    response = requests.get(request_url)
    
    # Checking if the response is successful (status code 200)
    if response.ok:
        
        # Returning the shortened URL from the response
        return response.text
    
    else:
        
        # Raising an exception if the response is not successful
        response.raise_for_status()

# Defining a class named CustomWindowApp
class CustomWindowApp:
    
    # Initializing the class instance with root as a parameter
    def __init__(self, root):
        
        # Assigning the root window to the instance variable self.root
        self.root = root
        
        # Setting the title of the root window
        self.root.title("Tobias Web Links")
        
        # Setting the geometry of the root window
        self.root.geometry("800x800")

        # Creating a background image using a custom tkinter image from a file named "url_link_image.png"
        self.background_image = ctk.CTkImage(Image.open("url_link_image.png"), size=(800, 800))
        
        # Creating a label widget with the background image and an empty text
        self.background_label = ctk.CTkLabel(master=self.root, image=self.background_image, text="")
        
        # Placing the background label in the root window at row 0, column 0 
        # with sticky attribute "nsew" (north, south, east, west)
        self.background_label.grid(row=0, column=0, sticky="nsew")
        
        # Lowering the background label to the bottom of the stacking order
        self.background_label.lower()
        
        # Calling the method create_widgets to create additional widgets
        self.create_widgets()
        
    # Defining a method to generate short links
    def generate_short_links(self):
        
        # Retrieving the long URL from entry1 widget
        long_url = self.entry1.get()
        
        try:
            
            # Using the tinyurl function to generate a short URL
            tinyurl_link = tinyurl(long_url)
            
            # Using the shorten_url_bitly method to generate a short URL using Bitly
            bitly_link = self.shorten_url_bitly(long_url)
            
            # Using the shorten_url_rebrandly method to generate a short URL using Rebrandly
            rebrandly_link = self.shorten_url_rebrandly(long_url)
            
            # Inserting the generated short URLs into respective output fields
            self.tinyurl_output.insert(0, tinyurl_link)
            self.bitly_output.insert(0, bitly_link)
            self.rebrandly_output.insert(0, rebrandly_link)
            
        except Exception as e:
            
            # Printing error message if an exception occurs
            print(f"Error: {e}")
            # Displaying an error message to the user (e.g., using a label or popup)
    
    # Defining a method to shorten a URL using Bitly
    def shorten_url_bitly(self, long_url):
        
        # Bitly API endpoint URL
        url = f"https://api-ssl.bitly.com/v4/shorten"
        
        # Headers required for making the API request
        headers = {
            "Authorization": f"Bearer {bitly_api_key}",
            "Content-Type": "application/json"
        }
        
        # Data payload containing the long URL
        data = {"long_url": long_url}
        
        try:
            
            # Sending a POST request to the Bitly API endpoint with headers and data payload
            response = requests.post(url, headers=headers, json=data)
            
            # Checking for any HTTP errors in the response
            response.raise_for_status()
            
            # Parsing the JSON response
            data = response.json()
            
            # Returning the shortened URL from the response data
            return data["link"]
        
        except requests.exceptions.HTTPError as err:
            
            # Handling HTTP errors
            print(f"HTTP error occurred: {err}")
            print(f"Response status code: {response.status_code}")
            print(f"Response text: {response.text}")
            raise
        
        except Exception as e:
            
            # Handling unexpected errors
            print(f"An unexpected error occurred: {e}")
            raise
        
    # Defining a method to shorten a URL using Rebrandly
    def shorten_url_rebrandly(self, long_url):
        
        # Rebrandly API endpoint URL
        url = "https://api.rebrandly.com/v1/links"
        
        # Headers required for making the API request
        headers = {
            "Content-Type": "application/json",
            "apikey": rebrandly_api_key,
            #"workspace": "YOUR_WORKSPACE_ID"  # Replace with your workspace ID
        }
        
        # Data payload containing the long URL and domain information
        data = {
            "destination": long_url,
            "domain": { "fullName": "rebrand.ly" }
        }
        
        try:
            
            # Sending a POST request to the Rebrandly API endpoint with headers and data payload
            response = requests.post(url, headers=headers, json=data)
            
            # Checking for any HTTP errors in the response
            response.raise_for_status()
            
            # Parsing the JSON response
            data = response.json()
            
            # Returning the shortened URL from the response data
            return data["shortUrl"]
        
        except requests.exceptions.HTTPError as err:
            
            # Handling HTTP errors
            print(f"HTTP error occurred: {err}")
            print(f"Response status code: {response.status_code}")
            print(f"Response text: {response.text}")
            raise
        
        except Exception as e:
            
            # Handling unexpected errors
            print(f"An unexpected error occurred: {e}")
            raise
        
    # Defining a method to create widgets
    def create_widgets(self):
        
        # Create a frame using customtkinter for layout
        self.frame = ctk.CTkFrame(master=self.root, fg_color="#050505", border_color="#fcfffd", border_width=1.3)

        # Binding event handlers for mouse enter and leave events to adjust border color and width
        self.frame.bind("<Enter>", lambda event: self.frame.configure(border_color="cyan", border_width=1.5))
        self.frame.bind("<Leave>", lambda event: self.frame.configure(border_color="#fcfffd", border_width=1.3))
        
        # Adjusting padding for desired width (experiment with values)
        self.frame.grid(row=0, column=0, padx=(150, 150), pady=(100, 210), sticky="nsew")

        # Centering content within the frame using a grid with 3 columns
        self.frame.grid_columnconfigure(0, weight=1)  # Make all columns equal width
        self.frame.grid_columnconfigure(1, weight=1)
        self.frame.grid_columnconfigure(2, weight=1)

        # Centering label with spacing from top
        label_font = ("Yu Gothic Medium", 20)  # Storing a common font for reuse
        
        # Creating a label with specified text, font, anchor, and text color
        label = ctk.CTkLabel(master=self.frame, text="Tobias Technologies Inc.\nWeb link creator",
                            font=label_font, anchor="center", text_color="#fcfffd")
        
        # Placing the label in the grid with specific row, column, column span, and padding
        label.grid(row=0, column=0, columnspan=3, pady=20)  # 20 pixels of padding from top

        output_box_font = ("French Script MT", 30)  # Font for output boxes

        # Creating a label for the URL address entry
        self.entry1_label = ctk.CTkLabel(master=self.frame, text="Url address ", font=output_box_font, text_color="#fa7e0a")
        
        # Placing the entry1_label in the grid with specific row, column, and alignment
        self.entry1_label.grid(row=2, column=0, sticky="e", padx=(5,5))

        # Creating an entry widget for entering URL address
        self.entry1 = ctk.CTkEntry(master=self.frame, width=300,
                                text_color="black", fg_color="#9af5f2")  # Setting placeholder text color to black
        
        # Placing the entry1 in the grid with specific row, column, and padding
        self.entry1.grid(row=2, column=1, sticky='w', padx=(5, 5), pady=(10, 20))  # 10 pixels from label, 20 pixels from bottom

        # Binding event handlers for focus in and focus out events to adjust border color and width
        self.entry1.bind("<FocusIn>", lambda event: self.frame.configure(border_color="cyan", border_width=1.5))
        self.entry1.bind("<FocusOut>", lambda event: self.frame.configure(border_color="#fcfffd", border_width=1.3))

        # Creating a button for generating links
        self.button_generate = ctk.CTkButton(master=self.frame, text="Generate", border_color="white", fg_color="black", width=200,
                                            border_width=1, height=10, font=("Yu Gothic Medium", 16), hover_color="#0d02ad",
                                            command=self.generate_short_links)
        
        # Placing the button_generate in the grid with specific row, column, and padding
        self.button_generate.grid(row=3, column=1, sticky='w', padx=(5, 5), pady=(10, 10))  # 10 pixels from entry
        
        # Creating output boxes with labels

        # Define the label texts for each output box
        label_texts = ["Tiny Url", "Bitly", "Rebrandly"]

        # Create a list of labels and entries using list comprehensions
        output_labels = [ctk.CTkLabel(master=self.frame, text=label_text, font=output_box_font, text_color="#fa7e0a") for label_text in label_texts]
        output_entries = [ctk.CTkEntry(master=self.frame, width=300, border_width=1, text_color="black", fg_color="#9af5f2") for _ in label_texts]

        # Place labels and entries in the grid
        for i, (label, entry) in enumerate(zip(output_labels, output_entries), start=4):
            label.grid(row=i, column=0, sticky="e", padx=(5,5))
            entry.grid(row=i, column=1, sticky="w", padx=(5, 5), pady=(10, 20))

        # Assign labels and entries to instance variables
        self.tinyurl_label, self.bitly_label, self.rebrandly_label = output_labels
        self.tinyurl_output, self.bitly_output, self.rebrandly_output = output_entries


# Check if the script is being run as the main program
if __name__ == "__main__":
    # Create the root window using customtkinter
    root = ctk.CTk()
    # Create an instance of the CustomWindowApp class with the root window
    app = CustomWindowApp(root)
    # Start the main event loop to display the GUI and handle user events
    root.mainloop()




        

