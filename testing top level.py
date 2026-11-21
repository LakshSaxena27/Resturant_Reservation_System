import tkinter as tk

def open_new_window():
    root.withdraw()  # Hide the main window
    new_window = tk.Toplevel()
    new_window.title("New Window")

    tk.Label(new_window, text="This is a new window").pack()
    tk.Button(new_window, text="Back", command=lambda: close_window(new_window)).pack()

def close_window(window):
    window.destroy()
    root.deiconify()  # Show the main window again

root = tk.Tk()
root.title("Main Window")

tk.Button(root, text="Open New Window", command=open_new_window).pack()

root.mainloop()
