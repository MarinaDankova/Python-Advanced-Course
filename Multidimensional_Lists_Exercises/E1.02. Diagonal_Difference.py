rows = int(input())

matrix = []

for _ in range(rows):
    matrix.append([(int(x)) for x in (input().split())])

primary = []
secondary = []

for row in range(rows):
    primary.append(matrix[row][row])
    secondary.append(matrix[row][rows - 1 - row])

diff = abs(sum(primary) - sum(secondary))
print(diff)
