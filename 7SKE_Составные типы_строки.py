# 1
def funstring_1(n, St):
    print(n*St) #Печать строки n раз
# funstring_1(n= int(input("Вв число:-")) ,St= input("ВВ строку"))

# 2
def funstring_2(N):
    for i in range (1, N+1): #цикл от 1 до N+1 (последнее не вкл)
        ke = "=" # Присвоение знака равно в каждой  итерации
        print(ke*(i)) #Печать ke.
# funstring_2(N = int(input("Количество ступенек")))

# 3.1
def funstring_3_1(Nstring):
    dict = {} #Словарь пустой
    for i in Nstring: #Цикл по значениям
        if i in dict: #Проверка их наличия в словаре
            dict[i]+=1 # Если есть добавляется 1
        else:
            dict[i]=1 # Нет, добавляется и значение = 1
    print(dict)
# funstring_3_1(Nstring = input())

# 3.2
def funstring_3_2(Nstring1):
    dict = {} #Создаем словарь
    for i in range (len(Nstring1)): #Цикл по индексам строки
        if Nstring1[i] in dict: # Если значение индекса есть в словаре
            dict[Nstring1[i]]+=1 # Добавляем +1 если есть
        else:
            dict[Nstring1[i]]=1 # Иначе создаем и приравниваем 1
    print(dict)
# funstring_3_2(Nstring1 = input())

# 4
def funstring_4(Predlogrnie):
    dict = {} # Создаем словарь
    a= Predlogrnie.split() #Разбиваем предложение
    for i in a: # По значениям слов
        ke = 'длинной ' + str(len(i)) # сколько букв в слове
        if ke in dict: # если число совпало, то +1
            dict[ke]+=1
        else: # иначе 1
            dict[ke]=1
    print(dict)
# funstring_4(Predlogrnie =  input())
