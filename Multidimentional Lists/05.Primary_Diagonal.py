# matrix=[[1,2,3],[4,5,6],[7,8,9]]  manipulation values in matrix
#
# for i in range(len(matrix)):
#     for j in range(len(matrix)):
#         matrix[i][j]+=1


n = int(input())

matrix = []

for row in range(n):
    matrix.append([int(el) for el in (input()).split()])

result = 0
for row in range(n):
    for col in range(n):
        if col == row:
            result += matrix[row][col]

print(result)

