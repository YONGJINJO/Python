case1 = "(1+2)*(3+5)"

print(len(case1))


grades = {}

grades["현승"] = 90
grades["형호"] = 100

print(grades)

finished_class = set()
finished_class.add("자료구조")
finished_class.add("알고리즘")
finished_class.add("데이터 사이언스")

print(finished_class)
finished_class.add("자료구조")
print(finished_class)
print("자료구조" in finished_class)
finished_class.remove("자료구조")
print(finished_class)