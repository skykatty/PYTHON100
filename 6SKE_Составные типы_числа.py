# Вариант 1: N = (сумма букв в фамилии + сумма букв в имени) % 5

N = (len('Скуднева')+len ("Екатерина"))%5
print(N)
#
# # 2. Вариант - Set
#
# # Сгенерировать [тип] размера (N  + 2) * 2
# # 1.
def funnum_1(N):
    tip = [i for i in range(1,N+2*2)]#Генерируем матрицу - list
    tip = set(tip) # к типу set
    print(tip)
zn1 = funnum_1(2)
#
# 2.
def funnum_2(zn1):
    tip_new = zn1 + [i + 1 for i in zn1] # дублируем значения и ув на 1
    tip_new = set (tip_new) # возвращаем к set
    print(tip_new)
zn2 = funnum_2([1, 2, 3, 4, 5])
#
# 3.
def funnum_3(zn3):
    zn3.sort() #Сортируем значения
    print(zn3[-(len(zn3)-1):-1]) #Вырезаем значения со второго по убыванию
                                # и до предпоследнего
funnum_3([1, 2, 3, 4, 5, 2, 3, 4, 5, 6])

# 4.
def funnum_4(zn4):
    zn_del=[] # пустой список для значений деления
    for i in range(len(zn4)): # цикл по индексам
        if i%3 == 1: # проверка условия деления индекса на 3 без остатка
            zn_del.append(zn4[i]) #добавляем посимвольно значения,
                                # при выполнении условия
    print(zn_del)
funnum_4([1, 2, 3, 4, 5, 2, 3, 4, 5, 6])


# 5.
def funnum_5():
    list=[1, 2, 3, 4, 5, 2, 3, 4, 5, 6]
    New_list = []
    for i in list:
        a = round(i/3)
        New_list.append(a)
    print(New_list)
funnum_5()

