# 1.
# # Перевод из любой в СС от 2-10
#
# def funnumbersystem_1():
#     sys_ch = int(input("Введите систему счисления: "))
#     num_sys_ch = input('Введите число в выбранной СС:')
#     num_10 = int(num_sys_ch, sys_ch)
#
#     base = int(input('Введите основание получаемой СС от 2-10: '))
#     if base == 10:
#         print("В {0} СС число: ".format(base)+str(num_10))
#         quit()
#     # Проверка если основание не в диопазоне от 2 до 9
#     if not (2 <= base <= 9):
#         quit()
#
#     new_Num = ''
#     # Пока значение больше 0
#     while num_10 > 0:
#         # Добавляем символ в начало строки
#         # Остаток деления на основание
#         new_Num = str(num_10 % base)+new_Num
#         # Число делится на основание + преобразование к
#         # целому значению
#         num_10 = int(num_10/base)
#     print("В {0} СС число: ".format(base))
#     return new_Num
# print(funnumbersystem_1())

# 2/
# def funnumbersystem_2():
#     a = input("Хотите перевести число из одной СС в др(да/нет)?\n")
#     while len(a)==2:
#         for i in range(1, len(a)):  # количество символов в ответе
#             if len(a) == 2:  # проверка желания играть
#                 sys_ch = int(input("Введите систему счисления: "))
#                 num_sys_ch = input('Введите число в выбранной СС:')
#                 num_10 = int(num_sys_ch, sys_ch)
#
#                 base = int(input('Введите основание получаемой СС от 2-10: '))
#                 if base == 10:
#             # print("В {0} СС число: ".format(base)+str(num_10))
#             # Проверка если основание не в диопазоне от 2 до 9
#                     if not (2 <= base <= 10):
#                         break
#
#                 new_Num = ''
#             # Пока значение больше 0
#                 while num_10 > 0:
#             # Добавляем символ в начало строки
#             # Остаток деления на основание
#                     new_Num = str(num_10 % base)+new_Num
#                 # Число делится на основание + преобразование к
#                 # целому значению
#                     num_10 = int(num_10/base)
#             print("В {0} СС число: ".format(base)+new_Num)
#             a = input("Хотите перевести число из одной СС в др(да/нет)?\n")
# print(funnumbersystem_2())
