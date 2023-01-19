divisor = int(input())
max_num = int(input())

# result = 0
# for num in range (1, max_num + 1):
for num in range (max_num + 1, 0, -1):
    if num % divisor == 0:
        print(num)
        break


# print(result)