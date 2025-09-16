from pico2d import *
import math
open_canvas()

boy = load_image('character.png')
grass = load_image('grass.png')
def move_rectangle():
    print("move rectangle")
    pass


def move_circle():
    print("move circle")
    r=210
    for deg in range(0, 360):


        x = 400 + r * math.cos(math.radians(deg))
        y = 300 + r * math.sin(math.radians(deg))
        clear_canvas_now()
        boy.draw_now(x, y)
        delay(0.01)
    pass


while True:
    move_circle()
    move_rectangle()
    break
    pass


close_canvas()
