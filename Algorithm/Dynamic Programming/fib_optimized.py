def fib_optimized(n):
    current = 1
    previous = 1
    for i in range(3, n + 1):
        current, previous = current + previous, current    # 파이썬스러운 변수 바꾸기
    return current

# 테스트
print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))
