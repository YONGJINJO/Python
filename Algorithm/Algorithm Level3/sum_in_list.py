'''def sum_in_list(search_sum, sorted_list):
    for element in sorted_list:
        if search_sum - element in sorted_list:
            return True
    return False
'''

def sum_in_list(search_sum, sorted_list):
    mid = len(sorted_list) // 2
    j = -1
    for i in range(mid + 1):
        if sorted_list[i] + sorted_list[j] == search_sum:
            return True
        elif sorted_list[i] + sorted_list[j] > search_sum:
            j -= 1
    return False


print(sum_in_list(15, [1, 2, 5, 6, 7, 9, 11]))
print(sum_in_list(15, [1, 2, 5, 7, 9, 11]))