import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageOps

def search():
    search_term = entry.get()
    if search_term:
        messagebox.showinfo("Search", f"Searching for: {search_term}")
    else:
        messagebox.showwarning("Search", "Please enter a search term")

# Set up the main window
root = tk.Tk()
root.title("Sample Tkinter Page")
root.geometry("400x600")

# Title (Header)
header = tk.Label(root, text="My Sample Page", font=("Helvetica", 20, "bold"))
header.pack(pady=20)

# Round Image
img = Image.open("your-image.jpg")  # Replace with your image path
img = ImageOps.fit(img, (150, 150), method=0, bleed=0.0, box=None)  # Resize and crop to a square
img = ImageTk.PhotoImage(img)

# Create a round mask for the image
mask = Image.new("L", (150, 150), 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0, 150, 150), fill=255)
img = ImageOps.fit(img, (150, 150), method=0, bleed=0.0, box=None)
img.putalpha(mask)

# Display image
img_label = tk.Label(root, image=img)
img_label.pack()

# Search Button and Entry
entry = tk.Entry(root, font=("Helvetica", 14))
entry.pack(pady=10)

search_button = tk.Button(root, text="Search", font=("Helvetica", 14), command=search)
search_button.pack(pady=5)

# Bottom Navigation Drawer (Fixed at bottom)
bottom_frame = tk.Frame(root, bg="#333", height=50)
bottom_frame.pack(side="bottom", fill="x")

nav_home = tk.Button(bottom_frame, text="Home", bg="#333", fg="white", font=("Helvetica", 12), relief="flat")
nav_home.pack(side="left", padx=20)

nav_about = tk.Button(bottom_frame, text="About", bg="#333", fg="white", font=("Helvetica", 12), relief="flat")
nav_about.pack(side="left", padx=20)

nav_contact = tk.Button(bottom_frame, text="Contact", bg="#333", fg="white", font=("Helvetica", 12), relief="flat")
nav_contact.pack(side="left", padx=20)

# Run the application
root.mainloop()
