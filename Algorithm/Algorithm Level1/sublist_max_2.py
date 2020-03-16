def sublist_max_2(profits):
    max_profit = 0
    for i in range(len(profits)):
        total = profits[i]
        for j in range(i + 1, len(profits)):
            total += profits[j]
            max_profit = max(max_profit,total)
    return max_profit

print(sublist_max_2([4, 3, 8, -2, -5, -3, -5, -3]))
print(sublist_max_2([2, 3, 1, -1, -2, 5, -1, -1]))
print(sublist_max_2([7, -3, 14, -8, -5, 6, 8, -5, -4, 10, -1, 8]))