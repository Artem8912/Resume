# Модуль, содержащий функции для работы с базой данных
import sqlite3 as sq
from os import path
import pathlib
from aiogram import Dispatcher
from aiogram.fsm.context import FSMContext
# Создаём объект логгер для ведения журнала отчётов о событиях при выполнении кода 
import logging
logger = logging.getLogger(__name__)

# Создаём объект базы данных, связывая его с конкретным файлом
db = sq.connect(str(pathlib.Path(__file__).parent) + '\database.db')
# Создаём объект курсора для совершения операций с базой данных
cur = db.cursor()

# Функция удаления таблицы всех запросов
async def delete_table():
    cur.execute('DROP TABLE Monitors')
# Функция удаления конкретного запроса     
async def delete_request(Product_id):
    
    cur.execute(f'DELETE FROM Monitors WHERE Product_id == {Product_id}')
    db.commit()
# Функция для упорядочивания запросов    
async def ordered_request(field): 
       requests = cur.execute(f"SELECT * FROM Monitors ORDER BY {field}").fetchall()
       for row in requests:
           
           print(row) 
       db.commit()
       return requests
# Функция для отображения всех запросов
async def show_request(): 
       requests = cur.execute(f"SELECT * FROM Monitors ").fetchall()
       for row in requests:
           print(row) 
       db.commit()
       return requests
# Функция для добавления единиц измерения    
async def add_units(ls:list):
    ls1 = [list(item) for item in ls]
    for el in ls1:
        
        el[3] = str(el[3])
        el[3]+= "$"
        el[4] = str(el[4])
        el[4]+= "кг"
    return ls1
    
# Функция для получения перечня идентификаторов запросов    
async def get_ids():
    requests = cur.execute(f"SELECT Product_id FROM Monitors").fetchall()  
    list_ids = []
    for el in requests:
        list_ids.append(el[0])
    db.commit() 
    return list_ids
# Функция для создания базы данных
async def db_start():
    
    cur.execute('CREATE TABLE IF NOT EXISTS Monitors(Product_id INTEGER PRIMARY KEY NOT NULL, Company TEXT, Technology_kind TEXT, Price INTEGER, Weight INTEGER,Color TEXT) ')
    
    db.commit()
    

# Функция, добавляющая  запрос в таблицу базы данных    
async def edit_monitor_info(state:FSMContext,Product_id):
        data = await state.get_data()
        cur.execute('INSERT INTO Monitors (Product_id,Company,Technology_kind,Price,Weight,Color) VALUES (?,?,?,?,?,?) ',(Product_id,data['Company'] ,data['Technology_kind'], 
                    data['Price'],data['Weight'],data['Color']))
        await state.set_data(data)
        
        db.commit()