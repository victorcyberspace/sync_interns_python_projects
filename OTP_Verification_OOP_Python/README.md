# OTP Verification App

## Overview

The OTP Verification App is a simple Python application that allows users to receive and verify OTP codes via email.<br> 
The app utilizes the [customtkinter]([https://github.com/TkinterEP/customtkinter](https://github.com/TomSchimansky/CustomTkinter)) library for a modern and visually appealing graphical user interface.<br> 
Additionally, it integrates the `smtplib` library to send OTP codes to the user's email address.

## Features

- **Modern GUI:** The app provides a user-friendly interface with rounded entry boxes, glow effects, and stylish buttons.

- **OTP Sending:** Users can receive OTP codes by clicking the "Send OTP" button. The generated OTP is sent to their provided email address.

- **OTP Verification:** Users can enter the received OTP in the app, and the system will verify its correctness, providing instant feedback.

- **Secure Email Sending:** The app uses the Gmail SMTP server to securely send OTP codes to the user's email address.

## Usage

1. **Installation:**
    - Make sure you have Python installed on your system.
    - Install the required libraries:
        ```bash
        pip install customtkinter
        ```

2. **Running the App:**
    - Execute the script:
        ```bash
        python otp_email_app.py
        ```
    - The app window will appear, allowing you to input your email, receive OTP, and verify the code.
    - make sure you don't leave out the background image file, window.png

3. **Email Configuration:**
    - Before using the app, update the sender's Gmail address and app password in the script to ensure successful OTP sending.

## Dependencies

- [customtkinter](https://github.com/TkinterEP/customtkinter): A custom-themed Tkinter library for creating modern GUIs in Python.
- [python-one-time-password](https://github.com/pyauth/pyotp): A python library for generating and verifying one-time passwords.

## Author

- Asiimwe Victor Emmanuel 

## License

This project is licensed under the MIT License
