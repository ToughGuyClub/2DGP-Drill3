from pico2d import *
import math
open_canvas()

boy = load_image('character.png')
grass = load_image('grass.png')


def move_right():
    print('moving right')
    pass


def move_top():
    print('moving top')
    for x in range(0,800,5):
        draw_boy(x,550)
    pass


def move_left():
    print('moving left')
    pass


def move_bottom():
    print('moving bottom')
    pass


def move_rectangle():
    print("move rectangle")
    move_right()
    move_top()
    move_left()
    move_bottom()

    pass


def move_circle():
    print("move circle")
    r=210
    for deg in range(270, -90,-1):
        x = 400 + r * math.cos(math.radians(deg))
        y = 300 + r * math.sin(math.radians(deg))
        draw_boy(x, y)
    pass


def draw_boy(x: float, y: float):
    clear_canvas_now()
    boy.draw_now(x, y)
    delay(0.01)


while True:
    # move_circle()
    move_rectangle()
    break
    pass


close_canvas()
