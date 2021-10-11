n = int(input())

dict = {}

for _ in range(n):
    name, grade = input().split()
    if name not in dict:
        dict[name] = []
    dict[name].append(grade)


for key, value in dict.items():
    if value:
        value_ = [float(x) for x in value]
        avg_grade = sum(value_) / len(value_)
        print(f'{key} -> {" ".join(value)} (avg: {avg_grade:.2f})')

