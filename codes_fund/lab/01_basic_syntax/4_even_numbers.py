n = int(input())
all_nums_even = True

for _ in range(n):
    number = int(input())

    if number % 2 != 0:
        all_nums_even = False
        print(f"{number} is odd!")
        break

if all_nums_even:
    print("All numbers are even.")