"# 🏍️ Sistema CRUD de Gestión de Motos

Una aplicación web moderna y completa para gestionar un inventario de motocicletas, desarrollada con Flask y MySQL.

## ✨ Características

- ✅ **Crear** - Registra nuevas motocicletas con sus especificaciones
- 📖 **Leer** - Visualiza el inventario completo de motos
- ✏️ **Actualizar** - Modifica la información de motos existentes
- 🗑️ **Eliminar** - Elimina registros de motos del sistema

## 🚀 Tecnologías Utilizadas

- **Backend**: Flask (Python)
- **Base de Datos**: MySQL
- **Frontend**: HTML5, CSS3, JavaScript
- **Arquitectura**: MVC (Model-View-Controller)

## 📋 Requisitos Previos

- Python 3.7 o superior
- MySQL Server 5.7 o superior
- pip (gestor de paquetes de Python)

## 🔧 Instalación

### 1. Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd motos
```

### 2. Crear entorno virtual (recomendado)

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar la Base de Datos

Crear la base de datos en MySQL:

```sql
CREATE DATABASE taller_motos;

USE taller_motos;

CREATE TABLE motos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    modelo VARCHAR(100) NOT NULL,
    marca VARCHAR(100) NOT NULL,
    color VARCHAR(50) NOT NULL,
    cilindraje VARCHAR(50) NOT NULL
);
```

### 5. Configurar la conexión

Edita el archivo `config/conexion.py` con tus credenciales de MySQL:

```python
conn = mysql.connector.connect(
    host='localhost',
    user='tu_usuario',
    password='tu_contraseña',
    database='taller_motos'
)
```

## 🎮 Uso

### Iniciar la aplicación

```bash
python app.py
```

La aplicación estará disponible en: `http://localhost:5000`

### Rutas disponibles

- `/create_page` - Formulario para crear nuevas motos
- `/read_page` - Ver todas las motos registradas
- `/update_page` - Actualizar información de motos
- `/delete_page` - Eliminar motos del sistema

## 📁 Estructura del Proyecto

```
motos/
│
├── app.py                  # Punto de entrada de la aplicación
├── requirements.txt        # Dependencias del proyecto
├── README.md              # Documentación
│
├── config/
│   └── conexion.py        # Configuración de la base de datos
│
├── controllers/           # Lógica de negocio (Controladores)
│   ├── create.py         # Controlador de creación
│   ├── read.py           # Controlador de lectura
│   ├── update.py         # Controlador de actualización
│   └── delete.py         # Controlador de eliminación
│
├── templates/            # Vistas HTML
│   ├── create.html
│   ├── read.html
│   ├── update.html
│   └── delete.html
│
└── static/              # Archivos estáticos
    ├── css/            # Estilos CSS
    ├── js/             # Scripts JavaScript
    └── img/            # Imágenes
```

## 🛠️ Funcionalidades por Módulo

### Crear Moto
Permite registrar una nueva motocicleta ingresando:
- Modelo
- Marca
- Color
- Cilindraje

### Consultar Motos
Muestra una tabla con todas las motocicletas registradas en el sistema.

### Actualizar Moto
Permite modificar la información de una motocicleta existente.

### Eliminar Moto
Permite eliminar un registro de motocicleta del sistema.

## 🤝 Contribuir

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto es de código abierto y está disponible bajo la Licencia MIT.

## 👤 Autor

Desarrollado con ❤️ para la gestión eficiente de inventarios de motocicletas.

---

⭐ Si te ha gustado este proyecto, no olvides darle una estrella!" 
