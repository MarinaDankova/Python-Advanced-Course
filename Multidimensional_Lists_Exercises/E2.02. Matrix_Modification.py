def is_invalid_position(n, row, col):
    if row < 0 or col < 0 or row >= n or col >= n:
        return True
    return False


n = int(input())

matrix = []

for _ in range(n):
    matrix.append([int(x) for x in input().split()])

while True:
    line = input()
    if line == 'END':
        break
    command, r, c, value = line.split()
    row, col, value = int(r), int(c), int(value)
    if is_invalid_position(n, row, col):
        print("Invalid coordinates")
        continue

    if command == 'Add':
        matrix[row][col] += value
    elif command == 'Subtract':
        matrix[row][col] -= value

for row_elements in matrix:
    print(' '.join([str(x) for x in row_elements]))
