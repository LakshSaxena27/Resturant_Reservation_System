import tkinter
from tkinter import*
from turtledemo.sorting_animate import show_text

from matplotlib.pyplot import connect
from twilio.rest import Client
from tkcalendar import Calendar
from PIL import Image, ImageTk
from captcha.image import ImageCaptcha
from datetime import timedelta,date
import random
import string
import sqlite3
from datetime import datetime

forgot_window = Tk() #creates a window
forgot_window.title("Forgot Password")
forgot_window.geometry("1920x1080")

conn = sqlite3.connect("Penash.db")
cursor = conn.cursor()

icon = PhotoImage(file='logo.png')
(forgot_window.iconphoto(True, icon))
heading_staff = Label(forgot_window,
                      text= "Penash The Indian Restaurant                   ", #Creating the main title of the windows
                      bg = "#981e2b",
                      fg = "white",
                      font = ("Times New Roman", 70),
                      bd = 3,
                      relief=SUNKEN)
heading_staff.place(x=-3,y=0)

location_staff = Label(forgot_window,
                       text= "Durham \n Croxdale \n Croxdale Inn \n DH6 5HX", #Creating the location title of the windows
                       bg = "#981e2b",
                       fg = "white",
                       font = ("Times New Roman", 16))
location_staff.place(x= 1150,y=5)

photo_logo = PhotoImage(file="logo.png")    #this is me implementing the logo
logo_label = Label(image=photo_logo)
logo_label.place(x=1350,y=5)

background = Label(forgot_window, bg='#981e2b', height=900, width=75)
background.place(x=500, y=100)
def main():
    forgot_window.destroy()
    main_window.deiconify()

main_menu_button = Login = Button(forgot_window,
                                  text="Main Menu",                          #Creating the button  that will take them to the Login window
                                  command= main,
                                   font = ("Times New Roman",20),
                                   activebackground= "#981e2b",
                                   bg= "#981e2b",
                                   activeforeground= "white",
                                   fg = "white" )

main_menu_button.place(x = 1376,y=115)

user_name_label = Label(forgot_window, text="Name: ",
                                 bg="#981e2b",
                                 fg="white",
                                 font=("Times New Roman", 20), bd=3,
                                 relief=RIDGE
                                 )
user_name_label.place(x=550, y=200)

user_name_entry = Entry(forgot_window, font=("Arial", 19))
user_name_entry.place(x=680, y=200)

user_number_label = Label(forgot_window, text="Number: ",
                     bg="#981e2b",
                     fg="white",
                     font=("Times New Roman", 20), bd=3,
                     relief=RIDGE
                     )
user_number_label.place(x=550, y=250)

user_number_entry = Entry(forgot_window, font=("Arial", 19))
user_number_entry.place(x=680, y=250)


def forgot():
    name = user_name_entry.get().strip()
    number = user_number_entry.get().strip()

    if not name or not number:
        fail_input_label = Label(forgot_window,
                                 text="Please fill in all fields",
                           bg="#981e2b",
                           fg="white",
                           font=("Times New Roman", 20))
        fail_input_label.place(x=300, y=400)
        return

    # Check in Staff_details table
    cursor.execute("SELECT * FROM Staff_details WHERE name = ? AND number = ?", (name, number))
    result = cursor.fetchone()

    if result:
        password = result[3]  # Assuming password is the 4th column (index 3)

        if number.startswith("0"):
            number = "+44" + number[1:]
        elif not number.startswith("+"):
            number = "+44" + number

        account_sid = "ACf01f6ff1a8c26bebd2e5c8ef02c6df27"
        auth_token = "8bed64fdcdfb72c361c1be476988f74c"
        client = Client(account_sid, auth_token)

        try:
            message = client.messages.create(
                body=f"Hi {name}, your password is: {password}",
                from_="+447476563170",
                to=number
            )
            send_label = Label(forgot_window,
                               text="Password sent to your number",
                               bg="#981e2b",
                               fg="white",
                               font=("Times New Roman", 20))
            send_label.place(x=300, y=400)
            return  # Stop here if found in Staff
        except Exception as e:
            fail_password_label = Label(forgot_window,
                                        text="Unable to send password",
                               bg="#981e2b",
                               fg="white",
                               font=("Times New Roman", 20))
            fail_password_label.place(x=300, y=400)

    # Check in Owner_details table if not found in Staff
    try:
        cursor.execute("SELECT * FROM Owner_details WHERE Name = ? AND Number = ?", (name, number))
        result = cursor.fetchone()

        if result:
            password = result[3]  # Assuming password is in 4th column

            if number.startswith("0"):
                number = "+44" + number[1:]
            elif not number.startswith("+"):
                number = "+44" + number

            account_sid = "ACf01f6ff1a8c26bebd2e5c8ef02c6df27"
            auth_token = "8bed64fdcdfb72c361c1be476988f74c"
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body=f"Hi {name}, your password is: {password}",
                from_="+447476563170",
                to=number)
            send_label = Label(forgot_window,
                               text="Password sent to your number",
                               bg="#981e2b",
                               fg="white",
                               font=("Times New Roman", 20))
            send_label.place(x=300, y=400)
            return

    except Exception as e:
        fail_search_label = Label(forgot_window,
                                  text="Name and number not found in database",
                           bg="#981e2b",
                           fg="white",
                           font=("Times New Roman", 20))
        fail_search_label.place(x=300, y=400)

    # If not found anywhere
    fail_label = Label(forgot_window,
                       text="Name and number not found in database",
                       bg="#981e2b",
                       fg="white",
                       font=("Times New Roman", 20))
    fail_label.place(x=300, y=400)

forgot_button = Button(forgot_window,
                             text="Send Password",
                             font=("Times New Roman", 20),
                             activebackground="#981e2b",
                             bg="#981e2b",
                             activeforeground="white",
                             fg="white",
                             command=forgot)
forgot_button.place(x=675,y=350)

forgot_window.mainloop()