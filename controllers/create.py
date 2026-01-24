from config.conexion import conn
from flask import Blueprint, render_template, request, url_for

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
        cursor = conn.cursor()
        if request.method != "POST":
                mensaje = "Error al registrar una moto"
                return render_template('read.html', mensaje=mensaje)
        cursor.execute(
                "INSERT INTO motos (modelo, marca, color, cilindraje) VALUES (%s, %s, %s, %s)", (modelo,marca,color,cilindraje)
            )
        conn.commit()
        mensaje = "Moto agregada correctamente"
        return render_template("create.html", mensaje=mensaje)