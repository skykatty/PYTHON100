# 1.
def funjusthurt_1(Price, Amony,A_x,Bmony,B_y):
    if (Amony*A_x+Bmony*B_y<Price): pass
    for i in range(0,Amony+1):
        for j in range(0,Bmony+1):
            if B_y*j + A_x* i == Price:
                return True
    return False
print(funjusthurt_1(24, 5, 4, 2,6))

# 2.
def funjusthurt_2():
    a=input("Введите число для подсчета разрядов:\n")
    b = len(a)
    print(b)
funjusthurt_2()


# 3.
def funjusthurt_3():
    n = input()
    for i in range(int(len(n) / 2)):
        if not n[i] == n[len(n) - i - 1]:
            print(False)
            break
    else:
        print("True")
print(funjusthurt_3())

# # 4.
str = 'aaa123bbb123xxx123ddd123'
print(str)
def funjusthurt_4(StrOld, StrNew):
    str = 'aaa123bbb123xxx123ddd123'
    lenStrOld = len(StrOld)
    # функция find() - возвращает индекс первого символа
    # подстроки.
    while str.find(StrOld)>0: # цикл для поиска нескольких одинаковых подстрок
        i = str.find(StrOld)# сохраняем индекс 1го элемента старой построки
    # Формируем строку: срез от начала до индекса старой
    #строки + новая подстрока + срез от конца до старой подстроки
        str = str[:i] + StrNew + str[i+lenStrOld:]
    return str
string = funjusthurt_4(StrOld = input('Old substring: '),StrNew = input("New Substring: "))
print(string)

# # 4a. replace
def funjusthurt_4_1():
    strin = input("Input string: \n")
    strOld = input('Old substring: ')
    strNew = input("New Substring: ")
    strin = strin.replace(strOld, strNew)
    print(strin)
funjusthurt_4_1()