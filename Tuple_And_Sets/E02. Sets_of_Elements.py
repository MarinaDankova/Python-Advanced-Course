n, m = input().split()

set_n = set()
set_m = set()

for x in range(int(n)):
    set_n.add(input())
for y in range(int(m)):
    set_m.add(input())
[print(z) for z in (set_n.intersection(set_m))]


