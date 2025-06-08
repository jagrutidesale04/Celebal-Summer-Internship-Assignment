print("\nWEEK 1 ASSIGNMENT")

rows = int(input("Enter the number of rows for the triangle patterns: "))

print("\nLower Triangular Pattern")
for i in range(1, rows + 1):
    print("*" * i)
  
print("\nUpper Triangular Pattern")
for i in range(rows, 0, -1):
    print(" " * (rows - i) + "*" * i)
  
print("\nPyramid Pattern")
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
