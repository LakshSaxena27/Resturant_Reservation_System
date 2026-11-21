import tkinter as tk
import random
import string

def generate_captcha(length=6):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def verify_captcha():
    user_input = entry.get().strip().upper()
    if user_input == captcha_text:
        result_label.config(text="✅ Correct!", fg="green")
    else:
        result_label.config(text="❌ Incorrect!", fg="red")

# Setup GUI
root = tk.Tk()
root.title("Simple CAPTCHA")
root.geometry("300x200")

captcha_text = generate_captcha()

# CAPTCHA Label
captcha_label = tk.Label(root, text=captcha_text, font=("Arial", 24), bg="white", fg="black")
captcha_label.pack(pady=20)

# Entry
entry = tk.Entry(root, font=("Arial", 16), justify="center")
entry.pack()

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Verify Button
verify_button = tk.Button(root, text="Verify", command=verify_captcha)
verify_button.pack(pady=5)

root.mainloop()


root.mainloop()
