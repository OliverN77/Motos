from config.conexion import conn
from flask import Blueprint, render_template, request

read = Blueprint('read', __name__)

@read.route("/")
def home():
    search_query = request.args.get('search_query', '')
    modelo = request.args.get('modelo', '')
    marca = request.args.get('marca', '')
    color = request.args.get('color', '')
    cilindraje_range = request.args.get('cilindraje_range', 'all')
    order_by = request.args.get('order_by', 'id_asc')
    
    connection = conn()
    cursor = None
    
    try:
        cursor = connection.cursor()
        
        query = "SELECT * FROM motos WHERE 1=1"
        params = []
        
        if search_query:
            query += " AND (modelo LIKE %s OR marca LIKE %s OR color LIKE %s)"
            search_param = f"%{search_query}%"
            params.extend([search_param, search_param, search_param])
        
        if modelo:
            query += " AND modelo LIKE %s"
            params.append(f"%{modelo}%")
        
        if marca:
            query += " AND marca LIKE %s"
            params.append(f"%{marca}%")
        
        if color:
            query += " AND color LIKE %s"
            params.append(f"%{color}%")
        
        if cilindraje_range != 'all':
            if cilindraje_range == '0-100':
                query += " AND cilindraje >= 0 AND cilindraje <= 100"
            elif cilindraje_range == '100-200':
                query += " AND cilindraje > 100 AND cilindraje <= 200"
            elif cilindraje_range == '200-300':
                query += " AND cilindraje > 200 AND cilindraje <= 300"
            elif cilindraje_range == '300-500':
                query += " AND cilindraje > 300 AND cilindraje <= 500"
            elif cilindraje_range == '500-750':
                query += " AND cilindraje > 500 AND cilindraje <= 750"
            elif cilindraje_range == '750-1000':
                query += " AND cilindraje > 750 AND cilindraje <= 1000"
            elif cilindraje_range == '1000-plus':
                query += " AND cilindraje > 1000"
        
        if order_by == 'id_asc':
            query += " ORDER BY id ASC"
        elif order_by == 'id_desc':
            query += " ORDER BY id DESC"
        elif order_by == 'modelo_asc':
            query += " ORDER BY modelo ASC"
        elif order_by == 'modelo_desc':
            query += " ORDER BY modelo DESC"
        elif order_by == 'marca_asc':
            query += " ORDER BY marca ASC"
        elif order_by == 'marca_desc':
            query += " ORDER BY marca DESC"
        elif order_by == 'cilindraje_asc':
            query += " ORDER BY cilindraje ASC"
        elif order_by == 'cilindraje_desc':
            query += " ORDER BY cilindraje DESC"
        
        cursor.execute(query, params)
        motos_list = cursor.fetchall()
        
        return render_template('read.html', 
                             motos=motos_list,
                             search_query=search_query,
                             modelo=modelo, 
                             marca=marca, 
                             color=color, 
                             cilindraje_range=cilindraje_range,
                             order_by=order_by)
    except Exception as e:
        print(f"Error al ejecutar la consulta: {e}")
        return render_template('read.html', 
                             motos=[],
                             search_query=search_query,
                             modelo=modelo, 
                             marca=marca, 
                             color=color, 
                             cilindraje_range=cilindraje_range,
                             order_by=order_by)
    finally:
        if cursor:
            cursor.close()
        connection.close()
