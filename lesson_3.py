#set
# коллекции


# lists = list(set([1, 2, 3, 2, 2, 6]))
# my_set = {1, 4, (1, 2), '6', 6}
# print(lists)

# text = '1 str befor 1 str afte 2 str nrfor 2 str after'
# # print(set(text))
# # print(text.split())
# set_text = (set(text.split()))
# print(' '.join(set_text))

# text = '1 str befor 1 str afte 2 str nrfor 2 str after'
# set_text = (set(text.split()))
# for i in set_text:
#     print(i)

# text = '1 str befor 1 str afte 2 str nrfor 2 str after'
# set_text = (set(text.split()))
# set_text.add(8)
# print(set_text)
#нелзя адд сделать через печать, так как значение должно созраняться.
# по этому, сначала используем метод, потом печатаем сам сет

# text = '1 str befor 1 str afte 2 str nrfor 2 str after'
# set_text = (set(text.split()))
# set_text.clear()
# print(set_text)

# text = '1 str befor 1 str afte 2 str nrfor 2 str after'
# set_text = (set(text.split()))
# a = set_text.pop()
# print(a)
# удаляет рандомный элемент (черный список)

from copy import deepcopy
# dict_types = {
#     'name': 'one',
#     'lessons': ['algebra', 'python', 'java']
# }
# new_dict = dict_types.copy()
# new_dict2 = deepcopy(dict_types)
# dict_types['lessons'].append('scala')
# print(new_dict)
# print(dict_types)
# print(new_dict2)
# здесь пример дип копи и простой копии

# from lesson_2 import num_fact
# ili tak
# import lesson_2
# lesson_2.num_fact
# ili
# from lesson_2 import *
# num_fact
# тут варианты импорта из других файлов, в той же директори,
# если данные в других директория, то будет по-другому


# set_text = {1, 3}
# new_set = {1, 2}
# print(set_text.difference(new_set))
# print(new_set.difference(set_text)) #sravnenie new set s set text
# print(new_set.symmetric_difference(set_text)) #spisok ne peresekaiushihs9 elementov

# set_text = {1, 3}
# new_set = {1, 2}
# new_set.symmetric_difference_update(set_text)
# print(new_set)
# print(set_text)

# set_text = {1, 3, 8}
# new_set = {1, 2, 3}
# print(set_text.intersection(new_set)) #vivod peresekaiushies9 elementi
# set_text.intersection_update(new_set) #nahodit peresecheniya i zamen9et v vibrannom sete
# # znacheniya na peresekaiushies9
# print(set_text)

# set_text = {1, 3, 8}
# new_set = {1, 2, 3}
# print(set_text.union(new_set))
# # просто объединяет 2 сета, пересекающиеся значения появятся 1 раз. Он не меняет ни один сет
# а выводит новый сет

# set_text = {1, 3, 8}
# new_set = {1, 2, 3}
# set_text.update(new_set)
# print(new_set)
# print(set_text)
# # здесь апдейт - он меняет сет, по этому сначал метод применяем, потом только печатаем

# set_text = {1, 3, 8}
# new_set = {1, 2, 3}
# print(set_text.isdisjoint(new_set))
# # если 2 сета обсолютно не имеют пересечений, то Тру. Если есть хоть 1 пересечение то Фолс

set_text = {1, 3, 2}
new_set = {1, 2, 3}
print(set_text.issubset(new_set))
# не объясню словами)))