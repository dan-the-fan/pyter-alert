import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk

# Create the root window
root = tk.Tk()

# Set the title of the window
root.title("Peter Alert")

# Remove the icon in the window
root.iconbitmap('')

# Set the size of the window
root.geometry("100x75")

# Remove the ability for the user to resize the window
root.resizable(False, False)

# Hide the minimize and maximize buttons
root.attributes('-toolwindow', True)
root.attributes('-topmost', True)

# Load the image using PIL
pil_image = Image.open("peter.gif")

# Resize the image to 50 pixels wide, maintaining the aspect ratio
width, height = pil_image.size
new_height = int(height * 50 / width)
pil_image = pil_image.resize((50, new_height))

# Convert the image to a PhotoImage object
image = ImageTk.PhotoImage(pil_image)

# Create the image label
label = tk.Label(root, image=image)
label.pack()

# Create the "Ok" button
button = tk.Button(root, text="Ok", command=root.destroy)
button.pack()

# Run the tkinter event loop
root.mainloop()
