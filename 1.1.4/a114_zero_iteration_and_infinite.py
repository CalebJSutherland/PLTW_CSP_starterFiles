#   a114_zero_iteration_and_infinite.py
#   Make a zero-iteration condition and follow it with an infinite loop.
#   Include some visual evidence that the second loop is infinite.
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)

# Add a loop with a zero-iteration condition


# Add an infinite loop
answer=input("what is your favorite number")
N=answer
while (N > 0):
  N=N+1
  print(N)

wn = trtl.Screen()
wn.mainloop()
