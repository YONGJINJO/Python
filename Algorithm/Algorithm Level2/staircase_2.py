'''def staircase_2(n):
    count = 0
    if n == 0 or n == 1:
        return 1
    count += staircase_2(n - 1) + staircase_2(n -2)
    return count
'''
def staircase_2(n):
    if n == 1 or n == 0:
        return 1
    a = 1
    b = 1
    for i in range(n):
        a, b = b, a + b
    return a

print(staircase_2(0))
print(staircase_2(6))
print(staircase_2(15))
print(staircase_2(25))
print(staircase_2(41))
