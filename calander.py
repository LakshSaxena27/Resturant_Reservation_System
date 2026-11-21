import tkinter as tk
from tkcalendar import Calendar

def get_date():
    selected_date = cal.get_date()
    print(f"Selected Date: {selected_date}")

# Create main window
root = tk.Tk()
root.title("Calendar Example")

# Create and place the calendar
cal = Calendar(root, selectmode='day',
               year=2025,
               month=3,
               day=24,)
cal.pack(pady=20)
# Button to get selected date
btn = tk.Button(root, text="Get Date", command=get_date)
btn.pack(pady=10)

# Run the main loop
root.mainloop()