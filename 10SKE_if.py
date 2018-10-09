# 1.a
#
# def funif_1a(Neiz_chislo, chislo = 36):
#     if chislo<Neiz_chislo: # Сравнение
#         print("Меньше")
#     elif chislo > Neiz_chislo: # Сравнение с исходным числом
#         print("Больше")
#     else:
#         chislo == Neiz_chislo
#         print('да, это оно')
# print(funif_1a(Neiz_chislo = int (input("введите число от 0 до 100: "))))


# 1б
# def funif_10b(a, Neiz_chislo = 0, chislo = 36, N=0):
#     for i in range(1, len(a)): # количество символов в ответе
#         if len(a) == 3:  # проверка желания играть
#             Neiz_chislo = 0
#             while chislo != Neiz_chislo: # пока не найден ответ
#                 Neiz_chislo = int(input("введите от 0 до 100: \n"))
#                 if chislo < Neiz_chislo:
#                     print("Меньше")
#                 elif chislo > Neiz_chislo:
#                     print("Больше")
#                 else:
#                     chislo == Neiz_chislo
#                     print('да, это оно')
#             a = input("Партия? Введите Yes/No:\n")
#             N+=1 # Счетчик на количество партий
#         else:
#             break
#     return N

# Kol_partii = funif_10b(a = input("Партия? Введите Yes/No:\n"))
# print("Количество партий:", Kol_partii)


# # 1в
# def funif_10c(a, Neiz_chislo = 0, chislo = 36, N=0, hod = 4):
#     for i in range(1, len(a)): # количество символов в ответе
#         if len(a) == 3:  # проверка желания играть
#
#             Neiz_chislo = 0
#             while chislo != Neiz_chislo: # пока не найден ответ
#                 Neiz_chislo = int(input("введите от 0 до 100: \n"))
#                 if hod == 0:
#                     break
#                 else:
#                     if chislo < Neiz_chislo:
#                         print("Меньше")
#                     elif chislo > Neiz_chislo:
#                         print("Больше")
#                     if chislo == Neiz_chislo:
#                         print('да, это оно')
#                         break
#                     hod-=1
#                     if hod ==0:
#                         break
#             a = input("Партия? Введите Yes/No:\n")
#             N+=1 # Счетчик на количество партий
#         else:
#             break
#     return N
#
# Kol_partii = funif_10c(a = input("Партия? Введите Yes/No:\n"))
# print("Количество партий:", Kol_partii)











# chislo = 36
# N=0
# hod=0
# while N < 100:
#     for i in range(1,5):
#         print("введите от 0 до 100")
#         while hod<8:
#             hod += 1
#         Neiz_chislo = int(input())
#         if chislo<Neiz_chislo:
#             print("Меньше")
#         elif chislo > Neiz_chislo:
#             print("Больше")
#         else:
#             chislo == Neiz_chislo
#             print('да, это оно')
#             break
#     N+=1
#     print('Еще раз?')
#     print("Количество партий: ", N)

