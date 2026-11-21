import tkinter
from tkinter import *
from tkcalendar import Calendar

cancelation_window = Tk() #creates a window
cancelation_window.geometry("1920x1080")
cancelation_window.title("Main menu")

cancelation_window.title("Cancelation")
cancelation_window.geometry("1920x1080")

background = Label(bg='#981e2b',
                   height=900,
                   width=75)
background.place(x=500,y=100)

icon = PhotoImage(file='logo.png')
cancelation_window.iconphoto(True, icon)
heading_cancelation = Label(text= "Penash The Indian Restaurant                   ", #Creating the main title of the windows
                         bg = "#981e2b",
                         fg = "white",
                         font = ("Times New Roman", 70),
                         bd = 3,
                         relief=SUNKEN)
heading_cancelation.place(x=-3,y=0)

location_cancelation = Label(text= "Durham \n Croxdale \n Croxdale Inn \n DH6 5HX", #Creating the location title of the windows
                         bg = "#981e2b",
                         fg = "white",
                         font = ("Times New Roman", 16))
location_cancelation.place(x= 1150,y=5)

photo_logo = PhotoImage(file="logo.png")    #this is me implementing the logo
logo_label = Label(image=photo_logo)
logo_label.place(x=1350,y=5)

def main():
    cancelation_window.destroy()
    import Main_Menu

main_menu_button = Login = Button(text="Main Menu",                          #Creating the button  that will take them to the Login window
               command= main,
               font = ("Times New Roman",20),
               activebackground= "#981e2b",
               bg= "#981e2b",
               activeforeground= "white",
               fg = "white" )

main_menu_button.place(x = 1376,y=115)

name_label = Label(text="Name:",                                             #creating a label for where they can enter their name
                   bg="#981e2b",
                   fg="white",
                   font=("Times New Roman", 25),
                   bd=3,
                   relief=RIDGE)
name_label.place(x=600,y=150)

name_entry = Entry(text = "", font=("Arial", 19))
name_entry.place(x = 710,y=155)

number_label = Label(text="Number:",                                          #creating a label for where they can enter their name
                   bg="#981e2b",
                   fg="white",
                   font=("Times New Roman", 25),
                   bd=3,
                   relief=RIDGE)
number_label.place(x=575,y=225)

number_entry = Entry(text = "", font=("Arial", 19))
number_entry.place(x = 710,y=230)

date_label = Label(text="Date:",                                                #creating a label for where they can enter the date they booked for
                   bg="#981e2b",
                   fg="white",
                   font=("Times New Roman", 25),
                   bd=3,
                   relief=RIDGE)
date_label.place(x=620,y=300)

calender = Calendar(cancelation_window, selectmode='day', year=2025, month=3, day=24)
calender.place(x = 710,y = 300)

calender = Calendar(cancelation_window,
               selectmode="day",
               year=2025,
               month=3,
               day=28,
               background="lightblue",
               foreground="black",
               font=("Arial", 12),
               borderwidth=2)

cancelation_window.mainloop()