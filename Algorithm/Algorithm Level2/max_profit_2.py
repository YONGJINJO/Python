def max_profit_2(stock_list):
    if len(stock_list) == 1:
        return None
    temp_max = stock_list[1] - stock_list[0]
    buy_position = stock_list[0]
    for i in range(1, len(stock_list)):
        #print("%d. %d" %(i, stock_list[i]))
        #print("temp_max = %d" %(t  emp_max))
        first_block = stock_list[i] - stock_list[i - 1]
        second_block = stock_list[i] - buy_position
        #print("one_block = %d" %(one_block))
        #print("second_block = %d" %(second_block))
        if first_block > temp_max and first_block > second_block:
            buy_position = stock_list[i - 1]
            temp_max = first_block
        elif second_block > temp_max:
            temp_max = second_block
    #print("max = %d" %(temp_max))
    return temp_max


print(max_profit_2([7, 1, 5, 3, 6, 4]))
print(max_profit_2([7, 6, 4, 3, 1]))
print(max_profit_2([11, 13, 9, 13, 20, 14, 19, 12, 19, 13]))
print(max_profit_2([12, 4, 11, 18, 17, 19, 1, 19, 14, 13, 7, 15, 10, 1, 3, 6]))