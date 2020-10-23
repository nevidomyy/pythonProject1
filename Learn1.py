#!/usr/bin/env python3
import sys          #Грузим библиотечный модуль
import math         #Математические вычисления
import random       #Генератор случайных чисел
print('Операционная система: ' + sys.platform)
print(2 ** 100)     #Возвести 2 в степень 100
x = 'Spam!'
print(x * 8)
y = (2 ** 1000)
print(len(str(y)))  #Вывести Длину(преобразовать в строку число Y)
S = 'Игорь'
print(len(S))       #Вывести длину строки Игорь
print(math.pi)      #Получить число пи
print(random.randint(1,100))    # Вывести случайно число в диапазоне от 1 до 100
St = 'Igor3232.exe'
if St.find('.')!=-1:
    print(St[: St.find('.')])   #Вывести все до точки
else:
    print(St)

