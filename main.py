import tkinter as tk
from tkinter import ttk
import pyautogui
import threading
import time

def autoclicker(key):
    while running:
        pyautogui.press(key)
        # Adjust the time delay as needed
        time.sleep(0.01)

def start_autoclicker():
    global running
    running = True
    key = selected_key.get()
    t = threading.Thread(target=autoclicker, args=(key,))
    t.start()

def stop_autoclicker():
    global running
    running = False

# GUI setup
root = tk.Tk()
root.title("Autoclicker")

selected_key = tk.StringVar()
key_dropdown = ttk.Combobox(root, textvariable=selected_key)
key_dropdown['values'] = ('a', 'b', 'c', 'd', 'e',' ')  # Add more keys as needed
key_dropdown.grid(column=0, row=0)

start_button = tk.Button(root, text="Start", command=start_autoclicker)
start_button.grid(column=1, row=0)

stop_button = tk.Button(root, text="Stop", command=stop_autoclicker)
stop_button.grid(column=2, row=0)

root.mainloop()
