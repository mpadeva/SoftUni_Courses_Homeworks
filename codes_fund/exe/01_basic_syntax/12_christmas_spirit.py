quantity = int(input())
days = int(input())

spirit_counter = 0
total_cost = 0

for i in range(1, days + 1):
    if i % 11 == 0:
        quantity += 2
    if i % 2 == 0:
        total_cost += (2 * quantity)
        spirit_counter += 5
    if i % 3 == 0:
        total_cost += (8 * quantity)
        spirit_counter += 13
    if i % 5 == 0:
        total_cost += (15 * quantity)
        spirit_counter += 17
        if i % 5 == 0 and i % 3 == 0:
            spirit_counter = spirit_counter + 30
    if i % 10 == 0:
        spirit_counter -= 20
        total_cost += (5 + 3 + 15)

if days % 10 == 0:
    spirit_counter -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {spirit_counter}")

