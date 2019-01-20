from tkinter import *
from tkinter.ttk import *
from functions import *

movie_get()
matches = search_movies("summer")
results = relevance_sort("summer", matches)


# Main window config
root = Tk()
root.config(bg="gray30")
root.geometry("900x600")
root.title("Sloth")
root.iconbitmap("wco_icon.ico")

# Color Theme
s = Style()
s.configure('TRadiobutton', background="gray30", foreground="SlateGray3")
s.configure('TButton', background="gray30", foreground="DodgerBlue3")
s.map('TButton', foreground=[('pressed', 'OrangeRed4')])
s.configure('TFrame', background="gray30")



# Serach bar
search_bar = Frame(root)
search_bar.grid(row=0, columnspan=4, sticky=W)
criteria = Entry(search_bar, width=50)
criteria.grid(row=0, sticky=W, padx=3)


# TODO Add command to these
# Frame ser_type
ser_type = Frame(root)
ser_type.grid(row=1, sticky=W)
all_ser = Radiobutton(ser_type, text="All The Things!", value=1)
dub_ser = Radiobutton(ser_type, text="Dubbed Anime", value=2)
sub_ser = Radiobutton(ser_type, text="Subbed Anime", value=3)
mov_ser = Radiobutton(ser_type, text="Movies", value=4)
car_ser = Radiobutton(ser_type, text="Cartoons", value=5)
all_ser.grid(row=0, sticky=W, column=0)
dub_ser.grid(row=0, sticky=W, column=1)
sub_ser.grid(row=0, sticky=W, column=2)
mov_ser.grid(row=0, sticky=W, column=3)
car_ser.grid(row=0, sticky=W, column=4)


# Results listbox
resultsbox = Listbox(root, width=120, height=15, bd=3,
                     bg="gray20", fg="SlateGray3",
                     activestyle="none",
                     selectforeground="OrangeRed4",
                     selectbackground="DodgerBlue3",
                     selectmode=SINGLE)
for item in results:
    resultsbox.insert(END, item)
resultsbox.grid(row=5, columnspan=4, sticky=E+W)

Button(root, text="Add").grid(row=5, column=4, padx=3)

root.mainloop()


