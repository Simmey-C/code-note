# 输出100以内的偶数
even_numbers = [x for x in range(1,101) if x % 2 == 0 ]
print (even_numbers)

# 等价于
even_numbers = filter(lambda x: x % 2 == 0, range(1,101))
print(list(even_numbers))