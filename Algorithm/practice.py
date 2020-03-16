water = {}
list = [1, 2, 3, 4, 5]
water[0] = list
list.append(6)
print(list)
water[0].append(7)
print(water)


for i in reversed(range(1,10)):
    print(i)