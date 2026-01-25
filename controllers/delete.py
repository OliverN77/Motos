from config.conexion import conn
from flask import Blueprint, render_template

delete = Blueprint('delete', __name__)

@delete.route('/delete_moto/<int:id>')
def delete_moto(id):
    mensaje = None
    connection = conn()
    
    try:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM motos WHERE id = %s', [id])
        connection.commit()
        cursor.close()
        mensaje = 'Moto eliminada correctamente'
    except Exception as e:
        mensaje = f'Error al eliminar la moto: {str(e)}'
    finally:
        connection.close()
    
    return render_template('delete.html', mensaje=mensaje)