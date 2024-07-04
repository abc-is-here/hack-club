import cv2
import pyautogui
from win32api import GetSystemMetrics
import numpy as np
import time
import os
import tkinter as tk
from tkinter import messagebox

def start_recording():
    location = location_entry.get()
    duration = duration_entry.get()

    try:
        duration = int(duration)
    except ValueError:
        messagebox.showerror("Invalid input", "Duration must be an integer.")
        return

    directory = os.path.dirname(location)
    if not os.path.exists(directory):
        os.makedirs(directory)

    width = GetSystemMetrics(0)
    height = GetSystemMetrics(1)
    dimensions = (width, height)

    format = cv2.VideoWriter_fourcc(*"XVID")
    output = cv2.VideoWriter(location, format, 20.0, dimensions)

    ti = time.time()
    ending_time = ti + duration + 5

    while True:
        img = pyautogui.screenshot()
        frame1 = np.array(img)
        frame = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB)
        output.write(frame)
        if time.time() > ending_time:
            break

    output.release()
    messagebox.showinfo("Success", "Screen recording has been saved successfully!")

root = tk.Tk()
root.title("Screen Recorder")

tk.Label(root, text="Enter location to save recording:").grid(row=0, column=0, padx=10, pady=10)
location_entry = tk.Entry(root, width=50)
location_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Enter duration of the video (seconds):").grid(row=1, column=0, padx=10, pady=10)
duration_entry = tk.Entry(root, width=50)
duration_entry.grid(row=1, column=1, padx=10, pady=10)

start_button = tk.Button(root, text="Start Recording", command=start_recording)
start_button.grid(row=2, column=0, columnspan=2, pady=20)

root.mainloop()
