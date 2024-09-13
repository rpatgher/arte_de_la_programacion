"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import *
from turtle import *

from freegames import path

car = path('car.gif')
# Pasando números a letras para las fichas
tiles = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')[:8] * 2
state = {'mark': None}
# Cambiando el número de cuadrados
hide = [True] * 16
taps = 0


def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        # Aumentar el tamaño de cada cuadrado
        forward(100)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    # Ajustar el tamaño de los cuadrados
    return int((x + 200) // 100 + ((y + 200) // 100) * 4)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    # Ajustar el tamaño de los cuadrados
    return (count % 4) * 100 - 200, (count // 4) * 100 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    
    # Contar los taps
    global taps

    spot = index(x, y)
    mark = state['mark']
    taps += 1

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None


    # Verificar si se han revelado todas las fichas y mostrar mensaje si sí
    if all(not h for h in hide):
        print("¡Has revelado todas las fichas!")
        goto(0, 0)
        write("¡Juego completado!", align="center", font=('Arial', 30, 'bold'))


def draw():

    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    # Ajustar el número de cuadrados
    for count in range(16):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        # Ajustar la posición de los números
        goto(x + 45, y + 30)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    # Mostrar el número de taps en la pantalla
    up()
    goto(-190, 190)
    write(f'Taps: {taps}', font=('Arial', 14, 'normal'))

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()