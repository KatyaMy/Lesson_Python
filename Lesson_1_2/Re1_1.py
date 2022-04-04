# Tab 1
# \n -- perenos stroki
# \t -- 4 slash
# \v -- вертикальная табуляция


# ______________________
# '  ' * 4 ---- 4 slash
# Ctr + D -- copy string
# Shift+Tab --- obratnii otstup


# a = 1
# b = 3
# c = 4
# print(a, b, c, sep='*', end="***")

# INPUT
# name = input("What you name?")
# print(type(name))
# print("Hello ", name)
# print(f"Hello, {name}")


# Task 2
# x = int(input("Number1: "))
# y = float(input("Number2: "))
# z = int(input("Number3: "))
# sum1 = x + y + z
# print(f"Total: {sum1}")


# Напишите программу, вычисляющую объём куба и площадь его полной поверхности, по введённому значению длины ребра.
# На вход программе подается одно целое число – длина ребра.
# Примечание. Объём куба и площадь полной поверхности можно вычислить по формулам V = a^3,  S = 6a^2

# Task 3

# lengthSide = 5
# V = lengthSide ** 3
# print(f"Volume cube = {V}")
# S = 6 * lengthSide ** 2
# print(f"Total surface area = {S}")

# Task 4
# x = int(input("Side: "))
# V = x ** 3
# print(f"Volume cube = {V}")
# S = 6 * x ** 2
# print(f"Total surface area = {S}")


# Task 5

# import string
# chars = list(string.ascii_lowercase[:10])
# for char, num in enumerate(chars, 10):
#     print(char, num)

# Task 6

# apple = 28
# while apple >= 10:
#     apple -= 2
#     if apple == 16:
#         continue
#
#     print(apple)

# Task 7
# x = "Word"
# for letter in x:
#      print(letter)
#
# Task 8
# lst = ["1", "2", "3", "4"]
# for element in lst:
#      print(element)
#      if element == "3":
#           break
# Task 8
# for elem in range(2, 22, 3):
#      print(elem)

# lst = [28, 34, 56, 7, 0, 98, 0]
# for elements in range(6,7):
#      print(lst[elements])


# Task Calculator

# number1 = int(input("Enter a number: "))
# c = input("Enter operation: ")
# number2 = int(input("Enter a one more number: "))
#
# if c == "*":
#     print(f" Total: {number1 * number2}")
# elif c == "-":
#     print(f"Total: {number1 - number2}")
# elif c == "+":
#     print(f"Total: {number1 + number2}")
# elif c == "/":
#     if number2 == 0:
#         print("Error NO division by zero!!!")
#     else:
#         print(f"Total: {number1 / number2}")
# else:
#     print("Invalid operation")

# Task Calculator 2

# number1 = input("Enter the first number ")
# number2 = input("Enter the second number ")
# operation = input("Enter * for multiple, / for division, + for sum, - for subtraction: ")
# while not number1.isdigit():
#     print("Give me a number!!!")
#     number1 = input("Enter the first number ")
# while not number2.isdigit():
#     print("Give me a number!!!")
#     number2 = input("Enter the second number ")
# while operation not in ['*', '/', '+', '-']:
#     print("Enter the correct operand ")
#     operation = input("Enter * for multiple, / for division, + for sum, - for subtraction: ")
# number1 = int(number1)
# number2 = int(number2)
# if operation == "*":
#     print(number1 * number2)
# elif operation == "/":
#     if number2 == 0:
#         print("No division by zero!!!!!!")
#     else:
#         print(number1 / number2)
# elif operation == "+":
#     print(number1 + number2)
# else:
#     print(number1 - number2)


# Task
# numbers = [12, 345, 67, 80, 91, 2, 1, 139, 0, 45, 2, 0, 22]
# for x in numbers:
#     if x == 139:
#         break
#     if x % 2 == 1:
#         print(x)


# Task v.1
# number = [18, 14, 10, 6, 2]
# for el in range(18, 1, -4):
#     print(el)

#Task v.2
# lst = []
# for x in range(18, 4, -4):
#     lst.append(x)
#     print(lst)

