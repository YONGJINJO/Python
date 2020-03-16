def merge(list1, list2):
    final_list = []
    num = 0
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            final_list.append(list1[i])
            i += 1
        else :
            final_list.append(list2[j])
            j += 1
    if i == len(list1):
        final_list += list2[j:]
    elif j == len(list2):
        final_list += list1[i:]
    return final_list



'''def merge(list1, list2):
    combined_list = list1 + list2
    combined_list.sort()
    if len(combined_list) <= 2:
        return combined_list
    total_list = merge(list1[:(len(list1) // 2)],list1[(len(list1) // 2):]) + merge(list2[:(len(list2) // 2)],list2[(len(list2) // 2):])
    total_list.sort()
    return total_list



# 코드를 작성하세요.
def merge(list1, list2):
    combined_list = list1 + list2
    combined_list.sort()
    print(combined_list)
    if len(combined_list) <= 2:
        print("short")
        return combined_list
    return merge(merge(list1[:(len(list1) // 2)],list1[(len(list1) // 2):]),merge(list2[:(len(list2) // 2)],list2[(len(list2) // 2):]))

'''

# 테스트
print(merge([1], []))

print(merge([], [1]))

print(merge([2], [1]))

print(merge([1, 2, 3, 4], [5, 6, 7, 8]))

print(merge([5, 6, 7, 8], [1, 2, 3, 4]))

print(merge([4, 7, 8, 9], [1, 3, 6, 10]))