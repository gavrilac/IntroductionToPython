"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Alexander Gavrilovich.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
####################################################################### ##
import rosegraphics as rg

window = rg.TurtleWindow()

blue_turtle = rg.SimpleTurtle()
blue_turtle = rg.SimpleTurtle('turtle')

red_turtle = rg.SimpleTurtle()
red_turtle = rg.SimpleTurtle('turtle')

blue_turtle.pen = rg.Pen('blue', 3)
blue_turtle.speed = 10  # Fast

red_turtle.pen = rg.Pen('red',5)
red_turtle.speed = 8

size = 100

# Do the indented code 13 times.  Each time draws a square.
for k in range(13):

    # Put the pen down, then draw a square of the given size:
    blue_turtle.draw_square(size)

    # Move a little below and to the right of where the previous
    # square started.  Do this with the pen up (so nothing is drawn).
    blue_turtle.pen_up()
    blue_turtle.right(90)
    blue_turtle.forward(45)
    blue_turtle.left(45)

    # Put the pen down again (so drawing resumes).
    # Make the size for the NEXT square be 12 pixels smaller.
    blue_turtle.pen_down()
    size = size - 30

size = 200

for k in range(13):

    red_turtle.draw_square(size)
    red_turtle.pen_up()
    red_turtle.right(90)
    red_turtle.forward(45)
    red_turtle.left(45)

    red_turtle.pen_down()
    size = size - 30


window.close_on_mouse_click()

