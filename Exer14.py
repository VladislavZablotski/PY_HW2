# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input("введите число N: "))
g = 2
while g < n:
    print(g)
    g = g * 2
    

