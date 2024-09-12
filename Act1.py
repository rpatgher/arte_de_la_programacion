"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""

from turtle import *

from freegames import vector


def line(start, end):
    """Draw line from start to end."""
    width(state['width'])  # Aplica el ancho de línea configurado
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    """Draw square from start to end."""
    width(state['width'])  # Aplica el ancho de línea configurado
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle(start, end):
    """Draw circle from start to end."""
    width(state['width'])  # Aplica el ancho de línea configurado
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    
    # Calcula el radio basado en la distancia entre los puntos de inicio y final
    radius = ((end.x - start.x) ** 2 + (end.y - start.y) ** 2) ** 0.5
    turtle.circle(radius)
    
    end_fill()


def rectangle(start, end):
    """Draw rectangle from start to end."""
    width(state['width'])  # Aplica el ancho de línea configurado
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for _ in range(2):
        forward(end.x - start.x)
        left(90)
        forward(end.y - start.y)
        left(90)

    end_fill()


def triangle(start, end):
    """Draw triangle from start to end."""
    width(state['width'])  # Aplica el ancho de línea configurado
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for _ in range(3):
        forward(end.x - start.x)
        left(120)

    end_fill()


def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    state[key] = value


state = {'start': None, 'shape': line, 'width': 1}  # Inicializamos con ancho de línea = 1
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()

# Ancho del trazo con teclas numéricas
onkey(lambda: store('width', 1), '1')  # Ancho de 1
onkey(lambda: store('width', 3), '2')  # Ancho de 3
onkey(lambda: store('width', 5), '3')  # Ancho de 5
onkey(lambda: store('width', 7), '4')  # Ancho de 7

# Deshacer el último trazo
onkey(undo, 'u')

# Colores
onkey(lambda: color('black'), 'K')  # Negro
onkey(lambda: color('white'), 'W')  # Blanco
onkey(lambda: color('green'), 'G')  # Verde
onkey(lambda: color('blue'), 'B')   # Azul
onkey(lambda: color('red'), 'R')    # Rojo

# Formas
onkey(lambda: store('shape', line), 'l')       # Línea
onkey(lambda: store('shape', square), 's')     # Cuadrado
onkey(lambda: store('shape', circle), 'c')     # Círculo
onkey(lambda: store('shape', rectangle), 'r')  # Rectángulo
onkey(lambda: store('shape', triangle), 't')   # Triángulo

done()
