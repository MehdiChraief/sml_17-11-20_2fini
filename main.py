from microbit import*
def on_gesture_shake():
    a=(randint(1, 6))
    basic.show_number(a)
    if a==1:
        basic.show_string(" Perdant")
    if a==6:
        basic.show_string(" Tricheur")
input.on_gesture(Gesture.SHAKE, on_gesture_shake)