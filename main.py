def on_gesture_logo_up():
    basic.show_arrow(ArrowNames.NORTH)
input.on_gesture(Gesture.LOGO_UP, on_gesture_logo_up)

def on_gesture_tilt_left():
    basic.show_arrow(ArrowNames.WEST)
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_gesture_screen_up():
    basic.show_icon(IconNames.YES)
input.on_gesture(Gesture.SCREEN_UP, on_gesture_screen_up)

def on_gesture_screen_down():
    basic.show_icon(IconNames.NO)
input.on_gesture(Gesture.SCREEN_DOWN, on_gesture_screen_down)

def on_gesture_shake():
    basic.show_icon(IconNames.TARGET)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_gesture_tilt_right():
    basic.show_arrow(ArrowNames.EAST)
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

def on_gesture_logo_down():
    basic.show_arrow(ArrowNames.SOUTH)
input.on_gesture(Gesture.LOGO_DOWN, on_gesture_logo_down)
