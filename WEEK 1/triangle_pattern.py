def lower_triangular(n):
    print("\nLower Triangular Pattern:")
    for i in range(1, n + 1):
        print("* " * i)

def upper_triangular(n):
    print("\nUpper Triangular Pattern:")
    for i in range(n, 0, -1):
        print("* " * i)

def pyramid(n):
    print("\nPyramid Pattern:")
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)

print("\nWEEK 1 ASSIGNMENT")
if __name__ == "__main__":
    try:
        n = int(input("Enter the number of rows : "))
        if n <= 0:
            print("Please enter a positive integer greater than 0.")
        else:
            lower_triangular(n)
            upper_triangular(n)
            pyramid(n)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

