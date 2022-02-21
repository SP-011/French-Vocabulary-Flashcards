from tkinter import *
import pandas as pd
from random import *

# ---------------------------- CONSTANTS ----------------------------#

BACKGR_COLR = "#B1DDC6"
curr_card = {}

# ---------------------------- EXCEPTION HANDLING ----------------------------#

try:
    data = pd.read_csv("data/words_to_learn.csv")
    to_learn = data.to_dict(orient="records")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")

# ---------------------------- TICK BUTTON FUNCTION ----------------------------#

def nxt_card():
    global curr_card, flip_timer
    window.after_cancel(flip_timer)
    curr_card = choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=curr_card["French"], fill="black")
    canvas.itemconfig(card_backgr, image=card_fr_img)
    flip_timer = window.after(3000, func=flip_card)

# ---------------------------- CROSS BUTTON FUNCTION ----------------------------#

def is_known():
    to_learn.remove(curr_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    nxt_card()

# ---------------------------- FLIPPING CARD FUNCTION ----------------------------#

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=curr_card["English"], fill="white")
    canvas.itemconfig(card_backgr, image=card_bk_img)

# ---------------------------- UI SETUP ----------------------------#

window = Tk()
window.title("Flash card French")
window.config(padx=50, pady=50, bg=BACKGR_COLR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_fr_img = PhotoImage(file="images/card_front.png")
card_bk_img = PhotoImage(file="images/card_back.png")
card_backgr = canvas.create_image(400, 263, image=card_fr_img)
card_title = canvas.create_text(400, 150, text="", font=["Ariel", 40, "italic"])
card_word = canvas.create_text(400, 263, text="", font=["Ariel", 60, "bold"])
canvas.config(bg=BACKGR_COLR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
cross_button = Button(image=cross_image, highlightthickness=0, command=nxt_card)
cross_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
tick_button = Button(image=check_image, highlightthickness=0, command=is_known)
tick_button.grid(row=1, column=1)

nxt_card()

window.mainloop()



