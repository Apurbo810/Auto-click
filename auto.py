import tkinter as tk
import pyautogui
import threading
import time
from pynput import keyboard

clicking = False
click_interval = 0.1  # Default: 600 clicks per minute (10 per sec)

def click_mouse():
    while clicking:
        pyautogui.click()
        time.sleep(click_interval)

def start_clicking():
    global clicking, click_interval
    try:
        cpm = int(cpm_entry.get())
        if cpm <= 0:
            raise ValueError
        click_interval = 60 / cpm
    except ValueError:
        cpm_entry.delete(0, tk.END)
        cpm_entry.insert(0, "Invalid")
        return

    if not clicking:
        clicking = True
        thread = threading.Thread(target=click_mouse)
        thread.start()

def stop_clicking():
    global clicking
    clicking = False

# Stop clicking when Esc is pressed
def on_key_press(key):
    global clicking
    if key == keyboard.Key.esc:
        clicking = False

listener = keyboard.Listener(on_press=on_key_press)
listener.start()

# GUI Setup
root = tk.Tk()
root.title("Auto Clicker")
root.geometry("300x200")
root.config(bg="#222222")

title = tk.Label(root, text="Python Auto Clicker", font=("Arial", 14), fg="white", bg="#222222")
title.pack(pady=10)

cpm_label = tk.Label(root, text="Clicks Per Minute:", fg="white", bg="#222222", font=("Arial", 10))
cpm_label.pack()

cpm_entry = tk.Entry(root, font=("Arial", 12), justify='center')
cpm_entry.insert(0, "600")
cpm_entry.pack(pady=5)

start_button = tk.Button(root, text="Start", command=start_clicking, bg="green", fg="white", font=("Arial", 12), width=10)
start_button.pack(pady=5)

stop_button = tk.Button(root, text="Stop", command=stop_clicking, bg="red", fg="white", font=("Arial", 12), width=10)
stop_button.pack(pady=5)

note = tk.Label(root, text="Press 'Esc' to stop clicking", fg="#aaaaaa", bg="#222222", font=("Arial", 9))
note.pack(pady=5)

root.mainloop()
