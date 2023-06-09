# -*- coding: utf-8 -*-
"""13_06_2023_4potok.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Z4O76dkpf4RtXHdu2XKMlIxn5nb2rckL
"""

#import sqlite3

# Создание первой таблицы

#connection = sqlite3.connect("teachers.db")
#cursor = connection.cursor()
#query = """CREATE TABLE School (
#School_Id INTEGER NOT NULL PRIMARY KEY,
#School_Name TEXT NOT NULL,
#Place_Count INTEGER NOT NULL);"""
#cursor.execute(query)
#connection.commit()
#connection.close()

#import sqlite3

# Наполнение первой таблицы

#connection = sqlite3.connect("teachers.db")
#cursor = connection.cursor()
#query = """INSERT INTO School (School_Id , School_Name , Place_Count)
#VALUES
#('1', 'Протон', 200),
#('2', 'Преспектива', 300),
#('3', 'Спектр', 400),
#('4', 'Содружество', 500);"""
#cursor.execute(query)
#connection.commit()
#connection.close()

#import sqlite3

# Создание второй таблицы

#connection = sqlite3.connect("teachers.db")
#cursor = connection.cursor()
#query = """CREATE TABLE Teacher (
#Teacher_Id INTEGER NOT NULL PRIMARY KEY,
#Teacher_Name TEXT NOT NULL,
#School_Id INTEGER NOT NULL,
#Joining_Date TEXT NOT NULL,
#Speciality TEXT NOT NULL,
#Salary INTEGER NOT NULL,
#Experience INTEGER);"""
#cursor.execute(query)
#connection.commit()
#connection.close()

#import sqlite3

# Наполнение второй таблицы
#connection = sqlite3.connect('teachers.db')
#cursor = connection.cursor()
#query = """INSERT INTO Teacher (Teacher_Id, Teacher_Name, School_Id, Joining_Date, Speciality, Salary, Experience)
#VALUES
#('101', 'Галина', '1', '2021-02-10', 'Физик', '40000', NULL),
#('102', 'Мария', '1', '2018-07-23', 'Химик', '20000', NULL),
# ('103', 'Ольга', '2', '2022-05-19', 'Информатик', '25000', NULL),
# ('104', 'Полина', '2', '2017-12-28', 'Физик', '28000', NULL),
# ('105', 'Лидия', '3', '2015-06-04', 'Информатик', '42000', NULL),
# ('106', 'Анастасия', '3', '2019-09-11', 'Учитель трудов', '30000', NULL),
# ('107', 'Ирина', '4', '2020-08-21', 'Информатик', '32000', NULL),
# ('108', 'Виктория', '4', '2017-10-17', 'Географ', '30000', NULL);"""
# cursor.execute(query)
# connection.commit()
# connection.close()

# import sqlite3

# def get_connection(): # Функция подключения.
#   connection = sqlite3.connect('teachers.db')
#   return connection

# def close_connection(connection): # Функция соединения и закрытия.
#   if connection:
#     connection.close() 

# def read_database_version(): # Функция вызова запроса версии.
#   try:
#     connection = get_connection()
#     cursor = connection.cursor()
#     cursor.execute("SELECT sqlite_version();")
#     version = cursor.fetchone()
#     print (version)
#     close_connection(connection)
#     print ("Вы подключись к версии Sqlite: ", version)
#   except (Exception, sqlite3.Error) as error:
#     print ('Ошибка в получении данных ', error)

#read_database_version()

# Задача 3.Проставить опыт работы всем учителям

# import sqlite3

# def get_connection():
#   connection = sqlite3.connect('teachers.db')
#   return connection

# def close_connection(connection):
#   if connection:
#     connection.close()

# def update_exp():
#   try:
#     connection = get_connection()
#     cursor = connection.cursor()
#     cursor.execute("UPDATE Teacher SET Experience = 15 WHERE School_Id = 3")
#     connection.commit()
#     close_connection(connection)
#   except (Exception, sqlite3.Error) as error:
#     print ('Ошибка в получении данных ', error)

