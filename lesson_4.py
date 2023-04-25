# напишите программу которая будет счить ссуму отдельных цифр заданного числа
# V1
# count = 0
# while True:
#     number = input('vvedite num: ')
#     if number.isdigit():
#         for i in number:
#             count += int(i)
#         break
# print(count)

# V2
# number = input('vvedite num: ')
# lists = list(number)
# print(lists)
# # здесь каждая цифра станет стр не подходит

# number = input('vvedite num: ')
# lists = [int(i) for i in number]
# print(lists)
# # в этом случае получаем список из отдельных целых чисел
# lists = sum([int(i) for i in number])
# print(lists)
# # а здесь выводим сумму этих чисел

# 2 пособа создать список из целых чисел
# lists = [i for i in range (50)]
# print(lists)
# lists = list(range(50))
# print(lists)

# Напишите программу которая находит наибольший общий делитель двух чисел
# num1 = 24
# num2 = 36
# while num2:
#     print(num1, num2)
#     num1, num2 = num2, num1 % num2
#     print(num1, num2)
# # print(num1)

# по заданному номеру строки фибоначи найти число

# fib1 = 1
# fib2 = 1
#
# row = int(('nomer elementa: '))
# row = row - 2
#
# while row > 0:
#     num1, num2 = num2, num1 + num2
#     row -= 1
# print(num2)

# # DODELAT'
# list = list(range(1001))
# print(list)
#
# prost = []
#
# for i in list:
#     if i !=0 and i % i and i % 1:
#         prost.append(i)
#         i += 1
#         continue


# Lists generator
# numbers = [i for i in range(1, 1000) if i % 3 == 0 and i % 15 == 0]
# print(numbers)
# numbers = [i if i > 100 else 0 for i in range(1, 1000) if i % 3 == 0 and i % 15 == 0]
# print(numbers)
# numbers = [i**2 for i in range(1, 1000) if i % 3 == 0 and i % 15 == 0]
# print(numbers)

# vivesti tolko glasnie bukvi iz teksta
# text = 'iphone'
# lists = ['a', 'e', 'i', 'o', 'u', 'y']
# letters = [i for i in text if i in lists]
# print(letters)

# text = list('iphoneo')
# lists = ['a', 'e', 'i', 'o', 'u', 'y']
# print(text)
# print(list(zip(text, lists)))

# text = 'iphone'
# lists = ['a', 'e', 'i', 'o', 'u', 'y']
# print(list(zip(text, lists)))

# names = ['Nazgul', 'Jenya', "Nurzada"]
# ages = [18, 17, 22]
# zip_list = list(zip(names, ages))
# print(zip_list)
#
# dicts = {}
#
# for i, y in zip(names, ages):
#     print(i,y)
#     dicts[i] = y
# print(dicts)

