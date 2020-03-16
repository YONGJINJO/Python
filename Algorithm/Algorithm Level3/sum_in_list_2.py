def sum_in_list_2(search_sum, sorted_list):
    i = 0
    j = len(sorted_list) - 1
    while i < j:
        current_sum = sorted_list[i] + sorted_list[j]
        if current_sum == search_sum:
            return True
        elif current_sum < search_sum:
            i += 1
        elif current_sum > search_sum:
            j -= 1
    return False


print(sum_in_list_2(15, [1, 2, 5, 6, 7, 9, 11]))
print(sum_in_list_2(15, [1, 2, 5, 7, 9, 11]))