# update_exp()

# # Задача 4 . Вывести данные о школе и учителе, используя идентификатор школы и идентификатор учителя
# import sqlite3

# def get_connection():
#   connection = sqlite3.connect('teachers.db')
#   return connection

# def close_connection(connection):
#   if connection:
#     connection.close()

# def get_school(school_id):
#   try:
#     connection = get_connection()
#     cursor = connection.cursor()
#     query = """SELECT * FROM School WHERE School_Id = ?"""
#     cursor.execute(query,(school_id,))
#     records = cursor.fetchall()
#     print ("Данные по школе:")
#     for row in records:
#       print ("ID школы:", row[0])
#       print ("Название школы:", row[1])
#       print ("Количество мест:", row[2])
#     close_connection(connection)
#   except (Exception, sqlite3.Error) as error:
#     print ('Ошибка в получении данных ', error)

# get_school(4)
# #get_teacher(102)

# # Задача 5 . Вывести список учителей по заданной специальности и зарплате
# import sqlite3

# def get_connection():
#   connection = sqlite3.connect('teachers.db')
#   return connection

# def close_connection(connection):
#   if connection:
#     connection.close()

# def get_techer_salary(speciality, salary):
#   try:
#     connection = get_connection()
#     cursor = connection.cursor()
#     query = """SELECT * FROM Teacher WHERE Speciality = ? AND Salary > ?"""
#     cursor.execute(query,(speciality, salary,))
#     records = cursor.fetchall()
#     for row in records:
#       print ("ID учителя:", row[0])
#       print ("Имя учителя:", row[1])
#       print ("ID школы:", row[2])
#       print ("Дата найма:", row[3])
#       print ("Специальность:", row[4])
#       print ("ЗП:", row[5])
#       print ("Опыт работы:", row[6], "\n")
#     close_connection(connection)
#   except (Exception, sqlite3.Error) as error:
#     print ('Ошибка в получении данных ', error)
# get_techer_salary("Физик", 20000)


# # Задача 6 . Вывести список учителей по ID школы
# import sqlite3

# def get_connection():
#   connection = sqlite3.connect('teachers.db')
#   return connection

# def close_connection(connection):
#   if connection:
#     connection.close()

# def get_school_name(school_id):
#   try:
#     connection = get_connection()
#     cursor = connection.cursor()
#     query = "SELECT * FROM School WHERE School_Id = ?"
#     cursor.execute(query,(school_id,))
#     record = cursor.fetchone()
#     close_connection(connection)
#     return record[1]
#   except (Exception, sqlite3.Error) as error:
#     print ('Ошибка в получении данных ', error)

# def get_teacher_data(school_id):
#   try:
#     connection = get_connection()
#     cursor = connection.cursor()
#     query = "SELECT * FROM Teacher WHERE School_Id = ?"
#     cursor.execute(query,(school_id,))
#     records = cursor.fetchall()
#     for row in records:
#       print ("ID учителя:", row[0])
#       print ("Имя учителя:", row[1])
#       print ("ID школы:", row[2])
#       print ("Название школы:", get_school_name(row[2]))
#       print ("Дата найма:", row[3])
#       print ("Специальность:", row[4])
#       print ("ЗП:", row[5])
#       print ("Опыт работы:", row[6], "\n")
#   except (Exception, sqlite3.Error) as error:
#     print ('Ошибка в получении данных ', error)


# get_teacher_data(1)


# Получить наименование таблиц из БД
# import sqlite3
# connection = get_connection()
# cursor = connection.cursor()
# cursor.execute("""SELECT * FROM sqlite_master WHERE type = 'table'""")
# tables = cursor.fetchall()
# connection.close()

# for table in tables:
#   # print(table) # информация по таблице
#   print(table[1]) # информация по названию таблиц

# Получить наименования столбцов
import sqlite3
connection = get_connection()
cursor = connection.cursor()
cursor.execute("""SELECT * FROM Teacher""")
colnames = cursor.description
connection.close()

for name in colnames:
  print(name[0])

