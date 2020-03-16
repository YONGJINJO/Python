def sublist_max_n_2(profits):
    temp = profits[0]
    temp_max = profits[0]
    for i in range(1, len(profits)):
        temp = max(profits[i], temp + profits[i])
        temp_max = max(temp, temp_max)
    return temp_max

print(sublist_max_n_2([7, -3, 4, -8]))
print(sublist_max_n_2([-2, -3, 4, -1, -2, 1, 5, -3, -1]))