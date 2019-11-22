from tkinter import *
from tkinter.ttk import *
from functions import *
import functions

startup()


results = []
queue = []

# Main window config
root = Tk()
root.config(bg="gray30")
root.geometry("1035x600")
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
boxes = Frame(root)
boxes.grid(row=2, sticky=N + W + E)
# TODO get resizing working
boxes.rowconfigure(0, weight=1)
boxes.columnconfigure(0, weight=1)

# Resultsbox Frame
results_frame = Frame(boxes)
results_frame.grid(row=1, column=1, sticky=N + W + E)

scrollbar_result = Scrollbar(results_frame, orient="vertical")
resultsbox = Listbox(results_frame, width=75, height=15, bd=3,
                    bg="gray20", fg="SlateGray3",
                    activestyle="none",
                    selectforeground="OrangeRed4",
                    selectbackground="DodgerBlue3",
                    selectmode=SINGLE)
resultsbox.grid(row=1, columnspan=1, sticky=W)
scrollbar_result.config(command=resultsbox.yview)
scrollbar_result.grid(row=1, column=2, sticky=W, ipady=99)



# Queuebox Frame
queue_frame = Frame(boxes)
queue_frame.grid(row=1, column=3, sticky=N + W + E)

scrollbar_queue = Scrollbar(queue_frame, orient="vertical")
queuebox = Listbox(queue_frame, width=75, height=15, bd=3,
                bg="gray20", fg="SlateGray3",
                activestyle="none",
                selectforeground="OrangeRed4",
                selectbackground="DodgerBlue3",
                selectmode=SINGLE)
queuebox.grid(row=1, column=1, columnspan=1, sticky=W)
scrollbar_queue.config(command=queuebox.yview)
scrollbar_queue.grid(row=1, column=2, sticky=W, ipady=99)


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
    resultsbox.delete(0, END)
    for item in results:
        resultsbox.insert(END, item)

def add2queue():
    global queue
    selected = resultsbox.selection_get()
    queue.append(selected)
    queuebox.insert(END, selected)

# TODO not work right is not see it as a list
def get_url():
    global main_dic, queue
    results = []
    key = queue
    if key is list:
        for title in key:
            results.append(main_dic[title])
    else:
        results.append(main_dic[key])
    print(results)

def remove_from_q():
    global queue
    dex = queuebox.curselection()
    selected = queuebox.selection_get()
    queue.remove(selected)
    queuebox.delete(dex)

def clear_q():
    global queue
    queue = []
    queuebox.delete(0, END)


# Controls Frame
controls_frame = Frame(boxes)
controls_frame.grid(row=1, column=2, sticky=W + E)

Button(controls_frame, command=add2queue, text="Add").grid(row=1, padx=3)
Button(controls_frame, command=remove_from_q, text="Remove").grid(row=2, padx=3)
Button(controls_frame, command=clear_q, text="Clear").grid(row=3, padx=3)
Button(search_bar, command=search_check, text="Search").grid(row=0, sticky=W, column=5)
Button(controls_frame, command=get_url, text="Get URLs").grid(row=4, padx=3)


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



mainloop()
