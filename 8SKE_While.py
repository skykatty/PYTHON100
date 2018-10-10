 # 1.
# def funsport_1(distance, day=0, km=0):
#     while km <= distance:
#         km =km + 2**2
#         day += 1
#     print(day)
# funsport_1(distance = int(input("Введите дистанцию:")))

#2.
# def funsport_2(distance, day = 0, num = 0, km = 0):
#     while km<=distance: # пока меньше дистанции
#         lastsim = 1
#         simple = False #Установка флага
#         while(not simple): # Пока не простое
#             simple = True # Смена флага
#             num+=1 # К числу добавляем 1
#             for i in range(2,int(num/2)): #Проверка на простое число
#                 if num%i ==0:
#                     simple = False
#         km += day + lastsim #Увеличиваем расстояние
#         day += 1 #Увеличиваем дни
#     print(day)
# funsport_2(distance = int(input("Введите расстояние: ")))

# 3.
# def funsport_3(distance = 0, km = 10, day = 0):
#     while day<=30: #пока дней не 30
#         day += 1 # итерация по дням
#         distance+=km # добавляем km
#         if day%2 == 0: # через день
#             km = km+km*0.1 # увеличение нормы на 10%
#     return round(distance)
# a = funsport_3(0)
# print(a)

#4.
# def funsport_4a(km = 10, day =1):
#     while km<=20: # пока не достигли 20 км
#         km = km+km*0.1 # увеличение дневной нормы
#         day+=1 # итерация по дням
#     return day
# b = funsport_4a(10)
# print(b)

# def funsport_4b(distance=0, km = 10, day =1):
#     while distance<=100: # пока не достигли 100
#         distance +=km # суммарное расстояние
#         km = km+km*0.1 # увеличение дневной нормы
#         day+=1 # итерация по дням
#     return day
# c = funsport_4b(0)
# print(c)


