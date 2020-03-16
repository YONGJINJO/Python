def consecutive_sum(start, end):
    if start == end:
        return start
    return consecutive_sum(start, int((start + end) / 2)) + consecutive_sum(int((start + end) / 2) + 1, end)
# 시간복잡도 O(n)
# 테스트
print(consecutive_sum(1, 10))
print(consecutive_sum(1, 100))
print(consecutive_sum(1, 253))
print(consecutive_sum(1, 388))