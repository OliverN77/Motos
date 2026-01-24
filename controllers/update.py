from config.conexion import conn
from flask import Blueprint, render_template, request, url_for, redirect

update = Blueprint('update', __name__)

@update.route('/ver_moto/<int:id>', methods=['GET'])
def ver_moto(id):
    mensaje = None
    cursor = conn.cursor()
    query = 'SELECT * FROM motos WHERE id = %s'
    cursor.execute(query, [id])
    item = cursor.fetchall()
    cursor.close()
    if item:
        return render_template('update.html', moto=item)
    else:
        mensaje = 'Moto no encontrada'
        return render_template('read.html', mensaje=mensaje)

@update.route('/update_item', methods=['POST'])
def update_moto():
    mensaje = None
    if request.method == 'POST':
        id = request.form["id"]
        modelo = request.form["modelo"]
        marca = request.form["marca"]
        color = request.form["color"]
        cilindraje = request.form["cilindraje"]
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE motos SET modelo = %s, marca = %s, color = %s, cilindraje = %s WHERE id = %s",
            (modelo, marca, color, cilindraje, id)
        )
        conn.commit()
        cursor.close()
        
        # Obtener los datos actualizados
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM motos WHERE id = %s', [id])
        item = cursor.fetchall()
        cursor.close()
        
        mensaje = 'Moto actualizada correctamente'
        return render_template('update.html', mensaje=mensaje, moto=item)
    else:
        mensaje = 'Error al actualizar la moto'
        return render_template('update.html', mensaje=mensaje)