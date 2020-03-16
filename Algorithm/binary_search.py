def binary_search(element, some_list):
    start = 0
    end = len(some_list) - 1
    while True:                 # O(lgn)
        mid = (end + start) // 2
        if element == some_list[mid]:
            return mid
        elif element > some_list[mid]:
            start = mid
        else :
            end = mid
        if start == end - 1:
            if element == some_list[start]:
                return start
            elif element == some_list[end]:
                return end
            else:
                return None

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))