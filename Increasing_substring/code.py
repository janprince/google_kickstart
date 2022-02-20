def processcase(case_num):

    # length of string,n and string, s
    n = int(input())
    s = input()

    # convert s to a list type
    s_list = list(s)

    # length of the longest strictly increasing substring that ends at position i
    lengths = []

    for i in range(n):
        if len(s_list) == 1:
            lengths.append(1)
            break
        elif i == 0:
            lengths.append(1)
            continue
        else:
            decreasing_chars = []
            for j in range(i, -1, -1):
                if s_list[j] > s_list[j - 1]:
                    decreasing_chars.append(s_list[j])
                    if j - 1 == 0:
                        decreasing_chars.append(s_list[j - 1])
                        break
                elif s_list[j] <= s_list[j-1]:
                    decreasing_chars.append(s_list[j])
                    break
            lengths.append(len(decreasing_chars))

    # string format for lengths
    len_str = " ".join([str(i) for i in lengths])
    print(f"Case #{case_num}: {len_str}")

num_cases = int(input())
for i in range(num_cases):
    processcase(i + 1)
