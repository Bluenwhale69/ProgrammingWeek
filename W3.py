def show_info():
    print("Program calculates area in square meters and square wa.")

def get_width():
    return float(input("Enter width (meters): "))

def get_length():
    return float(input("Enter length (meters): "))

def cal_area(width, length):
    return width * length

def show_area(area):
    print(f"Area = {area:.2f} square meters")

def show_area_in_SqWa(area):
    print(f"Area = {area / 4:.2f} square wa")

show_info()

width = get_width()
length = get_length()

area = cal_area(width, length)

show_area(area)
show_area_in_SqWa(area)