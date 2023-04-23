from tkinter import *
import math
import statistics
import time

app = Tk()
app.geometry("1200x800")
app.resizable(width=False, height=False)
app.title("Perfect Circle")

distsum, sumscore = [], []
tittxt = "Draw A Perfect Circle!"
whltxt, dcmtxt = 0, 0
canvas = Canvas(app, bg="black", bd=-2)
whllbl = canvas.create_text(545, 382, text=whltxt, font=("Fixedsys", 69), fill='green')
dcmlbl = canvas.create_text(655, 382, text=str(dcmtxt)+"%", font=("Fixedsys", 69), fill='green')
titlbl = canvas.create_text(600, 60, text=tittxt, font=("Fixedsys", 60), fill='green')

def get_position(event):
    global last_x, last_y, last_time
    last_x, last_y = event.x, event.y
    last_time = time.time()

def draw(event):
    global last_x, last_y, cur_time, pos1, pos2, dist, path, speed
    path = canvas.create_line((last_x, last_y, event.x, event.y), fill="green", width=7, tags="circle")
    last_x, last_y = event.x, event.y
    cur_time = time.time()
    pos1 = [600, 400]
    pos2 = [last_x, last_y]
    dist = math.dist(pos1, pos2)
    speed = dist/(cur_time-last_time)
    if dist >= 50 and speed>30:
        distsum.append(dist)
        for i in range(0, len(distsum)):
            delta = abs(distsum[0]-distsum[i])
            canvas.itemconfig(path, fill="green" if delta<10 else "yellow" if 10<delta<20 else "orange" if 20<delta<30 else "red")
            score = 100*(((distsum[0]-delta)-(distsum[0]*0.69))/(distsum[0]*0.31))
            sumscore.append(score)
            whltxt = int(statistics.fmean(sumscore))
            dcmtxt = int(statistics.fmean(sumscore)*10%10)
        canvas.itemconfig(whllbl, text=whltxt, fill="green" if whltxt>=90 else "yellow" if 85<=whltxt<90 else "orange" if 80<=whltxt<85 else "red")
        canvas.itemconfig(dcmlbl, text=str(dcmtxt)+"%", fill="green" if whltxt>=90 else "yellow" if 85<=whltxt<90 else "orange" if 80<=whltxt<85 else "red")
    elif dist<50:
        canvas.unbind("<B1-Motion>")
        canvas.itemconfig(titlbl, text="Too close to the center!")
        canvas.itemconfig(titlbl, fill="red")
    else:
        canvas.unbind("<B1-Motion>")
        canvas.itemconfig(titlbl, text="Too slow!")
        canvas.itemconfig(titlbl, fill="red")

def clear(event):
    canvas.delete("circle")
    distsum.clear()
    sumscore.clear()
    canvas.bind("<B1-Motion>", draw)
    canvas.itemconfig(titlbl, text=tittxt)
    canvas.itemconfig(titlbl, fill="green")

canvas.pack(anchor="nw", fill="both", expand=1)
canvas.create_oval(610, 410, 590, 390, fill="white")
canvas.bind("<Button-1>", get_position)
canvas.bind("<B1-Motion>", draw, add="+")
canvas.bind("<Button-1>", clear, add="+")

app.mainloop()