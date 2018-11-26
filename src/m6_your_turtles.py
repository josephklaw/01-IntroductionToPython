"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Joseph Law.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
#DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
jerry = rg.SimpleTurtle()
jerry.pen = rg.Pen('purple',2)
jerry.speed = 300
jack = rg.SimpleTurtle()
jack.pen = rg.Pen('orange',2)
jack.speed = 300
for k in range (100):
    jerry.forward(k)
    jerry.right(60)
    jack.forward(k)
    jack.left(30)
window.close_on_mouse_click()
