# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1
from random import randint

n = int(input('Размер массива: '))

array = [randint(0,10) for i in range(n)]
print(array)

s = int(input('Искомое число: '))

count = 0
for i in array:
    if i == s:
        count += 1

print(count)
