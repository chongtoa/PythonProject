#-*-utf-8-*-
from pynput.mouse import Button, Controller

# control mouse
mouse = Controller()

# Read poniter position
print("The current pointer position is {0}".format(mouse.position))

# set pointer position
mouse.position = (10, 20)
print("Now we have moved it to {0}".format(mouse.position))

# Move poniter relative to current positon
mouse.move(5, -5)

# Press and release
mouse.press(Button.left)
mouse.release(Button.left)

mouse.click(Button.left, 2)

# Scroll two steps down
mouse.scroll(0, 2)