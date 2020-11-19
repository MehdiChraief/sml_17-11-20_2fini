input.onGesture(Gesture.Shake, function on_gesture_shake() {
    let a = randint(1, 6)
    basic.showNumber(a)
    if (a == 1) {
        basic.showString(" Perdant")
    }
    
    if (a == 6) {
        basic.showString(" Tricheur")
    }
    
})
