'''def power(x, y):
    result = 1
    mul_value = x * x
    while y > 0 :
        if (y % 2) == 0:
            result *= mul_value
        else:
            result *= mul_value * x
        y = y // 2
'''
def power(x, y):
    if y == 1:
        return x
    subresult = power(x, y //2)
    if y % 2 == 1:
        return x * subresult * subresult
    else :
        return subresult * subresult



print(power(3, 5))
print(power(5, 6))
print(power(7, 9))