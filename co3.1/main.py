from graphics.rectangle import area as rect_area, perimeter as rect_perimeter
from graphics.circle import area as circle_area, perimeter as circle_perimeter

# 3D Cuboid
from graphics.threedgraphics.cuboid import *
cb_a = area
cb_p = perimeter

# 3D Sphere
from graphics.threedgraphics.sphere import *
sp_a = area
sp_p = perimeter

while True:  # loop until user chooses to exit
    # --- User Choice ---
    print("\nChoose a shape (or 0 to Exit):")
    print("1. Rectangle")
    print("2. Circle")
    print("3. Cuboid")
    print("4. Sphere")
    print("0. Exit")

    choice = input("Enter your choice (0-4): ")

    if choice == "0":
        print("Exiting program...")
        break

    elif choice == "1":
        length = float(input("Enter rectangle length: "))
        breadth = float(input("Enter rectangle breadth: "))
        print("Rectangle area:", rect_area(length, breadth))
        print("Rectangle perimeter:", rect_perimeter(length, breadth))

    elif choice == "2":
        radius = float(input("Enter circle radius: "))
        print("Circle area:", circle_area(radius))
        print("Circle perimeter:", circle_perimeter(radius))

    elif choice == "3":
        length = float(input("Enter cuboid length: "))
        breadth = float(input("Enter cuboid breadth: "))
        height = float(input("Enter cuboid height: "))
        print("Cuboid area:", cb_a(length, breadth, height))
        print("Cuboid perimeter:", cb_p(length, breadth, height))

    elif choice == "4":
        radius = float(input("Enter sphere radius: "))
        print("Sphere area:", sp_a(radius))
        print("Sphere perimeter:", sp_p(radius))

    else:
        print("Invalid choice! Please enter a number from 0 to 4.")
