from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=80, pady=80)

my_label = Label(text="I am a label", font=("Arial", 24))
my_label.grid(column=1, row=1)
my_label.config(padx=40, pady=40)

def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text.lower())
    
def button_clicked_too():
    new_text = input.get()
    my_label.config(text=new_text.upper())

button = Button(text="Click Me", command=button_clicked)
button.grid(column=2, row=2)

button = Button(text="Click Me Too!", command=button_clicked_too)
button.grid(column=3, row=1)

input = Entry(width=10)
input.grid(column=4, row=3)

window.mainloop()