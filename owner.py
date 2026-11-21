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

conn = sqlite3.connect("Penash.db")
cursor = conn.cursor()

owner_window = Tk()
owner_window.geometry("1920x1080")
owner_window.title("Owner")

icon = PhotoImage(file='logo.png')
owner_window.iconphoto(True, icon)

background = Label(owner_window, bg='#981e2b', height=900, width=75)
background.place(x=500, y=100)

heading_reservation = Label(
    owner_window,
    text="Penash The Indian Restaurant                   ",
    bg="#981e2b",
    fg="white",
    font=("Times New Roman", 70),
    bd=3,
    relief=SUNKEN
)
heading_reservation.place(x=-3, y=0)

location_reservation = Label(
    owner_window,
    text="Durham \n Croxdale \n Croxdale Inn \n DH6 5HX",
    bg="#981e2b",
    fg="white",
    font=("Times New Roman", 16)
)
location_reservation.place(x=1150, y=5)

owner_window.photo_logo = PhotoImage(file="logo.png")
logo_label = Label(owner_window, image=owner_window.photo_logo)
logo_label.place(x=1350, y=5)

def main():
    owner_window.destroy()
    main_window.deiconify()

main_menu_button = Button(
    owner_window,
    text="Main Menu",
    command=main,
    font=("Times New Roman", 20),
    activebackground="#981e2b",
    bg="#981e2b",
    activeforeground="white",
    fg="white"
)
main_menu_button.place(x=1376, y=115)

owner_label = Label(
    owner_window,
    text="Owner",
    bg="#981e2b",
    fg="white",
    font=("Times New Roman", 30),
    bd=3,
    relief=SUNKEN
)
owner_label.place(x=700, y=150)

def today():
    owner_window.withdraw()
    today_window = Toplevel()
    today_window.geometry("1920x1080")
    today_window.title("today")

    icon = PhotoImage(file='logo.png')
    owner_window.iconphoto(True, icon)

    background = Label(today_window, bg='#981e2b', height=900, width=75)
    background.place(x=500, y=100)

    heading_reservation = Label(
        today_window,
        text="Penash The Indian Restaurant                   ",
        bg="#981e2b",
        fg="white",
        font=("Times New Roman", 70),
        bd=3,
        relief=SUNKEN
    )
    heading_reservation.place(x=-3, y=0)

    location_reservation = Label(
        today_window,
        text="Durham \n Croxdale \n Croxdale Inn \n DH6 5HX",
        bg="#981e2b",
        fg="white",
        font=("Times New Roman", 16)
    )
    location_reservation.place(x=1150, y=5)

    today_window.photo_logo = PhotoImage(file="logo.png")
    logo_label = Label(today_window, image=today_window.photo_logo)
    logo_label.place(x=1350, y=5)

    conn = sqlite3.connect("Penash.db")
    cursor = conn.cursor()

    today_date = date.today().strftime("%#y/%#m/%#d")

    cursor.execute("SELECT * FROM Reservation_details WHERE Date = ?", (today_date,))
    rows = cursor.fetchall()

    # Create a Frame to hold the table
    grid_frame = Frame(today_window, bg="#981e2b")
    grid_frame.place(x=500, y=250)

    headers = ["Name", "Number", "Date", "Time", "People", "Under 4s"]

    for col, header in enumerate(headers):
        table_header = Label(grid_frame, text=header, font=("Times New Roman", 13, "bold"),
                             bg="#981e2b", fg="White", padx=10, pady=5)
        table_header.grid(row=0, column=col, padx=5, pady=5)

    for row_num, row_data in enumerate(rows, start=1):
        for col_num, cell_data in enumerate(row_data):
            data_label = Label(grid_frame, text=str(cell_data), font=("Times New Roman", 12),
                               bg="#981e2b", fg="White", padx=10, pady=5)
            data_label.grid(row=row_num, column=col_num, padx=5, pady=5)

    today_header = Label(today_window, text="Today's Reservations", font=("Times New Roman", 24), bg="#981e2b",
                   fg="white")
    today_header.place(x=600, y=180)

    def main():
        today_window.destroy()
        main_window.deiconify()

    def back():
        today_window.destroy()
        owner_window.deiconify()

    back_button = Button(
        today_window,
        text="Back",
        command=back,
        font=("Times New Roman", 20),
        activebackground="#981e2b",
        bg="#981e2b",
        activeforeground="white",
        fg="white"
    )
    back_button.place(x=0, y=115)

    main_menu_button = Button(
        today_window,
        text="Main Menu",
        command=main,
        font=("Times New Roman", 20),
        activebackground="#981e2b",
        bg="#981e2b",
        activeforeground="white",
        fg="white"
    )
    main_menu_button.place(x=1376, y=115)

    conn.close()


