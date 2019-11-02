from graph import *
import random

canvasSize(2000, 2000)
windowSize(2000, 2000)

x, y = 100, 100

colors = ["red", "green", "blue", "pink", "yellow", "brown", "black", "gray", "white", "orange"]

def base():
    penColor (random.choice(colors))
    brushColor (random.choice(colors))
    rectangle (x, y, x + 100 * rate, y + 100 * rate)

def roof():
    penColor (random.choice(colors))
    brushColor (random.choice(colors))
    polygon ([(x - 25 * rate, y), (x + 50 * rate, y - 50 * rate), (x + 125 * rate, y)])

def window():
    penColor (random.choice(colors))
    brushColor (random.choice(colors))
    rectangle (x + 5 * rate, y + 25 * rate, x + 45 * rate, y + 70 * rate)
    penColor (random.choice(colors))
    brushColor (random.choice(colors))
    rectangle (x + 20 * rate, y + 30 * rate, x + 40 * rate, y + 65 * rate)

def door():
    penColor(random.choice(colors))
    brushColor(random.choice(colors))
    rectangle(x + 60 * rate, y + 30 * rate, x + 80 * rate, y + 85 * rate)

def house():
    base()
    roof()
    window()
    door()
    
for _ in range(randint(2, 7)):
    rate = random.random() * 2
    house()
    x += randint(50, 200)
    y += randint(50, 200)

run() 
