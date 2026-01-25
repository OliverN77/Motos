import mysql.connector


conn = mysql.connector.connect(
        host='sql5.freesqldatabase.com',
        user='sql5815303',
        password='MhRxWzuYVv',
        database='sql5815303',
        port=3306
    )

if conn.is_connected():
    print ('Conexion exitosa')
else:
    print('Conexion fallida')