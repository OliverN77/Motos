from config.conexion import conn
from flask import Blueprint, render_template, request

update = Blueprint('update', __name__)

@update.route('/ver_moto/<int:id>', methods=['GET'])
def ver_moto(id):
    mensaje = None
    connection = conn()
    cursor = connection.cursor()
    
    try:
        query = 'SELECT * FROM motos WHERE id = %s'
        cursor.execute(query, [id])
        item = cursor.fetchall()
        
        if item:
            return render_template('update.html', moto=item)
        else:
            mensaje = 'Moto no encontrada'
            return render_template('read.html', mensaje=mensaje)
    except Exception as e:
        mensaje = f'Error: {str(e)}'
        return render_template('read.html', mensaje=mensaje)
    finally:
        cursor.close()
        connection.close()

@update.route('/update_item', methods=['POST'])
def update_moto():
    mensaje = None
    if request.method == 'POST':
        id = request.form["id"]
        modelo = request.form["modelo"]
        marca = request.form["marca"]
        color = request.form["color"]
        cilindraje = request.form["cilindraje"]
        
        connection = conn()
        cursor = connection.cursor()
        
        try:
            cursor.execute(
                "UPDATE motos SET modelo = %s, marca = %s, color = %s, cilindraje = %s WHERE id = %s",
                (modelo, marca, color, cilindraje, id)
            )
            connection.commit()
            cursor.close()
            
            # Obtener los datos actualizados
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM motos WHERE id = %s', [id])
            item = cursor.fetchall()
            
            mensaje = 'Moto actualizada correctamente'
            return render_template('update.html', mensaje=mensaje, moto=item)
        except Exception as e:
            mensaje = f'Error al actualizar la moto: {str(e)}'
            return render_template('update.html', mensaje=mensaje)
        finally:
            cursor.close()
            connection.close()