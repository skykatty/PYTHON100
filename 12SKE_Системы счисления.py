# 1.
# 10 -> 2
# def funnumsystem_1(x10):# Создаем пустую строку для записи двоичного числа
#     x2 = ''
#     # До тех пор, пока частное не равно 0
#     while x10>0:
#         # Конкатенация. Добавляем полученный символ на 1 место
#         # Остаток от деления в виде строки
#         x2 = str(x10 % 2)  + x2
#         # Делим число на 2
#         x10 = int (x10/2)
#     return x2
# x_2 = funnumsystem_1(x10 = int (input( "Введите число в десятичной СС: ")))
# print(x_2)



# 2.
# 2 -> 10
# def funnumsystem_2(n):
#     print(int (n , 2))
# print(funnumsystem_2(n = input()))

# 3.
# def funnumsystem_3(n_16):
#     print(int (n_16, 16))
# print(funnumsystem_3(n_16 = input()))


# 4.
# 10 -> 16
# def funnumsystem_4(n_10):
#     print(hex(n_10))
# print(funnumsystem_4(n_10 = int(input())))

# 5.
# 16 -> 2
# def funnumsystem_5(n_16) :
#     # Перевод в 10
#     n_10 = int(n_16, 16)
#     #  Перевод в 2
#     n_2 = bin(n_10)
#     # Вывод только самого числа
#     print(n_2[2:])
# print(funnumsystem_5(n_16 = input('Введите в 16 CC: ')))
#
# # 6.
# # # 2 -> 16
# def funnumsystem_6(n_2):
#     # Перевод в 10
#     n_10 = int(n_2, 2)
#     #  Перевод в 16
#     n_16 = hex(n_10)
#     # Вывод только самого числа
#     print(n_16[2:])
# print(funnumsystem_6(n_2 = input('Введите в 2 CC: ')))
