# While loop
def turn_right():
    turn_left()
    turn_left()
    turn_left()


while front_is_clear():
    move()

turn_left()

# Robot instructions
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()


# This is all done using the reeborg's world website where you're using python code to move a robot. Don't run it locally.
