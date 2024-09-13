"""Paint, para dibujar formas.

Ejercicios

1. Agregar un color.
2. Completar círculo.
3. Completar rectángulo.
4. Completar triángulo.
5. Agregar parámetro de ancho de línea.
"""

from turtle import *
from freegames import vector

def line(start, end):
    """Dibujar línea desde start hasta end."""
    width(state['width'])  # Aplica el ancho de línea configurado
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start, end):
    """Dibujar cuadrado desde start hasta end."""
    width(state['width'])  # Aplica el ancho de línea configurado
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

def circle_shape(start, end):
    """Dibujar círculo desde start hasta end."""
    width(state['width'])  # Aplica el ancho de línea configurado
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    # Calcula el radio basado en la distancia entre los puntos de inicio y final
    radius = ((end.x - start.x) ** 2 + (end.y - start.y) ** 2) ** 0.5
    circle(radius)  # Llama a la función circle de turtle

    end_fill()

def rectangle(start, end):
    """Dibujar rectángulo desde start hasta end."""
    width(state['width'])  # Aplica el ancho de línea configurado
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    # Calcula la anchura y la altura del rectángulo
    ancho = end.x - start.x
    alto = end.y - start.y

    for _ in range(2):
        forward(ancho)
        left(90)
        forward(alto)
        left(90)

    end_fill()

def triangle(start, end):
    """Dibujar triángulo desde start hasta end."""
    width(state['width'])  # Aplica el ancho de línea configurado
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    # Calcula la longitud de los lados del triángulo
    lado = ((end.x - start.x) ** 2 + (end.y - start.y) ** 2) ** 0.5

    for _ in range(3):
        forward(lado)
        left(120)

    end_fill()

def tap(x, y):
    """Almacenar punto de inicio o dibujar forma."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    """Almacenar valor en el estado bajo la llave key."""
    state[key] = value

# Estado inicial con soporte para ancho de línea
state = {'start': None, 'shape': line, 'width': 1}

setup(420, 420, 370, 0)
onscreenclick(tap)
listen()

# Configuración del ancho de línea con teclas numéricas
onkey(lambda: store('width', 1), '1')  # Ancho de 1
onkey(lambda: store('width', 3), '2')  # Ancho de 3
onkey(lambda: store('width', 5), '3')  # Ancho de 5
onkey(lambda: store('width', 7), '4')  # Ancho de 7

# Deshacer el último trazo
onkey(undo, 'u')

# Configuración de colores con teclas
onkey(lambda: color('black'), 'K')   # Negro
onkey(lambda: color('white'), 'W')   # Blanco
onkey(lambda: color('green'), 'G')   # Verde
onkey(lambda: color('blue'), 'B')    # Azul
onkey(lambda: color('red'), 'R')     # Rojo

# Selección de formas con teclas
onkey(lambda: store('shape', line), 'l')         # Línea
onkey(lambda: store('shape', square), 's')       # Cuadrado
onkey(lambda: store('shape', circle_shape), 'c') # Círculo
onkey(lambda: store('shape', rectangle), 'r')    # Rectángulo
onkey(lambda: store('shape', triangle), 't')     # Triángulo

done()
