#used for mass updating the database
import pyodbc
import datetime
import random
import string

with open ("databaselogin.txt", "r") as f:
    cs = f.read()

def connect():
    cnxn = pyodbc.connect(cs)
    return cnxn

def update_seats():
    cnxn = connect()
    cursor = cnxn.cursor()
    for Row in ["A","B","C","D","E","F","G","H","I","J"]:
        for number in range(1,21):
            seatid = Row + str(number)
            if number in range(1,10):
                seatRow = f"Row{Row}_A"
            elif number in range(11,20):
                seatRow = f"Row{Row}_B"
            cursor.execute("INSERT INTO Seats Values(?,?)", (seatid,seatRow))
    rows_affected = cursor.rowcount
    if rows_affected > 0:
        cnxn.commit()
        print("Added", rows_affected, "seats")

