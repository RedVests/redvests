import socket
import webbrowser
import threading
import tkinter as tk
from tkinter import messagebox
import time
import random
import sys

# Get user's IP address
def get_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print(f"Your IP Address is: {ip_address}")
    return ip_address

# Open the Rick Astley video
def rickroll():
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

# Create a bouncing window
def make_bouncing_window(i):
    def run_window():
        win = tk.Tk()
        win.title("Rickroll!")
        win.attributes("-topmost", True)
        win.resizable(False, False)
        win.overrideredirect(True)  # Remove window borders

        width, height = 300, 100
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()

        x = random.randint(0, screen_width - width)
        y = random.randint(0, screen_height - height)
        dx = random.choice([-4, 4])
        dy = random.choice([-3, 3])

        label = tk.Label(win, text="Never gonna give you up!", font=("Arial", 12), bg="white", fg="black")
        label.pack(expand=True, fill="both")

        win.geometry(f"{width}x{height}+{x}+{y}")

        def move():
            nonlocal x, y, dx, dy
            x += dx
            y += dy

            if x <= 0 or x + width >= screen_width:
                dx = -dx
            if y <= 0 or y + height >= screen_height:
                dy = -dy

            win.geometry(f"{width}x{height}+{x}+{y}")
            win.after(20, move)

        move()
        win.after(5000, win.destroy)  # Close after 5 seconds
        win.mainloop()

    threading.Thread(target=run_window, daemon=True).start()

# Spawn multiple bouncing windows
def spawn_windows(count=35):
    for i in range(count):
        make_bouncing_window(i)
        time.sleep(0.2)

# Show final message
def final_message():
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Finale", "NEVER GONNA GIVE YOU UP")
    root.destroy()

# Ask user for confirmation
def show_warning():
    root = tk.Tk()
    root.withdraw()
    response = messagebox.askyesno(
        "Warning!",
        "⚠️ This is a prank program intended for educational purposes only.\n\n"
        "It will open bouncing windows and play a video.\n\n"
        "Do you want to continue?"
    )
    root.destroy()
    return response

# Main routine
def main():
    if not show_warning():
        print("User cancelled execution.")
        sys.exit()

    get_ip()
    time.sleep(1)
    rickroll()
    time.sleep(3)
    spawn_windows(15)
    time.sleep(6)
    final_message()
    time.sleep(2)
    print("Program ending...")
    sys.exit()

if __name__ == "__main__":
    main()
