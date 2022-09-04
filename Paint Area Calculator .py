
def paint_calc(height,width,cover):
    can_needed=(height*width)/cover
    rounded=round(can_needed)
    if can_needed>rounded:
        print(f"You'll need {rounded+1} cans of paint.")
    else:
        print(f"You'll need {rounded} cans of paint.")
    








test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

