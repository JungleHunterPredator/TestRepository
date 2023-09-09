import math

print("Welcome to an Area and Volume Calulator!")

# Shapes (2D): Square, Rectangle, Triangle, Circle, Pentagon, Hexagon, Octagon
# Shapes (3D): Cube, Rectangular Prism, Cylinder, Shpere, Pyramid, Cone

# Area

def calSquare():
    a = int(input("enter the length of the Square (cm): "))
    area = a * a
    return area

def calRectangle():
    l = int(input("enter the length of the Rectangle (cm): "))
    w = int(input("enter the width of the Rectangle (cm): "))
    area = l * w
    return area

def calTriangle():
    b = int(input("enter the base of the Triangle (cm): "))
    h = int(input("enter the height of the Triangle (cm): "))
    area = b * h / 2
    return area

def calCircle():
    r = int(input("enter the radius of the Circle (cm): "))
    area = math.pi * (r * r)
    return area

def calPentagon():
    a = int(input("enter the length of one side of the Pentagon (cm): "))
    area = (math.sqrt(5 * (5 + 2 * (math.sqrt(5)))) * a * a) / 4
    return area

def calHexagon():
    a = int(input("enter the length of one side of the Hexagon (cm): "))
    area = ((3 * math.sqrt(3) * (a * a)) / 2)
    return area

def calOctagon():
    a = int(input("enter the length of one side of the Octagon (cm): "))
    area = (2 * (1 + (math.sqrt(2))) * a * a)
    return area

# Volume

def calCube():
    a = int(input("enter the length of the Cube (cm): "))
    volume = a * a * a
    return volume

def calRectanglePrism():
    l = int(input("enter the length of the Rectangle Prism (cm): "))
    w = int(input("enter the width of the Rectangle Prism (cm): "))
    h = int(input("enter the height of the Rectangle Prism (cm): "))
    volume = w * h * l
    return volume

def calCylinder():
    r = int(input("enter the radius of the Cylinder (cm): "))
    h = int(input("enter the height of the Cylinder (cm): "))
    volume = math.pi * (r * r) * h
    return volume