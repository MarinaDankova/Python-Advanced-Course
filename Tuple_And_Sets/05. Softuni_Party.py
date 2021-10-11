n = int(input())

all_quests = set()

for _ in range(n):
    all_quests.add(input())

ticket = input()

arrived = set()
while not ticket == 'END':
    arrived.add(ticket)
    ticket = input()


print(len(all_quests.difference(arrived)))
result = all_quests.difference(arrived)

sorted_result = sorted(result, key=lambda x: x[0])
[print(x) for x in sorted_result]

