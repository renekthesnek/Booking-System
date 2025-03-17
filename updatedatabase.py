#used for mass updating the database
import pyodbc
import hashlib
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
            print(f"Added {seatid} {seatRow} to database")
    rows_affected = cursor.rowcount
    if rows_affected > 0:
        cnxn.commit()
        print("successfully added seats")

def add_staff_users():
    cnxn = connect()
    cursor = cnxn.cursor()
    cursor.execute("INSERT INTO Users (userID,username,password_hash,first_name,last_name,Permission) VALUES (?,?,?,?,?,?)", (1,"Renk","6498303739743560f7a1817a54d0889f7fd69de9649584722ea69973","Reno","Barry","Staff"))
    cursor.execute("INSERT INTO Users (userID,username,password_hash,first_name,last_name,Permission) VALUES (?,?,?,?,?,?)", (2,"Helen","d63dc919e201d7bc4c825630d2cf25fdc93d4b2f0d46706d29038d01","Helen","B","Staff"))
    rows_affected = cursor.rowcount
    if rows_affected > 0:
        cnxn.commit()
        print("successfully added staff users")

def database_setup():
    update_seats()
    add_staff_users()
