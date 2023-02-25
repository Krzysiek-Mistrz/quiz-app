from tkinter import *
import random

def data():
    with open("dane/slowa.txt", "r") as file:
        for line in file:
            word1, word2 = line.split(sep=", ")
            words[word1] = word2
    for i in words:
        keys.append(i)

def loadData():
    global auxiliary
    #window.after_cancel(timer)
    choice = random.choice(keys)
    auxiliary = choice
    canvas.itemconfig(title, text="Englisch", fill="#000000", font=("Verdana", 35))
    canvas.itemconfig(word, text=choice, fill="#000000", font=("Verdana", 60, "bold"))
    canvas.itemconfig(beforeBackground, image=cardFrontImg)
    #timer = window.after(5000, func=translation)

def dontLoadData():
    global auxiliary
    if bool(words):
        try:
            words.pop(auxiliary)
            keys.remove(auxiliary)
            file = open("dane/words-to-remember.txt", "w")
            for i in words:
                file.write(i + ", " + words[i])
            file.close()
            #translation()
            #poniewaz wyrzucam auxilary wiec nie mozna sie do niego odwolac w translation
            loadData()
        except IndexError:
            canvas.itemconfig(title, text="End", fill="#1d6d60")
            canvas.itemconfig(word, text="You've learned all the vocabulary!", fill="#1d6d60", font=("Verdana", 30, "bold"))
            canvas.itemconfig(beforeBackground, image=cardBackImg)
    else:
        canvas.itemconfig(title, text="End", fill="#1d6d60")
        canvas.itemconfig(word, text="You've learned all the vocabulary!", fill="#1d6d60", font=("Verdana", 30, "bold"))
        canvas.itemconfig(beforeBackground, image=cardBackImg)

def translation():
    global auxiliary
    #global timer
    canvas.itemconfig(title, text="Translation", fill="#1d6d60")
    canvas.itemconfig(word, text=words[auxiliary], fill="#1d6d60")
    canvas.itemconfig(beforeBackground, image=cardBackImg)
    window.after(5000, func=loadData)

def correctData():
    global auxiliary
    anwser = entry.get()
    translatedWord = words[auxiliary]
    whether = True
    if len(anwser) == len(translatedWord)-1:
        for i in range(len(anwser)):
            if anwser[i] != translatedWord[i]:
                whether = False
    else:
        whether = False
    if whether:
        try:
            words.pop(auxiliary)
            keys.remove(auxiliary)
            loadData()
        except IndexError:
            canvas.itemconfig(title, text="End", fill="#1d6d60")
            canvas.itemconfig(word, text="You've learned all the vocabulary!", fill="#1d6d60", font=("Verdana", 30, "bold"))
            canvas.itemconfig(beforeBackground, image=cardBackImg)
    else:
        IncorrectData()
def IncorrectData():
    global auxiliary, correctButton, wrongButton
    #window.after_cancel(timer)
    correctButton.destroy()
    wrongButton.destroy()
    canvas.itemconfig(title, text="You gave incorrect translation", fill="#1d6d60", font=("Verdana", 20))
    canvas.itemconfig(word, text="Do you want to learn this word?", fill="#1d6d60", font=("Verdana", 30))
    canvas.itemconfig(beforeBackground, image=cardIncorrectImg)
    wrongButton = Button(image=wrongButtonImg, command=dontLoadData)
    wrongButton.grid(row=2, column=0, pady=10)
    wrongButton.config(highlightthickness=0)
    correctButton = Button(image=correctButtonImg, command=translation)
    correctButton.grid(row=2, column=1, pady=10)
    correctButton.config(highlightthickness=0)

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
entry.grid(row=1, column=0, pady=5, ipady=5)
entry.config(highlightthickness=0, borderwidth=3)
acceptAnwser = Checkbutton(text="Accept", borderwidth=2, background="#2ddb5b", command=correctData, activebackground="#2dbf5b")
acceptAnwser.grid(row=1, column=1, pady=5, ipady=5, ipadx=5)

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