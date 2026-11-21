import tkinter
from tkinter import*
import customtkinter
from tkcalendar import Calendar
from PIL import Image, ImageTk
from captcha.image import ImageCaptcha
from datetime import timedelta,date
import random
import string
import sqlite3
from datetime import datetime
from twilio.rest import Client
from itertools import cycle

main_window = Tk()                                                         #creates a window
main_window.geometry("1920x1080")
main_window.title("Main menu")

conn = sqlite3.connect("Penash.db")
cursor = conn.cursor()

def login():
    main_window.withdraw()
    login_window = tkinter.Toplevel()
    login_window.geometry("1920x1080")
    login_window.title("Logins")

    login_window.config(bg="black")

    conn = sqlite3.connect("Penash.db")
    cursor = conn.cursor()

    icon = PhotoImage(file='logo.png')
    login_window.iconphoto(True, icon)

    background_label = Label(login_window,
                             text="",
                             bg="#F5E9C7",
                             width=77,
                             height=100,
                             )
    background_label.place(x=500, y=129)

    login_title = Image.open("title.png")
    login_title = login_title.resize((1528, 125))
    login_title = ImageTk.PhotoImage(login_title)

    login_title_label = Label(login_window, image=login_title, borderwidth=0)
    login_title_label.image = login_title
    login_title_label.place(x=0, y=5)

    def main():
        login_window.destroy()
        main_window.deiconify()

    main_menu_button = customtkinter.CTkButton(login_window,
                                               text="Main Menu",
                                               bg_color="black",
                                               fg_color="#F5E9C7",
                                               font=("Georgia Pro", 20),
                                               command=main,
                                               corner_radius=70,
                                               text_color="black")

    main_menu_button.place(x=1376, y=130)

    username_label = Label(
        login_window,
        text="Username:",
        bg="#F5E9C7",
        fg="black",
        font=("Times New Roman", 25),
        bd=3
    )
    username_label.place(x=550, y=150)

    name_entry = Entry(login_window, font=("Arial", 19))
    name_entry.place(x=710, y=155)

    password_label = Label(
        login_window,
        text="Password:",
        bg="#F5E9C7",
        fg="black",
        font=("Times New Roman", 25),
        bd=3,
        )
    password_label.place(x=555, y=225)

    password_entry = Entry(login_window,
                           font=("Arial", 19),
                           show="*")
    password_entry.place(x=710, y=230)

    characters_label = Label(login_window, text="Characters: ",
                             bg="#F5E9C7",
                             fg="black",
                             font=("Times New Roman", 25),
                             bd=3)
    characters_label.place(x=545, y=375)

    captcha_text = {"value": ""}

    def generate_captcha():
        # Generate new CAPTCHA text
        letters = string.ascii_uppercase + string.digits
        text = "".join(random.choices(letters, k=5))
        captcha_text["value"] = text

        captcha = ImageCaptcha(width=200, height=80, font_sizes=(20, 30, 40, 50, 60))
        image_data = captcha.generate(text)
        image = Image.open(image_data).convert("RGB")
        image_tk = ImageTk.PhotoImage(image)

        captcha_label.configure(image=image_tk)
        captcha_label.image = image_tk


    captcha_label = Label(login_window)
    captcha_label.place(x=650, y=280)

    captcha_entry = Entry(login_window, font=("Arial", 19))
    captcha_entry.place(x=710, y=380)

    def check():
        name_input = name_entry.get()
        password_input = password_entry.get()
        captcha_input = captcha_entry.get().strip().upper()

        for widget in login_window.place_slaves():
            if isinstance(widget, Label):
                text = widget.cget("text")
                if text.startswith("Please") or "Error" in text or "successfully" in text:
                    widget.destroy()

        if not all([name_input, password_input]):
            error_label = (Label(login_window, text="Please fill in all Fields", fg="black", bg="#F5E9C7",
                  font=("Arial", 16)))
            error_label.place(x=650, y=750)
            return

        if captcha_input != captcha_text["value"]:
            captcha_error = (Label(login_window, text="Incorrect Captcha", fg="black", bg="#F5E9C7", font=("Arial", 16)))
            captcha_error.place(x=650, y=750)
            generate_captcha()
            captcha_entry.delete(0,tkinter.END)
            return

        try:
            cursor.execute("SELECT * FROM Staff_details WHERE Username = ? AND Password = ?",
                           (name_input, password_input))
            result = cursor.fetchone()

            if result:
                login_window.withdraw()
                staff_window = Toplevel()  # creates a window
                staff_window.geometry("1920x1080")
                staff_window.title("Staff Window")

                staff_window.title("Staff")
                staff_window.geometry("1920x1080")

                staff_window.config(bg="black")

                icon = PhotoImage(file='logo.png')
                (staff_window.iconphoto(True, icon))

                background_label = Label(staff_window,
                                         text="",
                                         bg="#F5E9C7",
                                         width=77,
                                         height=100,
                                         )
                background_label.place(x=500, y=129)

                staff_title = Image.open("title.png")
                staff_title = staff_title.resize((1528, 125))
                staff_title = ImageTk.PhotoImage(staff_title)

                staff_title_label = Label(staff_window, image=staff_title, borderwidth=0)
                staff_title_label.image = staff_title
                staff_title_label.place(x=0, y=5)

                background_label = Label(staff_window,
                                         text="",
                                         bg="#F5E9C7",
                                         width=77,
                                         height=100,
                                         )
                background_label.place(x=500, y=129)

                def main():
                    staff_window.destroy()
                    main_window.deiconify()

                main_menu_button = customtkinter.CTkButton(staff_window,
                                                           text="Main Menu",
                                                           bg_color="black",
                                                           fg_color="#F5E9C7",
                                                           font=("Georgia Pro", 20),
                                                           command=main,
                                                           corner_radius=70,
                                                           text_color="black")

                main_menu_button.place(x=1376, y=130)

                today_header = Label(staff_window, text="Today's Reservations", font=("Times New Roman", 24),
                                     bg="#F5E9C7",
                                     fg="black")
                today_header.place(x=600, y=180)

                today_date = date.today().strftime("%Y-%m-%d")

                cursor.execute("SELECT Name, Date, Time, People, Under4s FROM Reservation_details WHERE Date = ?",
                               (today_date,))
                rows = cursor.fetchall()

                # Create a Frame to hold the table
                grid_frame = Frame(staff_window, bg="#F5E9C7")
                grid_frame.place(x=500, y=250)

                headers = ["Name", "Date", "Time", "People", "Under 4s"]

                for col, header in enumerate(headers):
                    table_header = Label(grid_frame, text=header, font=("Times New Roman", 13, "bold"),
                                         bg="#F5E9C7", fg="Black", padx=10, pady=5)
                    table_header.grid(row=0, column=col, padx=5, pady=5)

                for row_num, row_data in enumerate(rows, start=1):
                    for col_num, cell_data in enumerate(row_data):
                        data_label = Label(grid_frame, text=str(cell_data), font=("Times New Roman", 12),
                                           bg="#F5E9C7", fg="black", padx=10, pady=5)
                        data_label.grid(row=row_num, column=col_num, padx=5, pady=5)

                staff_window.mainloop()

            else:
                error_label = Label(login_window, text="Incorrect Username or Password", fg="black", bg="#F5E9C7",
                                    font=("Arial", 16))
                error_label.place(x=650, y=750)

        except Exception as e:
                Label(login_window, text=f"Database Error: {e}", fg="black", bg="#F5E9C7",

                  font=("Arial", 16)).place(x=650, y=750)

        try:
            cursor.execute("SELECT * FROM Owner_details WHERE Username = ? AND Password = ?",
                           (name_input, password_input))
            result = cursor.fetchone()

            if result:
                login_window.withdraw()
                owner_window = Toplevel()
                owner_window.geometry("1920x1080")
                owner_window.title("Owner")

                icon = PhotoImage(file='logo.png')
                owner_window.iconphoto(True, icon)

                owner_title = Image.open("title.png")
                owner_title = owner_title.resize((1528, 125))
                owner_title = ImageTk.PhotoImage(owner_title)

                owner_window.config(bg = "black")

                owner_title_label = Label(owner_window, image=owner_title, borderwidth=0)
                owner_title_label.image = owner_title
                owner_title_label.place(x=0, y=5)

                background_label = Label(owner_window,
                                         text="",
                                         bg="#F5E9C7",
                                         width=77,
                                         height=100,
                                         )
                background_label.place(x=500, y=129)

                def main():
                    owner_window.destroy()
                    main_window.deiconify()

                main_menu_button = customtkinter.CTkButton(owner_window,
                                                           text="Main Menu",
                                                           bg_color="black",
                                                           fg_color="#F5E9C7",
                                                           font=("Georgia Pro", 20),
                                                           command=main,
                                                           corner_radius=70,
                                                           text_color="black")

                main_menu_button.place(x=1376, y=130)

                owner_label = Label(
                    owner_window,
                    text="Owner",
                    bg="#F5E9C7",
                    fg="black",
                    font=("Times New Roman", 30),
                    bd=3,

                )
                owner_label.place(x=700, y=150)

                def today(event=None, *args):
                    owner_window.withdraw()
                    today_window = tkinter.Toplevel()
                    today_window.geometry("1920x1080")
                    today_window.title("today")

                    icon = PhotoImage(file='logo.png')
                    owner_window.iconphoto(True, icon)

                    today_window.config(bg="black")

                    today_title = Image.open("title.png")
                    today_title = today_title.resize((1528, 125))
                    today_title = ImageTk.PhotoImage(today_title)

                    today_title_label = Label(today_window, image=today_title, borderwidth=0)
                    today_title_label.image = today_title
                    today_title_label.place(x=0, y=5)

                    background_label = Label(today_window,
                                             text="",
                                             bg="#F5E9C7",
                                             width=77,
                                             height=100,
                                             )
                    background_label.place(x=500, y=129)

                    def main():
                        today_window.destroy()
                        main_window.deiconify()

                    main_menu_button = customtkinter.CTkButton(today_window,
                                                               text="Main Menu",
                                                               bg_color="black",
                                                               fg_color="#F5E9C7",
                                                               font=("Georgia Pro", 20),
                                                               command=main,
                                                               corner_radius=70,
                                                               text_color="black")

                    main_menu_button.place(x=1376, y=130)

                    today_date = date.today().strftime("%Y-%m-%d")

                    cursor.execute("SELECT * FROM Reservation_details WHERE Date = ?", (today_date,))
                    rows = cursor.fetchall()

                    # Create a Frame to hold the table
                    grid_frame = Frame(today_window, bg="#F5E9C7")
                    grid_frame.place(x=500, y=250)

                    headers = ["Name", "Number", "Date", "Time", "People", "Under 4s"]

                    for col, header in enumerate(headers):
                        table_header = Label(grid_frame, text=header, font=("Times New Roman", 13, "bold"),
                                             bg="#F5E9C7", fg="black", padx=10, pady=5)
                        table_header.grid(row=0, column=col, padx=5, pady=5)

                    for row_num, row_data in enumerate(rows, start=1):
                        for col_num, cell_data in enumerate(row_data):
                            data_label = Label(grid_frame, text=str(cell_data), font=("Times New Roman", 12),
                                               bg="#F5E9C7", fg="black", padx=10, pady=5)
                            data_label.grid(row=row_num, column=col_num, padx=5, pady=5)

                    today_header = Label(today_window, text="Today's Reservations", font=("Times New Roman", 24),
                                         bg="#F5E9C7",
                                         fg="black")
                    today_header.place(x=600, y=180)

                    def back():
                        today_window.destroy()
                        owner_window.deiconify()

                    back_button = customtkinter.CTkButton(today_window,
                                                               text="Back",
                                                               bg_color="black",
                                                               fg_color="#F5E9C7",
                                                               font=("Georgia Pro", 20),
                                                               command=back,
                                                               corner_radius=70,
                                                               text_color="black")
                    back_button.place(x=0, y=130)
                    today_window.mainloop()



                today_button = customtkinter.CTkButton(owner_window,
                                                           text="Reservations for today",
                                                           bg_color="#F5E9C7",
                                                           fg_color="black",
                                                           font=("Georgia Pro", 20),
                                                           command=today,
                                                           corner_radius=70,
                                                           text_color="#F5E9C7")
                today_button.place(x=650, y=275)

                def all_reservations(owner_window=None, main_window=None):
                    import tkinter as tk
                    from tkinter import ttk, PhotoImage
                    from PIL import Image, ImageTk
                    import sqlite3
                    import customtkinter

                    if owner_window:
                        owner_window.withdraw()
                    all_reservations_window= tkinter.Toplevel()
                    all_reservations_window.geometry("1920x1080")
                    all_reservations_window.title("today")

                    icon = PhotoImage(file='logo.png')
                    all_reservations_window.iconphoto(True, icon)

                    all_reservations_window.config(bg="black")

                    today_title = Image.open("title.png")
                    today_title = today_title.resize((1528, 125))
                    today_title = ImageTk.PhotoImage(today_title)

                    today_title_label = Label(all_reservations_window, image=today_title, borderwidth=0)
                    today_title_label.image = today_title
                    today_title_label.place(x=0, y=5)

                    background_label = Label(all_reservations_window,
                                             text="",
                                             bg="#F5E9C7",
                                             width=77,
                                             height=100,
                                             )
                    background_label.place(x=500, y=129)

                    def main():
                        all_reservations_window.destroy()
                        if main_window:
                            main_window.deiconify()

                    main_menu_button = customtkinter.CTkButton(all_reservations_window,
                                                               text="Back",
                                                               bg_color="black",
                                                               fg_color="#F5E9C7",
                                                               font=("Georgia Pro", 20),
                                                               command=main,
                                                               corner_radius=70,
                                                               text_color="black")

                    main_menu_button.place(x=1376, y=130)

                        #Background frame for table
                    frame = tk.Frame(all_reservations_window, bg="#F5E9C7", width=1200, height=1000)
                    frame.place(x=150, y=125)
                    frame.pack_propagate(False)

                    # Treeview to display reservations
                    columns = ("Name", "Number", "Date", "Time", "People", "Under4s")
                    tree = ttk.Treeview(frame, columns=columns, show="headings", height=20)

                    for col in columns:
                        tree.heading(col, text=col)
                        tree.column(col, width=180, anchor="center")

                    vertical = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
                    tree.configure(yscrollcommand=vertical.set)

                    tree.pack(side="left", fill="both", expand=True)
                    vertical.pack(side="right", fill="y")

                    try:
                        conn = sqlite3.connect("Penash.db")  #my database file
                        cursor = conn.cursor()

                        cursor.execute("SELECT Name, Number, Date, Time, People, Under4s FROM Reservation_details")
                        rows = cursor.fetchall()

                        for row in rows:
                            tree.insert("", "end", values=row)



                        if not rows:
                            tk.Label(frame, text="No reservations found", bg="#F5E9C7", font=("Arial", 14)).pack(
                                pady=10)

                    except Exception as e:
                        tk.Label(frame, text=f"Error loading data:\n{e}", bg="#F5E9C7", fg="red",
                                 font=("Arial", 12)).pack(pady=10)

                previous_reservations = customtkinter.CTkButton(owner_window,
                                                       text="Previous reservations",
                                                       bg_color="#F5E9C7",
                                                       fg_color="black",
                                                       font=("Georgia Pro", 20),
                                                       command=all_reservations,
                                                       corner_radius=70,
                                                       text_color="#F5E9C7")
                previous_reservations.place(x=665, y=350)

                def staff():
                    owner_window.withdraw()
                    staff_window = tkinter.Toplevel()
                    staff_window.geometry("1920x1080")
                    staff_window.title("Staff")

                    manage_staff_label = Label(staff_window,
                                                text="Manage Staff",
                                                bg="#F5E9C7",
                                                fg="black",
                                                font=("Georgia Pro", 20)
                                                )
                    manage_staff_label.place(x=700, y=150)

                    def add():
                        owner_window.withdraw()
                        add_window = tkinter.Toplevel()
                        add_window.geometry("1920x1080")
                        add_window.title("Add Staff")

                        add_window.config(bg="black")

                        icon = PhotoImage(file='logo.png')
                        staff_window.iconphoto(True, icon)

                        add_title = Image.open("title.png")
                        add_title = add_title.resize((1528, 125))
                        add_title = ImageTk.PhotoImage(add_title)

                        add_title_label = Label(add_window, image=add_title, borderwidth=0)
                        add_title_label.image = add_title
                        add_title_label.place(x=0, y=5)

                        background_label = Label(add_window,
                                                 text="",
                                                 bg="#F5E9C7",
                                                 width=77,
                                                 height=100,
                                                 )
                        background_label.place(x=500, y=129)

                        def main():
                            add_window.destroy()
                            main_window.deiconify()

                        main_menu_button = customtkinter.CTkButton(add_window,
                                                                   text="Main Menu",
                                                                   bg_color="black",
                                                                   fg_color="#F5E9C7",
                                                                   font=("Georgia Pro", 20),
                                                                   command=main,
                                                                   corner_radius=70,
                                                                   text_color="black")

                        main_menu_button.place(x=1376, y=130)

                        def back():
                            add_window.destroy()
                            staff_window.deiconify()

                        staff_name_label = Label(add_window, text="Add Staff ",
                                                 bg="#F5E9C7",
                                                 fg="black",
                                                 font=("Times New Roman", 20), bd=3,

                                                 )
                        staff_name_label.place(x=700, y=150)

                        back_button = customtkinter.CTkButton(add_window,
                                                              text="Back",
                                                              bg_color="black",
                                                              fg_color="#F5E9C7",
                                                              font=("Georgia Pro", 20),
                                                              command=back,
                                                              corner_radius=70,
                                                              text_color="black")
                        back_button.place(x=0, y=130)

                        staff_name_label = Label(add_window, text="Name: ",
                                                 bg="#F5E9C7",
                                                 fg="black",
                                                 font=("Times New Roman", 20), bd=3,

                                                 )
                        staff_name_label.place(x=550, y=200)

                        staff_name_entry = Entry(add_window, font=("Arial", 19))
                        staff_name_entry.place(x=680, y=200
                                               )
                        staff_number_label = Label(add_window, text="Number: ",
                                                   bg="#F5E9C7",
                                                   fg="black",
                                                   font=("Times New Roman", 20), bd=3,

                                                   )
                        staff_number_label.place(x=550, y=250)

                        staff_number_entry = Entry(add_window, font=("Arial", 19))
                        staff_number_entry.place(x=680, y=250)

                        staff_username_label = Label(add_window, text="Username: ",
                                                     bg="#F5E9C7",
                                                     fg="black",
                                                     font=("Times New Roman", 20), bd=3,

                                                     )
                        staff_username_label.place(x=550, y=300)

                        staff_username_entry = Entry(add_window, font=("Arial", 19))
                        staff_username_entry.place(x=680, y=300)

                        staff_password_label = Label(add_window, text="Password: ",
                                                     bg="#F5E9C7",
                                                     fg="black",
                                                     font=("Times New Roman", 20), bd=3,

                                                     )
                        staff_password_label.place(x=550, y=350)

                        staff_password_entry = Entry(add_window, font=("Arial", 19))
                        staff_password_entry.place(x=680, y=350)

                        def Add_staff():
                            name = staff_name_entry.get().strip()
                            number = staff_number_entry.get().strip()
                            username = staff_username_entry.get().strip()
                            password = staff_password_entry.get()

                            for widget in add_window.place_slaves():
                                if isinstance(widget, Label):
                                    text = widget.cget("text")
                                    if text.startswith("Please") or "Error" in text or "successfully" in text:
                                        widget.destroy()

                            if not all([name, number, username, password]):
                                input_error = Label(add_window,text="Please fill in all fields", fg="black", bg="#F5E9C7",
                                                    font=("Arial", 16))
                                input_error.place(x=650, y=750)
                                add_window.after(3000, input_error.destroy)
                                return
                            if len(str(number)) != 11:
                                input_error = Label(add_window, text="Input Error: Invalid Number", fg="black",
                                                    bg="#F5E9C7",
                                                    font=("Arial", 16))
                                input_error.place(x=650, y=750)
                                add_window.after(3000, input_error.destroy)
                                return

                            try:
                                cursor.execute("""
                                        CREATE TABLE IF NOT EXISTS Staff_details (
                                            Name TEXT,
                                            Number TEXT,
                                            Username TEXT,
                                            Password TEXT
                                        )
                                    """)

                                cursor.execute(
                                    "INSERT INTO Staff_details (Name, Number, Username, Password) VALUES (?, ?, ?, ?)",
                                    (name, number, username, password)
                                )
                                conn.commit()
                                staff_error = Label(add_window, text=f"Added staff successful ", fg="black",
                                                    bg="#F5E9C7",
                                                    font=("Arial", 16))
                                staff_error.place(x=650, y=750)
                                add_window.after(3000, staff_error.destroy)

                                staff_name_entry.delete(0, tkinter.END)
                                staff_number_entry.delete(0, tkinter.END)
                                staff_username_entry.delete(0, tkinter.END)
                                staff_password_entry.delete(0, tkinter.END)

                            except Exception as e:
                                staff_error = Label(add_window, text=f"Unable to remove staff", fg="black",
                                                    bg="#F5E9C7",
                                                    font=("Arial", 16))
                                staff_error.place(x=650, y=750)
                                add_window.after(3000, staff_error.destroy)

                        staff_add_button = customtkinter.CTkButton(add_window,
                                                              text="Add staff",
                                                              bg_color="#F5E9C7",
                                                              fg_color="black",
                                                              font=("Georgia Pro", 20),
                                                              command=Add_staff,
                                                              corner_radius=70,
                                                              text_color="#F5E9C7")
                        staff_add_button.place(x=675, y=450)

                    def delete():
                        owner_window.withdraw()
                        delete_window = tkinter.Toplevel()
                        delete_window.geometry("1920x1080")
                        delete_window.title("Delete Staff")

                        icon = PhotoImage(file='logo.png')
                        delete_window.iconphoto(True, icon)

                        delete_title = Image.open("title.png")
                        delete_title = delete_title.resize((1528, 125))
                        delete_title = ImageTk.PhotoImage(delete_title)

                        delete_window.config(bg="black")

                        delete_title_label = Label(delete_window, image=delete_title, borderwidth=0)
                        delete_title_label.image = delete_title
                        delete_title_label.place(x=0, y=5)

                        background_label = Label(delete_window,
                                                 text="",
                                                 bg="#F5E9C7",
                                                 width=77,
                                                 height=100,
                                                 )
                        background_label.place(x=500, y=129)

                        def main():
                            delete_window.destroy()
                            main_window.deiconify()

                        main_menu_button = customtkinter.CTkButton(delete_window,
                                                                   text="Main Menu",
                                                                   bg_color="black",
                                                                   fg_color="#F5E9C7",
                                                                   font=("Georgia Pro", 20),
                                                                   command=main,
                                                                   corner_radius=70,
                                                                   text_color="black")

                        main_menu_button.place(x=1376, y=130)

                        def back():
                            delete_window.destroy()
                            staff_window.deiconify()

                        back_button = customtkinter.CTkButton(delete_window,
                                                              text="Back",
                                                              bg_color="black",
                                                              fg_color="#F5E9C7",
                                                              font=("Georgia Pro", 20),
                                                              command=back,
                                                              corner_radius=70,
                                                              text_color="black")
                        back_button.place(x=0, y=130)

                        staff_name_label = Label(delete_window, text="Delete Staff",
                                                 bg="#F5E9C7",
                                                 fg="black",
                                                 font=("Times New Roman", 20), bd=3,

                                                 )
                        staff_name_label.place(x=700, y=150)


                        staff_name_label = Label(delete_window, text="Name: ",
                                                 bg="#F5E9C7",
                                                 fg="black",
                                                 font=("Times New Roman", 20), bd=3,

                                                 )
                        staff_name_label.place(x=550, y=200)

                        staff_name_entry = Entry(delete_window, font=("Arial", 19))
                        staff_name_entry.place(x=680, y=200)

                        staff_number_label = Label(delete_window, text="Number: ",
                                                   bg="#F5E9C7",
                                                   fg="black",
                                                   font=("Times New Roman", 20), bd=3,

                                                   )
                        staff_number_label.place(x=550, y=250)

                        staff_number_entry = Entry(delete_window, font=("Arial", 19))
                        staff_number_entry.place(x=680, y=250)

                        def delete_staff():
                            name = staff_name_entry.get().strip()
                            number = staff_number_entry.get().strip()

                            if not name or not number:
                                input_error = Label(delete_window, text="Please fill in all fields",
                                                    fg="black", bg="#F5E9C7", font=("Arial", 16))
                                input_error.place(x=650, y=750)
                                delete_window.after(3000, input_error.destroy)
                                return

                            if len(str(number)) != 11:
                                input_error = Label(delete_window, text="Input Error: Invalid Number", fg="black",
                                                    bg="#F5E9C7",
                                                    font=("Arial", 16))
                                input_error.place(x=650, y=750)
                                delete_window.after(3000, input_error.destroy)
                                return

                            # ensure you have a valid connection
                            global conn
                            global cursor
                            if conn is None:
                                conn = sqlite3.connect("your_database.db")
                                cursor = conn.cursor()

                            cursor.execute("SELECT * FROM Staff_details WHERE name = ? AND number = ?", (name, number))
                            result = cursor.fetchone()

                            if result:
                                cursor.execute("DELETE FROM Staff_details WHERE name = ? AND number = ?",
                                               (name, number))
                                conn.commit()
                                staff_removed = Label(delete_window, text="Staff removed successfully",
                                                      fg="black", bg="#F5E9C7", font=("Arial", 16))
                                staff_removed.place(x=650, y=750)
                                delete_window.after(3000, staff_removed.destroy)
                            else:
                                staff_error = Label(delete_window, text="Unable to remove staff",
                                                    fg="black", bg="#F5E9C7", font=("Arial", 16))
                                staff_error.place(x=650, y=750)
                                delete_window.after(3000, staff_error.destroy)

                        staff_delete_button = customtkinter.CTkButton(delete_window,
                                                              text="Remove Staff",
                                                              bg_color="#F5E9C7",
                                                              fg_color="black",
                                                              font=("Georgia Pro", 20),
                                                              command=delete_staff,
                                                              corner_radius=70,
                                                              text_color="#F5E9C7")
                        staff_delete_button.place(x=675, y=350)

                    icon = PhotoImage(file='logo.png')
                    staff_window.iconphoto(True, icon)

                    staff_title = Image.open("title.png")
                    staff_title = staff_title.resize((1528, 125))
                    staff_title = ImageTk.PhotoImage(staff_title)

                    staff_title_label = Label(staff_window, image=staff_title, borderwidth=0)
                    staff_title_label.image = staff_title
                    staff_title_label.place(x=0, y=5)

                    staff_window.config(bg="black")

                    def main():
                        staff_window.destroy()
                        main_window.deiconify()

                    main_menu_button = customtkinter.CTkButton(staff_window,
                                                               text="Main Menu",
                                                               bg_color="black",
                                                               fg_color="#F5E9C7",
                                                               font=("Georgia Pro", 20),
                                                               command=main,
                                                               corner_radius=70,
                                                               text_color="black")

                    main_menu_button.place(x=1376, y=130)

                    background_label = Label(staff_window,
                                             text="",
                                             bg="#F5E9C7",
                                             width=77,
                                             height=100,
                                             )
                    background_label.place(x=500, y=129)


                    def back():
                        staff_window.destroy()
                        owner_window.deiconify()

                    back_button = customtkinter.CTkButton(staff_window,
                                                          text="Back",
                                                          bg_color="black",
                                                          fg_color="#F5E9C7",
                                                          font=("Georgia Pro", 20),
                                                          command=back,
                                                          corner_radius=70,
                                                          text_color="black")
                    back_button.place(x=0, y=130)

                    add_button = customtkinter.CTkButton(staff_window,
                                                          text="Add Staff",
                                                          bg_color="#F5E9C7",
                                                          fg_color="black",
                                                          font=("Georgia Pro", 20),
                                                          command=add,
                                                          corner_radius=70,
                                                          text_color="#F5E9C7")
                    add_button.place(x=680, y=350)

                    delete_button = customtkinter.CTkButton(staff_window,
                                                          text="Delete Staff",
                                                          bg_color="#F5E9C7",
                                                          fg_color="black",
                                                          font=("Georgia Pro", 20),
                                                          command=delete,
                                                          corner_radius=70,
                                                          text_color="#F5E9C7")
                    delete_button.place(x=680, y=450)

                staff_button = customtkinter.CTkButton(owner_window,
                                                      text="Manage Staff",
                                                      bg_color="#F5E9C7",
                                                      fg_color="black",
                                                      font=("Georgia Pro", 20),
                                                      command=staff,
                                                      corner_radius=70,
                                                      text_color="#F5E9C7")
                staff_button.place(x=685, y=425)

                def predictions():
                    import tkinter as tk
                    from tkinter import ttk, PhotoImage, SUNKEN
                    import sqlite3
                    from datetime import datetime, timedelta
                    from collections import Counter
                    import numpy as np
                    import matplotlib.pyplot as plt
                    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
                    from sklearn.linear_model import LinearRegression

                    owner_window.withdraw()
                    predictions_window = tkinter.Toplevel()
                    predictions_window.geometry("1920x1080")
                    predictions_window.title("Staff")

                    predictions_window.config(bg="black")


                    icon = PhotoImage(file='logo.png')
                    predictions_window.iconphoto(True, icon)

                    predict_title = Image.open("title.png")
                    predict_title = predict_title.resize((1528, 125))
                    predict_title = ImageTk.PhotoImage(predict_title)

                    manage_owners_label = Label(predictions_window,
                                                text="Predictions",
                                                bg="#F5E9C7",
                                                fg="black",
                                                font=("Georgia Pro", 20)
                                                )
                    manage_owners_label.place(x=700, y=150)

                    predict_title_label = Label(predictions_window, image=predict_title, borderwidth=0)
                    predict_title_label.image = predict_title
                    predict_title_label.place(x=0, y=5)

                    def main():
                        predictions_window.destroy()
                        main_window.deiconify()

                    main_menu_button = customtkinter.CTkButton(predictions_window,
                                                               text="Main Menu",
                                                               bg_color="black",
                                                               fg_color="#F5E9C7",
                                                               font=("Georgia Pro", 20),
                                                               command=main,
                                                               corner_radius=70,
                                                               text_color="black")

                    main_menu_button.place(x=1376, y=130)

                    def back():
                        predictions_window.destroy()
                        owner_window.deiconify()

                    back_button = customtkinter.CTkButton(predictions_window,
                                                          text="Back",
                                                          bg_color="black",
                                                          fg_color="#F5E9C7",
                                                          font=("Georgia Pro", 20),
                                                          command=back,
                                                          corner_radius=70,
                                                          text_color="black")
                    back_button.place(x=0, y=130)

                    background_label = Label(predictions_window,
                                             text="",
                                             bg="#F5E9C7",
                                             width=77,
                                             height=100,
                                             )
                    background_label.place(x=500, y=129)
                    predictions_label = Label(predictions_window,
                                                text="Predictions",
                                                bg="#F5E9C7",
                                                fg="black",
                                                font=("Georgia Pro", 20)
                                                )
                    predictions_label.place(x=700, y=150)

                    def load_dates():
                        cursor.execute("SELECT Date FROM Reservation_details")
                        raw_dates = [row[0] for row in cursor.fetchall()]


                        dates = []
                        date_format = "%Y-%m-%d"  # Changed as per the format in database
                        for d in raw_dates:
                            try:
                                dates.append(datetime.strptime(d, date_format).date())
                            except Exception:
                                invalid_date = Label(text="invalid dates", bg='#F5E9C7', fg="black",
                                                     font=("Times New Roman", 16))
                                invalid_date.place(x=200, y=150)
                                predictions_window.after(3000,invalid_date.destroy)
                        return dates

                    def graph(dates):
                        if not dates:
                            return None, None, None

                        counts = Counter(dates)
                        sorted_dates = sorted(counts)
                        counts_list = [counts[d] for d in sorted_dates]

                        X = np.array([d.toordinal() for d in sorted_dates]).reshape(-1, 1)
                        y = np.array(counts_list)

                        model = LinearRegression()
                        model.fit(X, y)

                        last_day = sorted_dates[-1]
                        future_dates = [last_day + timedelta(days=i) for i in range(1, 29)]
                        future_X = np.array([d.toordinal() for d in future_dates]).reshape(-1, 1)
                        predictions = model.predict(future_X)
                        predictions = np.clip(predictions, 0, None)

                        fig = plt.figure(figsize=(8, 4))
                        plt.subplots_adjust(left=0.15, right=0.95, bottom=0.3, top=0.9)
                        plt.plot(sorted_dates, counts_list, label="Historical Reservations", marker='o')
                        plt.plot(future_dates, predictions, label="Predicted Reservations (Next 4 Weeks)",
                                 linestyle='--', marker='x')
                        plt.title("Reservation Counts: Historical and Predicted")
                        plt.xlabel("Date")
                        plt.ylabel("Number of Reservations")
                        plt.xticks(rotation=45)
                        plt.legend()
                        plt.grid(True)
                        plt.tight_layout()

                        return fig, future_dates, predictions

                    def show_prediction_table(parent, future_dates, predicted_counts):
                        tree = ttk.Treeview(parent, columns=("Date", "Predicted Reservations"), show='headings',
                                            height=12)
                        tree.heading("Date", text="Date")
                        tree.heading("Predicted Reservations", text="Predicted Reservations")
                        tree.column("Date", width=170, anchor='center')
                        tree.column("Predicted Reservations", width=170, anchor='center')

                        for date, count in zip(future_dates, predicted_counts):
                            if date.weekday() != 6:  # Skip Sundays
                                tree.insert("", "end", values=(date.strftime("%a %d %b %Y"), f"{count:.1f}"))

                        tree.place(x=400, y=870)

                    # Call the logic within your window
                    reservation_dates = load_dates()
                    fig, future_dates, predictions = graph(reservation_dates)

                    if fig:
                        canvas = FigureCanvasTkAgg(fig, master=predictions_window)
                        canvas.draw()
                        canvas.get_tk_widget().place(x=525, y=200, width=500, height=250)
                        show_prediction_table(predictions_window, future_dates, predictions)

                        import pandas as pd

                        conn2 = sqlite3.connect("Penash.db")
                        query = "SELECT Date, People FROM Reservation_details"
                        data = pd.read_sql_query(query, conn2)
                        conn2.close()

                        data['Date'] = pd.to_datetime(data['Date'])
                        data['People'] = pd.to_numeric(data['People'], errors='coerce')

                        daily_avg = data.groupby('Date')['People'].mean().reset_index()
                        daily_avg.columns = ['Date', 'Average_Group_Size']

                        moving_avg = daily_avg['Average_Group_Size'].rolling(window=3).mean().iloc[-1]
                        future_dates_avg = [daily_avg['Date'].iloc[-1] + timedelta(days=i) for i in range(1, 8)]
                        future_avg = [moving_avg] * 7

                        future_data = pd.DataFrame({'Date': future_dates_avg,
                                                    'Average_Group_Size': future_avg})

                        # BAR CHART
                        fig2 = plt.figure(figsize=(8, 4))
                        plt.subplots_adjust(left=0.15, right=0.95, bottom=0.3, top=0.9)
                        plt.bar(daily_avg['Date'], daily_avg['Average_Group_Size'], label='Past Avg Group Size')
                        plt.bar(future_data['Date'], future_data['Average_Group_Size'],
                                label='Predicted Avg (Next 7 days)')

                        plt.title("Average Group Size Per Day (Past + Next Week)")
                        plt.xlabel("Date")
                        plt.ylabel("Average Group Size")
                        plt.xticks(rotation=45)
                        plt.legend()
                        plt.tight_layout()

                        canvas2 = FigureCanvasTkAgg(fig2, master=predictions_window)
                        canvas2.draw()
                        canvas2.get_tk_widget().place(x=525, y=500, width=500, height=250)
                    else:
                        tk.Label(predictions_window, text="No reservation data found to display predictions.",
                                 bg='#F5E9C7', fg="black", font=("Times New Roman", 20)).place(x=600, y=400)

                prediction_button = customtkinter.CTkButton(owner_window,
                                                      text="Predictions",
                                                      bg_color="#F5E9C7",
                                                      fg_color="black",
                                                      font=("Georgia Pro", 20),
                                                      command=predictions,
                                                      corner_radius=70,
                                                      text_color="#F5E9C7")
                prediction_button.place(x=695, y=500)

                def manage_owner():
                    owner_window.withdraw()
                    manage_owner_window = tkinter.Toplevel()
                    manage_owner_window.geometry("1920x1080")
                    manage_owner_window.title("Manage Owners")

                    manage_owner_window.config(bg="black")

                    manage_owners_label = Label(manage_owner_window,
                                                text = "Manage Owners",
                                                bg = "#F5E9C7",
                                                fg = "black",
                                                font=("Georgia Pro", 20)
                                                )
                    manage_owners_label.place(x=700,y=150)

                    def add_owner():
                        owner_window.withdraw()
                        add_owner_window = tkinter.Toplevel()
                        add_owner_window.geometry("1920x1080")
                        add_owner_window.title("Add Owner")

                        icon = PhotoImage(file='logo.png')
                        add_owner_window.iconphoto(True, icon)

                        add_owner_window.config(bg="black")

                        add_title = Image.open("title.png")
                        add_title = add_title.resize((1528, 125))
                        add_title = ImageTk.PhotoImage(add_title)

                        add_title_label = Label(add_owner_window, image=add_title, borderwidth=0)
                        add_title_label.image = add_title
                        add_title_label.place(x=0, y=5)

                        def main():
                            add_owner_window.destroy()
                            main_window.deiconify()

                        main_menu_button = customtkinter.CTkButton(add_owner_window,
                                                                   text="Main Menu",
                                                                   bg_color="black",
                                                                   fg_color="#F5E9C7",
                                                                   font=("Georgia Pro", 20),
                                                                   command=main,
                                                                   corner_radius=70,
                                                                   text_color="black")

                        main_menu_button.place(x=1376, y=130)

                        def back():
                            add_owner_window.destroy()
                            manage_owner_window.deiconify()

                        back_button = customtkinter.CTkButton(add_owner_window,
                                                              text="Back",
                                                              bg_color="black",
                                                              fg_color="#F5E9C7",
                                                              font=("Georgia Pro", 20),
                                                              command=back,
                                                              corner_radius=70,
                                                              text_color="black")
                        back_button.place(x=0, y=130)

                        add_owner_label = Label(add_owner_window, text="Name: ",
                                                 bg="#F5E9C7",
                                                 fg="black",
                                                 font=("Times New Roman", 20), bd=3,

                                                 )
                        add_owner_label.place(x=700, y=200)

                        background_label = Label(add_owner_window,
                                                 text="",
                                                 bg="#F5E9C7",
                                                 width=77,
                                                 height=100,
                                                 )
                        background_label.place(x=500, y=129)

                        add_owner_label = Label(add_owner_window, text="Add Owner ",
                                                bg="#F5E9C7",
                                                fg="black",
                                                font=("Times New Roman", 20), bd=3,
                                                )
                        add_owner_label.place(x=700, y=150)

                        owner_name_label = Label(add_owner_window, text="Name: ",
                                                 bg="#F5E9C7",
                                                 fg="black",
                                                 font=("Times New Roman", 20), bd=3,

                                                 )
                        owner_name_label.place(x=550, y=200)

                        owner_name_entry = Entry(add_owner_window, font=("Arial", 19))
                        owner_name_entry.place(x=680, y=200
                                               )
                        owner_number_label = Label(add_owner_window, text="Number: ",
                                                   bg="#F5E9C7",
                                                   fg="black",
                                                   font=("Times New Roman", 20), bd=3,

                                                   )
                        owner_number_label.place(x=550, y=250)

                        owner_number_entry = Entry(add_owner_window, font=("Arial", 19))
                        owner_number_entry.place(x=680, y=250)

                        owner_username_label = Label(add_owner_window, text="Username: ",
                                                     bg="#F5E9C7",
                                                     fg="black",
                                                     font=("Times New Roman", 20), bd=3,

                                                     )
                        owner_username_label.place(x=550, y=300)

                        owner_username_entry = Entry(add_owner_window, font=("Arial", 19))
                        owner_username_entry.place(x=680, y=300)

                        owner_password_label = Label(add_owner_window, text="Password: ",
                                                     bg="#F5E9C7",
                                                     fg="black",
                                                     font=("Times New Roman", 20), bd=3,

                                                     )
                        owner_password_label.place(x=550, y=350)

                        owner_password_entry = Entry(add_owner_window, font=("Arial", 19))
                        owner_password_entry.place(x=680, y=350)

                        def Add_owners():
                            name = owner_name_entry.get().strip()
                            number = owner_number_entry.get().strip()
                            username = owner_username_entry.get().strip()
                            password = owner_password_entry.get()

                            for widget in add_owner_window.place_slaves():
                                if isinstance(widget, Label):
                                    text = widget.cget("text")
                                    if text.startswith("Please") or "Error" in text or "successfully" in text:
                                        widget.destroy()

                            if not all([name, number, username, password]):
                                input_error = Label(add_owner_window,text="Please fill in all fields", fg="black", bg="#F5E9C7",
                                                    font=("Arial", 16))
                                input_error.place(x=650, y=750)
                                add_owner_window.after(3000, input_error.destroy)

                                return

                            if len(str(number)) != 11:
                                input_error = Label(add_owner_window, text="Input Error: Invalid Number", fg="black",
                                                    bg="#F5E9C7",
                                                    font=("Arial", 16))
                                input_error.place(x=650, y=750)
                                add_owner_window.after(3000, input_error.destroy)
                                return

                            try:
                                cursor.execute("""
                                    CREATE TABLE IF NOT EXISTS Owner_details (
                                        Name TEXT,
                                        Number TEXT,
                                        Username TEXT,
                                        Password TEXT
                                    )
                                """)

                                cursor.execute(
                                    "INSERT INTO Owner_details (Name, Number, Username, Password) VALUES (?, ?, ?, ?)",
                                    (name, number, username, password)
                                )
                                conn.commit()
                                data_inserted = Label(add_owner_window, text=f"Owner added successful", fg="black",
                                                       bg="#F5E9C7",
                                                       font=("Arial", 16))
                                data_inserted.place(x=650, y=750)
                                add_owner_window.after(3000, data_inserted.destroy)

                                owner_name_entry.delete(0, tkinter.END)
                                owner_number_entry.delete(0, tkinter.END)
                                owner_username_entry.delete(0, tkinter.END)
                                owner_password_entry.delete(0, tkinter.END)

                            except Exception as e:
                                database_error = Label(add_owner_window, text=f"Database Error: {e}", fg="black", bg="#F5E9C7",
                                                       font=("Arial", 16))
                                database_error.place(x=650, y=750)
                                login_window.after(3000,database_error.destroy)

                        add_owner_button = customtkinter.CTkButton(add_owner_window,
                                                              text="Add",
                                                              bg_color="#F5E9C7",
                                                              fg_color="black",
                                                              font=("Georgia Pro", 20),
                                                              command=Add_owners,
                                                              corner_radius=70,
                                                              text_color="#F5E9C7")
                        add_owner_button.place(x=675, y=450)

                    def delete_owners():
                        owner_window.withdraw()
                        delete_owner_window = tkinter.Toplevel()
                        delete_owner_window.geometry("1920x1080")
                        delete_owner_window.title("Delete Owners")

                        icon = PhotoImage(file='logo.png')
                        delete_owner_window.iconphoto(True, icon)

                        delete_owner_window.config(bg="black")

                        delete_title = Image.open("title.png")
                        delete_title = delete_title.resize((1528, 125))
                        delete_title = ImageTk.PhotoImage(delete_title)

                        delete_title_label = Label(delete_owner_window, image=delete_title, borderwidth=0)
                        delete_title_label.image = delete_title
                        delete_title_label.place(x=0, y=5)

                        background_label = Label(delete_owner_window,
                                                 text="",
                                                 bg="#F5E9C7",
                                                 width=77,
                                                 height=100,
                                                 )
                        background_label.place(x=500, y=129)

                        def main():
                            delete_owner_window.destroy()
                            main_window.deiconify()

                        main_menu_button = customtkinter.CTkButton(delete_owner_window,
                                                                   text="Main Menu",
                                                                   bg_color="black",
                                                                   fg_color="#F5E9C7",
                                                                   font=("Georgia Pro", 20),
                                                                   command=main,
                                                                   corner_radius=70,
                                                                   text_color="black")

                        main_menu_button.place(x=1376, y=130)

                        def back():
                            delete_owner_window.destroy()
                            manage_owner_window.deiconify()

                        back_button = customtkinter.CTkButton(delete_owner_window,
                                                              text="Back",
                                                              bg_color="black",
                                                              fg_color="#F5E9C7",
                                                              font=("Georgia Pro", 20),
                                                              command=back,
                                                              corner_radius=70,
                                                              text_color="black")
                        back_button.place(x=0, y=130)

                        delete_owner_label = Label(delete_owner_window, text="Delete Owner ",
                                                 bg="#F5E9C7",
                                                 fg="black",
                                                 font=("Times New Roman", 20), bd=3,
                                                 )
                        delete_owner_label.place(x=700, y=150)

                        owner_name_label = Label(delete_owner_window, text="Name: ",
                                                 bg="#F5E9C7",
                                                 fg="black",
                                                 font=("Times New Roman", 20), bd=3,

                                                 )
                        owner_name_label.place(x=550, y=200)

                        owner_name_entry = Entry(delete_owner_window, font=("Arial", 19))
                        owner_name_entry.place(x=680, y=200)

                        owner_number_label = Label(delete_owner_window, text="Number: ",
                                                   bg="#F5E9C7",
                                                   fg="black",
                                                   font=("Times New Roman", 20), bd=3,

                                                   )
                        owner_number_label.place(x=550, y=250)

                        owner_number_entry = Entry(delete_owner_window, font=("Arial", 19))
                        owner_number_entry.place(x=680, y=250)

                        def delete_owner():
                            name = owner_name_entry.get().strip()
                            number = owner_number_entry.get().strip()

                            if not name or not number:
                                input_error = Label(delete_owner_window,text="Please fill in all fields", fg="black", bg="#F5E9C7",
                                                     font=("Arial", 16))
                                input_error.place(x=650, y=750)
                                delete_owner_window.after(3000, input_error.destroy)
                                return
                            if len(str(number)) != 11:
                                input_error = Label(delete_owner_window, text="Input Error: Invalid Number", fg="black",
                                                    bg="#F5E9C7",
                                                    font=("Arial", 16))
                                input_error.place(x=650, y=750)
                                delete_owner_window.after(3000, input_error.destroy)
                                return

                            cursor.execute("SELECT * FROM Owner_details WHERE name = ? AND number = ?", (name, number))
                            result = cursor.fetchone()

                            if result:
                                cursor.execute("DELETE FROM Owner_details WHERE Name = ? AND Number = ?",
                                               (name, number))
                                conn.commit()
                                user_removed = Label(delete_owner_window,text="Owner has been removed", fg="black", bg="#F5E9C7",
                                                     font=("Arial", 16))
                                user_removed.place(x=650, y=750)
                                delete_owner_window.after(3000,user_removed.destroy)
                            else:
                                user_not_found = Label(delete_owner_window,text="Owner not found", fg="black", bg="#F5E9C7",
                                                     font=("Arial", 16))
                                user_not_found.place(x=650, y=750)
                                delete_owner_window.after(3000, user_not_found.destroy)

                        delete_owner_button = customtkinter.CTkButton(delete_owner_window,
                                                              text="Delete",
                                                              bg_color="#F5E9C7",
                                                              fg_color="black",
                                                              font=("Georgia Pro", 20),
                                                              command=delete_owner,
                                                              corner_radius=70,
                                                              text_color="#F5E9C7")
                        delete_owner_button.place(x=675, y=350)

                    icon = PhotoImage(file='logo.png')
                    manage_owner_window.iconphoto(True, icon)

                    manage_title = Image.open("title.png")
                    manage_title = manage_title.resize((1528, 125))
                    manage_title = ImageTk.PhotoImage(manage_title)

                    manage_owner_window.config(bg="black")

                    manage_title_label = Label(manage_owner_window, image=manage_title, borderwidth=0)
                    manage_title_label.image = manage_title
                    manage_title_label.place(x=0, y=5)

                    background_label = Label(manage_owner_window,
                                             text="",
                                             bg="#F5E9C7",
                                             width=77,
                                             height=100,
                                             )
                    background_label.place(x=500, y=129)

                    def main():
                        manage_owner_window.destroy()
                        main_window.deiconify()

                    main_menu_button = customtkinter.CTkButton(manage_owner_window,
                                                               text="Main Menu",
                                                               bg_color="black",
                                                               fg_color="#F5E9C7",
                                                               font=("Georgia Pro", 20),
                                                               command=main,
                                                               corner_radius=70,
                                                               text_color="black")

                    main_menu_button.place(x=1376, y=130)

                    def back():
                        manage_owner_window.destroy()
                        owner_window.deiconify()

                    back_button = customtkinter.CTkButton(manage_owner_window,
                                                          text="Back",
                                                          bg_color="black",
                                                          fg_color="#F5E9C7",
                                                          font=("Georgia Pro", 20),
                                                          command=back,
                                                          corner_radius=70,
                                                          text_color="black")
                    back_button.place(x=0, y=130)

                    add_button = customtkinter.CTkButton(manage_owner_window,
                                                          text="Add owners",
                                                          bg_color="#F5E9C7",
                                                          fg_color="black",
                                                          font=("Georgia Pro", 20),
                                                          command=add_owner,
                                                          corner_radius=70,
                                                          text_color="#F5E9C7")
                    add_button.place(x=680, y=350)

                    delete_button = customtkinter.CTkButton(manage_owner_window,
                                                         text="Delete owners",
                                                         bg_color="#F5E9C7",
                                                         fg_color="black",
                                                         font=("Georgia Pro", 20),
                                                         command=delete_owners,
                                                         corner_radius=70,
                                                         text_color="#F5E9C7")
                    delete_button.place(x=680, y=450)

                manage_owner_button = customtkinter.CTkButton(owner_window,
                                                     text="Manage owners",
                                                     bg_color="#F5E9C7",
                                                     fg_color="black",
                                                     font=("Georgia Pro", 20),
                                                     command=manage_owner,
                                                     corner_radius=70,
                                                     text_color="#F5E9C7")
                manage_owner_button.place(x=680, y=575)


        except Exception as e:
            database_error = Label(login_window, text=f"Database Error: {e}", fg="black", bg="#F5E9C7",
                  font=("Arial", 16))
            database_error.place(x=650, y=750)
            login_window.after(3000,database_error.destroy)

    def forgot_password():
        login_window.withdraw()
        forgot_window = Toplevel()  # creates a window
        forgot_window.title("Forgot Password")
        forgot_window.geometry("1920x1080")

        conn = sqlite3.connect("Penash.db")
        cursor = conn.cursor()

        icon = PhotoImage(file='logo.png')
        (forgot_window.iconphoto(True, icon))

        forgot_title = Image.open("title.png")
        forgot_title = forgot_title.resize((1528, 125))
        forgot_title = ImageTk.PhotoImage(forgot_title)

        forgot_window.config(bg="black")

        forgot_title_label = Label(forgot_window, image=forgot_title, borderwidth=0)
        forgot_title_label.image = forgot_title
        forgot_title_label.place(x=0, y=5)

        background_label = Label(forgot_window,
                                 text="",
                                 bg="#F5E9C7",
                                 width=77,
                                 height=100,
                                 )
        background_label.place(x=500, y=129)

        def main():
            forgot_window.destroy()
            main_window.deiconify()

        main_menu_button = customtkinter.CTkButton(forgot_window,
                                                   text="Main Menu",
                                                   bg_color="black",
                                                   fg_color="#F5E9C7",
                                                   font=("Georgia Pro", 20),
                                                   command=main,
                                                   corner_radius=70,
                                                   text_color="black")

        main_menu_button.place(x=1376, y=130)

        user_name_label = Label(forgot_window, text="Name: ",
                                bg="#F5E9C7",
                                fg="black",
                                font=("Times New Roman", 20), bd=3,

                                )
        user_name_label.place(x=550, y=200)

        user_name_entry = Entry(forgot_window, font=("Arial", 19))
        user_name_entry.place(x=680, y=200)

        user_number_label = Label(forgot_window, text="Number: ",
                                  bg="#F5E9C7",
                                  fg="black",
                                  font=("Times New Roman", 20), bd=3,

                                  )
        user_number_label.place(x=550, y=250)

        user_number_entry = Entry(forgot_window, font=("Arial", 19))
        user_number_entry.place(x=680, y=250)

        def back():
            forgot_window.destroy()
            login_window.deiconify()

        back_button = customtkinter.CTkButton(forgot_window,
                                              text="Back",
                                              bg_color="black",
                                              fg_color="#F5E9C7",
                                              font=("Georgia Pro", 20),
                                              command=back,
                                              corner_radius=70,
                                              text_color="black")
        back_button.place(x=0, y=130)

        def forgot():
            name = user_name_entry.get().strip()
            number = user_number_entry.get().strip()

            if not name or not number:
                fail_input_label = Label(forgot_window,
                                         text="Please fill in all fields",
                                         bg="#F5E9C7",
                                         fg="black",
                                         font=("Times New Roman", 20))
                fail_input_label.place(x=600, y=550)
                forgot_window.after(3000,fail_input_label.destroy)
                return
            if len(str(number)) != 11:
                input_error = Label(forgot_window, text="Input Error: Invalid Number", fg="black",
                                    bg="#F5E9C7",
                                    font=("Arial", 16))
                input_error.place(x=650, y=550)
                forgot_window.after(3000, input_error.destroy)
                return


            try:
                cursor.execute("SELECT password FROM Staff_details WHERE name = ? AND number = ?",
                               (name, number))
                result = cursor.fetchone()

                if result:
                    password = result[0]

                    if number.startswith("0"):
                        send_number = "+44" + number[1:]
                    elif not number.startswith("+"):
                        send_number = "+44" + number
                    else:
                        send_number = number

                    # Send SMS
                    account_sid = "ACf01f6ff1a8c26bebd2e5c8ef02c6df27"
                    auth_token = "8bed64fdcdfb72c361c1be476988f74c"
                    client = Client(account_sid, auth_token)

                    try:
                        client.messages.create(
                            body=f"Hi {name}, your password is: {password}",
                            from_="+447476563170",
                            to=send_number
                        )
                        send_label = Label(forgot_window,
                                           text="Password sent to your number",
                                           bg="#F5E9C7",
                                           fg="black",
                                           font=("Times New Roman", 20))
                        send_label.place(x=650, y=750)

                        user_name_entry.delete(0, tkinter.END)
                        user_number_entry.delete(0, tkinter.END)

                        return
                    except Exception as e:
                        fail_password_label = Label(forgot_window,
                                                    text="Unable to send password",
                                                    bg="#F5E9C7",
                                                    fg="black",
                                                    font=("Times New Roman", 20))
                        fail_password_label.place(x=60, y=550)
                        fail_password_label.after(3000,fail_password_label.destroy)
                        return

                # --- Owner_details lookup (if not found in Staff) ---
                cursor.execute("SELECT password FROM Owner_details WHERE name = ? AND number = ?",
                               (name, number))
                result = cursor.fetchone()

                if result:
                    password = result[0]

                    if number.startswith("0"):
                        send_number = "+44" + number[1:]
                    elif not number.startswith("+"):
                        send_number = "+44" + number
                    else:
                        send_number = number

                    account_sid = "ACf01f6ff1a8c26bebd2e5c8ef02c6df27"
                    auth_token = "8bed64fdcdfb72c361c1be476988f74c"
                    client = Client(account_sid, auth_token)

                    try:
                        client.messages.create(
                            body=f"Hi {name}, your password is: {password}",
                            from_="+447882964553",
                            to=send_number
                        )
                        send_label = Label(forgot_window,
                                           text="Password sent to your number",
                                           bg="#F5E9C7",
                                           fg="black",
                                           font=("Times New Roman", 20))
                        send_label.place(x=600, y=550)
                        forgot_window.after(3000,send_label.destroy)

                        user_name_entry.delete(0, tkinter.END)
                        user_number_entry.delete(0, tkinter.END)

                        return
                    except Exception as e:
                        fail_password_label = Label(forgot_window,
                                                    text="Unable to send password",
                                                    bg="#F5E9C7",
                                                    fg="black",
                                                    font=("Times New Roman", 20))
                        fail_password_label.place(x=650, y=750)
                        forgot_window.after(3000,fail_password_label.destroy)

                        return

            except Exception as e:
                fail_search_label = Label(forgot_window,
                                          text="Database error (check console)",
                                          bg="#F5E9C7",
                                          fg="black",
                                          font=("Times New Roman", 20))
                fail_search_label.place(x=650, y=750)
                print("Database error:", e)
                return

            # --- If not found in either table ---
            fail_label = Label(forgot_window,
                               text="Name and number not found in database",
                               bg="#F5E9C7",
                               fg="black",
                               font=("Times New Roman", 20))
            fail_label.place(x=650, y=550)

        forgot_button = customtkinter.CTkButton(forgot_window,
                                             text="Send Password",
                                             bg_color="#F5E9C7",
                                             fg_color="black",
                                             font=("Georgia Pro", 20),
                                             command=forgot,
                                             corner_radius=70,
                                             text_color="#F5E9C7")
        forgot_button.place(x=675, y=350)

    forgot_button = customtkinter.CTkButton(login_window,
                                            text="Forgot Password",
                                            bg_color="#F5E9C7",
                                            fg_color="black",
                                            font=("Georgia Pro", 20),
                                            command=forgot_password,
                                            corner_radius=70,
                                            text_color="#F5E9C7")
    forgot_button.place(x=675, y=450)

    login_button = customtkinter.CTkButton(login_window,
                                            text="Login",
                                            bg_color="#F5E9C7",
                                            fg_color="black",
                                            font=("Georgia Pro", 20),
                                            command=check,
                                            corner_radius=70,
                                            text_color="#F5E9C7")
    login_button.place(x=710, y=700)

    generate_captcha()

