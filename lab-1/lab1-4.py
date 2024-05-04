rows = int(input("no of rows: "))
cols = int(input("no of columns: "))

if rows != cols:
    print("Error: Determinant can only be calculated for square matrices.")
else:
    a= []
    print("Enter the elements of the matrix (row-wise, separated by space):")
    for i in range(rows):
        row = list(map(int, input().split()))
        if len(row) != cols:
            print("error:entered no of cols doent not match the given cols")
            break
        a.append(row)

    def det_2x2(matrix):
        return a[0][0] * a[1][1] - a[0][1] * a[1][0]

    # Function to calculate determinant of a matrix
    def det(a):
        size = len(a)
        if size == 1:
            return a[0][0]
        elif size == 2:
            return det_2x2(a)
        else:
            result = 0
            for j in range(size):
                x = [row[:j] + row[j + 1:] for row in a[1:]]
                result += ((-1) ** j) * a[0][j] * det_2x2(x)
            return result

    result = det(a)
    print("Determinant of the matrix:", result)
