BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random

current_cards = {}

try:
    data = pandas.read_csv("./data/word_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/english_words.csv")

to_learn = data.to_dict(orient="records")







def pick_a_card():
    global current_cards
    # print(ENGLISH)

    current_cards = random.choice(to_learn)
    canvas.itemconfig(can_img, image=card_front_img)
    canvas.itemconfig(language_text,fill="black")
    canvas.itemconfig(word_text, fill="black")
    english = current_cards["English"]
    hindi = current_cards["Hindi"]
    canvas.itemconfig(word_text, text=english)
    window.after(3000, flash_card)

def flash_card():
    global current_cards
    canvas.itemconfig(language_text, text="Hindi", fill="white")
    canvas.itemconfig(word_text, text=current_cards["Hindi"], fill="white")
    canvas.itemconfig(can_img, image=card_back_img)

def save_data():
    global current_cards
    to_learn.remove(current_cards)
    pick_a_card()
    data= pandas.DataFrame(to_learn)
    data.to_csv("./data/word_to_learn.csv", index=False)


    # df.to_csv("./data/word_to_learn.csv", index=False)





# -------------------------------------------UI---------------------------------- #
window = Tk()
window.config(bg=BACKGROUND_COLOR, pady=20, padx=20)

card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
right_img = PhotoImage(file="./images/right.png")
wrong_img = PhotoImage(file="./images/wrong.png")

canvas = Canvas(width=800, height=526, highlightthickness=0, highlightcolor=BACKGROUND_COLOR, bg=BACKGROUND_COLOR)
can_img = canvas.create_image(400, 263, image=card_front_img)
language_text = canvas.create_text(400, 150, text="English", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

right_button = Button(image=right_img, command=save_data)
right_button.config(highlightthickness=0, bg=BACKGROUND_COLOR)
right_button.grid(column=0, row=1)

wrong_button = Button(image=wrong_img, command=pick_a_card)
wrong_button.config(highlightthickness=0, bg=BACKGROUND_COLOR)
wrong_button.grid(column=1, row=1)

pick_a_card()

window.mainloop()
