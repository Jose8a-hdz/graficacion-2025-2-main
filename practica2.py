import turtle

# Configuración de la ventana
turtle.setup(600, 600)
turtle.bgcolor("white")

# Crear objeto turtle
t = turtle.Turtle()
t.shape("square")
t.color("red")
t.penup()  # Para que no deje rastro al moverse

# Velocidad de movimiento
paso = 2

# Funciones de movimiento
def mover_arriba():
    y = t.ycor()
    t.sety(y + paso)

def mover_abajo():
    y = t.ycor()
    t.sety(y - paso)

def mover_izquierda():
    x = t.xcor()
    t.setx(x - paso)

def mover_derecha():
    x = t.xcor()
    t.setx(x + paso)

def salir():
    turtle.bye()
# Asignar teclas
turtle.listen()
turtle.onkeypress(mover_arriba, "Up")
turtle.onkeypress(mover_abajo, "Down")
turtle.onkeypress(mover_izquierda, "Left")
turtle.onkeypress(mover_derecha, "Right")
turtle.onkeypress(salir,"Escape")
# Mantener ventana abierta
turtle.done()

