'''
<<<<<<< HEAD
Напишите программу, которая вычисляет площадь круга с заданным пользователем 
радиусом.

Sample Input 1:
1.1

Sample Output 1:
3.8013271108436504
'''
radius = float(input("Введите радиус круга: "))

area = 3.14 * radius**2

print(area)
=======
Дана строкаes, состоящая ровно из двух слов, разделенных пробелом. 
Переставьте эти слова местами. Результат запишите в строку и выведите получившуюся строку.

При решении этой задачи не стоит пользоваться циклами и инструкцией if.
'''
# Дана строка из двух слов, разделенных пробелом
s = "Hello World"

# Перестановка слов местами
new_s = " ".join(reversed(s.split()))

print(new_s)
>>>>>>> 56c667a (first commit)
