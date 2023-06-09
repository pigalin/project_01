# Задача 2.2. 

# Напишите функцию, которая возвращает номер квартал по номеру месяца
# Например: 
# месяц 2 (февраль) является частью первого квартала; 
# месяц 6 (июнь) является частью второго квартала; 
# месяц 11 (ноябрь) является частью четвертого квартала.

def quarter_of(month):
    if month in [1]:
        return 'месяц 1 (январь) является частью первого квартала.'
    if month in [2]:
        return 'месяц 2 (февраль) является частью первого квартала.'
    if month in [3]:
        return 'месяц 3 (март) является частью первого квартала.'
    if month in [4]:
        return 'месяц  (апрель) является частью второго квартала.'
    if month in [5]:
        return 'месяц  (май) является частью второго квартала.'
    if month in [6]:
        return 'месяц  (июнь) является частью второго квартала.'
    if month in [7]:
        return 'месяц  (июль) является частью третьего квартала.'
    if month in [8]:
        return 'месяц  (август) является частью третьего квартала.'
    if month in [9]:
        return 'месяц  (сентябрь) является частью третьего квартала.'
    if month in [10]:
        return 'месяц  (октябрь) является частью четвёртого квартала.'
    if month in [11]:
        return 'месяц  (ноябрь) является частью четвёртого квартала.'
    if month in [12]:
        return 'месяц  (декабрь) является частью четвёртого квартала.'
    elif month:
        return 'такого месяца нет'


month = int(input("Введите номер месяца: "))
print(quarter_of(month))

'''
month = int(input("Введите номер месяца: "))
if month in [1]:
    print('месяц 1 (январь) является частью первого квартала.') 
if month in [2]:
    print('месяц 2 (февраль) является частью первого квартала.')
if month in [3]:
    print('месяц 3 (март) является частью первого квартала.')
if month in [4]:
    print('месяц 4 (апрель) является частью второго квартала.')
if month in [5]:
    print('месяц 5 (май) является частью второго квартала.')
if month in [6]:
    print('месяц 6 (июнь) является частью второго квартала.')
if month in [7]:
    print('месяц 7 (июль) является частью третьего квартала.')
if month in [8]:
    print('месяц 8 (август) является частью третьего квартала.')
if month in [9]:
    print('месяц 9 (сентябрь) является частью третьего квартала.')
if month in [10]:
    print('месяц 10 (октябрь) является частью четвёртого квартала.')
if month in [11]:
    print('месяц 11 (ноябрь) является частью четвёртого квартала.')
if month in [12]:
    print('месяц 12 (декабрь) является частью четвёртого квартала.')
elif month:
    print('такого месяца нет')
'''