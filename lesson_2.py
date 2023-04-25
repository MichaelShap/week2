#for loop, while loop
# name = 'Nazgul'
# for i in name:
#     print(i.upper())

# names = ['Nurzada', 'Jarkynai', 'Jenya']
# for name in names:
#     print(name)

# names = {'name': 'Nurzada', 'name2': 'Jarkynai', 'name3': 'Jenya'}
# # for name in names:
# #     print(name)
# #
# # for name in names.keys():
# #     print(name)
# #
# # for name in names.values():
# #     print(name)
#
# for name in names.items():
#     print(name)
#
# for key, value in names.items():
#     print(key, value)


# names = {'name': 'Nurzada', 'name2': 'Jarkynai', 'name3': 'Jenya'}
# names_replace = {}
# for key, value in names.items():
#     names_replace[key] = value.replace('a', 'z')
# print(names_replace)

# a = range(10)
# print(a)
# b = list(range(10))
# print(b)
# c = list(range(0, 10, 3))
# print(c)

# for i in range(0, 8):
#     print(i)
# for a in range(8, 0, -1):
#     print(a)
# for a in range(8, -1, -1):
#     print(a)

# names = ['Nurzada', 'Jarkynai', 'Jenya']
# for i in enumerate(names):
#     print(i)


# list_1 = []
# for i in range(1, 1000):
#     if i%3 == 0 and i%5 == 0:
#         list_1.append(i)
# print(list_1)

# num_fact = int(input('vvedite num: '))
# fact = 1
# for i in range(1, num_fact + 1):
#     fact *= i
# print(fact)
# # заданное число 4 - в этом случае умножит 1*2*3*4 = 24

# num_fact = int(input('vvedite num: '))
# fact = 1
# for i in range(1, num_fact + 1):
#     fact += i
# print(fact)


# i = 1
# while i <= 10:
#     print(i)
#     i += 1
    # fdfgdg останавливает цилк i+=1


# i = 1
# while True:
#     print(i)
#     if i >= 10:
#         break
#     i += 1

# list = []
# i = 1
# while i <= 50:
#     if i % 3 == 0 and i % 5 == 0:
#         i += 1
#         continue
#     list.append(i)
#     i += 1
# print(list)

#выше и ниже - 2 варианта, второй через Тру / Фолс

# list = []
# i = 1
# while True:
#     if i >=50:
#         break
#     if i % 3 == 0 and i % 5 == 0:
#         i += 1
#         continue
#     list.append(i)
#     i += 1
# print(list)

# list = []
# i = 1
# while i <= 5:
#     if i % 3 == 0:
#         i += 1
#         continue
#     list.append(i)
#     i += 1
# print(list)


# city = "canada"
# city_list = list("_" * len(city))
#
# while "_" in city_list:
#     letter = input("Введите букву: ")
#
#     if not letter or len(letter) > 1:
#         print(" Введите одну букву.")
#         continue
#
#     if letter.lower() in city:
#         for index, value in enumerate(city):
#             if letter.lower() == value:
#                 city_list[index] = letter.lower()
#         print("".join(city_list))
#     else:
#         print("Такой буквы в слове нет.")
#
# print("Вы угадали! Это был город", city)




