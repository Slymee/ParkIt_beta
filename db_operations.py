import mysql.connector
import tkinter as tk
from datetime import datetime


# from tkinter import *
# from tkinter import filedialog

def guiMessageDisplay(message):
    window = tk.Tk()

    label = tk.Label(window, text=" ")
    label.pack()

    label.config(text=message)

    window.mainloop()




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
        cursor.close()
        dbConnect.close()
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
    # print(datas)

    selectSQL = f"SELECT vehi_plate FROM current_vehicle_table WHERE vehi_plate = '{vehi_plate}'"
    cursor.execute(selectSQL)
    result = cursor.fetchall()

    if(len(result) == 0):
        cursor.execute('INSERT INTO current_vehicle_table(vehi_plate, vehi_entry_date, vehi_entry_time) VALUES(%s,%s,%s)', datas)
        dbConnect.commit()
        print("Vehicle Registered!!")
        guiMessageDisplay("Vehicle Registered!!")

    else:
        print("Vehicle Already Exists!!")
        guiMessageDisplay("Vehicle Already Exists!!")

    cursor.close()
    dbConnect.close()



def vehicleExit(vehi_plate, vehi_exit_date, vehi_exit_time):
    dbConnect = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '',
    database = 'parkit_database'
    )
    cursor=dbConnect.cursor()
    
    datas = (vehi_plate, vehi_exit_date, vehi_exit_time)
    basePrice , increamentPrice = fetchPrice()

    selectSQL = f"SELECT vehi_entry_date, vehi_entry_time FROM current_vehicle_table WHERE vehi_plate = '{vehi_plate}'"
    cursor.execute(selectSQL)
    result = cursor.fetchall()
    vehi_entry_time = None
    vehi_entry_date = None

    for row in result:
        vehi_entry_date = row[0]
        vehi_entry_time = row[1]

    if vehi_entry_date is not None and vehi_entry_time is not None:
        print(vehi_entry_time)
        print((vehi_exit_time))

        full_entry_datetime = f"{vehi_entry_date} {vehi_entry_time}:00"

        full_entry_datetime = datetime.strptime(full_entry_datetime,"%Y-%m-%d %H:%M:%S")

        full_exit_datetime = f"{vehi_exit_date} {vehi_exit_time}:00"
        full_exit_datetime = datetime.strptime(full_exit_datetime,"%Y-%m-%d %H:%M:%S")

        time_diff = full_exit_datetime - full_entry_datetime
        
        time_diff_in_hour = time_diff.seconds // 3600
        
        price = basePrice + time_diff_in_hour * increamentPrice

        printBill=(f"You parked for {time_diff_in_hour} hour. Your total price is {price}")
        print(printBill)

        insertSQL= f"INSERT INTO all_vehicle_table(vehi_plate, vehi_entry_date, vehi_entry_time, vehi_fees) VALUES('{vehi_plate}','{vehi_entry_date}','{vehi_entry_time}','{price}')"
        deleteSQL = f"DELETE FROM current_vehicle_table WHERE vehi_plate='{vehi_plate}'"
        cursor.execute(insertSQL)
        cursor.execute(deleteSQL)
        dbConnect.commit()

        guiMessageDisplay(printBill)

    else:
        print("New vehicle cannot exit")

    cursor.close()
    dbConnect.close()

        # entry_day = int(str(vehi_entry_date).split("-")[2])
        # exit_day = int(str(vehi_exit_date).split("-")[2])

        # diff_date = exit_day - entry_day

        # if diff_date < 0:
        #     print("Not possible")
        # elif diff_date == 0:
        #     print("Same day exit") 
            
    #         exit_hour = int(str(vehi_exit_time).split(':')[0])
    #         entry_hour = int(str(vehi_entry_time).split(':')[0])

    #         diff_hour = exit_hour - entry_hour
    #         price = 0
    #         print_data = ""
    #         if diff_hour <= 0:
    #             price = basePrice

    #             print_data = f"You parked for lass than an hour. So the base price is {price}"
    #         else:
    #             price = basePrice + (increamentPrice * diff_hour)
    #             print_data = f"You parked for {diff_hour} hour so the price is {price}"

    #         print(print_data)

    #     else:
    #         print("Different day exit")

    # else:
    #     print("No data found")

        







    # for row in result:
    #     if row[0] is None:
            # cursor.execute('INSERT INTO current_vehicle_table(vehi_plate, vehi_entry_date, vehi_entry_time) VALUES(%s,%s,%s)', datas)
            # dbConnect.commit()
            # print("Vehicle Registered")
    #         break

    #     else:
    #         print("Vehicle Already registered")
    #         break