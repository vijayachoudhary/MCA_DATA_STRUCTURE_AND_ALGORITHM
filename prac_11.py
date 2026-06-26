def demonstrate_column_major():
    matrix = [
        [8, 9, 10],
        [11, 12, 13],
        [14, 15, 16]
    ]

    rows = len(matrix)
    cols = len(matrix[0])

    flat_memory = []

    print("Logical 2D Matrix View:")
    for row in matrix:
        print(row)

    # Column Major Order Traversal
    for j in range(cols):
        for i in range(rows):
            flat_memory.append(matrix[i][j])

    print("\nColumn Major Order (Flat Memory Representation):")
    print(flat_memory)


# Run program
demonstrate_column_major()