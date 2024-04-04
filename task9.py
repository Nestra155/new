'''
<<<<<<< HEAD
Напишите программу, которая принимает на вход 3 длины сторон треугольника
и вычисляет площадь треугольника по формуле Герона.
'''
from math import *

a = int(input("введите число:"))
b = int(input("введите число:"))
c = int(input("введите число:"))
p = (a + b + c)/2
Area = sqrt((p * (p - a) * (p - b) * (p - c)))
print(Area)
=======
Данаe строкаs. Замените в этой строке все цифры 1 на слово one.
'''
# Дана строка
s = "I have 1 apple and 2 oranges."

# Преобразуем строку в список символов для удобства работы
chars = list(s)

# Заменяем все вхождения цифры 1 на слово "one"
for i in range(len(chars)):
    if chars[i] == '1':
        chars[i] = 'o'
        chars.insert(i+1, 'n')
        chars.insert(i+2, 'e')

# Преобразуем список обратно в строку
new_s = ''.join(chars)

print(new_s)
>>>>>>> 56c667a (first commit)
