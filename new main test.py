import tkinter as tk
from PIL import Image, ImageTk

# Tkinter setup
root = tk.Tk()
root.title("Transparent")
label_width, label_height = 1020, 100

# Load and resize your image to fit the label
image_path = "Penash background.png"
image = Image.open(image_path).resize((label_width, label_height))
tk_image = ImageTk.PhotoImage(image)

# Create a canvas with the same size
canvas = tk.Canvas(root, width=label_width, height=label_height)
canvas.pack()

# Display the image on the canvas
canvas.create_image(0, 0, anchor="nw", image=tk_image)

# Overlay "transparent" text
# In Tkinter, we simulate transparency by using a contrasting color or stipple effect
# Using 'white' text with 'xor' blending effect is a common trick
canvas.create_text(
    label_width//2,
    label_height//2,
    text="HELLO",
    font=("Arial", 60, "bold"),
    fill="white"
)

root.mainloop()





