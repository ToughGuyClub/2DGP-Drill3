from pico2d import *
import math

open_canvas()

boy = load_image('character.png')
grass = load_image('grass.png')


def move_right(x):
    print('moving right')
    for i in range(70):
        x += 5
        draw_boy(x, 90)

    pass


def move_top():
    print('moving top')
    for y in range(90, 550, 5):
        draw_boy(750, y)
    pass


def move_left():
    print('moving left')
    for x in range(750, 50, -5):
        draw_boy(x, 550)
    pass


def move_bottom():
    print('moving bottom')
    for y in range(550, 90, -5):
        draw_boy(50, y)
    pass


def move_rectangle():
    print("move rectangle")
    move_right(400)
    move_top()
    move_left()
    move_bottom()
    move_right(50)
    pass


def move_circle():
    print("move circle")
    r = 210
    for deg in range(270, -90, -1):
        x = 400 + r * math.cos(math.radians(deg))
        y = 300 + r * math.sin(math.radians(deg))
        draw_boy(x, y)
    pass


def draw_boy(x: float, y: float):
    clear_canvas_now()
    boy.draw_now(x, y)
    delay(0.01)


def move_lefttop():
    print("move lefttop")
    for i in range(70):
        clear_canvas_now()
        x = 750 - i * 5
        y = 90 + i * (460 / 70)
        boy.draw_now(x, y)
        delay(0.01)
    pass


def move_leftbottom():
    print("move leftbottom")
    for i in range(70):
        clear_canvas_now()
        x = 400 - i * 5
        y = 550 - i * (460 / 70)
        boy.draw_now(x, y)
        delay(0.01)
    pass


def move_triangle():
    print("move triangle")
    move_right(400)
    move_lefttop()
    move_leftbottom()
    move_right(50)
    pass


while True:
    move_rectangle()
    move_triangle()
    move_circle()

    pass

close_canvas()
