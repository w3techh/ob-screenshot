#!/usr/bin/env python3

import tkinter as tk
from tkinter import messagebox
import subprocess
import datetime
import os

def take_screenshot():
    try:
        # Create ~/screenshots directory if it doesn't exist
        screenshots_dir = os.path.expanduser("~/Screenshots")
        os.makedirs(screenshots_dir, exist_ok=True)

        # Create filename with timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = os.path.join(screenshots_dir, f"screenshot_{timestamp}.png")

        # Minimize window before screenshot
        root.iconify()
        root.update()

        # Run scrot with selection mode
        subprocess.run(["scrot", "-s", filename])

        # Restore window
        root.deiconify()

        # messagebox.showinfo("Success", f"Screenshot saved as:\n{filename}")

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create main window
root = tk.Tk()
root.title("Simple Screenshot Tool")
root.geometry("300x150")
root.resizable(False, False)

# UI
label = tk.Label(root, text="Click the button to take a screenshot", pady=10)
label.pack()

btn = tk.Button(root, text="📸 Take Screenshot", command=take_screenshot, height=2)
btn.pack(pady=10)

quit_btn = tk.Button(root, text="Quit", command=root.quit)
quit_btn.pack()

root.mainloop()