def reservation():
    main_window.withdraw()  
    reservation_window = tkinter.Toplevel()
    reservation_window.geometry("1920x1080")
    reservation_window.title("Reservation")
    reservation_window.config(bg="#000a14")

    conn = sqlite3.connect("Penash.db")
    cursor = conn.cursor()

    background_label = Label(reservation_window,
                             text="",
                             bg="#F5E9C7",
                             width=77,
                             height=100,
                             )
    background_label.place(x=500, y=129)

    icon = PhotoImage(file='logo.png')
    reservation_window.iconphoto(True, icon)

    reservation_title = Image.open("title.png")
    reservation_title = reservation_title.resize((1528, 125))
    reservation_title = ImageTk.PhotoImage(reservation_title)

    reservation_title_label = Label(reservation_window, image=reservation_title, borderwidth=0)
    reservation_title_label.image = reservation_title
    reservation_title_label.place(x=0, y=5)

    def main():
        reservation_window.destroy()
        main_window.deiconify()

    main_menu_button = customtkinter.CTkButton(reservation_window,
                                               text="Main Menu",
                                               bg_color="#F5E9C7",
                                               fg_color="black",
                                               font=("Georgia Pro", 20),
                                               command=main,
                                               corner_radius=70,
                                               text_color="#F5E9C7")

    main_menu_button.place(x=1376, y=130)

    left_images = [
        ImageTk.PhotoImage(Image.open("curry.jpg").resize((500, 700))),
        ImageTk.PhotoImage(Image.open("curry_2.jpg").resize((500, 700))),
        ImageTk.PhotoImage(Image.open("naan.jpg").resize((500, 700)))
    ]

    right_images = [
        ImageTk.PhotoImage(Image.open("lollipop.jpg").resize((500, 700))),
        ImageTk.PhotoImage(Image.open("panner.PNG").resize((500, 700))),
        ImageTk.PhotoImage(Image.open("biryani.jpg").resize((500, 700)))
    ]

    left_iter = cycle(left_images)
    right_iter = cycle(right_images)

    left_label = Label(reservation_window, borderwidth=0)
    left_label.place(x=0, y=100, anchor="nw")
    left_label.lower()

    right_label = Label(reservation_window, borderwidth=0)
    right_label.place(relx=1.0, y=100, anchor="ne")
    right_label.lower()

    def change_left():
        img = next(left_iter)
        left_label.config(image=img)
        left_label.image = img
        main_window.after(10000, change_left)

    def change_right():
        img = next(right_iter)
        right_label.config(image=img)
        right_label.image = img
        main_window.after(10000, change_right)

    change_left()
    change_right()

    name_label = Label(reservation_window, text="Name:",
                       bg="#F5E9C7",
                       fg="black",
                       font=("Times New Roman", 25), bd=3,
                       )
    name_label.place(x=600, y=150)

    name_entry = Entry(reservation_window, font=("Arial", 19))
    name_entry.place(x=710, y=155)

    number_label = Label(reservation_window, text="Number:",
                         bg="#F5E9C7",
                         fg="black",
                         font=("Times New Roman", 25),
                         bd=3,
                         )
    number_label.place(x=575, y=200)

    number_entry = Entry(reservation_window, font=("Arial", 19))
    number_entry.place(x=710, y=205)

    date_label = Label(reservation_window, text="Date:",
                       bg="#F5E9C7",
                       fg="black",
                       font=("Times New Roman", 25), bd=3,
                       )
    date_label.place(x=620, y=250)

    tomorrow = date.today() + timedelta(days=1)
    max_date = date.today() + timedelta(days=30)
    cal = Calendar(reservation_window, selectmode='day',
                   mindate=tomorrow,
                   maxdate=max_date,
                   background="#F5E9C7",
                   fg="black",
                   bg="black",
                   headersbackground="#F5E9C7",
                   headersforeground="black",
                   selectbackground="#F5E9C7",
                   selectforeground="black",
                   borderwidth=5)
    cal.place(x=700, y=250)

    time_label = Label(reservation_window, text="Time:",
                       bg="#F5E9C7",
                       fg="black",
                       font=("Times New Roman", 25),
                       bd=3,
                       )
    time_label.place(x=620, y=450)

    time_option = tkinter.StringVar()
    time_option.set("16:00")
    time_options = ["16:00", "17:00", "18:00", "19:00", "20:00", "21:00"]
    time_dropdown = OptionMenu(reservation_window, time_option, *time_options)
    time_dropdown.config(font=("Times New Roman", 18),
                         bg="#F5E9C7",
                         fg="black",
                         activebackground="#F5E9C7",
                         activeforeground="black")
    time_dropdown.place(x=710, y=450)

    people_label = Label(reservation_window, text="People:",
                       bg="#F5E9C7",
                       fg="black",
                       font=("Times New Roman", 25), bd=3,
                       )
    people_label.place(x=600, y=500)

    people_option = tkinter.StringVar()
    people_option.set("1")
    peoples = [str(i) for i in range(1, 13)]

    under4s_label = Label(reservation_window, text="Under 4's:",
                       bg="#F5E9C7",
                       fg="black",
                       font=("Times New Roman", 25), bd=3,
                       )
    under4s_label.place(x=565, y=550)

    under4s_option = tkinter.StringVar()
    under4s_option.set("0")
    under4s_dropdown = OptionMenu(reservation_window, under4s_option, "0")
    under4s_dropdown.config(font=("Times New Roman", 18),
                            bg="#F5E9C7",
                            fg="black",
                            activebackground="#F5E9C7",
                            activeforeground="black")
    under4s_dropdown.place(x=710, y=550)

    def people_under4s(*args):
        menu = under4s_dropdown["menu"]
        menu.delete(0, 'end')
        if people_option.get().isdigit():
            for i in range(int(people_option.get())):
                menu.add_command(label=str(i), command=lambda value=str(i): under4s_option.set(value))

    people_dropdown = OptionMenu(reservation_window, people_option, *peoples, command=people_under4s)
    people_dropdown.config(font=("Times New Roman", 18),
                           bg="#F5E9C7", fg="black",
                           activebackground="#F5E9C7",
                           activeforeground="black")
    people_dropdown.place(x=710, y=500)

    captcha_text = {"value": ""}
    captcha_label = Label(reservation_window)
    captcha_label.place(x=710, y=598)

    characters_label = Label(reservation_window,
                             text="Characters: ",
                             bg="#F5E9C7",
                             fg="black",
                             font=("Times New Roman", 25),
                             bd=3, )
    characters_label.place(x=540, y=680)
    captcha_entry = Entry(reservation_window, font=("Arial", 19))
    captcha_entry.place(x=710, y=685)

    def generate_captcha():
        letters = string.ascii_uppercase + string.digits
        text = "".join(random.choices(letters, k=5))
        captcha_text["value"] = text
        captcha = ImageCaptcha(width=200, height=80, font_sizes=(20, 30, 40, 50, 60))
        image_data = captcha.generate(text)
        image = Image.open(image_data).convert("RGB")
        image_tk = ImageTk.PhotoImage(image)
        captcha_label.configure(image=image_tk)
        captcha_label.image = image_tk

    def confirm_reservation():
        name = name_entry.get().strip()
        number = number_entry.get().strip()
        raw_date = cal.get_date()
        calendar_date = datetime.strptime(raw_date, "%m/%d/%y").strftime("%Y-%m-%d")
        time = time_option.get()
        people = people_option.get()
        under4s = under4s_option.get()
        captcha_input = captcha_entry.get().strip().upper()

        calendar_date

        for widget in reservation_window.place_slaves():
            if isinstance(widget, Label):
                text = widget.cget("text")
                if text.startswith("Please") or "Error" in text or "successfully" in text:
                    widget.destroy()


        if not all([name, number, calendar_date, time, people, under4s]):
            input_error = Label(reservation_window, text="Input Error: All fields required", fg="black", bg="#F5E9C7",
                  font=("Arial", 16))
            input_error.place(x=650, y=750)
            reservation_window.after(3000,input_error.destroy)
            return

        if len(str(number)) != 11:
            input_error = Label(reservation_window, text="Input Error: Invalid Number", fg="black", bg="#F5E9C7",
                                font=("Arial", 16))
            input_error.place(x=650, y=750)
            reservation_window.after(3000, input_error.destroy)
            return

        if captcha_input != captcha_text["value"]:
            incorrect_captcha = Label(reservation_window, text="Incorrect Captcha", fg="black", bg="#F5E9C7", font=("Arial", 16))
            incorrect_captcha.place(x=650, y=750)
            reservation_window.after(3000,incorrect_captcha.destroy)
            captcha_entry.delete(0, tkinter.END)
            generate_captcha()

            return

        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Reservation_details (
                    Name TEXT,
                    Number TEXT,
                    Date TEXT,
                    Time TEXT,
                    People TEXT,
                    Under4s TEXT
                )
            """)
            cursor.execute(
                "INSERT INTO Reservation_details (Name, Number, Date, Time, People, Under4s) VALUES (?, ?, ?, ?, ?, ?)",
                (name, number, calendar_date, time, people, under4s)
            )
            conn.commit()

            if number.startswith("0"):
                send_number = "+44" + number[1:]
            elif not number.startswith("+"):
                send_number = "+44" + number
            else:
                send_number = number

            account_sid = "ACf01f6ff1a8c26bebd2e5c8ef02c6df27"
            auth_token = "8bed64fdcdfb72c361c1be476988f74c"
            client = Client(account_sid, auth_token)

            try:
                client.messages.create(
                    body=f"Hi {name}, your reservation for {calendar_date} at {time} has been confirmed for {people} people (Under 4s: {under4s}).",
                    from_="+447882964553",
                    to=send_number
                )

                client.messages.create(
                    body=f"New Reservation:\nName: {name}\nNumber: {number}\nDate: {calendar_date}\nTime: {time}\nPeople: {people}\nUnder 4s: {under4s}",
                    from_="+447882964553",
                    to="+447305123119"
                )

                sms_label = Label(reservation_window,
                                  text="Reservation Confirmed & Confirmation SMS Sent!",
                                  fg="black", bg="#F5E9C7",
                                  font=("Arial", 16))
                sms_label.place(x=650, y=750)
                reservation_window.after(3000, sms_label.destroy)
            except Exception as sms_error:
                error_label = Label(reservation_window,
                                    text=f"Reservation saved, but Corfirmation SMS failed.",
                                    fg="black", bg="#F5E9C7",
                                    font=("Arial", 16))
                error_label.place(x=550, y=750)
                reservation_window.after(3000, error_label.destroy)


            name_entry.delete(0, tkinter.END)
            number_entry.delete(0, tkinter.END)
            captcha_entry.delete(0, tkinter.END)
            generate_captcha()

        except Exception as e:
            confirm_error = Label(reservation_window, text=f"Unable to confirm reservation: {e}", fg="black", bg="#F5E9C7",
                  font=("Arial", 16))
            confirm_error.place(x=650, y=750)
            reservation_window.after(3000,confirm_error.destroy)

    reserve_button = customtkinter.CTkButton(reservation_window,
                                            text="Confirm",
                                            bg_color="#F5E9C7",
                                            fg_color="black",
                                            font=("Georgia Pro", 20),
                                            command=confirm_reservation,
                                            corner_radius=70,
                                            text_color="#F5E9C7")
    reserve_button.place(x=710, y=720)

    generate_captcha()



def cancelation():
    main_window.withdraw()
    cancelation_window = tkinter.Toplevel()
    cancelation_window.geometry("1920x1080")
    cancelation_window.title("Main menu")

    cancelation_window.title("Cancelation")
    cancelation_window.geometry("1920x1080")

    conn = sqlite3.connect("Penash.db")
    cursor = conn.cursor()

    background_label = Label(cancelation_window,
                             text="",
                             bg="#F5E9C7",
                             width=77,
                             height=100,
                             )
    background_label.place(x=500, y=129)

    icon = PhotoImage(file='logo.png')
    cancelation_window.iconphoto(True, icon)

    cancel_title = Image.open("title.png")
    cancel_title = cancel_title.resize((1528, 125))
    cancel_title = ImageTk.PhotoImage(cancel_title)

    cancel_title_label = Label(cancelation_window, image=cancel_title, borderwidth=0)
    cancel_title_label.image = cancel_title
    cancel_title_label.place(x=0, y=5)

    def main():
        cancelation_window.destroy()
        main_window.deiconify()

    main_menu_button = customtkinter.CTkButton(cancelation_window,
                                           text="Main Menu",
                                           bg_color="#F5E9C7",
                                           fg_color="black",
                                           font=("Georgia Pro", 20),
                                           command=main,
                                           corner_radius=70,
                                           text_color="#F5E9C7")

    main_menu_button.place(x=1376, y=130)

    left_images = [
        ImageTk.PhotoImage(Image.open("curry.jpg").resize((500, 700))),
        ImageTk.PhotoImage(Image.open("curry_2.jpg").resize((500, 700))),
        ImageTk.PhotoImage(Image.open("naan.jpg").resize((500, 700)))
    ]

    right_images = [
        ImageTk.PhotoImage(Image.open("lollipop.jpg").resize((500, 700))),
        ImageTk.PhotoImage(Image.open("panner.PNG").resize((500, 700))),
        ImageTk.PhotoImage(Image.open("biryani.jpg").resize((500, 700)))
    ]

    # Create iterators
    left_iter = cycle(left_images)
    right_iter = cycle(right_images)

    # Place labels
    left_label = Label(cancelation_window, borderwidth=0)
    left_label.place(x=0, y=100, anchor="nw")
    left_label.lower()

    right_label = Label(cancelation_window, borderwidth=0)
    right_label.place(relx=1.0, y=100, anchor="ne")
    right_label.lower()

    # Track jobs so we can cancel them later
    left_job = None
    right_job = None

    def change_left():
        """Update left image every 10s"""
        global left_job
        if left_label.winfo_exists():
            img = next(left_iter)
            left_label.config(image=img)
            left_label.image = img
            left_job = main_window.after(10000, change_left)

    def change_right():
        """Update right image every 10s"""
        global right_job
        if right_label.winfo_exists():
            img = next(right_iter)
            right_label.config(image=img)
            right_label.image = img
            right_job = main_window.after(10000, change_right)

    # Start slideshow
    change_left()
    change_right()

    def on_close():
        """Cancel jobs and close the window safely"""
        global left_job, right_job
        if left_job:
            main_window.after_cancel(left_job)
            left_job = None
        if right_job:
            main_window.after_cancel(right_job)
            right_job = None
        cancelation_window.destroy()

    # Override window close button
    cancelation_window.protocol("WM_DELETE_WINDOW", on_close)

    name_label = Label(cancelation_window,
                       text="Name:",  # creating a label for where they can enter their name
                       bg="#F5E9C7",
                       fg="black",
                       font=("Times New Roman", 25),
                       bd=3,
                       )
    name_label.place(x=600, y=150)

    name_entry = Entry(cancelation_window,
                       text="", font=("Arial", 19))
    name_entry.place(x=710, y=155)

    number_label = Label(cancelation_window,
                         text="Number:",  # creating a label for where they can enter their name
                         bg="#F5E9C7",
                         fg="black",
                         font=("Times New Roman", 25),
                         bd=3,
                         )
    number_label.place(x=575, y=225)

    number_entry = Entry(cancelation_window,
                         text="", font=("Arial", 19))
    number_entry.place(x=710, y=230)

    date_label = Label(cancelation_window,
                       text="Date:",  # creating a label for where they can enter the date they booked for
                       bg="#F5E9C7",
                       fg="black",
                       font=("Times New Roman", 25),
                       bd=3,
                       )
    date_label.place(x=620, y=300)

    tomorrow = date.today() + timedelta(days=1)
    max_date = date.today() + timedelta(days=30)

    calender = Calendar(cancelation_window, selectmode='day', year=2025, month=3, day=24,
                   mindate=tomorrow,
                   maxdate=max_date,
                   background="#F5E9C7",
                   foreground="black",
                   bordercolor="black",
                   headersbackground="#F5E9C7",
                   headersforeground="black",
                   selectbackground="#F5E9C7",
                   selectforeground="black", )
    calender.place(x=710, y=300)

    captcha_text = {"value": ""}

    def generate_captcha():
        letters = string.ascii_uppercase + string.digits
        text = "".join(random.choices(letters, k=5))
        captcha_text["value"] = text

        captcha = ImageCaptcha(width=200, height=80, font_sizes=(20, 30, 40, 50, 60))
        image_data = captcha.generate(text)
        image = Image.open(image_data).convert("RGB")
        image_tk = ImageTk.PhotoImage(image)

        captcha_label.configure(image=image_tk)
        captcha_label.image = image_tk

    captcha_label = Label(cancelation_window)
    captcha_label.place(x=710, y=490)

    characters_label = Label(cancelation_window, text="Characters: ",
                             bg="#F5E9C7",
                             fg="black",
                             font=("Times New Roman", 25),
                             bd=3,
                             )
    characters_label.place(x=540, y=580)

    captcha_entry = Entry(cancelation_window, font=("Arial", 19))
    captcha_entry.place(x=710, y=580)

    def cancel_reservation():
        name = name_entry.get().strip()
        number = number_entry.get().strip()
        calendar_date_raw = calender.get_date()
        try:
            calendar_date = datetime.strptime(calendar_date_raw, "%m/%d/%y").strftime("%Y-%m-%d")
        except ValueError:
            # if the calendar returns already in YYYY-MM-DD format
            calendar_date = calendar_date_raw
        captcha_input = captcha_entry.get().strip().upper()

        for widget in cancelation_window.place_slaves():
            if isinstance(widget, Label):
                text = widget.cget("text")
                if text.startswith("Please") or "Error" in text or "successfully" in text:
                    widget.destroy()

        if not all([name, number, calendar_date]):
            incorrect_label = Label(cancelation_window, text="Please fill in all fields", fg="black", bg="#F5E9C7",
                  font=("Arial", 16))
            incorrect_label.place(x=650, y=750)

            cancelation_window.after(3000,incorrect_label.destroy)
            return

        if len(str(number)) != 11:
            input_error = Label(cancelation_window, text="Input Error: Invalid Number", fg="black", bg="#F5E9C7",
                                font=("Arial", 16))
            input_error.place(x=650, y=750)
            cancelation_window.after(3000, input_error.destroy)
            return

        if captcha_input != captcha_text["value"]:
            incorrect_captcha = Label(cancelation_window, text="Incorrect Captcha", fg="black", bg="#F5E9C7", font=("Arial", 16))
            incorrect_captcha.place(x=650, y=750)
            cancelation_window.after(3000,incorrect_captcha.destroy)
            captcha_entry.delete(0, tkinter.END)
            generate_captcha()
            return

        try:
            cursor.execute("SELECT * FROM Reservation_details WHERE name = ? AND number = ? AND date = ?",
                           (name, number, calendar_date))
            result = cursor.fetchone()

            if result:
                cursor.execute("DELETE FROM Reservation_details WHERE name = ? AND number = ? AND date = ?",
                               (name, number, calendar_date))
                conn.commit()
                success_Label = (Label(cancelation_window, text="Reservation cancelled successfully!", fg="black", bg="#F5E9C7",
                      font=("Arial", 16)))
                success_Label.place(x=650, y=700)
                cancelation_window.after(3000,success_Label.destroy)
            else:
                reservation_error = Label(cancelation_window, text="No matching reservation found.", fg="black", bg="#F5E9C7",
                      font=("Arial", 16))
                reservation_error.place(x=650, y=750)
                cancelation_window.after(3000,reservation_error.destroy)

        except Exception as e:
            database_error = Label(cancelation_window, text=f"Database Error: {e}", fg="black", bg="#F5E9C7",
                  font=("Arial", 16))
            database_error.place(x=650, y=750)
            cancelation_window.after(3000,database_error.destroy)

        name_entry.delete(0, tkinter.END)
        number_entry.delete(0, tkinter.END)
        captcha_entry.delete(0, tkinter.END)
        generate_captcha()

    cancel_button = customtkinter.CTkButton(cancelation_window,
                                             text="Confirm",
                                             bg_color="#F5E9C7",
                                             fg_color="black",
                                             font=("Georgia Pro", 20),
                                             command=cancel_reservation,
                                             corner_radius=70,
                                             text_color="#F5E9C7")
    cancel_button.place(x=710,y=650)

    generate_captcha()

icon = PhotoImage(file='logo.png')
main_window.iconphoto(True, icon)

main_title = Image.open("title.png")
main_title = main_title.resize((1528,125))
main_title = ImageTk.PhotoImage(main_title)

title_label = Label(main_window, image=main_title,
                   borderwidth=0,
                   )
title_label.place(x=0, y=5)

background_label = Label(main_window,
                        text="",
                        bg="#F5E9C7",
                        width=77,
                        height=100,
                        )
background_label.place(x=500, y=129)

reservation_button = customtkinter.CTkButton(main_window,
                                       text="Book a table",
                                       bg_color="#F5E9C7",
                                       fg_color="black",
                                       font=("Georgia Pro", 60),
                                       command=reservation,
                                       corner_radius=70,
                                       text_color="#F5E9C7")
reservation_button.place(x=600,y=200)

cancel_reservation_button = customtkinter.CTkButton(main_window,
                                       text="Cancel a table",
                                       bg_color="#F5E9C7",
                                       fg_color="black",
                                       font=("Georgia Pro", 60),
                                       command=cancelation,
                                       corner_radius=70,
                                       text_color="#F5E9C7")
cancel_reservation_button.place(x=580,y=400)

login_button = customtkinter.CTkButton(main_window,
                                       text="Login",
                                       bg_color="#F5E9C7",
                                       fg_color="black",
                                       font=("Georgia Pro", 60),
                                       command=login,
                                       corner_radius=70,
                                       text_color="#F5E9C7")
login_button.place(x=680,y=600)

left_images = [
    ImageTk.PhotoImage(Image.open("curry.jpg").resize((500, 700))),
    ImageTk.PhotoImage(Image.open("curry_2.jpg").resize((500, 700))),
    ImageTk.PhotoImage(Image.open("naan.jpg").resize((500, 700)))
]

right_images = [
    ImageTk.PhotoImage(Image.open("lollipop.jpg").resize((500, 700))),
    ImageTk.PhotoImage(Image.open("panner.PNG").resize((500, 700))),
    ImageTk.PhotoImage(Image.open("biryani.jpg").resize((500, 700)))
]

left_iter = cycle(left_images)
right_iter = cycle(right_images)

left_label = Label(main_window, borderwidth=0)
left_label.place(x=0, y=100, anchor="nw")
left_label.lower()

right_label = Label(main_window,borderwidth=0)
right_label.place(relx=1.0, y=100, anchor="ne")
right_label.lower()

def change_left():
    img = next(left_iter)
    left_label.config(image=img)
    left_label.image = img
    main_window.after(5000, change_left)

def change_right():
    img = next(right_iter)
    right_label.config(image=img)
    right_label.image = img
    main_window.after(5000, change_right)

change_left()
change_right()

main_window.mainloop()

conn.close()