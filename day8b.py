# Challenge

import math


def paint_calc(height, width, coverage):
    paint_cans = (height * width) / coverage
    paint_cans = math.ceil(paint_cans)
    print(f"You'll need {paint_cans} cans of paint")


test_h = int(input("Height of wall? "))
test_w = int(input("Width of wall? "))
coverage = 5
paint_calc(test_h, test_w, coverage)
