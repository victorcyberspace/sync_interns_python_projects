# Import the tkinter.ttk module for themed widgets.
from tkinter.ttk import *

# Import the tkinter module for basic GUI widgets.
from tkinter import *

# Import the PIL.ImageTk and PIL.Image modules for image support.
from PIL import ImageTk, Image

# Import the datetime module for date and time handling.
from datetime import datetime

# Import the time module for sleep() functionality.
from time import sleep

# Import the pygame.mixer module for audio playback.
from pygame import mixer

# Import the threading module for multi-threading.
from threading import Thread

# Import the start_alarm() and stop_alarm() functions from the alarm_methods module.
from alarm_methods import stop_alarm

from tkinter import messagebox



# Create a Tkinter window
window = Tk()

# Set the title of the window to "Clock"
window.title("Clock")

# Set the size of the window to 400x160 pixels
window.geometry("600x260")

# Set the background color of the window to #FFE9C2 (light peach)
window.configure(bg="#FFE9C2")
  

# Create a frame with a width of 402 pixels and a height of 6 pixels, with a background color of #00F7F3.
frame_line = Frame(window, width=602, height=6, bg="#050505")

# Place the frame in the 0th row and 0th column of the grid.
frame_line.grid(row=0, column=0)


# Create a frame with a width of 402 and a height of 291, with a light purple background color.
frame_body = Frame(window, width=602, height=371, bg="#f0f75c")

# Place the frame on the grid in row 1, column 0.
frame_body.grid(row=1, column=0)


# Open the image file "alarm.png"
img = Image.open('alarm.png')

# Resize the image to a width of 110 pixels and a height of 110 pixels, using the ANTIALIAS filter to produce a smooth image
img = img.resize((130, 130), Image.LANCZOS)

# Convert the PIL Image object to a Tkinter PhotoImage object
img = ImageTk.PhotoImage(img)


# Create a Label widget to display the application logo.
app_image = Label(frame_body, height=130, image=img, bg="#f0f75c")

# Place the Label widget at the top left corner of the frame.
app_image.place(x=11, y=31)


# Create a Label widget with the text "Alarm", a height of 2, an Pinchik font, and a yellow background color
name = Label(frame_body, text="Alarm", height=2, font=("Pinchik", 50, "normal"), bg="#f0f75c")

# Place the Label widget at coordinates (140, 11) in the frame
name.place(x=170, y=43)


# Create a Label widget to display the text "Hours"
hour = Label(frame_body, text = "hrs", height=2, font=("Pinchik", 30, "normal"), bg="#f0f75c")

# Place the Label widget at position (140, 41) in the frame_body widget
hour.place(x=320, y=11)

hrs = [f"{i:02d}" for i in range(13)]

# Create a Combobox object to select the current hour
c_hour = Combobox(frame_body, width=3, font=("Century Gothic", 16, "normal"), values=[h for h in hrs])

# Set the default value of the Combobox to the first hour in the list
c_hour.current(0)

# Place the Combobox at the coordinates (140, 80)
c_hour.place(x=320, y=80)

mins = [f"{i:02d}" for i in range(61)]

# Create a Label widget with the text "Mins", height 2, pinchik font, and background color #f0f75c.
minutes = Label(frame_body, text = "min", height=2, font=("Pinchik", 30, "normal"), bg="#f0f75c")

# Place the Label widget at coordinates (200, 41).
minutes.place(x=380, y=11)

# Create a Combobox widget with 3 characters width, Century Gothic font, and values from the `time_elements.mins` list.
c_min = Combobox(frame_body, width=3, font=("Century Gothic", 16, "normal"), values=[m for m in mins])

# Set the current selection of the Combobox widget to the first item.
c_min.current(0)

# Place the Combobox widget at coordinates (200, 80).
c_min.place(x=380, y=80)

secs = [f"{i:02d}" for i in range(61)]

# Create a Label widget with the text "Secs", height 2, Pinchik font, and background color #f0f75c.
seconds = Label(frame_body, text="sec", height=2, font=("Pinchik", 30, "normal"), bg="#f0f75c")

# Place the Label widget at coordinates (260, 41).
seconds.place(x=440, y=11)

# Create a Combobox widget to select the seconds
c_secs = Combobox(frame_body, width=3, font=("Century Gothic", 16, "normal"), values=[s for s in secs])

# Set the default value to the first second
c_secs.current(0)

# Place the Combobox widget at position (260, 80)
c_secs.place(x=440, y=80)


