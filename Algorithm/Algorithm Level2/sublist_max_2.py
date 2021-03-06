def sublist_max_2(profits, start = 0, end = None):
    if end is None:
        end = len(profits) - 1
    if start == end:
        return profits[start]
    mid = (start + end) // 2
    left_max = sublist_max_2(profits, start, mid)
    right_max = sublist_max_2(profits, mid + 1, end)
    central = central_max(profits, start, end)
    true_max = max(left_max, right_max, central)
    return true_max

def central_max(profits, start, end):
    mid = (start + end) // 2
    left_max = profits[mid]
    right_max = profits[mid + 1]
    left_value = left_max
    right_value = right_max
    for i in range(mid - 1, -1):
        left_value += profits[i]
        left_max = max(left_value, left_max)
    for i in range(mid + 2, end):
        right_value += profits[i]
        right_max = max(right_value, right_max)
    return left_max + right_max

list1 = [-2, -3, 4, -1, -2, 1, 5, -3]
print(sublist_max_2(list1, 0, len(list1) - 1))

list2 = [4, 7, -6, 9, 2, 6, -5, 7, 3, 1, -1, -7, 2]
print(sublist_max_2(list2, 0, len(list2) - 1))

list3 = [9, -8, 0, -7, 8, -6, -3, -8, 9, 2, 8, 3, -5, 1, -7, -1, 10, -1, -9, -5]
print(sublist_max_2(list3, 0, len(list3) - 1))

list4 = [-9, -8, -8, 6, -4, 6, -2, -3, -10, -8, -9, -9, 6, 2, 8, -1, -1]
print(sublist_max_2(list4, 0, len(list4) - 1))