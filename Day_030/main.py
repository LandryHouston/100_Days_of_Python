from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

FONT_NAME = 'Calibri'

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = ''.join(password_list)
    password_input.delete(0, 'end')
    password_input.insert(0, password)
    pyperclip.copy(password)


def export():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    
    if password == "" or website == "" or email == "":
        messagebox.showerror(title="Password Manager", message="Please don't leave any fields empty!")
    else:
        if messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}\nPassword: {password}\nIs it okay to save?"):
            output = f"{website} | {email} | {password}\n"
            with open('passwords.csv', 'a') as f:
                f.write(output)
                website_input.delete(0, END)
                password_input.delete(0, END)
                website_input.focus()
                messagebox.showinfo(title="Password Manager", message="Password saved successfully!")


window = Tk()
window.title("Passsword Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website = Label(font=(FONT_NAME, 14))
website.config(text="Website:")
website.grid(column=0, row=1)

email_username = Label(font=(FONT_NAME, 14))
email_username.config(text="Email/Username:")
email_username.grid(column=0, row=2)

password = Label(font=(FONT_NAME, 14))
password.config(text="Password:")
password.grid(column=0, row=3)

website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2, sticky="EW", padx=(20, 40))
website_input.focus()

email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2, sticky="EW", padx=(20, 40))
email_input.insert(0, "LandryH@landryhouston.com")

password_input = Entry(width=21)
password_input.grid(column=1, row=3, sticky="EW", padx=(20, 40))

generate_password = Button(text="Generate Password", command=generate_password)
generate_password.grid(column=2, row=3, sticky="EW", padx=(0, 40))

add_button = Button(text="Add", width=36, command=export)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW", padx=(20, 40))


window.mainloop()