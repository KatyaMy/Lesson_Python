# function
# """ vizov funkcii   Если несколько раз встречается один и тот же код лучше оформить функцию
# Функция нужна для повторного использования кода в ваших программах
# EXMP .1
# def sum_function(x, y):
#     result = x + y
#     return result
#
#
# a1 = 14
# b1 = 33
# res = sum_function(a1, b1)
# print(f"result: {res}")

# EXMPL 2.

# def compare_function(x, y):
#     if x > y:
#         # print("true")
#         return True
#     else:
#         # print("false")
#         return False
#
#
# print(compare_function(3, 4))

# EXMP 3.

# def compare_function(x, y):
#     print(y)
#     if x > y:
#         return x
#     else:
#         return 0
#
#
# print(compare_function(7, 4 + 4))

# EXMPL 5. global and local peremennie
# x = 45
#
#
# def dummy_function():
#     global x
#     x = "test 100"
#     print(x)
#
#
# # dummy_function()
# print(x)
#