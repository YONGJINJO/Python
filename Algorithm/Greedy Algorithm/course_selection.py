def course_selection(course_list):
    sorted_list = sorted(course_list, key = lambda course_list : course_list[1])
    max_course = [sorted_list[0]]
    for number in sorted_list:
        if max_course[-1][1] < number[0]:
            max_course.append(number)
    return max_course


# 테스트
print(course_selection([(6, 10), (2, 3), (4, 5), (1, 7), (6, 8), (9, 10)]))
print(course_selection([(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]))
print(course_selection([(4, 7), (2, 5), (1, 3), (8, 10), (5, 9), (2, 5), (13, 16), (9, 11), (1, 8)]))
