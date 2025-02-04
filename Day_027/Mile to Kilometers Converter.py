from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=200)
window.config(padx=50, pady=50)

miles_input = Entry(width=5)
miles_input.grid(column=2, row=1)

miles_label = Label(text="Miles")
miles_label.grid(column=3, row=1)

label = Label(text="is equal to")
label.grid(column=1, row=2)

calculate_label = Label(text=0)
calculate_label.grid(column=2, row=2)

km_label = Label(text="Km")
km_label.grid(column=3, row=2)

def miles_to_km():
    new_text = miles_input.get()
    calculate_label.config(text=round(int(new_text)*1.609344, 2))

button = Button(text="Calculate", command=miles_to_km)
button.grid(column=2, row=3)

window.mainloop()