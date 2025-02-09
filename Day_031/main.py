from tkinter import *
import pandas as pd
import random


BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = 'Ariel'

df = pd.read_csv("data/es_en_top1000.csv").to_dict(orient="records")


def next_card():
    # Pick a random word and language
    randchoice = random.choice(df)
    canvas.itemconfig(card_title, text=list(randchoice.keys())[0])
    canvas.itemconfig(card_word, text=list(randchoice.values())[0])


def flip_card():
    canvas.item

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

window.after(3000, func=flip_card)

canvas = Canvas(height=526, width=800)
logo_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=logo_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)
card_title = canvas.create_text(400, 150, font=(FONT_NAME, 40, "italic"), tags="word_text")
card_word = canvas.create_text(400, 263, font=(FONT_NAME, 60, "bold"), tags="word_text")

cross_image = PhotoImage(file='images/wrong.png')
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=next_card)
known_button.grid(column=1, row=1)


next_card()

window.mainloop()
