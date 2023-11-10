# Project - Treasure hunt

print("Welcome to the treasure hunt game.")


option1 = input("You've come across a fork in the road. Where do you want to go? Left or Right? ")

if option1 == "Right":
    print("Game over. You were eaten alive by angry bears.")
else:
    option2 = input("You've come acress a lake of fire. What do you want to do? get on the wooden boat or wait? (Boat or Wait) ")
    if option2 == "Boat":
        print("You are dumb. Your dumb wooden boat got burned in the LAKE OF FIRE <-- 🔥")
    else:
        option3 = input("You've come acress 4 stupid coloured doors. Why would anyone have coloured doors? Anyways...choose 1. (Red, Black, White) ")
        if option3 == "Red":
            print("You are dumb. You really thought a red door would be it? REALLY?")
        elif option3 == "Black":
            print("You are dumb. You really thought a black door would be it? REALLY?")
        else:
            print("You got lucky. Here...enjoy the stupid treasure. It's a $0.01 pen.")