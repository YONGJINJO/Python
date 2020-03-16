def fib_tab(n):
    fib = [0, 1, 1]
    for i in range(3, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]

# 테스트
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))