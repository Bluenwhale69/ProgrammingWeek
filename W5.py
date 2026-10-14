
def show_info():
    print("Area Calculation Program")
    print("------------------------")

def get_data():
    widths = []
    lengths = []

    n = int(input("How many rectangles? "))

    for i in range(n):
        print(f"\nRectangle {i + 1}")
        width = float(input("Enter width (meters): "))
        length = float(input("Enter length (meters): "))

        widths.append(width)
        lengths.append(length)

    return widths, lengths

def cal_area(width, length):
    return width * length

def show_area(area):
    print(f"Area: {area:.2f} square meters")
    print(f"Area: {area / 4:.2f} square wa")

# Main program
show_info()

widths, lengths = get_data()

areas = []

for i in range(len(widths)):
    area = cal_area(widths[i], lengths[i])
    areas.append(area)

    print(f"\nRectangle {i + 1}")
    show_area(area)

print("\nAll areas:", areas)
