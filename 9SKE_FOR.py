# 1.
def funfor_1(l_list, N=20):
    for i in range(1,N): # от 1 до N по индексам
        l_list.append(l_list[-1]+l_list[-2]) # складываем последние
        # элементы в списке
    return l_list
a = funfor_1([1,1])
print(a)

# 2.
def funfor_2(l, N=10):
    for i in range(1,N): # от 1 до N
        l.append(l[-1] + l[-2] + l[-3]) #суммируем последние 3
    return l
b = funfor_2([1,1,1])
print(b)

# 3.
def funfor_3(N):
    print([i**2 for i in range(1,N,2)]) # генератор по нечетным числам
funfor_3(20)

# # 4.
def funfor_4(visota = 5, shirina = 4):
    ke = "*"
    print(shirina*ke) # первая строка
    for i in range(1,visota-1):
        print(ke+"  "+ke)  # середина прямоугольника
    print(shirina*ke) # последняя строка
funfor_4(visota= int(input("Задайте высоту:")))

# 5.
def funfor_5(A =1, B = 4, sum = 0, oper = 1):
    for i in range(A,B+1):
        sum = sum + i # сумма натуральных чесел
        if (oper!=0) and (i!= 0): # от умножения на "0"
            oper = oper*i # произведение чисел
    return sum, oper
print(funfor_5())

# 6.
def funfor_6(A=1, B=22, a=[], b=[]):
    for i in range(A,B+1):
        if i%2 == 0: # проверка четности
            a.append(i) # список для четных
        else:
            b.append(i) # список для нечетных
    sum = a+b  # общий список
    return sum
result = funfor_6(1,20)
print(result)

# 7.
def funfor_7(A = [], b=[], c=[]):
    for i in range(len(A)): # по длине списка, индексам
        if A[i]<0:  # проверка отрицательных чисел
            b.append(A[i])
        else: # положительное
            c.append(A[i])
    return b,c
print(funfor_7([-3,2,4,-5,-7,10,-15,2]))