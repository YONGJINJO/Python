'''def max_profit_memo(price_list, count, cache):
    if count < 1:
        cache[count] = price_list[count]
        return cache[count]
    elif count in cache:
        return cache[count]
    if count < len(price_list):
        max_value = price_list[count]
    else:
        max_value = 0
    for i in range(1, count // 2 + 1):
        max_value = max(max_value, max_profit_memo(price_list, i, cache) + max_profit_memo(price_list, count - i, cache))
    cache[count] = max_value
    return cache[count]

def max_profit(price_list, count):
    cache = {}
    return max_profit_memo(price_list, count, cache)
'''

def max_profit(price_list, count):
    max_tab = price_list[:2]
    for i in range(2, count + 1):
        if i < len(price_list):
            max_value = price_list[i]
        else:
            max_value = 0
        for j in range(1, i // 2 + 1):
            max_value = max(max_value, max_tab[j] + max_tab[i - j])
        max_tab.append(max_value)
    return max_tab[count]


print(max_profit([0, 200, 600, 900, 1200, 2000], 5))
print(max_profit([0, 300, 600, 700, 1100, 1400], 8))
print(max_profit([0, 100, 200, 400, 600, 900, 1200, 1300, 1500, 1800], 9))
