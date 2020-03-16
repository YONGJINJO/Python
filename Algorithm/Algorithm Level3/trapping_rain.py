'''def trapping_rain(buildings):
    total_water = 0
    for i in range(1, len(buildings) - 1):
        max_left = max(buildings[:i])
        max_right = max(buildings[i + 1:])
        upper_bound = min(max_left, max_right)

        total_water += max(0, upper_bound - buildings[i])
'''
def trapping_rain(buildings):
    total_water = 0
    right_list = [0]
    max_left = buildings[0]
    for i in range(1, len(buildings)):
        max_right = max(right_list[0], buildings[len(buildings) - i])
        right_list.insert(0, max_right)
    for i in range(1, len(buildings) - 1):
        max_left = max(max_left, buildings[i - 1])
        upper_bound = min(max_left, right_list[i])

        total_water += max(0, upper_bound - buildings[i])

    return total_water


print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))