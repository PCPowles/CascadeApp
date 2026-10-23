import ctypes
import tkinter as tk
from tkinter import messagebox

# Load the Windows user32 library so we can call the Windows API
user32 = ctypes.windll.user32

def cascade_windows():
    """
    Cascades all open top-level windows.
    wHow = 4 (MDITILE_ZORDER) arranges them in their current stacking order.
    """
    result = user32.CascadeWindows(0, 4, 0, 0, 0)

    if result == 0:
        status_label.config(text="No windows were found to cascade.")
    else:
        status_label.config(text=f"Successfully cascaded {result} window(s).")

# --- Build the form (window) ---
root = tk.Tk()
root.title("Window Cascader")
root.geometry("320x150")      # width x height in pixels
root.resizable(False, False)

# Title text
title_label = tk.Label(root, text="Click to cascade all open windows",
                       font=("Segoe UI", 10))
title_label.pack(pady=(15, 10))

# The button — clicking it runs cascade_windows()
cascade_button = tk.Button(root, text="Cascade Windows",
                           font=("Segoe UI", 11, "bold"),
                           width=18, command=cascade_windows)
cascade_button.pack()

# Status text that updates after each click
status_label = tk.Label(root, text="", font=("Segoe UI", 9), fg="gray")
status_label.pack(pady=10)

# Start the app (keeps the window open and listening for clicks)
root.mainloop()