# Задача 1.3.

# Напишите скрипт, который принимает от пользователя номер месяца, 
# а возвращает количество дней в нем.
# Результат проверки вывести на консоль
# Допущение: в феврале 28 дней
# Если номер месяца некорректен - сообщить об этом

# Например,
    # Введите номер месяца: 3
    # Вы ввели март. 31 дней

    # Введите номер месяца: 2
    # Вы ввели февраль. 28 дней

    # Введите номер месяца: 15
    # Такого месяца нет!

month = int(input("Введите номер месяца:"))

if month == 1:
    print("Вы ввели месяц январь, 31 день")
if month == 2:
    print("Вы ввели месяц февраль, 28 дней")
if month == 3:
    print("Вы ввели месяц март, 31 день")
if month == 4:
    print("Вы ввели месяц апрель, 30 дней")
if month == 5:
    print("Вы ввели месяц май, 31 день")
if month == 6:
    print("Вы ввели месяц июнь, 30 дней")
if month == 7:
    print("Вы ввели месяц июль, 31 день")
if month == 8:
    print("Вы ввели месяц август, 31 день")
if month == 9:
    print("Вы ввели месяц сентябрь, 30 дней")
if month == 10:
    print("Вы ввели месяц октябрь, 31 день")
if month == 11:
    print("Вы ввели месяц ноябрь, 30 дней")
if month == 12:
    print("Вы ввели месяц декабрь, 31 день")
if month >= 13:
    print("Такого месяца нет!")