nums = tuple([float(el) for el in input().split()])  # тюпъл с лист с числа

result = {}  #  dictionary

for num in nums:
    if num not in result:
        result[num] = 0  # create a dictionary
    result[num] += 1

for key, value in result.items():
    print(f'{key} - {value} times')

# or
# [print(f'{key} - {value} times') for key, value in result.items()]


# sorting

# sorted_result=sorted(result.items(), key =lambda x:x[0])
# or #sorted_result=sorted(result.items(), key =lambda x:x[1])
# or #sorted_result=sorted(result.items(), key =lambda x:x[1], reversed=True)
# or #sorted_result=sorted(result.items(), key =lambda x:-x[1])

# for key,value in sorted_result:
# print(f'{key} - {value} times')
