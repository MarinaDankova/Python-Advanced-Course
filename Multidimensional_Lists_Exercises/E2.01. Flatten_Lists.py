numbers= input().split('|')

result=[]

for n in range(len(numbers)-1,-1,-1):
    elements=numbers[n].split()
    result+=elements

print(' '.join(result))
