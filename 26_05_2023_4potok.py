# -*- coding: utf-8 -*-
"""26_05_2023_4potok.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aH4OAS66ue5U2o1PbTkJamg8nuxRZHuD
"""

from traitlets.config.loader import ArgumentParser
x = 5
y = 'Privet mir'
x = 10
z = 1.05
arr = [1,2,3,4,5,1.05,"test1"]

arr2 = arr

print(type(arr))
print(arr)

print(len(arr))
print(arr2)

try:
  x = int(input("Введи делимое: "))
  y = int(input("Введи делитель: "))
  a = x/y
  print(a)
except ZeroDivisionError:
  print ("Деление на 0")
  x = int(input("Введи делимое: "))
  y = int(input("Введи делитель: "))
  a = x/y
  print(a)
finally:
  print ("Блок файнали отработал")

import random
a = random.randint(50,70)
print (a)

import random
arr = [1,2,3,4,5,67,80, "ntgjgj", 'fb3eogb'] # Создал переменную со значениями
# b = random.choice(arr)
print ("b")

import random

x = random.random()
print (x)

import random

brocok1 = random.randint(1,6)
brocok2 = random.randint(1,6)
brocok3 = random.randint(1,6)
brocok4 = random.randint(1,6)

total = brocok1 + brocok2 + brocok3 + brocok4

print ("Бросок №1: ",brocok1, "Бросок №2: ",brocok2, "Бросок №3: ",brocok3, "Бросок №4: ",brocok4)
print ("Всего очков: ", total)

import random

x = 4
y = []
total = 0

while x != 0:
  brocok = random.randint(1,6)
  x -= 1
  y.append(brocok)
  print (y)

for i in y:
  total += i
  print (total)

print ("Всего очков: ", total)

import random 

chars = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
lenght = input("Длинна пароля: ")
password =""

try:
  lenght = int(lenght)
  for i in range(lenght):
    password += random.choice(chars)
  print (password)
except ValueError:
  print("Вы ввели буквы заместо цифр для длинны пароля")
  lenght = input("Длинна пароля: ")
  lenght = int(lenght)
  for i in range(lenght):
    password += random.choice(chars)
  print (password)

x = 5.78
y = int(x)
print (y)