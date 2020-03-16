def max_profit(stock_list):
    max_profit_so_far = stock_list[1] - stock_list[0]
    temp_value = stock_list[1] - stock_list[0]
    min_value = stock_list[0]
    if max_profit_so_far < 0:
        min_value = stock_list[1]
    for i in range(2, len(stock_list)):
        max_profit_so_far = max(stock_list[i] - min_value, max_profit_so_far)
        min_value = min(min_value, stock_list[i])
    return max_profit_so_far

'''
앞의 이익에 비해서 다른 점은 min_value를 하나 더 기억해줘야 한다는 것이다
지금 문제를 풀면서 내가 오해하고 있던 것은
어떤 값이 내가 찾는 값에 현재 가장 근접할 경우 나는 그것의 상세한 정보를 다 알고 있어야 한다고 생각했다.
그러나 이 문제를 가만히 보면
나는 두 지점의 최대 차이를 찾기 위해
두 지점이 정확히 어딘지를 알 필요가 없다는 것이다
이 문제는 부분 문제를 풀어가는 식으로 뒤에 요소 하나를 추가해 가면서 최대값을 계속 비교한다
그러면 작은 부분에서의 최대값과 요소 하나가 추가된 뒤에 최대값을 비교하면 되는 것일 뿐이다.
요소하나가 추가된 뒤 최대값은 추가된 요소와 그 전 부분에서 최소값을 뺐을 때 최대값이 나온다
즉, 나느 최소값만을 계속 최신화 시켜 주면서 비교 하면 충분히 최대값을 찾을 수 있다는 얘기이다.
'''

# 테스트
print(max_profit([7, 1, 5, 3, 6, 4]))
print(max_profit([7, 6, 4, 3, 1]))
print(max_profit([11, 13, 9, 13, 20, 14, 19, 12, 19, 13]))
print(max_profit([12, 4, 11, 18, 17, 19, 1, 19, 14, 13, 7, 15, 10, 1, 3, 6]))