n = int(input())

set_names = set()

for _ in range(n):
    set_names.add(input())
[print("".join(x)) for x in set_names]

