# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции sorted, max и min использовать нельзя!
"""
def minimum(arr):
    pass

def maximum(arr):
    pass
"""
def minimum(arr): 
    n = arr[0]
    for m in arr:
        # print(m)
        if m < n:
           n = m
    return n 

def maximum(arr): 
    x = arr[0]
    for m in arr:
        # print(m)
        if m > x:
           x = m
    return x


list = [1,4,5,2,6,12,8,-1,14,-2]
result1 = minimum(list)
result2 = maximum(list)
print("Минимальное значение  -",result1)  # вернется -2
print("Максимальное значение -",result2)  # вернется 14
print(list, " -> max =", result2, ",", "min =", result1)

