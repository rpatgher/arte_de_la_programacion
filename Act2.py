"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange
from turtle import *
from freegames import square, vector

# Configuración inicial
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
delay = 100  # Retraso inicial en milisegundos

# Parámetros para mover la comida
food_move_interval = 8000  # Intervalo en milisegundos para mover la comida

def change(x, y):
    """Cambiar la dirección de la serpiente."""
    aim.x = x
    aim.y = y

def move_snake():
    """Mover la serpiente hacia adelante un segmento."""
    head = snake[-1].copy()
    head.move(aim)

    # Implementar el envuelto de bordes
    head.x = (head.x + 200) % 400 - 200
    head.y = (head.y + 200) % 400 - 200

    if head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        place_food()
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move_snake, delay)

def place_food():
    """Colocar la comida en una nueva posición aleatoria."""
    food.x = randrange(-15, 15) * 10
    food.y = randrange(-15, 15) * 10

def move_food():
    """Mover la comida a una nueva posición aleatoria a intervalos regulares."""
    place_food()
    ontimer(move_food, food_move_interval)

def increase_speed():
    """Aumentar la velocidad de la serpiente."""
    global delay
    if delay > 20:
        delay -= 20
        print(f'Velocidad aumentada. Retraso: {delay} ms')

def decrease_speed():
    """Disminuir la velocidad de la serpiente."""
    global delay
    delay += 20
    print(f'Velocidad disminuida. Retraso: {delay} ms')

def on_click(x, y):
    """Cambiar la dirección de la serpiente basada en la posición del clic del ratón."""
    head = snake[-1]
    dx = x - head.x
    dy = y - head.y

    # Determinar la dirección basada en la posición del clic
    if abs(dx) > abs(dy):
        if dx > 0:
            change(10, 0)
        else:
            change(-10, 0)
    else:
        if dy > 0:
            change(0, 10)
        else:
            change(0, -10)

def setup_game():
    """Configuración inicial del juego."""
    setup(420, 420, 370, 0)
    hideturtle()
    tracer(False)
    listen()

    # Controles de teclado para cambiar la dirección
    onkey(lambda: change(10, 0), 'Right')
    onkey(lambda: change(-10, 0), 'Left')
    onkey(lambda: change(0, 10), 'Up')
    onkey(lambda: change(0, -10), 'Down')

    # Controles de teclado para ajustar la velocidad
    onkey(increase_speed, 'plus')   # Aumentar velocidad con la tecla '+'
    onkey(decrease_speed, 'minus')  # Disminuir velocidad con la tecla '-'

    # Control por clics del ratón
    onscreenclick(on_click)

    move_snake()
    move_food()
    done()

def main():
    """Función principal para iniciar el juego."""
    setup_game()

if __name__ == '__main__':
    main()
