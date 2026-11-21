import tkinter as tk
import tkinter.font as tkfont

root = tk.Tk()
fonts = list(tkfont.families())
fonts.sort()
for f in fonts:
    print(f)
