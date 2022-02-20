test_cases = int(input("number of test cases: "))

for i in range(test_cases):
    N_houses, B_budget = (int(input("No of houses: ")), int(input("Budget: ")))
    house_prices = []

    for n in range(N_houses):
        price = int(input(f"Enter price of house {n + 1}: "))
        house_prices.append(price)

    house_prices.sort()
    sum = 0
    max_houses = 0
    for (index, o) in enumerate(house_prices):
        if sum < B_budget and sum+o <= B_budget:
            sum += o
            max_houses = index + 1
        else:
            break

    print(f"Case #{i+1}: {max_houses}")
