from config.conexion import conn
from flask import Blueprint, render_template, url_for

delete = Blueprint('delete', __name__)

@delete.route('/delete_moto/<int:id>')
def delete_moto(id):
    mensaje = None
    try:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM motos WHERE id = %s', [id])
        conn.commit()
        cursor.close()
        mensaje = 'Moto eliminada correctamente'
    except Exception as e:
        mensaje = f'Error al eliminar la moto: {str(e)}'
    
    return render_template('delete.html', mensaje=mensaje)