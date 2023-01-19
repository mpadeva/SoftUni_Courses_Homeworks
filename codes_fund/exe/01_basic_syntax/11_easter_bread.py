budget = float(input())

flour_price = float(input())
eggs_price = 0.75 * flour_price
milk_price = 1.25 * flour_price
milk_price_per_loaf = 0.25 * milk_price

loaf_price = flour_price + eggs_price + milk_price_per_loaf

loaves_counter = 0
coloured_eggs_counter = 0

while loaf_price <= budget:
    loaves_counter += 1
    budget -= loaf_price
    coloured_eggs_counter += 3

    if loaves_counter % 3 == 0:
        coloured_eggs_counter -= (loaves_counter -2)

print(f'You made {loaves_counter} loaves of Easter bread! Now you have {coloured_eggs_counter} eggs and {budget:.2f}BGN left.')