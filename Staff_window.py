import tkinter
from tkinter import*
from turtledemo.sorting_animate import show_text

from tkcalendar import Calendar
from PIL import Image, ImageTk
from captcha.image import ImageCaptcha
from datetime import timedelta,date
import random
import string
import sqlite3
from datetime import datetime

staff_window = Tk() #creates a window
staff_window.title("Staff")
staff_window.geometry("1920x1080")

icon = PhotoImage(file='logo.png')
(staff_window.iconphoto(True, icon))
heading_staff = Label(staff_window,
                      text= "Penash The Indian Restaurant                   ", #Creating the main title of the windows
                      bg = "#981e2b",
                      fg = "white",
                      font = ("Times New Roman", 70),
                      bd = 3,
                      relief=SUNKEN)
heading_staff.place(x=-3,y=0)

location_staff = Label(staff_window,
                       text= "Durham \n Croxdale \n Croxdale Inn \n DH6 5HX", #Creating the location title of the windows
                       bg = "#981e2b",
                       fg = "white",
                       font = ("Times New Roman", 16))
location_staff.place(x= 1150,y=5)

photo_logo = PhotoImage(file="logo.png")    #this is me implementing the logo
logo_label = Label(image=photo_logo)
logo_label.place(x=1350,y=5)

background = Label(staff_window, bg='#981e2b', height=900, width=75)
background.place(x=500, y=100)

def main():
    staff_window.destroy()
    main_window.deiconify()

main_menu_button = Login = Button(staff_window,
                                  text="Main Menu",                          #Creating the button  that will take them to the Login window
                                  command= main,
                                   font = ("Times New Roman",20),
                                   activebackground= "#981e2b",
                                   bg= "#981e2b",
                                   activeforeground= "white",
                                   fg = "white" )

main_menu_button.place(x = 1376,y=115)

today_header = Label(staff_window, text="Today's Reservations", font=("Times New Roman", 24), bg="#981e2b",
                   fg="white")
today_header.place(x=600, y=180)

conn = sqlite3.connect("Penash.db")
cursor = conn.cursor()

today_date = date.today().strftime("%#y/%#m/%#d")

cursor.execute("SELECT Name, Date, Time, People, Under4s FROM Reservation_details WHERE Date = ?", (today_date,))
rows = cursor.fetchall()

# Create a Frame to hold the table
grid_frame = Frame(staff_window, bg="#981e2b")
grid_frame.place(x=500, y=250)

headers = ["Name", "Date", "Time", "People", "Under 4s"]

for col, header in enumerate(headers):
    table_header = Label(grid_frame, text=header, font=("Times New Roman", 13, "bold"),
                         bg="#981e2b", fg="White", padx=10, pady=5)
    table_header.grid(row=0, column=col, padx=5, pady=5)

for row_num, row_data in enumerate(rows, start=1):
    for col_num, cell_data in enumerate(row_data):
        data_label = Label(grid_frame, text=str(cell_data), font=("Times New Roman", 12),
                           bg="#981e2b", fg="White", padx=10, pady=5)
        data_label.grid(row=row_num, column=col_num, padx=5, pady=5)

staff_window.mainloop()