from tkinter import *
from tkinter.ttk import *
from functions import *
import functions

### ------ !!!FOR TESTING ONLY!!! ------ ###
startup()
# matches = search_movies("summer")
# results = relevance_sort("summer", matches)
### ------ !!!FOR TESTING ONLY!!! ------ ###
results = []

# Main window config
root = Tk()
root.config(bg="gray30")
root.geometry("1000x600")
root.title("Sloth")
# root.iconbitmap("wco_icon.ico")

# Color Theme
s = Style()
s.configure('TRadiobutton', background="gray30", foreground="SlateGray3")
s.configure('TButton', background="gray30", foreground="DodgerBlue3")
s.map('TButton', foreground=[('pressed', 'OrangeRed4')])
s.configure('TFrame', background="gray30")

# Search bar
search_bar = Frame(root)
search_bar.grid(row=0, columnspan=4, sticky=W)
searchbox = Entry(search_bar, width=50)
searchbox.focus_set()
searchbox.grid(row=0, sticky=W, padx=3)

# Listboxes
# TODO add scroll bars to listboxs
boxes = Frame(root)
boxes.grid(row=2, sticky=N + W + E)
# TODO get resizing working
boxes.rowconfigure(0, weight=1)
boxes.columnconfigure(0, weight=1)
resultsbox = Listbox(boxes, width=75, height=15, bd=3,
                    bg="gray20", fg="SlateGray3",
                    activestyle="none",
                    selectforeground="OrangeRed4",
                    selectbackground="DodgerBlue3",
                    selectmode=SINGLE)
resultsbox.grid(row=1, columnspan=4, sticky=W)
scrollbar = Scrollbar(boxes, orient="vertical")
scrollbar.config(command=resultsbox.yview())
scrollbar.grid(row=1, rowspan=4, column=5, sticky=W)

queue = Listbox(boxes, width=75, height=15, bd=3,
                bg="gray20", fg="SlateGray3",
                activestyle="none",
                selectforeground="OrangeRed4",
                selectbackground="DodgerBlue3",
                selectmode=SINGLE)
queue.grid(row=1, column=7, columnspan=4, sticky=W)


# Functions
def search_check():
    global results
    criteria = searchbox.get()
    if functions.all_sear:
        results = search_all(criteria)
    if functions.dub_sear:
        results = search_dub(criteria)
    if functions.sub_sear:
        results = search_sub(criteria)
    if functions.mov_sear:
        results = search_movies(criteria)
    if functions.cart_sear:
        results = search_carts(criteria)
    resultsbox.delete(0, 100)
    for item in results:
        resultsbox.insert(END, item)


Button(search_bar, command=search_check, text="Search").grid(row=0, sticky=W, column=5)

# Frame ser_type
ser_type = Frame(root)
ser_type.grid(row=1, sticky=W)
all_ser = Radiobutton(ser_type, command=lambda: search_type(1), text="All The Things!", value=1)
dub_ser = Radiobutton(ser_type, command=lambda: search_type(2), text="Dubbed Anime", value=2)
sub_ser = Radiobutton(ser_type, command=lambda: search_type(3), text="Subbed Anime", value=3)
mov_ser = Radiobutton(ser_type, command=lambda: search_type(4), text="Movies", value=4)
car_ser = Radiobutton(ser_type, command=lambda: search_type(5), text="Cartoons", value=5)

all_ser.grid(row=0, sticky=W, column=0)
dub_ser.grid(row=0, sticky=W, column=1)
sub_ser.grid(row=0, sticky=W, column=2)
mov_ser.grid(row=0, sticky=W, column=3)
car_ser.grid(row=0, sticky=W, column=4)
all_ser.invoke()

controls = Frame(boxes)
controls.grid(row=1, column=6, sticky=W)
# TODO make and assign commands to add/remove buttons
Button(controls, text="Add").grid(row=1, padx=3)
Button(controls, text="Remove").grid(row=2, padx=3)

mainloop()
