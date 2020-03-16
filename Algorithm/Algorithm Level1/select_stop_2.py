def select_stops_2(water_stops, capacity):
    stops = []
    current = capacity - water_stops[0]
    for i in range(1, len(water_stops)):
        distance = water_stops[i] - water_stops[i - 1]
        current -= distance
        if current < 0:
            stops.append(water_stops[i - 1])
            current = capacity - distance
    stops.append(water_stops[-1])
    return stops

list1 = [1, 4, 5, 7, 11, 12, 13, 16, 18, 20, 22, 24, 26]
print(select_stops_2(list1, 4))

list2 = [5, 8, 12, 17, 20, 22, 23, 24, 28, 32, 38, 42, 44, 47]
print(select_stops_2(list2, 6))