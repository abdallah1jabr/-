from microbit import *
x = 1
while True:
    if button_a.get_presses():
        pin1.write_digital(1)
    elif button_b.get_presses():
        pin1.write_digital(0)
    