from tkinter import *
from tkinter.ttk import *
from functions import *

### ------ !!!FOR TESTING ONLY!!! ------ ###
# movie_get()
# matches = search_movies("summer")
# results = relevance_sort("summer", matches)
### ------ !!!FOR TESTING ONLY!!! ------ ###


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
# TODO make and assign command to search button


# Functions
def search_check():
    criteria = searchbox.get()
    print(searchbox.get())
    print(criteria)
    if dub_sear:
        search_dub(criteria)
    if sub_sear:
        search_sub(criteria)
    if mov_sear:
        search_movies(criteria)
        print("searchin mov for" + criteria)
    if cart_sear:
        search_carts(criteria)
    else:
        search_all(criteria)


Button(search_bar, command=search_check, text="Search").grid(row=0, sticky=W, column=5)

# TODO make and assign commands to radiobuttons
# Frame ser_type
ser_type = Frame(root)
ser_type.grid(row=1, sticky=W)
all_ser = Radiobutton(ser_type, command=search_type(), text="All The Things!", value=1)
dub_ser = Radiobutton(ser_type, command=search_type("dubbed"), text="Dubbed Anime", value=2)
sub_ser = Radiobutton(ser_type, command=search_type("subbed"), text="Subbed Anime", value=3)
mov_ser = Radiobutton(ser_type, command=search_type("movie"), text="Movies", value=4)
car_ser = Radiobutton(ser_type, command=search_type("cartoon"), text="Cartoons", value=5)

all_ser.grid(row=0, sticky=W, column=0)
dub_ser.grid(row=0, sticky=W, column=1)
sub_ser.grid(row=0, sticky=W, column=2)
mov_ser.grid(row=0, sticky=W, column=3)
car_ser.grid(row=0, sticky=W, column=4)
all_ser.invoke()

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
for item in results:
        resultsbox.insert(END, item)
resultsbox.grid(row=1, columnspan=4, sticky=W)

queue = Listbox(boxes, width=75, height=15, bd=3,
                bg="gray20", fg="SlateGray3",
                activestyle="none",
                selectforeground="OrangeRed4",
                selectbackground="DodgerBlue3",
                selectmode=SINGLE)
queue.grid(row=1, column=7, columnspan=4, sticky=W)

controls = Frame(boxes)
controls.grid(row=1, column=6, sticky=W)
# TODO make and assign commands to add/remove buttons
Button(controls, text="Add").grid(row=1, padx=3)
Button(controls, text="Remove").grid(row=2, padx=3)

mainloop()
