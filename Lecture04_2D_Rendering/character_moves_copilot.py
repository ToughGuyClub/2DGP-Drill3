from pico2d import *
import math

open_canvas()

boy = load_image('character.png')
grass = load_image('grass.png')

def draw_boy(x: float, y: float):
    clear_canvas_now()
    grass.draw_now(400, 30)
    boy.draw_now(x, y)
    delay(0.01)

def move_right(x):
    print('moving right')
    for i in range(70):
        x += 5
        draw_boy(x, 90)

def move_top():
    print('moving top')
    for y in range(90, 550, 5):
        draw_boy(750, y)

def move_left():
    print('moving left')
    for x in range(750, 50, -5):
        draw_boy(x, 550)

def move_bottom():
    print('moving bottom')
    for y in range(550, 90, -5):
        draw_boy(50, y)

def move_lefttop():
    print("move lefttop")
    for i in range(70):
        x = 750 - i * 5
        y = 90 + i * (460 / 70)
        draw_boy(x, y)

def move_leftbottom():
    print("move leftbottom")
    for i in range(70):
        x = 400 - i * 5
        y = 550 - i * (460 / 70)
        draw_boy(x, y)

def move_rectangle():
    print("move rectangle")
    move_right(400)  # 시작점 400에서 시작
    move_top()
    move_left()
    move_bottom()
    move_right(50)   # 다시 시작점으로

def move_triangle():
    print("move triangle")
    move_right(400)  # 시작점 400에서 시작
    move_lefttop()
    move_leftbottom()
    move_right(50)   # 다시 시작점으로

def move_circle():
    print("move circle")
    cx, cy = 400, 300  # 원의 중심점
    r = 210  # 반지름
    # 시계 방향으로 원운동 (270도에서 -90도)
    for deg in range(270, -90, -1):
        x = cx + r * math.cos(math.radians(deg))
        y = cy + r * math.sin(math.radians(deg))
        draw_boy(x, y)

while True:
    move_rectangle()
    move_triangle()
    move_circle()

close_canvas()
