# 1.按照每个元组的第二个元素排序
my_list = [(1, 5), (3, 2), (2, 8), (4, 1)]

# 使用 def 定义函数作为 key
def get_second_element(item):
    return item[1]
sorted_list_def = sorted(my_list, key=get_second_element)
print(f"使用 def 排序: {sorted_list_def}") # 输出: [(4, 1), (3, 2), (1, 5), (2, 8)]

# 使用 lambda 作为 key（更简洁）
sorted_list_lambda = sorted(my_list, key=lambda item: item[1])
print(f"使用 lambda 排序: {sorted_list_lambda}") # 输出: [(4, 1), (3, 2), (1, 5), (2, 8)]

# 2.使用 lambda 和 map 函数
numbers = [1, 2, 3, 4, 5]

# 将每个数字平方
squared_numbers_lambda = list(map(lambda x: x**2, numbers))
print(f"使用 lambda 和 map: {squared_numbers_lambda}") # 输出: [1, 4, 9, 16, 25]

# 相当于列表推导式：
squared_numbers_comprehension = [x**2 for x in numbers]
print(f"使用列表推导式: {squared_numbers_comprehension}") # 输出: [1, 4, 9, 16, 25]

# 3.使用 lambda 和 filter 函数
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 筛选偶数
even_numbers_lambda = list(filter(lambda x: x % 2 == 0, numbers))
print(f"使用 lambda 和 filter: {even_numbers_lambda}") # 输出: [2, 4, 6, 8, 10]

# 相当于列表推导式：
even_numbers_comprehension = [x for x in numbers if x % 2 == 0]
print(f"使用列表推导式: {even_numbers_comprehension}") # 输出: [2, 4, 6, 8, 10]