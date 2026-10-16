def show_info():
    print("Program to calculate area of a rectangle")

def get_width():
    return float(input("Enter width (meters): "))

def get_length():
    return float(input("Enter length (meters): "))

def cal_area(width, length):
    return width * length

def show_area(area):
    print("Area:", area, "square meters")

def show_area_in_SqWa(area):
    print("Area:", area / 4, "square wah")

# Main program
show_info()

width = get_width()
length = get_length()

area = cal_area(width, length)

show_area(area)
show_area_in_SqWa(area)
