# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5


from random import randint

n = int(input('Размер массива: '))
array = [randint(0,10) for i in range(n)]
print(array)

s = int(input('Искомое число: '))
find = array[0]
diff = s - find
for i in array:
    if abs(s - i) < diff:
        find = i
        diff = s - find
print(find)