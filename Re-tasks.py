'''Семинар 2 задача 3

     Было:   '''
# # Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# # Пример:
# # - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
# # Первый вариант: формула как в примере
# number = int(input("Введите число N: "))
# ar = {}
# sum = 0
# for n in range(1, number+1):
#     ar[n] = 3 * n + 1
#     sum += ar[n]
# print(ar)
# print('Сумма элементов списка равна', sum)

'''Использовали list comprehension для словаря ar
        Стало:   '''
# number = int(input("Введите число N: "))
# ar = {_: (3 * _ + 1) for _ in range(1, number + 1)}
# res = 0
# for n in range(1, number + 1):
#     res += ar[n]
# print(ar)
# print('Сумма элементов списка равна', res)


'''Задачи к ДЗ'''
# # Задача 1. Вводится список целых чисел в одну строчку через пробел.
# # Необходимо оставить в нем только двузначные числа.
# # Реализовать программу с использованием функции filter.
# # Результат отобразить на экране в виде последовательности
# # оставшихся чисел в одну строчку через пробел.
# # пример - 8 11 0 -23 140 1 => 11 -23
#
# list_num = list(map(str, list(filter(lambda x: 10 <= abs(x) <100, map(int, \
#             list(input('Введите список целых чисел через пробел: ').split())) ))))
# print(" ".join(list_num))



# # Задача 2. Дан список, вывести отдельно буквы и цифры.
# # a = ( "a", 'b', '2', '3' ,'c')
# # b = ( 'a' , 'b' , 'c')
# # c = ( '2', '3')
#
# start_list = ['a', 'b', '2', '3', 'c']
# print('a =', start_list)
# print('b =', list(filter(lambda x: not x.isdigit(), start_list)))
# print('c =', list(filter(lambda x: x.isdigit(), start_list)))



# # Задача 3. Преобразовать набора списков
# # users = ['user1','user2','user3','user4','user5']
# # ids = [4, 5, 9, 14, 7] salary = [111,222,333] в другой набор
# # ['user1', 4, 111]
# # ['user2', 5, 222]
# # ['user3', 9, 333]
# # и потом вернуть в исходное состояние
# # ['user1', 'user2', 'user3']
# # [4, 5, 9]
# # [111, 222, 333]
#
# users = ['user1','user2','user3','user4','user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111,222,333]
# rar = list(zip(users, ids, salary))
# print(rar)
# users, ids, salary = zip(*rar)
# print(f'users = {users}\nids = {ids}\nsalary = {salary}')
