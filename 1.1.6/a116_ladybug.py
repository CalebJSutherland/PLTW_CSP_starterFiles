#   a116_ladybug.py
import turtle as trtl

# create ladybug head
ladybug = trtl.Turtle()
ladybug.goto(0,-10)
ladybug.pensize(40)
ladybug.circle(5)

#add legs
legs = 12
length = 70
incrament = 360 / legs
ladybug.pensize(5)


ladybug.goto(0,-50)
ladybug.setheading(incrament*12)
ladybug.forward(length)
ladybug.goto(0,-50)
ladybug.setheading(incrament*11)
ladybug.forward(length)
ladybug.goto(0,-50)
ladybug.setheading(incrament*1)
ladybug.forward(length)
ladybug.goto(0,-50)
ladybug.setheading(incrament*7)
ladybug.forward(length)
ladybug.goto(0,-50)
ladybug.setheading(incrament*6)
ladybug.forward(length)
ladybug.goto(0,-50)
ladybug.setheading(incrament*5)
ladybug.forward(length)
ladybug.penup()
ladybug.goto(0,0)


# and body
ladybug.setheading(0)
ladybug.penup()
ladybug.goto(0, -70) 
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)

# config dots
num_dots = 1
xpos = -25
ypos = -60
ladybug.pensize(10)

# draw two sets of dots
while (num_dots <= 2 ):
  ladybug.penup()
  ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos + 15, ypos + 30)
  ladybug.pendown()
  ladybug.circle(2)

  # position next dots
  xpos = ypos + 15
  xpos = xpos + 50
  num_dots = num_dots + 1


ladybug.hideturtle()

wn = trtl.Screen()
wn.mainloop()