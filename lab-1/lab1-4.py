rows = int(input("Number of rows: "))
cols = int(input("Number of columns: "))

if rows != cols:
    print("Error: Determinant can only be calculated for square matrices.")
else:
    a = []
    print("Enter the elements of the matrix (row-wise, separated by space):")
    for i in range(rows):
        row = list(map(int, input().split()))
        if len(row) != cols:
            print("error:entered no of cols doent not match the given cols")
            break
        a.append(row)

    # Function to calculate determinant of a 2x2 matrix
    def det_2x2(matrix):
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    # Function to calculate determinant of a matrix
    def det(matrix):
        size = len(matrix)
        if size == 1:
            return matrix[0][0]
        elif size == 2:
            return det_2x2(matrix)
        else:
            result = 0
            for j in range(size):
                x = [row[:j] + row[j + 1:] for row in matrix[1:]]
                result += ((-1) ** j) * matrix[0][j] * det(x)
            return result

    result = det(a)
    print("Determinant of the matrix:", result)
