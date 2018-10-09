def conNS(int(x), si1 ,si2):
    he_max = ['','A','B','C','D','E','F']
    # if si2 == 10:
    x = int(x, si1) # Преобразуем по основанию в 10-тичную систему
    # else:
    b = ''
    if x%si2 > 9: # Для 16-тиричной
        b = he_max[x%si2-9]
    while x >= si2: # Пока не закончится остаток
        x = x//si2
        if x%si2 > 9: # Для 16-тиричной
            b += he_max[x%si2-9]
        b += str(x%si2)
    return b[::-1] # Как при вычислении на бумаге начинаем с конца

print (conNS(11AA0,16,10))
