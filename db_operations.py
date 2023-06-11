import mysql.connector
import tkinter as tk


# from tkinter import *
# from tkinter import filedialog

def dbConnect():
    dbConnect = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '',
    database = 'parkit_database'
    )
    return dbConnect




def fetchPrice():
    dbConnect = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '',
    database = 'parkit_database'
    )
    cursor = dbConnect.cursor()
    cursor.execute('SELECT * FROM parking_price_table')

    for row in cursor.fetchall():
        return row[0], row[1]
    
    cursor.close()
    dbConnect.close()




def vehicleEntry(vehi_plate, vehi_entry_date, vehi_entry_time):

    dbConnect = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '',
    database = 'parkit_database'
    )
    cursor = dbConnect.cursor()

    datas = (vehi_plate, vehi_entry_date, vehi_entry_time)


    cursor.execute('SELECT vehi_plate FROM current_vehicle_table')

    for row in cursor.fetchall():
        if(row[0]==vehi_plate):
            print("Vehicle Exists!!")
            break
        else:
            cursor.execute('INSERT INTO current_vehicle_table(vehi_plate, vehi_entry_date, vehi_entry_time) VALUES(%s,%s,%s)', datas)
            print("Vehicle Registered")
            dbConnect.commit()

            

    




