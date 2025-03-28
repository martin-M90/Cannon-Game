from random import randrange
from turtle import *
from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 15  # Aumento de velocidad del proyectil (antes /25)
        speed.y = (y + 200) / 15  # Aumento de velocidad del proyectil (antes /25)

def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    "Draw ball and targets."
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

def move():
    "Move ball and targets."
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 1  # Aumento de velocidad de los balones (antes -0.5)

        # Si el balón sale de la pantalla, reaparece en la derecha
        if target.x < -210:
            target.x = 200
            target.y = randrange(-150, 150)

    if inside(ball):
        speed.y -= 0.5  # Aumento de la gravedad (antes -0.35)
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()
    ontimer(move, 35)  # Intervalo más rápido para mayor velocidad del juego (antes 50ms)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
