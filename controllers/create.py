from config.conexion import conn
from flask import Blueprint, render_template, request

create = Blueprint('create', __name__)

@create.route('/create_page')
def create_page():
    return render_template('create.html')

@create.route('/create_register', methods=["GET", "POST"])
def create_register():
    mensaje = None
    if request.method == "POST":
        modelo = request.form["modelo"]
        marca = request.form["marca"]
        color = request.form["color"]
        cilindraje = request.form["cilindraje"]
        
        connection = conn()
        cursor = connection.cursor()
        
        try:
            cursor.execute(
                "INSERT INTO motos (modelo, marca, color, cilindraje) VALUES (%s, %s, %s, %s)", 
                (modelo, marca, color, cilindraje)
            )
            connection.commit()
            mensaje = "Moto agregada correctamente"
        except Exception as e:
            mensaje = f"Error al registrar la moto: {str(e)}"
        finally:
            cursor.close()
            connection.close()
        
        return render_template("create.html", mensaje=mensaje)