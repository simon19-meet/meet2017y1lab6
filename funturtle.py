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
up_arrow="Up"
left_arrow="Left"
down_arrow="Down"
right_arrow="Right"
spacebar="space"

up=0
left=1
down=2
right=3
direction=up
def up():
    global direction
    direction=up
    print('You pressed up!')
    old_pos=turtle.pos()
    x=old_pos[0]
    y=old_pos[1]
    turtle.goto(x,y+10)
    print(turtle.pos())
def left():
    global direction
    direction=left
    print('You pressed left!')
    old_pos=turtle.pos()
    x=old_pos[0]
    y=old_pos[1]
    turtle.goto(x-10,y)
    print(turtle.pos())
def down():
    global direction
    direction=down
    print('You pressed down!')
    old_pos=turtle.pos()
    x=old_pos[0]
    y=old_pos[1]
    turtle.goto(x,y-10)
    print(turtle.pos())
def right():
    global direction
    direction=right
    print('You pressed right!')
    old_pos=turtle.pos()
    x=old_pos[0]
    y=old_pos[1]
    turtle.goto(x+10,y)
    print(turtle.pos())
turtle.onkeypress(up, up_arrow)
turtle.onkeypress(left, left_arrow)
turtle.onkeypress(down, down_arrow)
turtle.onkeypress(right, right_arrow)
turtle.onkeypress(turtle.stamp, spacebar)
turtle.listen()
turtle.mainloop()

