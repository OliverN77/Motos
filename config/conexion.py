import mysql.connector


conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='taller_motos'
    )

if conn.is_connected():
    print ('Conexion exitosa')
else:
    print('Conexion fallida')