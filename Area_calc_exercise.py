import math
def paint_calc(height,width,cover):
    area = height * width
    number_of_cans = math.ceil(area / coverage)

    print(f"You'll need {number_of_cans} cans of paints")

test_h = int(input("Height of the wall:"))
test_w = int(input("width of the wall:"))
coverage = 5
paint_calc(height = test_h , width = test_w , cover= coverage)