import tkinter as tk
from tkinter import ttk
from functools import partial

def show_people(right_frame):
    # Clear all widgets from right_frame
    for widget in right_frame.winfo_children():
        widget.destroy()

    # Create the form
    ttk.Label(right_frame, text="Name:").grid(row=0, column=0, padx=5, pady=5)
    name_entry = ttk.Entry(right_frame)
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    ttk.Label(right_frame, text="Rank:").grid(row=1, column=0, padx=5, pady=5)
    rank = tk.StringVar()
    rank.set("Private") # default value
    rank_menu = ttk.OptionMenu(right_frame, rank, "جندي", "عريف", "رقيب")
    rank_menu.grid(row=1, column=1, padx=5, pady=5)

    ttk.Label(right_frame, text="Phone Number:").grid(row=2, column=0, padx=5, pady=5)
    phone_entry = ttk.Entry(right_frame)
    phone_entry.grid(row=2, column=1, padx=5, pady=5)

    def foo():
        print(phone_entry.get())

    submit_button = ttk.Button(right_frame, text="Submit", command= foo)
    submit_button.grid(row=3, column=0, columnspan=2, pady=5)

def person_layout(right_frame):
    # Clear all widgets from right_frame
    for widget in right_frame.winfo_children():
        widget.destroy()

    # Create the form
    ttk.Label(right_frame, text="Name:").grid(row=0, column=0, padx=5, pady=5)
    name_entry = ttk.Entry(right_frame)
    name_entry.grid(row=0, column=1, padx=5, pady=5)

def leave_layout(right_frame):
    pass

root = tk.Tk()

# Create a frame for the left panel
left_frame = tk.Frame(root, width=200, bg='grey')
left_frame.pack_propagate(0) # Don't allow the widgets inside to determine the frame's width
left_frame.pack(fill='both', side='left', expand=True)

# Create a frame for the right panel
right_frame = tk.Frame(root, width=600, bg='white')
right_frame.pack_propagate(0) # Don't allow the widgets inside to determine the frame's width
right_frame.pack(fill='both', side='right', expand=True)

# Create buttons and add them to the left frame
button1 = tk.Button(left_frame, text='الناس', command= partial(show_people, right_frame))
button1.pack(fill='x')

button2 = tk.Button(left_frame, text='شخص', command= partial(person_layout, right_frame))
button2.pack(fill='x')

button3 = tk.Button(left_frame, text='اجازة', command= partial(leave_layout, right_frame))
button3.pack(fill='x')

root.mainloop()
