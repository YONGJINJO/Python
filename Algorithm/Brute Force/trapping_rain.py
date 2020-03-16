def trapping_rain(buildings):
    total_height = 0
    for i in range(1, len(buildings) - 1):
        max_left = max(buildings[:i])
        max_right = max(buildings[i:])
        upper_bound = min(max_left, max_right)
        total_height += (0, upper_bound - buildings[i])
    return total_height






'''def trapping_rain(buildings):
    rain_amount = 0
    count = 0
    while count < len(buildings) - 1:
        next_count = count + 1
        while next_count > count and next_count <= len(buildings) - 1:
            if buildings[count] <= buildings[next_count]:
                plus = ((next_count - count - 1) * buildings[count]) - sum(buildings[count + 1: next_count])
                rain_amount += plus
                count = next_count
                continue
            else:
                next_count += 1
        if count != next_count:
            count += 1
    return rain_amount

print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
'''