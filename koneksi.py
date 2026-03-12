import mysql.connector

def database():
    DATA = mysql.connector.connect(
        host = "localhost",
        user = "user",
        password = "password",
        database = "data_kependudukan_indonesia"
    )
    return DATA