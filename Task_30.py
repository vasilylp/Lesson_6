"""Задача 30: Заполните массив элементами арифметической
прогрессии. Её первый элемент, разность и количество
элементов нужно ввести с клавиатуры. Формула для
получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки."""

# a = int(input("Введите число A :"))
# d = int(input("Введите шаг прогрессии d :"))
# n = int(input("Введите длинну арифметической прогрессии n :"))

# progress = []
# for i in range(1,n + 1):
#     an = a + (i - 1) * d
#     progress.append(an)
# print(progress)

# Solution 2_________________________________
a, d, n = map(int, input("Введите 3 числа через пробел : ").split())
for i in range (a, a + (n - 1) * d + 1, d):
    print(i)



