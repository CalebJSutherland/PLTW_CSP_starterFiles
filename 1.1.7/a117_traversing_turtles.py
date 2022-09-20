#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl
# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  new_color=turtle_colors.pop()
  t.pencolor(new_color)
  t.fillcolor(new_color)
  my_turtles.append(t)


#  cordenent information
startx = 0
starty = 0
a = 45

# move to cordenent
for t in my_turtles:
  t.penup()
  t.goto(startx, starty)
  t.pendown()
  t.right(a)     
  t.forward(50)

# alter cordent	
  a = a + 45
  startx = t.xcor()
  starty = t.ycor()

wn = trtl.Screen()
wn.mainloop()
