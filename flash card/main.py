from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    words_to_learn = original_data.to_dict(orient="records")
else:
    words_to_learn = data.to_dict(orient="records")


def change_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_to_learn)
    current_card["French"]
    canvas.itemconfig(card_text, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_text, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back)


def is_known():
    words_to_learn.remove(current_card)
    data = pandas.DataFrame(words_to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    change_card()



#-----------------------Create a screen-----------------------------------------------#
window = Tk()
window.title("Vocab Card")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)




#-----------------------Create the front card-----------------------------------------------#
canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")

card_background = canvas.create_image(400, 263, image=card_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)



#-----------------------Create the text-----------------------------------------------#
card_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))



#-----------------------Create the buttons-----------------------------------------------#
cross_image = PhotoImage(file="images/wrong.png")
cross_button = Button(image=cross_image,command=change_card)
cross_button.grid(column=0, row=1)

tick_image = PhotoImage(file="images/right.png")
tick_button = Button(image=tick_image, command=is_known)
tick_button.grid(column=1, row=1)


change_card()




window.mainloop()

