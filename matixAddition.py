mat1Rows = int(input("Enter the number of rows for the first matrix: "))
mat1Cols = int(input("Enter the number of columns for the first matrix: "))

mat2Rows = int(input("Enter the number of rows for the second matrix: "))
mat2Cols = int(input("Enter the number of columns for the second matrix: "))

if mat1Rows != mat2Rows or mat1Cols != mat2Cols:
    print("Matrix addition is not possible. Dimensions are not compatible.")
    exit()

# Input for the first matrix
matrix1 = []
print("Enter the elements of the first matrix:")
for i in range(mat1Rows):
    row = []
    for j in range(mat1Cols):
        element = int(input(f"Enter {i + 1}th row & {j + 1}th column element of the first matrix: "))
        row.append(element)
    matrix1.append(row)

# Input for the second matrix
matrix2 = []
print("\nEnter the elements of the second matrix:")
for i in range(mat2Rows):
    row = []
    for j in range(mat2Cols):
        element = int(input(f"Enter {i + 1}th row & {j + 1}th column element of the second matrix: "))
        row.append(element)
    matrix2.append(row)

# Matrix addition
result = [[0 for _ in range(mat1Cols)] for _ in range(mat1Rows)]
for i in range(mat1Rows):
    for j in range(mat1Cols):
        result[i][j] = matrix1[i][j] + matrix2[i][j]

print("\nResult of matrix addition:")
for i in range(mat1Rows):
    print("|", end=" ")
    for j in range(mat1Cols):
        if j < mat1Cols - 1:
            print(result[i][j], end=", ")
        else:
            print(result[i][j], end=" | ")
    print()
