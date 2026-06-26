#Two-dimensional array

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input(f"Enter element for position ({i},{j}): "))
        row.append(element)
    matrix.append(row)

print("2D Array (Matrix):")
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], end=' ')
    print()

