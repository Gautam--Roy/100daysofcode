# While loop
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()



# Robot instructions
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()


# This is all done using the reeborg's world website where you're using python code to move a robot. Don't run it locally.