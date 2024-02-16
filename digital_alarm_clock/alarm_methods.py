from pygame import mixer
from threading import Thread
from tkinter import messagebox

    
def stop_alarm():
    mixer.music.stop()
    # Display message in a messagebox
    messagebox.showinfo("Message", "THAT'S IT FROM ME: THANK YOU SYNC INTERNS")
    