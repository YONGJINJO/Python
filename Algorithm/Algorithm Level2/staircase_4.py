def staircase_4(stairs, possible_steps):
    '''if stairs == 0 or stairs == 1:
        return 1
    count = 0
    for i in range(len(possible_steps)):
        if possible_steps[i] > stairs:
            plus = 0
        else:
            plus = staircase_4(stairs - possible_steps[i], possible_steps)
        count += plus
    return count
'''
    number = [1, 1]
    for height in range(2, stairs + 1):
        number.append(0)
        for step in possible_steps:
            if height - step >= 0:
                number[height] += number[height - step]
    return number[stairs]

print(staircase_4(5, [1, 2, 3]))
print(staircase_4(6, [1, 2, 3]))
print(staircase_4(7, [1, 2, 4]))
print(staircase_4(8, [1, 3, 5]))
