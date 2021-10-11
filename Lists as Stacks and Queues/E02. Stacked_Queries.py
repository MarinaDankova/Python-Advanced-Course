N = int(input())
stack = []

for i in range(N):
    command = input()
    if command.startswith('1'):
        command = command.split()
        stack.append(command[1])
    elif command.startswith('2'):
        command = command.split()
        stack.pop()
    elif command.startswith('3'):
        if stack:
            print(max(stack))
    elif command.startswith('4'):
        if stack:
            print(min(stack))

reversed_stack = []

while stack:
    reversed_stack.append(stack.pop())

print(', '.join(reversed_stack))

