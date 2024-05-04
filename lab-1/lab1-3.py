rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

print("Enter the elements of the first matrix (row-wise, separated by space):")
a = []
for i in range(rows):
    row = list(map(int, input().split()))
    if len(row) != columns:
        print("error:entered no of cols doent not match the given cols")
        break
    a.append(row)

print("Enter the elements of the second matrix (row-wise, separated by space):")
b = []
for i in range(rows):
    row = list(map(int, input().split()))
    if len(row) != columns:
        print("error:entered no of cols doent not match the given cols")
        break
    b.append(row)

sum = []
for i in range(rows):
    sum_row = []
    for j in range(columns):
        sum_row.append(a[i][j] + b[i][j])
    sum.append(sum_row)

print("Sum of the two matrices:")
for row in sum:
    print(row)
