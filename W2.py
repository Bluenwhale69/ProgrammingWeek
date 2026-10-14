def show_info():
    print("This program will calculate area of a land")
    print("given width and length")
    print("created by <Wattanin>")

show_info()

def show_area():
    width = float(input("Enter width (in meter): "))
    length = float(input("Enter length (in meter): "))
    area = width * length
    
    print("The result area is", area, "(in square meter)")
    
show_area()