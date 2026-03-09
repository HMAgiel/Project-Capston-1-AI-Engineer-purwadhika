import mysql.connector

def database():
    DATA = mysql.connector.connect(
        host = "localhost",
        user = "user",
        password = "Batu123456789!",
        database = "data_kependudukan_indonesia"
    )
    return DATA