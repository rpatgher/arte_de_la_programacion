"""Cannon, hitting targets with projectiles.

Exercises

1. Keep score by counting target hits.
2. Vary the effect of gravity.
3. Apply gravity to the targets.
4. Change the speed of the ball.
"""

from random import randrange
from turtle import *

from freegames import vector

ball = vector(-200, -200)
speed = vector(5, 5)
targets = []
# Variable para la gravedad
gravity = 0.35
# Variable para el puntaje
score = 0

def tap(x, y):
    """Respond to screen tap."""
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25


def inside(xy):
    """Return True if xy within screen."""
    return -200 < xy.x < 200 and -200 < xy.y < 200


def draw():
    """Draw ball and targets."""
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')


    # Muestra el puntaje en la pantalla
    goto(-190, 190)
    write(f'Score: {score}', font=('Arial', 14, 'normal'))

    update()


def move():
    """Move ball and targets."""


    # Variables globales
    global score, gravity

    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 0.5 
        target.y -= 0.1

    if inside(ball):
        # Aplica la gravedad a la velocidad de la bola
        speed.y -= gravity
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)
        else:
            score += 1

    draw()

    for target in targets:
        if not inside(target):
            return

    gravity = randrange(10, 40) / 100

    ontimer(move, 50)

def change_speed(new_speed):
    """Cambiar la velocidad de la bola."""
    global speed
    # Multiplica la velocidad actual por la nueva velocidad
    speed.x *= new_speed
    speed.y *= new_speed


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()