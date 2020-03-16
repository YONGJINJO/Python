def selection_sort(string):
    for i in range(len(string)):
        temp_small = string[i]
        temp_location = i
        for j in range(i + 1, len(string)):
            if temp_small > string[j]:
                temp_small = string[j]
                temp_location = j
        temp = string[i]
        string[i] = temp_small
        string[temp_location] = temp
    return string


A = [5, 2, 3, 7, 8, 9, 10, 1, 4]
print(len(A))
print(selection_sort(A))
