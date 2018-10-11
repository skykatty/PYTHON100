# def funnumsystem_4(n_10):
#     print(hex(n_10))
#

# 1.
# # 8 -> 16
def funnumsystem_1(n_8):
    # Перевод в 10
    n_10 = int(n_8, 8)
    #  Перевод в 16
    n_16 = hex(n_10)
    # Вывод только самого числа
    print (n_16[2:])
print(funnumsystem_1(n_8 = input('Введите в 8 CC: ')))

# 2.
# 16 -> 8
def funnumsystem_2(n_16):
    # Перевод в 10
    n_10 = int(n_16, 16)
    #  Перевод в 8
    n_8 = oct(n_10)
    # Вывод только самого числа
    print(n_8[2:])
print(funnumsystem_2(n_16 = input('Введите в 16 CC: ')))

# 3.
# 10 -> 7
# Перевод из 10 в 7
def funnumsystem_3():
    num_10 = int(input('Введите число: '))
    base = 7
    new_Num = ''
    # Пока значение больше 0
    while num_10 > 0:
        # Добавляем символ в начало строки
        # Остаток деления на основание
        new_Num = str(num_10 % base)+new_Num
        # Число делится на основание + преобразование к
        # целому значению
        num_10 = int(num_10/base)
    print("В 7 СС число: ", new_Num)
    return new_Num
a = print(funnumsystem_3())
print(a)

# 4. 7 -> 10
def funnumsystem_4():
    num_7 = input('Введите число в 7 СС:')
    print(int(num_7, 7))
print(funnumsystem_4())

# 5.
# Перевод из 10 в 3
def funnumsystem_5():
    num_10 = int(input('Введите число: '))
    base = 3
    new_Num = ''
    # Пока значение больше 0
    while num_10 > 0:
        # Добавляем символ в начало строки
        # Остаток деления на основание
        new_Num = str(num_10 % base)+new_Num
        # Число делится на основание + преобразование к
        # целому значению
        num_10 = int(num_10/base)
    return new_Num
print("В 3 СС число: "+ funnumsystem_5())

# 6.
# 3 -> 10
def funnumsystem_6():
    num_3 = input('Введите число в 3 СС:')
    num_10 = int(num_3, 3)
    return num_10
print("В 3 СС число: " + str(funnumsystem_6()))

# 7.
def funnumsystem_7():
    num_3 = input('Введите число в 3 СС:')
    # Перевод в 10 СС
    num_10 = int(num_3, 3)
    base = 7
    new_Num = ''
    # Пока значение больше 0
    while num_10 > 0:
        # Добавляем символ в начало строки
        # Остаток деления на основание
        new_Num = str(num_10 % base)+new_Num
        # Число делится на основание + преобразование к
        # целому значению
        num_10 = int(num_10/base)
    return new_Num
print("В 7 СС число: "+ funnumsystem_7())


# 8.
# 7 -> 3
def funnumsystem_8():
    num_7 = input('Введите число в 7 СС:')
    # Перевод в 10 СС
    num_10 = int(num_7, 7)
    base = 3
    new_Num = ''
    # Пока значение больше 0
    while num_10 > 0:
        # Добавляем символ в начало строки
        # Остаток деления на основание
        new_Num = str(num_10 % base)+new_Num
        # Число делится на основание + преобразование к
        # целому значению
        num_10 = int(num_10/base)
    return new_Num
print("В 3 СС число: " +funnumsystem_8())


