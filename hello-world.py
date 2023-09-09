print("Hello Mathematics World!")

height = int(input("Enter the height of the shape (cm): "))
length = int(input("Enter the length of the shape (cm): "))
depth = int(input("Enter the depth of the shape (cm): "))

square = length * height
cube = square * depth

print("")
print("--------------------------------->")
print("Info on the shape: ")
print("height:", height, "cm")
print("length:", length, "cm")
print("depth:", depth, "cm")
print("area:", square, "cm2")
print("volume:", cube, "cm3")
print("")