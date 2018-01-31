# Celsius / Fahrenheit temperature converter


def menu():
    print("\n1. Convert Celsius to Fahrenheit")
    print("2. Convert Fahrenheit to Celsius")
    print("3. Exit")
    pick = int(input("Enter your choice: "))
    return pick


def to_celsius(f):
    return int((f - 32) / 1.8)


def to_fahrenheit(c):
    return int(c * 1.8 + 32)


def main():
    choice = menu()
    while choice != 3:
        if choice == 1:
            # convert C to F
            c = eval(input("Enter degrees in Celsius: "))
            print(str(c) + "C = " + str(to_fahrenheit(c)) + "F")
        elif choice == 2:
            # convert F to C
            f = eval(input("Enter degrees in Fahrenheit: "))
            print(str(f) + "F = " + str(to_celsius(f)) + "C")
        else:
            print("Invalid entry.")
        choice = menu()


main()