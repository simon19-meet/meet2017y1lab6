import turtle
##turtle.shape('turtle')
##square=turtle.clone()
##square.shape('square')
##square.goto(100,100)
##square.goto(300,300)
##square.stamp()
##square.goto(100,100)
##square.penup()
##square.goto(0,0)
##square.pendown()
##square.goto(0,100)
##square.goto(100,100)
##square.goto(100,0)
##square.goto(0,0)
##triangle=turtle.clone()
##turtle.shape('triangle')
##triangle.goto(100,100)
##triangle.goto(0,200)
##triangle.goto(0,0)
##triangle.goto(200,200)
##triangle.stamp()
##triangle.goto(-100,-100)
up_arrow="up"
left_arrow="left"
down_arrow="down"
right_arrow="right"
spacebar="space"

Up=0
Left=1
Down=2
Right=3
direction=up
def up():
    global direction
    direction=Up
    print('You pressed up!')
def left():
    global direction
    direction=Left
    print('You pressed left!')
def down():
    global direction
    direction=Down
    print('You pressed down!')
def right():
    global direction
    direction=Right
    print('You pressed right!')
turtle.onkeypress(up, Up)
turtle.mainloop()

