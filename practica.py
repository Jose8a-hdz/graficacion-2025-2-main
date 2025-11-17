import turtle
import figuras as f
# Configuración de la ventana
turtle.setup(600, 600)
turtle.bgcolor("red")

# Crear objeto turtle
t = turtle.Turtle()
t.penup()  # No queremos que deje rastro al moverse
t.speed(0)
t.hideturtle()   # Oculta el cursor
pasos = 5
lado = 50
f.triangulo()

# Función para dibujar un cuadrado en la posición actual
def dibujar_cuadrado():
    print(lado)
    t.pendown()
    t.begin_fill()
    for _ in range(4):
        t.forward(lado)   # lado del cuadrado
        t.right(90)
    t.end_fill()
    t.penup()

# Dibujar el cuadrado inicial
t.goto(-25, 25)  # centrar mejor el cuadrado
dibujar_cuadrado()

# Funciones de movimiento
def mover_arriba():
    t.clear()                 # borrar dibujo anterior
    t.sety(t.ycor() + pasos)     # mover hacia arriba
    dibujar_cuadrado()        # redibujar cuadrado

def mover_abajo():
    t.clear()
    t.sety(t.ycor() - pasos)
    dibujar_cuadrado()

def mover_izquierda():
    t.clear()
    t.setx(t.xcor() - pasos)
    dibujar_cuadrado()

def mover_derecha():
    t.clear()
    t.setx(t.xcor() + pasos)
    dibujar_cuadrado()

def aumentar():
    global lado
    lado = lado + 5
    dibujar_cuadrado()

def disminuir():
    global lado
    lado = lado - 5
    dibujar_cuadrado()
# Asignar teclas
turtle.listen()
turtle.onkeypress(mover_arriba, "Up")
turtle.onkeypress(mover_abajo, "Down")
turtle.onkeypress(mover_izquierda, "Left")
turtle.onkeypress(mover_derecha, "Right")
turtle.onkeypress(turtle.bye,"Escape")
turtle.onkeypress(aumentar,"plus")
turtle.onkeypress(disminuir,"minus")
turtle.done()

