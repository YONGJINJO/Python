def binary_search(string, x, p = 0, r = None):
    if r == None:
        r = len(string) - 1
    if p > r:
        return None
    mid = (p + r) // 2
    if string[mid] == x:
        return mid
    elif string[mid] > x:
        return binary_search(string, x, mid + 1, r)
    else:
        return binary_search(string, x, p, mid - 1)



A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(A, 5))