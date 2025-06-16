import sqlite3 as sq
from aiogram import Dispatcher
from aiogram.fsm.context import FSMContext
import logging
logger = logging.getLogger(__name__)

db = sq.connect(r'C:\Users\DNS\Desktop\Git works 2\Bots\Resume\DataBase_bot\Service\general_database.db')
cur = db.cursor()

async def delete_table():
    cur.execute('DROP TABLE Monitors')
    
async def delete_request(Product_id):
    
    cur.execute(f'DELETE FROM Monitors WHERE Product_id == {Product_id}')
    db.commit()
    
async def ordered_request(field): 
       requests = cur.execute(f"SELECT * FROM Monitors ORDER BY {field}").fetchall()
       for row in requests:
           print(row) 
       db.commit()
       return requests

async def show_request(): 
       requests = cur.execute(f"SELECT * FROM Monitors ").fetchall()
       for row in requests:
           print(row) 
       db.commit()
       return requests
   
async def get_ids():
    requests = cur.execute(f"SELECT Product_id FROM Monitors").fetchall()  
    list_ids = []
    for el in requests:
        list_ids.append(el[0])
    db.commit() 
    return list_ids

async def db_start():
    
    cur.execute('CREATE TABLE IF NOT EXISTS Monitors(Product_id INTEGER PRIMARY KEY NOT NULL, Company TEXT, Technology_kind TEXT, Price TEXT, Weight TEXT,Color TEXT) ')
    
    db.commit()
    

    
async def edit_monitor_info(state:FSMContext,Product_id):
        data = await state.get_data()
        cur.execute('INSERT INTO Monitors (Product_id,Company,Technology_kind,Price,Weight,Color) VALUES (?,?,?,?,?,?) ',(Product_id,data['Company'] ,data['Technology_kind'], 
                    data['Price'],data['Weight'],data['Color']))
        await state.set_data(data)
        
        db.commit()