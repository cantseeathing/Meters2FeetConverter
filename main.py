import tkinter as tk
from tkinter import ttk
import tkinter.font as font


try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


def calculate_feet(*args):
    try:
        meters = float(mtr_value.get())
        feet = meters * 3.28084
        feet_value.set(f'{feet:0.3f}')
        # ft_display.configure(text=feet)
    except ValueError:
        pass


root = tk.Tk()
root.title('Distance Converter')

font.nametofont('TkDefaultFont').configure(size=15)

root.columnconfigure(0, weight=1)
root.geometry('600x300')

mtr_value = tk.StringVar()
feet_value = tk.StringVar(value='Feet shown here')

main = ttk.Frame(root, padding=(30, 15))
main.grid()

mtr_label = ttk.Label(main, text='Meters:')
mtr_input = ttk.Entry(main, width=10, textvariable=mtr_value, font=('Segoe UI', 15))

ft_label = ttk.Label(main, text='Feet:')
ft_display = ttk.Label(main, textvariable=feet_value)

calc_button = ttk.Button(main, text='Calculate', command=calculate_feet)

mtr_label.grid(column=0, row=0, sticky='W')
mtr_input.grid(column=1, row=0, sticky='EW')

mtr_input.focus()

ft_label.grid(column=0, row=1, sticky='W')
ft_display.grid(column=1, row=1, sticky='EW')

calc_button.grid(column=0, row=2, columnspan=2, sticky='EW')

for child in main.winfo_children():
    child.grid_configure(padx=15, pady=15)

root.bind('<Return>', calculate_feet)
root.bind('<KP_Enter>', calculate_feet)

root.mainloop()
