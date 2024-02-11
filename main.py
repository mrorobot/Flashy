from tkinter import *
import pandas
import random
data = pandas.read_csv("data.csv")
data_dict=data.to_dict(orient="records")
fr_word={}
def next():
    global fr_word, flip_timer
    fr_word=random.choice(data["French"])
    canvas.itemconfig(titel, text="French")
    canvas.itemconfig(words, text=fr_word)
    
def flip_card():

    canvas.itemconfig(titel, text="English")
    en_word=random.choice(data["English"])
    canvas.itemconfig(words, text=en_word)
    canvas.itemconfig(main_img, image=back_img)


BACKGROUND="#B1DDC6"
window=Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND)
flip_timer=window.after(3000, func=flip_card)
canvas=Canvas(width=800, height=500)
front_img=PhotoImage(file="Minimalist-Background-HD (1).png")
main_img=canvas.create_image(400, 250, image=front_img)

back_img=PhotoImage(file="wp9066761 (1).png")
canvas.itemconfig(main_img, image=back_img)
titel=canvas.create_text(400, 80, text="Title", font=("Ariel", 40, "italic"))
words=canvas.create_text(400, 160, text="word", font=("Ariel", 40, "italic"))
canvas.config(bg=BACKGROUND, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_img=PhotoImage(file="cross (1).png")
cross_button=Button(image=cross_img, command=next)
cross_button.grid(column=0, row=1)
correct_img=PhotoImage(file="correct (1).png")
cross_button=Button(image=correct_img, command=next)
cross_button.config(bg=BACKGROUND, highlightthickness=0)
cross_button.grid(column=1, row=1)
next()
window.mainloop()
