import math

print("==================")
print("Area Calculator 📐")
print("==================")

while True:
    print("\n1) Triangle")
    print("2) Rectangle")
    print("3) Square")
    print("4) Circle")
    print("5) Quit")

    choice = input("\nWhich shape: ")

    if choice == "1":
        base = float(input("Base: "))
        height = float(input("Height: "))
        area = 0.5 * base * height
        print(f"\nThe area is {area}")

    elif choice == "2":
        length = float(input("Length: "))
        width = float(input("Width: "))
        area = length * width
        print(f"\nThe area is {area}")

    elif choice == "3":
        side = float(input("Side: "))
        area = side ** 2
        print(f"\nThe area is {area}")

    elif choice == "4":
        radius = float(input("Radius: "))
        area = math.pi * radius ** 2
        print(f"\nThe area is {area:.2f}")

    elif choice == "5":
        print("\nGoodbye! 👋")
        break

    else:
        print("\nInvalid choice. Please select a valid option.")
