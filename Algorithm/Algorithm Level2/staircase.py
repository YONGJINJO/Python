def staircase(n):
    if n == 0 or n == 1:
        return 1
    a = 1
    b = 1
    for i in range(n):
        a, b = b, a + b
    return a

'''
    왜 처음한게 시간이 초과 되었을까?
    그건 한번 계산한걸 보관하지 않고 또 계산해야되니까 시간복잡도가 2^n이 된다
    2 의 41승 의 경우 어마어마한 시간이 걸리므로 시간이 초과되는 듯
    그러므로 한번 계산한 걸 보관해서 그걸 또 계산하지 않고 다시 사용하는 것이 필요하다
    이부분 복습하기
'''

print(staircase(0))
print(staircase(5))
print(staircase(15))
print(staircase(25))
print(staircase(41))