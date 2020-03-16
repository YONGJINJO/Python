# 높이 n개의 계단을 올라가는 방법을 리턴한다

def staircase(stairs, possible_steps):
    if len(possible_steps) == 1 or stairs == 1 or stairs == 0:
        return 1
    elif stairs < 0:
        return 0
    stair = {}
    stair_case = 0
    for step in possible_steps:
        temp_case = staircase(stairs - step, possible_steps)
        stair_case += temp_case
    if stairs in stair:
        return stair[stairs]
    else:
        stair[stairs] = stair_case
    return stair[stairs]



print(staircase(5, [1, 2, 3]))
print(staircase(6, [1, 2, 3]))
print(staircase(7, [1, 2, 4]))
print(staircase(8, [1, 3, 5]))