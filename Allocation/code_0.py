# input_1
input_1 = input()
test_cases = int(input_1)

for i in range(test_cases):

    # input_2
    input_2 = input()
    input_2 = input_2.split()
    N_houses, B_budget = (int(input_2[0]), int(input_2[1]))

    # input_3
    input_3 = input()
    input_3 = input_3.split()
    house_prices = [int(i) for i in input_3]
    house_prices.sort()

    sum = 0
    max_houses = 0
    for (index, o) in enumerate(house_prices):
        if sum < B_budget and sum+o <= B_budget:
            sum += o
            max_houses = index + 1
        else:
            break

    print(f"Case #{i + 1}: {max_houses}")

"""
    lines of input looks like this:
    3                                           # no of test cases
    4 100                                       # no of houses & budget
    20 90 40 90                                 # prices of the houses
    4 50                                        # no of houses & budget
    30 30 10 10                                 # prices of the houses
    3 300                                       # no of houses & budget
    999 999 999                                 # prices of the houses
"""