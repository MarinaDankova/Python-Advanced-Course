rows = int(input())

matrix = []

for row in range(rows):
    matrix.append([int(el) for el in input().split(', ')])
only_even = [[x for x in row if x % 2 == 0] for row in matrix]

print(only_even)

