while True:
    line = input()
    if line == "End":
        break
    #   с break спираме изпълнението на цикъла
    if line == "SoftUni":
        continue
    #   с continue прескачаме думата СофтУни и не изпълняваме кода

    for ch in line:
        print(f"{ch}{ch}", end='')

    print()

