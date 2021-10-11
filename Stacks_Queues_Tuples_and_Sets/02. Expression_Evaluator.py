from collections import deque

arithmetic_expressions = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a // b,
}
chars = input().split()

numbers = deque()
for ch in chars:
    if ch in arithmetic_expressions:
        result = numbers.popleft()
        while numbers:
            number = numbers.popleft()
            result = arithmetic_expressions[ch](result, number)
        numbers.append((result))

    else:
        numbers.append(int(ch))
print(numbers.popleft())

