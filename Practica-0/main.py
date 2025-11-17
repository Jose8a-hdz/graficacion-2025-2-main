"""pratica-0
Aprendiendo a usar la tortuga donalleto
"""

import turtle as t
from random import random

def teleport(x: float,y:float)-> None:
    """Mueve el curso o tortuga a la posicion x,y sin dibujar lineas"""
    t.penup()
    t.setx(x)
    t.sety(y)
    t.pendown()

def dibuja():
    """ aki dibuja como loco """
    for _ in range(100):
        steps = int(random() * 100)
        angle = int(random() * 360)
        t.right(angle)
        t.fd(steps)
    
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
teleport(300,300)
t.circle(10)
input("dame tu dinero")