today_button = Button(owner_window,text = "Reservations \n for today",
                      font=("Times New Roman", 20),
                      activebackground="#981e2b",
                      bg="#981e2b",
                      activeforeground="white",
                      fg="white",
                      command= today
                      )
today_button.place (x = 677,y=250)

def all_reservations():
    owner_window.withdraw()
    All_window = tkinter.Toplevel()
    All_window.geometry("1920x1080")
    All_window.title("All Reservations")

    icon = PhotoImage(file='logo.png')
    All_window.iconphoto(True, icon)

    background = Label(All_window, bg='#981e2b', height=900, width=75)
    background.place(x=500, y=100)

    heading_reservation = Label(
        All_window,
        text="Penash The Indian Restaurant                   ",
        bg="#981e2b",
        fg="white",
        font=("Times New Roman", 70),
        bd=3,
        relief=SUNKEN
    )
    heading_reservation.place(x=-3, y=0)

    location_reservation = Label(
        All_window,
        text="Durham \n Croxdale \n Croxdale Inn \n DH6 5HX",
        bg="#981e2b",
        fg="white",
        font=("Times New Roman", 16)
    )
    location_reservation.place(x=1150, y=5)

    All_window.photo_logo = PhotoImage(file="logo.png")
    logo_label = Label(All_window, image=All_window.photo_logo)
    logo_label.place(x=1350, y=5)

    def main():
        All_window.destroy()
        main_window.deiconify()

    def back():
        All_window.destroy()
        owner_window.deiconify()

    back_button = Button(
        All_window,
        text="Back",
        command=back,
        font=("Times New Roman", 20),
        activebackground="#981e2b",
        bg="#981e2b",
        activeforeground="white",
        fg="white"
    )
    back_button.place(x=0, y=115)

    conn = sqlite3.connect("Penash.db")
    cursor = conn.cursor()

    tommorow_date = (date.today() + timedelta(days=1)).strftime('%Y-%m-%d')

    cursor.execute("SELECT * FROM Reservation_details WHERE Date >= ?", (tommorow_date,))
    rows = cursor.fetchall()

    # Create a Frame to hold the table
    grid_frame = Frame(All_window, bg="#981e2b")
    grid_frame.place(x=500, y=250)

    headers = ["Name", "Number", "Date", "Time", "People", "Under 4s"]

    for col, header in enumerate(headers):
        table_header = Label(grid_frame, text=header, font=("Times New Roman", 13, "bold"),
                             bg="#981e2b", fg="White", padx=10, pady=5)
        table_header.grid(row=0, column=col, padx=5, pady=5)

    for row_num, row_data in enumerate(rows, start=1):
        for col_num, cell_data in enumerate(row_data):
            data_label = Label(grid_frame, text=str(cell_data), font=("Times New Roman", 12),
                               bg="#981e2b", fg="White", padx=10, pady=5)
            data_label.grid(row=row_num, column=col_num, padx=5, pady=5)

    today_header = Label(All_window, text="Tomorrow's Reservations", font=("Times New Roman", 24), bg="#981e2b",
                         fg="white")
    today_header.place(x=600, y=180)

    main_menu_button = Button(
        All_window,
        text="Main Menu",
        command=main,
        font=("Times New Roman", 20),
        activebackground="#981e2b",
        bg="#981e2b",
        activeforeground="white",
        fg="white"
    )
    main_menu_button.place(x=1376, y=115)



previous_reservations = Button(owner_window,text = "reservations \n for future",
                       font=("Times New Roman", 20),
                       activebackground="#981e2b",
                       bg="#981e2b",
                       activeforeground="white",
                       fg="white",
                       command=all_reservations)
previous_reservations.place(x=680,y=350)

