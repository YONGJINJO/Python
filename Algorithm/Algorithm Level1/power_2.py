def power_2(x, y):
    if y == 1:
        return x
    if y % 2 == 1:
        return x * power_2(x, y // 2) * power_2(x, y // 2)
    else:
        return power_2(x, y // 2) * power_2(x, y // 2)



print(power_2(3, 5))
print(power_2(5, 6))
print(power_2(7, 9))

