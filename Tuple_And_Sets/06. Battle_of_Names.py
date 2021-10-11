import math

n = int(input())

odd_set = set()
even_set = set()
row = 0

for _ in range(n):
    name = list(input())
    row += 1
    name_sum = math.floor((sum([ord(x) for x in name]))/row)
    if name_sum % 2 == 1:
        odd_set.add(name_sum)
    else:
        even_set.add(name_sum)
sum_odd = sum(odd_set)
sum_even = sum(even_set)
if sum_even == sum_odd:
    result = (odd_set.union(even_set))
    print(", ".join(str(x) for x in result))
elif sum_odd > sum_even:
    result = (odd_set.difference(even_set))
    print(", ".join(str(x) for x in result))
elif sum_even > sum_odd:
    result = odd_set.symmetric_difference(even_set)
    print(", ".join(str(x) for x in result))

