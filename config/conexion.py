import mysql.connector
import os
from flask import g

def conn():
    connection = mysql.connector.connect(
        host=os.environ.get('HOST'),
        user=os.environ.get('USER'),
        password=os.environ.get('PASSWORD'),
        database=os.environ.get('DATABASE'),
        port=int(os.environ.get('PORT', 3306))
    )
    return connection