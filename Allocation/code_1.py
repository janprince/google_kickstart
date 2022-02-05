test_cases = int(input("number of test cases: "))

for i in range(test_cases):
    N_houses, B_budget = (int(input("No of houses: ")), int(input("Budget: ")))
    house_prices = []

    for n in range(N_houses):
        price = int(input(f"Enter price of house {n + 1}"))
        house_prices.append(price)

    house_prices.sort()
    sum = 0
    max_houses = 0
    for o in house_prices:
        if sum < B_budget:
            sum += o
        else:
            max_houses = house_prices.index(o)
            break

    print(f"Case #{i+1}: max_houses")
