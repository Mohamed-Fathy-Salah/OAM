from tkinter import CENTER, Tk, Frame, Button, Label, Entry, W
from tkinter import ttk
from functools import partial
from queries import *
from mutations import *
import datetime
from constants import *

def show_people(right_frame):
    # Clear all widgets from right_frame
    for widget in right_frame.winfo_children():
        widget.destroy()

    # data = [
        # ['ID', 'Name', 'City', 'Age'],
        # [1, 'John', 'New York', 25],
        # [2, 'Jane', 'Los Angeles', 30],
        # [3, 'Mike', 'Chicago', 35]
    # ]
    data = get_people()
    columns = list(data[0].keys())

    table = ttk.Treeview(right_frame)
    table.pack()

    table['columns'] = tuple(columns)
    for column in columns:
        table.column(column, anchor=CENTER)
        table.heading(column, text=column, anchor=CENTER)

    for item in data:
        values = [item[column] for column in columns]
        table.insert('', 'end', values=values)

def person_layout(right_frame):
    # Clear all widgets from right_frame
    for widget in right_frame.winfo_children():
        widget.destroy()

    rank_options = ["Soldier", "Captain", "Sergeant"]

    residence_options = [
        "Cairo", "Alexandria", "Giza", "Shubra El-Kheima", "Port Said",
        "Suez", "Luxor", "Mansoura", "El-Mahalla El-Kubra", "Tanta",
        "Asyut", "Ismailia", "Fayyum", "Zagazig", "Aswan",
        "Damietta", "Damanhur", "Minya", "Beni Suef", "Hurghada",
        "Qena", "Sohag", "Shibin El Kom", "Banha", "Arish",
        "Edfu", "Kom Ombo", "Kafr El Sheikh", "Desouk", "Mallawi",
        "Bilbais", "Idfu", "Manfalut", "Qalyub", "Akhmim"
    ]

    states = [PRESENT, LEAVE, ERRAND, SICK, ABSENT, PRISON, DETENTION]
    
    military_number_label = Label(right_frame, text="Military Number:")
    military_number_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)
    military_number_entry = Entry(right_frame)
    military_number_entry.grid(row=0, column=1, padx=5, pady=5)

    rank_label = Label(right_frame, text="Rank:")
    rank_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)
    rank_dropdown = ttk.Combobox(right_frame, values=rank_options)
    rank_dropdown.grid(row=1, column=1, padx=5, pady=5)

    name_label = Label(right_frame, text="Name:")
    name_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)
    name_entry = Entry(right_frame)
    name_entry.grid(row=2, column=1, padx=5, pady=5)

    residence_label = Label(right_frame, text="Residence:")
    residence_label.grid(row=3, column=0, padx=5, pady=5, sticky=W)
    residence_dropdown = ttk.Combobox(right_frame, values=residence_options)
    residence_dropdown.grid(row=3, column=1, padx=5, pady=5)

    brigade_label = Label(right_frame, text="Brigade:")
    brigade_label.grid(row=4, column=0, padx=5, pady=5, sticky=W)
    brigade_entry = Entry(right_frame)
    brigade_entry.grid(row=4, column=1, padx=5, pady=5)

    demobilization_label = Label(right_frame, text="Demobilization Date:")
    demobilization_label.grid(row=5, column=0, padx=5, pady=5, sticky=W)
    demobilization_entry = Entry(right_frame)
    demobilization_entry.grid(row=5, column=1, padx=5, pady=5)

    phone_label = Label(right_frame, text="Phone Number:")
    phone_label.grid(row=6, column=0, padx=5, pady=5, sticky=W)
    phone_entry = Entry(right_frame)
    phone_entry.grid(row=6, column=1, padx=5, pady=5)

    national_id_label = Label(right_frame, text="National ID:")
    national_id_label.grid(row=7, column=0, padx=5, pady=5, sticky=W)
    national_id_entry = Entry(right_frame)
    national_id_entry.grid(row=7, column=1, padx=5, pady=5)

    state_label = Label(right_frame, text="State:")
    state_label.grid(row=8, column=0, padx=5, pady=5, sticky=W)
    state_entry = ttk.Combobox(right_frame, values=states)
    state_entry.grid(row=8, column=1, padx=5, pady=5)

    def submit():
        create_person(
        military_number=military_number_entry.get(),
        rank=rank_dropdown.get(),
        name=name_entry.get(),
        residence=residence_dropdown.get(),
        brigade=brigade_entry.get(),
        demobilization_date= datetime.datetime.strptime(demobilization_entry.get(), "%Y-%m-%d").date(),
        phone_number=phone_entry.get(),
        national_id=national_id_entry.get() 
                )

    submit_button = Button(right_frame, text="Submit", command= submit)
    submit_button.grid(row=9, column=0, columnspan=2, pady=5)

def leave_layout(right_frame):
    pass

def run():
    root = Tk()

    left_frame = Frame(root, width=100, bg='grey')
    left_frame.pack_propagate()
    left_frame.pack(fill='both', side='left', expand=False)

    right_frame = Frame(root, width=900, bg='white')
    right_frame.pack_propagate()
    right_frame.pack(fill='both', side='right', expand=True)

    button1 = Button(left_frame, text='الناس', command= partial(show_people, right_frame))
    button1.pack(fill='x')

    button2 = Button(left_frame, text='شخص', command= partial(person_layout, right_frame))
    button2.pack(fill='x')

    button3 = Button(left_frame, text='اجازة', command= partial(leave_layout, right_frame))
    button3.pack(fill='x')

    root.mainloop()
