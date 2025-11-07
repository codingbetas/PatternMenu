# Pattern Menu Program

def half_pyramid(n):
    for i in range(1, n + 1):
        print("* " * i)

def inverted_half_pyramid(n):
    for i in range(n, 0, -1):
        print("* " * i)

def full_pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)

def inverted_full_pyramid(n):
    for i in range(n, 0, -1):
        print(" " * (n - i) + "* " * i)

def diamond(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "* " * i)

def hollow_full_pyramid(n):
    for i in range(1, n + 1):
        if i == 1:
            print(" " * (n - i) + "*")
        elif i == n:
            print("* " * n)
        else:
            print(" " * (n - i) + "*" + " " * (2 * (i - 1) - 1) + "*")

def hollow_diamond(n):
    # upper part
    for i in range(1, n + 1):
        if i == 1:
            print(" " * (n - i) + "*")
        else:
            print(" " * (n - i) + "*" + " " * (2 * (i - 1) - 1) + "*")
    # lower part
    for i in range(n - 1, 0, -1):
        if i == 1:
            print(" " * (n - i) + "*")
        else:
            print(" " * (n - i) + "*" + " " * (2 * (i - 1) - 1) + "*")

def hourglass(n):
    for i in range(n, 0, -1):
        print(" " * (n - i) + "* " * i)
    for i in range(2, n + 1):
        print(" " * (n - i) + "* " * i)

# --- Main Program ---
while True:
    print("\nPattern Menu")
    print("1. Half Pyramid")
    print("2. Inverted Half Pyramid")
    print("3. Full Pyramid")
    print("4. Inverted Full Pyramid")
    print("5. Diamond")
    print("6. Hollow Full Pyramid")
    print("7. Hollow Diamond")
    print("8. Hourglass")
    print("9. Exit")

    choice = int(input("Enter your choice (1-9): "))
    if choice == 9:
        print("Goodbye!")
        break

    n = int(input("Enter the number of rows: "))

    if choice == 1:
        half_pyramid(n)
    elif choice == 2:
        inverted_half_pyramid(n)
    elif choice == 3:
        full_pyramid(n)
    elif choice == 4:
        inverted_full_pyramid(n)
    elif choice == 5:
        diamond(n)
    elif choice == 6:
        hollow_full_pyramid(n)
    elif choice == 7:
        hollow_diamond(n)
    elif choice == 8:
        hourglass(n)
    else:
        print("Invalid choice! Please enter a number between 1–9.")
