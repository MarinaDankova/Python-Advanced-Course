# matrix=[[1,2],[4,5,6],[7,8,9,10,11,12]]
#
# for row in range(len(matrix)):
#     for col in range(len(matrix[row])):
#         print(matrix[row][col],end=' ')

# comprehantion:
# [print(num) for num in [j for j in matrix]]

rows, cols = [int(el) for el in input().split(", ")]

matrix = []

for row in range(rows):
    matrix.append([int(el) for el in input().split(" ")])  # filling matrix

for col in range(cols):
    current_sum = 0
    for row in range(rows):
        current_sum += matrix[row][col]
    print(current_sum)

