def find_same_number_2(some_list):
    list1 = []
    for number in some_list:
        if number in list1:
            return number
        else:
            list1.append(number)
    return None

print(find_same_number_2([1, 4, 3, 5, 3, 2]))
print(find_same_number_2([4, 1, 5, 2, 3, 5]))
print(find_same_number_2([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))
