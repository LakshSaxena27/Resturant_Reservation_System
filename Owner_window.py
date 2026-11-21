import tkinter
from tkinter import *

Owner_window = Tk() #creates a window
Owner_window.geometry("1920x1080")
Owner_window.title("Main menu")

Owner_window.title("Logins")
Owner_window.geometry("1920x1080")

icon = PhotoImage(file='logo.png')
Owner_window.iconphoto(True, icon)
heading_owner = Label(text= "Penash The Indian Restaurant                   ", #Creating the main title of the windows
                         bg = "#981e2b",
                         fg = "white",
                         font = ("Times New Roman", 70),
                         bd = 3,
                         relief=SUNKEN)
heading_owner.place(x=-3,y=0)

location_owner = Label(text= "Durham \n Croxdale \n Croxdale Inn \n DH6 5HX", #Creating the location title of the windows
                         bg = "#981e2b",
                         fg = "white",
                         font = ("Times New Roman", 16))
location_owner.place(x= 1150,y=5)

photo_logo = PhotoImage(file="logo.png")    #this is me implementing the logo
logo_label = Label(image=photo_logo)
logo_label.place(x=1350,y=5)

def main():
    Owner_window.destroy()
    import Main_Menu

main_menu_button = Login = Button(text="Main Menu",                          #Creating the button  that will take them to the Login window
               command= main,
               font = ("Times New Roman",20),
               activebackground= "#981e2b",
               bg= "#981e2b",
               activeforeground= "white",
               fg = "white" )

main_menu_button.place(x = 1376,y=115)

Owner_window.mainloop()