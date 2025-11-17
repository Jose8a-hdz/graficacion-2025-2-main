
import turtle

# Configuración global
t = turtle.Turtle()
t.pensize(3)
t.hideturtle()   # ocultamos el cursor para que solo se vean las figuras

# Función para dibujar cuadrado
def cuadrado(lado=100, color="red"):
    t.color(color)
    t.pendown()
    for _ in range(4):
        t.forward(lado)
        t.right(90)
    t.penup()

# Función para dibujar triángulo
def triangulo(lado=100, color="blue"):
    t.color(color)
    t.pendown()
    for _ in range(3):
        t.forward(lado)
        t.left(120)
    t.penup()

# Función para dibujar círculo
def circulo(radio=50, color="green"):
    t.color(color)
    t.pendown()
    t.circle(radio)
    t.penup()

# Función para dibujar línea
def linea(longitud=200, color="purple"):
    t.color(color)
    t.pendown()
    t.forward(longitud)
    t.penup()

# Función para mover la tortuga a una posición
def mover(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
