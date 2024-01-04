import  turtle

turtle.speed(700)
turtle.color('white')
turtle.bgcolor('black')
b = 200
while b > 0:
    turtle.left(b)
    turtle.forward(b * 3)
    b = b - 1
turtle.Screen().getcanvas().tk.splitlist(turtle.Screen().getcanvas().tk.call('info', "tclversion"))
