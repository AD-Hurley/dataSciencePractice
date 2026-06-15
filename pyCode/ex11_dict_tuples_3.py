import math


def circle_calc(radius):
    area=math.pi*radius**2
    circumference=2*math.pi*radius
    diameter=2*radius

    return area,circumference,diameter

if __name__=="__main__":
    radius=float(input("Enter a radius: "))
    area,circumference,diameter=circle_calc(radius)
    print(f"The area of the circle is: {round(area,2)}")
    print(f"The circumference of the circle is: {round(circumference,2)}")
    print(f"The diameter of the circle is: {round(diameter,2)}")