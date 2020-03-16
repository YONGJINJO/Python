def min_fee(pages_to_print):
    total_fee = 0
    pages_to_print = sorted(pages_to_print)
    for number in range(len(pages_to_print)):
        total_fee += sum(pages_to_print[:(number + 1)])
    return total_fee



# 테스트
print(min_fee([6, 11, 4, 1]))
print(min_fee([3, 2, 1]))
print(min_fee([3, 1, 4, 3, 2]))
print(min_fee([8, 4, 2, 3, 9, 23, 6, 8]))
