from tkinter import *
import random

def data():
    with open("dane/slowa.txt", "r") as file:
        for line in file:
            word1, word2 = line.split(sep=", ")
            words[word1] = word2
    for i in words:
        keys.append(i)
    print(keys)

def loadData():
    global auxiliary
    #window.after_cancel(timer)
    choice = random.choice(keys)
    auxiliary = choice
    canvas.itemconfig(title, text="Englisch", fill="#000000", font=("Verdana", 35))
    canvas.itemconfig(word, text=choice, fill="#000000", font=("Verdana", 60, "bold"))
    canvas.itemconfig(beforeBackground, image=cardFrontImg)
    #timer = window.after(5000, func=translation)

def translation():
    global auxiliary
    #global timer
    canvas.itemconfig(title, text="Translation", fill="#1d6d60")
    canvas.itemconfig(word, text=words[auxiliary], fill="#1d6d60")
    canvas.itemconfig(beforeBackground, image=cardBackImg)
    window.after(5000, func=loadData)

def correctData():
    global auxiliary
    anwser = entry.get(); translatedWord = words[auxiliary]
    whether = True
    for i in range(len(anwser)):
        if anwser[i] != translatedWord[i]:
            whether = False
    if whether:
        loadData()
    else:
        print(entry.get())
        print(words[auxiliary])

keys = []
words = {}

auxiliary = ""
background = "#B1DDC6"
window = Tk()
window.title("quiz")
window.config(padx=50, pady=50, bg=background)
#timer = window.after(5000, func=translation)
data()

canvas = Canvas(width=800, height=526)
cardFrontImg = PhotoImage(file="zdjecia/card_front.png")
cardBackImg = PhotoImage(file="zdjecia/card_back.png")
cardIncorrectImg = PhotoImage(file="zdjecia/card_incorrect.png")
beforeBackground = canvas.create_image(400, 263, image=cardFrontImg)
canvas.grid(row=0, column=0, columnspan=2)
#canvas.config(bg=background, highlightthickness=0)
title = canvas.create_text(400, 150, text="Title", font=("Verdana", 35))
word = canvas.create_text(400, 280, text="word", font=("Verdana", 60, "bold"))

entry = Entry(master=window, width=50, fg="green", bg="white")
entry.insert(0, "write your translation")
entry.grid(row=1, column=0, pady=5)
entry.config(highlightthickness=0, borderwidth=3)
acceptAnwser = Checkbutton(text="Accept", borderwidth=2, background="green", command=correctData)
acceptAnwser.grid(row=1, column=1, pady=5)

wrongButtonImg = PhotoImage(file="zdjecia/wrong.png")
wrongButton = Button(image=wrongButtonImg, command=correctData)
wrongButton.grid(row=2, column=0, pady=10)
wrongButton.config(highlightthickness=0)
correctButtonImg = PhotoImage(file="zdjecia/right.png")
correctButton = Button(image=correctButtonImg, command=correctData)
correctButton.grid(row=2, column=1, pady=10)
correctButton.config(highlightthickness=0)

loadData()

window.mainloop()