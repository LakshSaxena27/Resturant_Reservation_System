from tkinter import*
from PIL import Image, ImageTk
from captcha.image import ImageCaptcha
import random
import string
import os
from Main_Menu import main_window

login_window = Tk()
login_window.geometry("1920x1080")
login_window.title("Logins")

login_window.config(bg="#FFD700")

icon = PhotoImage(file ='logo.png')
main_window.iconphoto(True, icon)

background = Label(login_window, bg='#981e2b', height=900, width=75)
background.place(x=500, y=100)

heading_reservation = Label(
    login_window,
    text="Penash The Indian Restaurant                   ",
    bg="#981e2b",
    fg="white",
    font=("Times New Roman", 70),
    bd=3,
    relief=SUNKEN
)
heading_reservation.place(x=-3, y=0)

location_reservation = Label(
    login_window,
    text="Durham \n Croxdale \n Croxdale Inn \n DH6 5HX",
    bg="#981e2b",
    fg="white",
    font=("Times New Roman", 16)
)
location_reservation.place(x=1150, y=5)

photo_logo = PhotoImage(file="logo.png")    #this is me implementing the logo
logo_label = Label(image=photo_logo)
logo_label.place(x=1350,y=5)


def main():
    login_window.destroy()



main_menu_button = Button(
    login_window,
    text="Main Menu",
    command=main,
    font=("Times New Roman", 20),
    activebackground="#981e2b",
    bg="#981e2b",
    activeforeground="white",
    fg="white"
)
main_menu_button.place(x=1376, y=115)

username_label = Label(
    login_window,
    text="Username:",
    bg="#981e2b",
    fg="white",
    font=("Times New Roman", 25),
    bd=3,
    relief=RIDGE
)
username_label.place(x=550, y=150)

name_entry = Entry(login_window, font=("Arial", 19))
name_entry.place(x=710, y=155)

password_label = Label(
    login_window,
    text="Password:",
    bg="#981e2b",
    fg="white",
    font=("Times New Roman", 25),
    bd=3,
    relief=RIDGE
)
password_label.place(x=555, y=225)

password_entry = Entry(login_window, font=("Arial", 19))
password_entry.place(x=710, y=230)

characters_label = Label(login_window, text="Characters: ",
                         bg="#981e2b",
                         fg="white",
                         font=("Times New Roman", 25),
                         bd=3,
                         relief=RIDGE)
characters_label.place(x=545, y=375)

login_window.captchaLabel = Label(login_window)
login_window.captchaLabel.place(x=500,y=375)

login_window.captchaLabel.config(width=300, height=100)
captcha_image = ImageCaptcha(width=280, height=90)

captcha_entry = Entry(login_window, font=("Arial", 19))
captcha_entry.place(x=710, y=380)

cancel_button = Button(login_window,
                       text="Login",
                       font=("Times New Roman", 25),
                       activebackground="white",
                       bg="white",
                       activeforeground="#981e2b",
                       fg="#981e2b")
cancel_button.place(x=710, y=650)

login_window.mainloop()