def staff():
    owner_window.withdraw()
    staff_window = tkinter.Toplevel()
    staff_window.geometry("1920x1080")
    staff_window.title("Staff")

    def add():
        owner_window.withdraw()
        add_window = tkinter.Toplevel()
        add_window.geometry("1920x1080")
        add_window.title("Add Staff")

        icon = PhotoImage(file='logo.png')
        staff_window.iconphoto(True, icon)

        background = Label(add_window, bg='#981e2b', height=900, width=75)
        background.place(x=500, y=100)

        heading_reservation = Label(
            add_window,
            text="Penash The Indian Restaurant                   ",
            bg="#981e2b",
            fg="white",
            font=("Times New Roman", 70),
            bd=3,
            relief=SUNKEN
        )
        heading_reservation.place(x=-3, y=0)

        location_reservation = Label(
            add_window,
            text="Durham \n Croxdale \n Croxdale Inn \n DH6 5HX",
            bg="#981e2b",
            fg="white",
            font=("Times New Roman", 16)
        )
        location_reservation.place(x=1150, y=5)

        add_window.photo_logo = PhotoImage(file="logo.png")
        logo_label = Label(add_window, image=add_window.photo_logo)
        logo_label.place(x=1350, y=5)

        def main():
            add_window.destroy()
            main_window.deiconify()

        def back():
            add_window.destroy()
            staff_window.deiconify()

        back_button = Button(
            add_window,
            text="Back",
            command=back,
            font=("Times New Roman", 20),
            activebackground="#981e2b",
            bg="#981e2b",
            activeforeground="white",
            fg="white"
        )
        back_button.place(x=0, y=115)

        main_menu_button = Button(
            add_window,
            text="Main Menu",
            command=main,
            font=("Times New Roman", 20),
            activebackground="#981e2b",
            bg="#981e2b",
            activeforeground="white",
            fg="white"
        )
        main_menu_button.place(x=1376, y=115)

        staff_name_label = Label(add_window,text="Name: ",
                            bg = "#981e2b",
                            fg = "white",
                            font = ("Times New Roman", 20), bd = 3,
                            relief = RIDGE
                            )
        staff_name_label.place(x = 550,y=200)

        staff_name_entry = Entry(add_window, font=("Arial", 19))
        staff_name_entry.place(x=680, y=200
                               )
        staff_number_label = Label(add_window,text="Number: ",
                                 bg="#981e2b",
                                 fg="white",
                                 font=("Times New Roman", 20), bd=3,
                                 relief=RIDGE
                                 )
        staff_number_label.place(x=550, y=250)

        staff_number_entry = Entry(add_window, font=("Arial", 19))
        staff_number_entry.place(x=680, y=250)

        staff_username_label = Label(add_window,text="Username: ",
                                 bg="#981e2b",
                                 fg="white",
                                 font=("Times New Roman", 20), bd=3,
                                 relief=RIDGE
                                 )
        staff_username_label.place(x=550, y=300)

        staff_username_entry = Entry(add_window, font=("Arial", 19))
        staff_username_entry.place(x=680, y=300)

        staff_password_label = Label(add_window,text="Password: ",
                                 bg="#981e2b",
                                 fg="white",
                                 font=("Times New Roman", 20), bd=3,
                                 relief=RIDGE
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
                    Label(
                        add_window,
                        text="Input Error: All fields required",
                        fg="white",
                        bg="#981e2b",
                        font=("Arial", 16)
                    ).place(x=200, y=500)
                    print("Please fill in all inputs")
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
                    print("Insert successful")

                    Label(add_window, text="Data inserted successfully!", fg="white", bg="#981e2b",
                          font=("Arial", 16)).place(x=200, y=500)

                    staff_name_entry.delete(0, tkinter.END)
                    staff_number_entry.delete(0, tkinter.END)
                    staff_username_entry.delete(0, tkinter.END)
                    staff_password_entry.delete(0, tkinter.END)

                except Exception as e:
                    Label(add_window, text=f"Error inserting data: {e}", fg="white", bg="#981e2b",
                          font=("Arial", 16)).place(x=200, y=500)

        staff_add_button = Button(add_window,
                                     text="Add Staff",
                                     font=("Times New Roman", 20),
                                     activebackground="#981e2b",
                                     bg="#981e2b",
                                     activeforeground="white",
                                     fg="white",
                                     command=Add_staff)
        staff_add_button.place(x=675, y=450)


    def delete():
        owner_window.withdraw()
        delete_window = tkinter.Toplevel()
        delete_window.geometry("1920x1080")
        delete_window.title("Delete Staff")

        icon = PhotoImage(file='logo.png')
        delete_window.iconphoto(True, icon)

        background = Label(delete_window, bg='#981e2b', height=900, width=75)
        background.place(x=500, y=100)

        heading_reservation = Label(
            delete_window,
            text="Penash The Indian Restaurant                   ",
            bg="#981e2b",
            fg="white",
            font=("Times New Roman", 70),
            bd=3,
            relief=SUNKEN
        )
        heading_reservation.place(x=-3, y=0)

        location_reservation = Label(
            delete_window,
            text="Durham \n Croxdale \n Croxdale Inn \n DH6 5HX",
            bg="#981e2b",
            fg="white",
            font=("Times New Roman", 16)
        )
        location_reservation.place(x=1150, y=5)

        delete_window.photo_logo = PhotoImage(file="logo.png")
        logo_label = Label(delete_window, image=delete_window.photo_logo)
        logo_label.place(x=1350, y=5)

        def main():
            delete_window.destroy()
            main_window.deiconify()

        def back():
            delete_window.destroy()
            staff_window.deiconify()

        back_button = Button(
            delete_window,
            text="Back",
            command=back,
            font=("Times New Roman", 20),
            activebackground="#981e2b",
            bg="#981e2b",
            activeforeground="white",
            fg="white"
        )
        back_button.place(x=0, y=115)

        main_menu_button = Button(
            delete_window,
            text="Main Menu",
            command=main,
            font=("Times New Roman", 20),
            activebackground="#981e2b",
            bg="#981e2b",
            activeforeground="white",
            fg="white"
        )
        main_menu_button.place(x=1376, y=115)

        staff_name_label = Label(delete_window, text="Name: ",
                                 bg="#981e2b",
                                 fg="white",
                                 font=("Times New Roman", 20), bd=3,
                                 relief=RIDGE
                                 )
        staff_name_label.place(x=550, y=200)

        staff_name_entry = Entry(delete_window, font=("Arial", 19))
        staff_name_entry.place(x=680, y=200)

        staff_number_label = Label(delete_window, text="Number: ",
                             bg="#981e2b",
                             fg="white",
                             font=("Times New Roman", 20), bd=3,
                             relief=RIDGE
                             )
        staff_number_label.place(x=550, y=250)

        staff_number_entry = Entry(delete_window, font=("Arial", 19))
        staff_number_entry.place(x=680, y=250)

        def delete_staff():
            name = staff_name_entry.get().strip()
            number = staff_number_entry.get().strip()

            if not name or not number:
                print("Please enter both name and number.")
                return

            cursor.execute("SELECT * FROM Staff_details WHERE name = ? AND number = ?", (name, number))
            result = cursor.fetchone()

            if result:
                cursor.execute("DELETE FROM Staff_details WHERE Name = ? AND Number = ?", (name, number))
                conn.commit()
                print("User deleted successfully.")
            else:
                print("No matching user found.")

        staff_delete_button = Button(delete_window,
                                     text="Delete Staff",
                                     font=("Times New Roman", 20),
                                     activebackground="#981e2b",
                                     bg="#981e2b",
                                     activeforeground="white",
                                     fg="white",
                                     command=delete_staff)
        staff_delete_button.place(x=675,y=350)

    icon = PhotoImage(file='logo.png')
    staff_window.iconphoto(True, icon)

    background = Label(staff_window, bg='#981e2b', height=900, width=75)
    background.place(x=500, y=100)

    heading_reservation = Label(
        staff_window,
        text="Penash The Indian Restaurant                   ",
        bg="#981e2b",
        fg="white",
        font=("Times New Roman", 70),
        bd=3,
        relief=SUNKEN
    )
    heading_reservation.place(x=-3, y=0)

    location_reservation = Label(
        staff_window,
        text="Durham \n Croxdale \n Croxdale Inn \n DH6 5HX",
        bg="#981e2b",
        fg="white",
        font=("Times New Roman", 16)
    )
    location_reservation.place(x=1150, y=5)

    staff_window.photo_logo = PhotoImage(file="logo.png")
    logo_label = Label(staff_window, image=staff_window.photo_logo)
    logo_label.place(x=1350, y=5)

    def main():
        staff_window.destroy()
        main_window.deiconify()

    def back():
        staff_window.destroy()
        owner_window.deiconify()

    back_button = Button(
        staff_window,
        text="Back",
        command=back,
        font=("Times New Roman", 20),
        activebackground="#981e2b",
        bg="#981e2b",
        activeforeground="white",
        fg="white"
    )
    back_button.place(x=0, y=115)

    main_menu_button = Button(
        staff_window,
        text="Main Menu",
        command=main,
        font=("Times New Roman", 20),
        activebackground="#981e2b",
        bg="#981e2b",
        activeforeground="white",
        fg="white"
    )

    main_menu_button.place(x=1376, y=115)

    add_button = Button(staff_window, text="Add Staff",
                          font=("Times New Roman", 20),
                          activebackground="#981e2b",
                          bg="#981e2b",
                          activeforeground="white",
                          fg="white",
                          command=add
                          )
    add_button.place(x=680, y=350)

    delete_button = Button(staff_window, text="Delete Staff",
                          font=("Times New Roman", 20),
                          activebackground="#981e2b",
                          bg="#981e2b",
                          activeforeground="white",
                          fg="white",
                          command=delete
                           )
    delete_button.place(x=680, y=450)


staff_button = Button(owner_window,text = "Manage staff",
                      font=("Times New Roman", 20),
                      activebackground="#981e2b",
                      bg="#981e2b",
                      activeforeground="white",
                      fg="white",
                      command=staff
                      )
staff_button.place(x=680,y=450)

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
    predictions_window = tk.Toplevel()
    predictions_window.geometry("1920x1080")
    predictions_window.title("Staff")

    # Set icon and background color
    icon = PhotoImage(file='logo.png')
    predictions_window.iconphoto(True, icon)
    bg_color = "#981e2b"
    tk.Label(predictions_window, bg=bg_color, height=900, width=75).place(x=500, y=100)

    # Header labels
    heading_label = (Label(predictions_window, text="Penash The Indian Restaurant                 ", bg=bg_color, fg="white",
             font=("Times New Roman", 70), bd=3, relief=SUNKEN))
    heading_label.place(x=-3, y=0)

    location_label= Label(predictions_window, text="Durham \n Croxdale \n Croxdale Inn \n DH6 5HX", bg=bg_color, fg="white",
             font=("Times New Roman", 16))
    location_label.place(x=1150, y=5)

    # Logo image
    predictions_window.photo_logo = PhotoImage(file="logo.png")
    logo = (Label(predictions_window, image=predictions_window.photo_logo))
    logo.place(x=1350, y=5)

    # Buttons to go back or main menu
    def back():
        predictions_window.destroy()
        owner_window.deiconify()

    def main():
        predictions_window.destroy()
        main_window.deiconify()

    back_button = (Button(predictions_window, text="Back", command=back, font=("Times New Roman", 20),
              bg=bg_color, fg="white", activebackground=bg_color, activeforeground="white"))
    back_button.place(x=0, y=115)

    main_menu_button = Button(predictions_window, text="Main Menu", command=main, font=("Times New Roman", 20),
              bg=bg_color, fg="white", activebackground=bg_color, activeforeground="white")
    main_menu_button.place(x=1376, y=115)

    bg_color = "#981e2b"

    def load_dates():
        conn = sqlite3.connect("Penash.db")
        cursor = conn.cursor()
        cursor.execute("SELECT Date FROM Reservation_details")
        raw_dates = [row[0] for row in cursor.fetchall()]
        conn.close()

        dates = []
        date_format = "%Y-%m-%d"  # Change if needed to match your database format
        for d in raw_dates:
            try:
                dates.append(datetime.strptime(d, date_format).date())
            except Exception:
                invalid_date = Label(text = "invalid dates", bg=bg_color, fg="white",
             font=("Times New Roman", 16))
                invalid_date.place(x=200,y=150)
        return dates

    def create_plot(dates):
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
        plt.plot(sorted_dates, counts_list, label="Historical Reservations", marker='o')
        plt.plot(future_dates, predictions, label="Predicted Reservations (Next 4 Weeks)", linestyle='--', marker='x')
        plt.title("Reservation Counts: Historical and Predicted")
        plt.xlabel("Date")
        plt.ylabel("Number of Reservations")
        plt.xticks(rotation=45)
        plt.legend()
        plt.grid(True)
        plt.tight_layout()

        return fig, future_dates, predictions

    def show_prediction_table(parent, future_dates, predicted_counts):
        tree = ttk.Treeview(parent, columns=("Date", "Predicted Reservations"), show='headings', height=12)
        tree.heading("Date", text="Date")
        tree.heading("Predicted Reservations", text="Predicted Reservations")
        tree.column("Date", width=180, anchor='center')
        tree.column("Predicted Reservations", width=180, anchor='center')

        for date, count in zip(future_dates, predicted_counts):
            if date.weekday() != 6:  # Skip Sundays
                tree.insert("", "end", values=(date.strftime("%a %d %b %Y"), f"{count:.1f}"))

        tree.place(x=100, y=870)

    # Call the logic within your window
    reservation_dates = load_dates()
    fig, future_dates, predictions = create_plot(reservation_dates)

    if fig:
        canvas = FigureCanvasTkAgg(fig, master=predictions_window)
        canvas.draw()
        canvas.get_tk_widget().place(x=100, y=150, width=600, height=300)
        show_prediction_table(predictions_window, future_dates, predictions)
    else:
        tk.Label(predictions_window, text="No reservation data found to display predictions.",
                 bg=bg_color, fg="white", font=("Times New Roman", 20)).place(x=600, y=400)


prediction_button = Button(owner_window,text="Predictions",
                           font=("Times New Roman", 20),
                           activebackground="#981e2b",
                           bg="#981e2b",
                           activeforeground="white",
                           fg="white",
                           command=predictions
                           )
prediction_button.place(x=690,y=525)

def manage_owner():
    owner_window.withdraw()
    manage_owner_window = tkinter.Toplevel()
    manage_owner_window.geometry("1920x1080")
    manage_owner_window.title("Staff")

    def add_owner():
        owner_window.withdraw()
        add_owner_window = tkinter.Toplevel()
        add_owner_window.geometry("1920x1080")
        add_owner_window.title("Add Owner")

        icon = PhotoImage(file='logo.png')
        add_owner_window.iconphoto(True, icon)

        background = Label(add_owner_window, bg='#981e2b', height=900, width=75)
        background.place(x=500, y=100)

        heading_reservation = Label(
            add_owner_window,
            text="Penash The Indian Restaurant                   ",
            bg="#981e2b",
            fg="white",
            font=("Times New Roman", 70),
            bd=3,
            relief=SUNKEN
        )
        heading_reservation.place(x=-3, y=0)

        location_reservation = Label(
            add_owner_window,
            text="Durham \n Croxdale \n Croxdale Inn \n DH6 5HX",
            bg="#981e2b",
            fg="white",
            font=("Times New Roman", 16)
        )
        location_reservation.place(x=1150, y=5)

        add_owner_window.photo_logo = PhotoImage(file="logo.png")
        logo_label = Label(add_owner_window, image=add_owner_window.photo_logo)
        logo_label.place(x=1350, y=5)

        def main():
            add_owner_window.destroy()
            main_window.deiconify()

        def back():
            add_owner_window.destroy()
            manage_owner_window.deiconify()

        back_button = Button(
            add_owner_window,
            text="Back",
            command=back,
            font=("Times New Roman", 20),
            activebackground="#981e2b",
            bg="#981e2b",
            activeforeground="white",
            fg="white"
        )
        back_button.place(x=0, y=115)

        main_menu_button = Button(
            add_owner_window,
            text="Main Menu",
            command=main,
            font=("Times New Roman", 20),
            activebackground="#981e2b",
            bg="#981e2b",
            activeforeground="white",
            fg="white"
        )
        main_menu_button.place(x=1376, y=115)

        owner_name_label = Label(add_owner_window,text="Name: ",
                            bg = "#981e2b",
                            fg = "white",
                            font = ("Times New Roman", 20), bd = 3,
                            relief = RIDGE
                            )
        owner_name_label.place(x = 550,y=200)

        owner_name_entry = Entry(add_owner_window, font=("Arial", 19))
        owner_name_entry.place(x=680, y=200
                               )
        owner_number_label = Label(add_owner_window,text="Number: ",
                                 bg="#981e2b",
                                 fg="white",
                                 font=("Times New Roman", 20), bd=3,
                                 relief=RIDGE
                                 )
        owner_number_label.place(x=550, y=250)

        owner_number_entry = Entry(add_owner_window, font=("Arial", 19))
        owner_number_entry.place(x=680, y=250)

        owner_username_label = Label(add_owner_window,text="Username: ",
                                 bg="#981e2b",
                                 fg="white",
                                 font=("Times New Roman", 20), bd=3,
                                 relief=RIDGE
                                 )
        owner_username_label.place(x=550, y=300)

        owner_username_entry = Entry(add_owner_window, font=("Arial", 19))
        owner_username_entry.place(x=680, y=300)

        owner_password_label = Label(add_owner_window,text="Password: ",
                                 bg="#981e2b",
                                 fg="white",
                                 font=("Times New Roman", 20), bd=3,
                                 relief=RIDGE
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
                Label(
                    add_owner_window,
                    text="Input Error: All fields required",
                    fg="white",
                    bg="#981e2b",
                    font=("Arial", 16)
                ).place(x=200, y=500)
                print("Please fill in all inputs")
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
                print("Insert successful")

                Label(add_owner_window, text="Data inserted successfully!", fg="white", bg="#981e2b",
                      font=("Arial", 16)).place(x=200, y=500)

                owner_name_entry.delete(0, tkinter.END)
                owner_number_entry.delete(0, tkinter.END)
                owner_username_entry.delete(0, tkinter.END)
                owner_password_entry.delete(0, tkinter.END)

            except Exception as e:
                Label(add_owner_window, text=f"Error inserting data: {e}", fg="white", bg="#981e2b",
                      font=("Arial", 16)).place(x=200, y=500)

        staff_add_button = Button(add_owner_window,
                                     text="Add Owner",
                                     font=("Times New Roman", 20),
                                     activebackground="#981e2b",
                                     bg="#981e2b",
                                     activeforeground="white",
                                     fg="white",
                                     command=Add_owners)
        staff_add_button.place(x=675, y=450)


    def delete_owners():
        owner_window.withdraw()
        delete_owner_window = tkinter.Toplevel()
        delete_owner_window.geometry("1920x1080")
        delete_owner_window.title("Delete Staff")

        icon = PhotoImage(file='logo.png')
        delete_owner_window.iconphoto(True, icon)

        background = Label(delete_owner_window, bg='#981e2b', height=900, width=75)
        background.place(x=500, y=100)

        heading_reservation = Label(
            delete_owner_window,
            text="Penash The Indian Restaurant                   ",
            bg="#981e2b",
            fg="white",
            font=("Times New Roman", 70),
            bd=3,
            relief=SUNKEN
        )
        heading_reservation.place(x=-3, y=0)

        location_reservation = Label(
            delete_owner_window,
            text="Durham \n Croxdale \n Croxdale Inn \n DH6 5HX",
            bg="#981e2b",
            fg="white",
            font=("Times New Roman", 16)
        )
        location_reservation.place(x=1150, y=5)

        delete_owner_window.photo_logo = PhotoImage(file="logo.png")
        logo_label = Label(delete_owner_window, image=delete_owner_window.photo_logo)
        logo_label.place(x=1350, y=5)

        def main():
            delete_owner_window.destroy()
            main_window.deiconify()

        def back():
            delete_owner_window.destroy()
            manage_owner_window.deiconify()

        back_button = Button(
            delete_owner_window,
            text="Back",
            command=back,
            font=("Times New Roman", 20),
            activebackground="#981e2b",
            bg="#981e2b",
            activeforeground="white",
            fg="white"
        )
        back_button.place(x=0, y=115)

        main_menu_button = Button(
            delete_owner_window,
            text="Main Menu",
            command=main,
            font=("Times New Roman", 20),
            activebackground="#981e2b",
            bg="#981e2b",
            activeforeground="white",
            fg="white"
        )
        main_menu_button.place(x=1376, y=115)

        owner_name_label = Label(delete_owner_window, text="Name: ",
                                 bg="#981e2b",
                                 fg="white",
                                 font=("Times New Roman", 20), bd=3,
                                 relief=RIDGE
                                 )
        owner_name_label.place(x=550, y=200)

        owner_name_entry = Entry(delete_owner_window, font=("Arial", 19))
        owner_name_entry.place(x=680, y=200)

        owner_number_label = Label(delete_owner_window, text="Number: ",
                             bg="#981e2b",
                             fg="white",
                             font=("Times New Roman", 20), bd=3,
                             relief=RIDGE
                             )
        owner_number_label.place(x=550, y=250)

        owner_number_entry = Entry(delete_owner_window, font=("Arial", 19))
        owner_number_entry.place(x=680, y=250)

        def delete_staff():
            name = owner_name_entry.get().strip()
            number = owner_name_entry.get().strip()

            if not name or not number:
                print("Please enter both name and number.")
                return

            cursor.execute("SELECT * FROM Owner_details WHERE name = ? AND number = ?", (name, number))
            result = cursor.fetchone()

            if result:
                cursor.execute("DELETE FROM Owner_details WHERE Name = ? AND Number = ?", (name, number))
                conn.commit()
                print("User deleted successfully.")
            else:
                print("No matching user found.")

        staff_delete_button = Button(delete_owner_window,
                                     text="Delete Staff",
                                     font=("Times New Roman", 20),
                                     activebackground="#981e2b",
                                     bg="#981e2b",
                                     activeforeground="white",
                                     fg="white",
                                     command=delete_staff)
        staff_delete_button.place(x=675,y=350)

    icon = PhotoImage(file='logo.png')
    manage_owner_window.iconphoto(True, icon)

    background = Label(manage_owner_window, bg='#981e2b', height=900, width=75)
    background.place(x=500, y=100)

    heading_reservation = Label(
        manage_owner_window,
        text="Penash The Indian Restaurant                   ",
        bg="#981e2b",
        fg="white",
        font=("Times New Roman", 70),
        bd=3,
        relief=SUNKEN
    )
    heading_reservation.place(x=-3, y=0)

    location_reservation = Label(
        manage_owner_window,
        text="Durham \n Croxdale \n Croxdale Inn \n DH6 5HX",
        bg="#981e2b",
        fg="white",
        font=("Times New Roman", 16)
    )
    location_reservation.place(x=1150, y=5)

    manage_owner_window.photo_logo = PhotoImage(file="logo.png")
    logo_label = Label(manage_owner_window, image=manage_owner_window.photo_logo)
    logo_label.place(x=1350, y=5)

    def main():
        manage_owner_window.destroy()
        main_window.deiconify()

    def back():
        manage_owner_window.destroy()
        owner_window.deiconify()

    back_button = Button(
        manage_owner_window,
        text="Back",
        command=back,
        font=("Times New Roman", 20),
        activebackground="#981e2b",
        bg="#981e2b",
        activeforeground="white",
        fg="white"
    )
    back_button.place(x=0, y=115)

    main_menu_button = Button(
        manage_owner_window,
        text="Main Menu",
        command=main,
        font=("Times New Roman", 20),
        activebackground="#981e2b",
        bg="#981e2b",
        activeforeground="white",
        fg="white"
    )

    main_menu_button.place(x=1376, y=115)

    add_button = Button(manage_owner_window, text="Add Staff",
                          font=("Times New Roman", 20),
                          activebackground="#981e2b",
                          bg="#981e2b",
                          activeforeground="white",
                          fg="white",
                          command=add_owner
                          )
    add_button.place(x=680, y=350)

    delete_button = Button(manage_owner_window, text="Delete Staff",
                          font=("Times New Roman", 20),
                          activebackground="#981e2b",
                          bg="#981e2b",
                          activeforeground="white",
                          fg="white",
                          command=delete_owners
                           )
    delete_button.place(x=680, y=450)

manage_owner_button = Button(owner_window,text="Manage Owner",
                           font=("Times New Roman", 20),
                           activebackground="#981e2b",
                           bg="#981e2b",
                           activeforeground="white",
                           fg="white",
                           command=manage_owner
                           )
manage_owner_button.place(x=670,y=600)


owner_window.mainloop()