def confirm_exit():
    answer = input("Are you sure you want to exit? (y/n): ").strip().lower()
    if answer == "y":
        print("Exiting the game.")
        return True

    elif answer == "n":
        print("Returning to the game.")
        return False

    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        return confirm_exit()

def confirm_int():
    while True:
        try:
            value = int(input("Enter your choice: "))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def confirm_float():
    while True:
        try:
            value = float(input("Enter a number: "))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid float.")