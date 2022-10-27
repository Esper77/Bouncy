from tkinter import *
from PIL import Image, ImageTk
width = 640
height = 640
window = Tk()

flagx = 1
flagy = 1

canvas = Canvas(width=width, height=height, bg="#FFFFFF")
img_tk = ImageTk.PhotoImage(Image.open("dvd.png").resize((100, 100)))

dvd = canvas.create_image(100, 100, image=img_tk, anchor=NW)


def image_move():
    global canvas
    global x
    global y
    global flagy
    global flagx

    x, y = canvas.coords(dvd)

    if x + 110 >= width:
        flagx = -1
    if y + 110 >= height:
        flagy = -1
    if x <= 0:
        flagx = 1
    if y <= 0:
        flagy = 1
    canvas.move(dvd, 10 * flagx, 15 * flagy)
    canvas.after(5, image_move)


canvas.pack()


canvas.after(5, image_move)
mainloop()
