def sublist_max(profits):
    max_profit_so_far = profits[0]
    max_check = profits[0]
    for i in ranage(1, len(profits)):
        max_check = max(max_check + profits[i], profits[i])
        max_profit_so_far = max(max_check, max_profit_so_far)
    return max_profit_so_far


'''def sublist_max(profits):
    if len(profits) == 1:
        return profits[0]
    first_possibility = sublist_max(profits[:-1])
    second_possibility = profits[-1]
    for i in range(len(profits)):
        second_possibility = max(second_possibility, sum(profits[i:]))
    return max(second_possibility, first_possibility)


def sublist_max(profits):
    ex_list = {}
    for i in range(len(profits)):
        if profits[i] > 0 :
            ex_list[i] = profits[i]
    positive_location = list(ex_list.keys())
    max_list = []
    i = 0
    max_value = ex_list[positive_location[i]]
    positive_list = []
    while i < len(positive_location) - 1:
        print(ex_list[positive_location[i + 1]])
        if sum(ex_list[positive_location[i]:positive_location[i + 1]]) > 0:
            max_value = max(max_value,sum(ex_list[positive_location[i]:(positive_location[i + 1] + 1)]))
        i += 1
    return max_value
    '''


# 테스트
print(sublist_max([7, -3, 4, -8]))
print(sublist_max([-2, -3, 4, -1, -2, 1, 5, -3, -1]))