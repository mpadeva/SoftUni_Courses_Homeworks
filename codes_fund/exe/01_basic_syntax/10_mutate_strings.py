# temp = 'Hello word'
# print(temp[5:7])

first = input()
second = input()

result = first
for index in range(len(first)):
    if first[index] == second[index]:
        continue

    result = second[:index + 1] + first[index + 1:]
    print(result)