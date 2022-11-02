from tkinter import *


view = Tk()

view.title("Mile Kilomrter converter")
view.minsize(width=400, height=200)
view.config(padx=100, pady=100)

def calculate():
    miles = float(input.get())
    # km = miles * 1.689
    ############################ Round up ###################
    km = round(miles * 1.689)
    label_4.config(text=f"{km}")

label_1 = Label(text="Is Equal To")
label_1.grid(column=0, row=1)

input = Entry(width=10)
input.grid(column=1, row=0)


label_2 = Label(text="Miles")
label_2.grid(column=2, row=0)


label_3 = Label(text="Km")
label_3.grid(column=2, row=1)


label_4 = Label(text="0")
label_4.grid(column=1, row=1)

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)



view.mainloop()

