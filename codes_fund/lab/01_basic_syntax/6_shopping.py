budget = int(input())
command = input()


while command != "End":
    current_price = int(command)
    budget -= current_price
    if budget < 0:
        print(f"You went in overdraft!")
        break

    command = input()

else:
    print(f"You bought everything needed.")