# Create a Combobox widget for the customer period, with a width of 3, font of Century Gothic, and values of AM and PM.
c_period = Combobox(frame_body, width=3, font=("Century Gothic", 16, "normal"), values=["AM", "PM"])

# Set the current value of the Combobox widget to AM.
c_period.current(0)

# Place the Combobox widget at coordinates (320, 80) in the frame.
c_period.place(x=500, y=80)

countdown_hours = Combobox(frame_body, width=3, font=("Century Gothic", 16, "normal"), values=[f"{i:02d}" for i in range(24)])
countdown_hours.current(0)
countdown_hours.place(x=320, y=120)  # Adjust position

countdown_minutes = Combobox(frame_body, width=3, font=("Century Gothic", 16, "normal"), values=[f"{i:02d}" for i in range(61)])
countdown_minutes.current(0)
countdown_minutes.place(x=380, y=120)  # Adjust position

# Seconds for countdown timer
countdown_seconds = Combobox(frame_body, width=3, font=("Century Gothic", 16, "normal"), values=[f"{i:02d}" for i in range(61)])
countdown_seconds.current(0)
countdown_seconds.place(x=440, y=120)  # Adjust position


def start_alarm():
    t = Thread(target=alarm)
    t.start()

    
# Create an integer variable to store the selected value
selected = IntVar()


# Create a radio button 
radio1 = Radiobutton(frame_body, text='Start', value=1, variable=selected, font=("Pinchik", 30, "normal"), bg="#f0f75c", command=start_alarm)

# Place the radio button at coordinates (140, 200).
radio1.place(x=140, y=200)



def sound_alarm():
    
    # Load the magic system sound effect asynchronously
    mixer.music.load('dance.mp3')

    # Create a separate thread to display the message box
    message_thread = Thread(target=show_message)
    message_thread.start()

    # Play the magic system sound effect once the music is loaded
    mixer.music.play()

    # Wait for the message thread to finish (optional)
    message_thread.join()

    # Reset the selected option to 0
    selected.set(0)

def show_message():
    messagebox.showinfo("Message", "HEY! WAKE UP, WE GOT FISH TO CATCH.")



    # Create a Radiobutton object with the text "Stop", value 1, variable selected, pinchik font, background color #f0f75c, and command stop_alarm.
    radio2 = Radiobutton(frame_body, text='Stop', value=2, variable=selected, font=("Pinchik", 30, "normal"), bg="#f0f75c", command=stop_alarm)

    # Place the Radiobutton object at coordinates (200, 120).
    radio2.place(x=290, y=200)


    
def alarm():
    """
    This function defines an alarm clock.

    Args:
        None

    Returns:
        None
    """
    # Get the set alarm time from the combo boxes
    alarm_hour = int(c_hour.get())
    alarm_minute = int(c_min.get())
    alarm_second = int(c_secs.get())
    alarm_period = c_period.get()

    # Get the current system time
    now = datetime.now()
    current_hour = int(now.strftime("%I"))
    current_minute = int(now.strftime("%M"))
    current_second = int(now.strftime("%S"))
    current_period = now.strftime("%p")

    # Convert system time and alarm time to 24-hour format
    if alarm_period == "PM":
        alarm_hour = (alarm_hour + 12) % 24
    if current_period == "PM":
        current_hour = (current_hour + 12) % 24

    # Calculate the difference between alarm time and current time
    hour_diff = alarm_hour - current_hour
    minute_diff = alarm_minute - current_minute
    second_diff = alarm_second - current_second

    # Ensure all time differences are non-negative and handle potential negative values
    time_difference = (
        (hour_diff % 24) * 3600 + (minute_diff % 60) * 60 + (second_diff % 60)
    )
    
    # Start countdown timer from the time difference
    while time_difference >= 0:
        countdown_hours.set(str(time_difference // 3600).zfill(2))
        countdown_minutes.set(str((time_difference % 3600) // 60).zfill(2))
        countdown_seconds.set(str(time_difference % 60).zfill(2))
        sleep(1)
        time_difference -= 1
        

    
    # When countdown reaches zero, trigger the alarm
    sound_alarm()

# No need for the following lines anymore
# Initialize the Pygame mixer.
# mixer.init()

# Start the Tkinter mainloop.
# window.mainloop()

                        
                       
       
# Initialize the Pygame mixer.
mixer.init()

# Start the Tkinter mainloop.
window.mainloop()
