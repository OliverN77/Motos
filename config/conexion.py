import mysql.connector

def conn():
    connection = mysql.connector.connect(
        host='sql5.freesqldatabase.com',
        user='sql5815303',
        password='MhRxWzuYVv',
        database='sql5815303',
        port=3306
    )
    return connection