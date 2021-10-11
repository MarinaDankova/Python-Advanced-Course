rows = int(input())

matrix = []

for row in range(rows):
    matrix.append([int(el) for el in input().split(', ')])

list = [(x) for rows in matrix for x in rows]
print(list)


