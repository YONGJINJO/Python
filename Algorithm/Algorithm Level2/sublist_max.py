def sublist_max(profits, start, end):
    if start == end:
        return profits[start]
    left_max = sublist_max(profits, start, (start + end) // 2)
    right_max = sublist_max(profits, (start + end) // 2 + 1, end)
    central_value = central_max(profits, start, end)
    return max(left_max, right_max, central_value)


def central_max(profits, start, end):
    mid = (start + end) // 2
    right_max = profits[mid + 1]
    left_max = profits[mid]
    left_value = 0
    right_value = 0
    for i in range(mid + 1, end + 1):
        right_value += profits[i]
        right_max = max(right_max, right_value)

    for i in range(mid, start - 1, -1):
        left_value += profits[i]
        left_max = max(left_max, left_value)

    return left_max + right_max





list1 = [-2, -3, 4, -1, -2, 1, 5, -3]
print(sublist_max(list1, 0, len(list1) - 1))

list2 = [4, 7, -6, 9, 2, 6, -5, 7, 3, 1, -1, -7, 2]
print(sublist_max(list2, 0, len(list2) - 1))

list3 = [9, -8, 0, -7, 8, -6, -3, -8, 9, 2, 8, 3, -5, 1, -7, -1, 10, -1, -9, -5]
print(sublist_max(list3, 0, len(list3) - 1))

list4 = [-9, -8, -8, 6, -4, 6, -2, -3, -10, -8, -9, -9, 6, 2, 8, -1, -1]
print(sublist_max(list4, 0, len(list4) - 1))