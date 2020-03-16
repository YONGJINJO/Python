def fib_memo(n, cache):
    if n == 1 or n == 2:
        return 1
    if n in cache:
        return cache[n]
    cache[n] = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)
    return cache[n]

def fib(n):
    cache = {}
    return fib_memo(n, cache)

def fib_tab(n):
    fib_table = [0, 1, 1]

    for i in range(3, n + 1):
        fib_table.append(fib_table[i - 1] + fib_table[i - 2])

    return fib_table[n]

def fib_optimized(n):
    current = 1
    previous = 0
    for i in range(1, n):
        current, previous = current + previous, current

    return current


print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))