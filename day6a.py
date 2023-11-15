# Code for reeborg's world


def turn_left():
    print("Turned left")


def turn_around():
    turn_left()
    turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()