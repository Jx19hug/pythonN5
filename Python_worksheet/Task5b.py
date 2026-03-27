#menu
print("The Equation Program")

while True:
    print("\nPlease select an option from the following menu")
    print("1. Calculate the speed")
    print("2. Calculate the distance")
    print("3. Calculate the time")
    print("4. Calculate the area of a rectangular room")
    print("5. Exit Program")
    choice = input("Enter choice (1-5): ").strip()

    if choice == '1':
        try:
            distance = float(input("Enter distance (e.g. meters): "))
            time = float(input("Enter time (e.g. seconds): "))
        except ValueError:
            print("Invalid input; please enter numeric values.")
            continue
        if time == 0:
            print("Time cannot be zero.")
        else:
            speed = distance / time
            print(f"Speed = {speed} (distance unit / time unit)")

    elif choice == '2':
        try:
            speed = float(input("Enter speed (e.g. meters/second): "))
            time = float(input("Enter time (e.g. seconds): "))
        except ValueError:
            print("Invalid input; please enter numeric values.")
            continue
        distance = speed * time
        print(f"Distance = {distance} (distance unit)")

    elif choice == '3':
        try:
            distance = float(input("Enter distance (e.g. meters): "))
            speed = float(input("Enter speed (e.g. meters/second): "))
        except ValueError:
            print("Invalid input; please enter numeric values.")
            continue
        if speed == 0:
            print("Speed cannot be zero.")
        else:
            time = distance / speed
            print(f"Time = {time} (time unit)")

    elif choice == '4':
        try:
            length = float(input("Enter room length (e.g. meters): "))
            width = float(input("Enter room width (e.g. meters): "))
        except ValueError:
            print("Invalid input; please enter numeric values.")
            continue
        if length < 0 or width < 0:
            print("Length and width must be non-negative.")
        else:
            area = length * width
            print(f"Area = {area} square units")

    elif choice == '5':
        print("Exiting program.")
        break

    else:
        print("Invalid selection. Please choose a number from 1 to 5.")