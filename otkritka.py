from tkinter import *
from PIL import ImageTk, Image
import random
root = Tk()
root.title("С Новым Годом!")
root.resizable(width=False, height=False)
cWidth = 1280
cHeight = 720


c = Canvas(root, width=cWidth, height=cHeight, bg="#A52A2A")
c.pack()


image = ImageTk.PhotoImage(file=r'C:\Users\Senpai\Desktop\elka.png')
c.create_image(100, 100, image=image, anchor=NW)


def createText():
    cText = ('''
    В двери Новый год стучится,
    Дед Мороз к нам в гости мчится,
    В небе праздничный салют,
    И часы двенадцать бьют.
    
    Огоньки сверкают ярко.
    Свечи, шарики, подарки.
    Скоро сказка в дом войдет,
    Скоро будет Новый год!
    
    Поздравляю Вас с 
    наступающим Новым Годом!
    Пусть все мечты сбываются!
    ''')
    c.create_text(cWidth*2/3+50, cHeight/2, text = cText, fill = "white", font="Times 24 bold")

def createSnow(t, n):
    for i in range(500):
        x = random.randint(1, cWidth)
        y = random.randint(-cHeight*n-8, cHeight*(1-n))
        size = random.randint(3, 8)
        c.create_oval(x, y, x + size, y+size, fill = "white", tag = t)

def motion():
    global indicator, indicator_count
    c.move("tagOne", 0, 1)
    c.move("tagTwo", 0, 1)
    c.move(indicator, 0, 1)
    if c.coords(indicator)[1] < cHeight + 1:
        root.after(20, motion)
    else:
        c.move(indicator, 0, -cHeight)
        root.after(20, motion)
        if indicator_count == 0:
            c.delete("tagOne")
            createSnow('tagOne', 1)
            indicator_count = 1
        else:
            c.delete('tagTwo')
            createSnow('tagTwo', 1)
            indicator_count = 0


def main():
    global indicator, indicator_count

    indicator = c.create_oval(23, -5, 28, 0, fill = 'white')
    indicator_count = 0

    createText()
    createSnow('tagOne', 0)
    createSnow('tagOne', 1)

    motion()
main()

root.mainloop()