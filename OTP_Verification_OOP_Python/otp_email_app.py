# Import necessary libraries and modules

# Import the customtkinter library for enhanced UI elements
import customtkinter

# Import the Image module from PIL to work with images
from PIL import Image

# Import the CTkMessagebox class for custom message boxes
from CTkMessagebox import CTkMessagebox

# Import the smtplib library for sending emails
import smtplib

# Import the pyotp library for generating and verifying one-time passwords
import pyotp

# Import the random module for generating random numbers
import random


# Set appearance mode and default color theme using customtkinter

# Set the application's appearance mode to "dark"
customtkinter.set_appearance_mode("dark")

# Set the default color theme to "dark-blue"
customtkinter.set_default_color_theme("dark-blue")

# Define the LoginApp class for the OTP verification application
class LoginApp:

    # Constructor method to initialize the application
    def __init__(self):

        # Create the main application window using customtkinter

        # Create a CTk window instance for the main application
        self.root = customtkinter.CTk()

        # Set the initial size of the window to 600x600 pixels
        self.root.geometry("600x600")

        # Disable resizing of the window
        self.root.resizable(False, False)

        # Call the method to create GUI elements
        self.create_widgets()

        # Add hover effect to the frame

        # Define a function to handle mouse enter events on the frame
        def on_enter(event):
            
            # Change the border color to cyan and increase the border width
            self.frame.configure(border_color="cyan", border_width=1.5)

        # Define a function to handle mouse leave events on the frame
        def on_leave(event):
            
            # Change the border color to #fc00d7 and keep the border width
            self.frame.configure(border_color="#fc00d7", border_width=1.5)

        # Bind the on_enter function to the "<Enter>" event on the frame
        self.frame.bind("<Enter>", on_enter)

        # Bind the on_leave function to the "<Leave>" event on the frame
        self.frame.bind("<Leave>", on_leave)

    # Method to create GUI elements
    def create_widgets(self):

        # Create a frame using customtkinter for layout

        # Create a CTkFrame instance to organize the elements within the window
        self.frame = customtkinter.CTkFrame(master=self.root, border_color="#f2058b", border_width=1.5)

        # Position the frame within the window using grid layout
        self.frame.grid(row=0, column=0, padx=(100, 90), pady=(150, 210), sticky="nsew", columnspan=3)

        # Load background image using CTkImage

        # Load an image from the file "window.png" and create a CTkImage instance
        self.background_image = customtkinter.CTkImage(Image.open("window.png"), size=(600, 600))

        # Create a label to display the background image
        self.background_label = customtkinter.CTkLabel(master=self.root, image=self.background_image, text="")

        # Position the background label to cover the entire window
        self.background_label.grid(row=0, column=0, sticky="nsew")

        # Place background label behind everything using lower()

        # Ensure the background label stays behind other elements
        self.background_label.lower()

        # Create a label for the application title

        # Create a CTkLabel instance for the application title
        label = customtkinter.CTkLabel(master=self.frame, text="Tobias Technologies Inc.\nOTP Verification System", font=("Yu Gothic Medium", 20), anchor="center")

        # Position the title label within the frame
        label.grid(row=1, column=0, pady=5, padx=(10, 0))

        # Create entry widgets for email and OTP input

        # Create a CTkEntry instance for recipient email input
        self.entry1 = customtkinter.CTkEntry(master=self.frame, placeholder_text="recipient email", width=160)

        # Position the email entry widget within the frame
        self.entry1.grid(row=2, column=1, pady=10, padx=(0, 1))

        # Create a CTkEntry instance for OTP code input, masking the characters
        self.entry2 = customtkinter.CTkEntry(master=self.frame, placeholder_text="otp code", show="*", width=160)

        # Position the OTP entry widget within the frame
        self.entry2.grid(row=3, column=1, pady=10, padx=(0, 1))

        # Create buttons for sending and verifying OTP

        # Create a CTkButton instance for sending OTP, linked to the send_otp function
        self.button_send_otp = customtkinter.CTkButton(master=self.frame, text="Send OTP", command=self.send_otp, hover_color="#8200fc", width=130)

        # Position the Send OTP button within the frame
        self.button_send_otp.grid(row=2, column=0, pady=10, padx=(0, 5))

        # Create a CTkButton instance for verifying OTP, linked to the verify_otp function
        self.button_verify_otp = customtkinter.CTkButton(master=self.frame, text="Verify OTP", command=self.verify_otp, hover_color="#8200fc", width=130)

        # Position the Verify OTP button within the frame
        self.button_verify_otp.grid(row=3, column=0, pady=10, padx=(0, 5))

        # Create a checkbox for "Remember Me" option

        # Create a CTkCheckBox instance for the "Remember Me" option
        self.checkbox = customtkinter.CTkCheckBox(master=self.frame, text="Remember Me")

        # Position the checkbox within the frame
        self.checkbox.grid(row=4, column=0, pady=12, padx=10)

    # Method to send OTP
    def send_otp(self):

        # Retrieve the recipient email entered by the user
        recipient_email = self.entry1.get()

        # Validate the recipient email
        if not recipient_email:
            
            # Display an error message if the email is empty
            self.show_error_message("Please enter a valid email address.")
            
            return  # Exit the function if the email is invalid

        # Generate a random 6-digit OTP code
        otp_code = str(random.randint(100000, 999999))

        # Send the OTP code to the recipient email using a separate function
        self.send_otp_email(recipient_email, otp_code)

        # Optionally store the OTP code and recipient email for later verification (e.g., for persistence)
        self.stored_otp_code = otp_code
        self.stored_recipient_email = recipient_email

        # Display a success message to the user
        self.show_success_message("OTP sent successfully!")


        

    # Method to verify OTP
    def verify_otp(self):

        # Retrieve the OTP code entered by the user
        user_input_otp = self.entry2.get()

        # Validate the user input
        if not user_input_otp:
            
            # Display an error message if the OTP code is empty
            self.show_error_message("Please enter the OTP code.")
            
            return  # Exit the function if the OTP is not entered

        # Check if the stored OTP code and recipient email exist (indicating a previous OTP send)
        if hasattr(self, 'stored_otp_code') and hasattr(self, 'stored_recipient_email'):

            # Compare the user-entered OTP with the stored OTP code
            if user_input_otp == self.stored_otp_code:
                
                # Display a success message if the OTP is correct
                self.show_success_message("OTP verification successful!")
                
            else:
                
                # Display an error message with a retry option if the OTP is incorrect
                self.show_error_retry_message("Wrong OTP code, please try again!")
                
        else:
            
            # Display an error message if the OTP has not been sent yet
            self.show_error_message("Please send OTP first.")


    # Method to send OTP email
    def send_otp_email(self, recipient_email, otp_code):

        # Set up email server details for sending OTP

        # Specify the SMTP server to use for sending emails
        email_server = "smtp.gmail.com"

        # Specify the port number for connecting to the SMTP server
        email_port = 587

        # Provide the email address and password for authentication
        email_username = "kaknovinch@gmail.com"
        email_password = "nyfdvdfiwpjgjrht"  # Replace with the actual password

        # Set up the email message content

        # Set the subject line for the email
        subject = "OTP Verification"

        # Compose the body of the email, including the OTP code
        body = f"Your OTP code is: {otp_code}"

        # Combine the subject and body into a complete email message
        message = f"Subject: {subject}\n\n{body}"

        try:
            # Connect to the email server

            # Create an SMTP server instance for sending emails
            server = smtplib.SMTP(email_server, email_port)

            # Initiate TLS encryption for secure communication
            server.starttls()

            # Log in to the email server using the provided credentials
            server.login(email_username, email_password)

            # Send the email

            # Send the composed email from the specified sender to the recipient
            server.sendmail(email_username, recipient_email, message)

            # Close the connection to the email server
            server.quit()

        except Exception as e:
            
            # Print an error message if any exceptions occur during email sending
            print(f"Error sending OTP email: {e}")


    # Method to show success message
    def show_success_message(self, message):
        
        # Create a custom message box with a success icon and "OK" button
        CTkMessagebox(message=message, icon="check", option_1="OK", title="Success")

    # Method to show error message with retry option
    def show_error_retry_message(self, message):
        
        # Create a custom message box with an error icon, "Retry" and "Cancel" buttons
        msg = CTkMessagebox(title="Error", message=message, icon="cancel", option_1="Retry", option_2="Cancel")

        # Handle user's choice
        if msg.get() == "Retry":
            print("Retrying the operation...")
            
            # Optionally, you can perform additional actions upon retry
            
        else:
            
            print("Operation canceled.")

    # Method to show generic error message
    def show_error_message(self, message):
        
        # Create a custom message box with an error icon and "OK" button
        CTkMessagebox(title="Error", message=message, icon="cancel", option_1="OK")

    # Method to run the application
    def run(self):
        
        # Start the main event loop for the application
        self.root.mainloop()

# Main entry point of the script
if __name__ == "__main__":
    
    # Create an instance of the LoginApp class
    app = LoginApp()
    
    # Run the application
    app.run()

