""" 
API de gestión de proveedores, categorías, ubicaciones, productos y usuarios.
"""

import datetime
import os  # Importación estándar
import MySQLdb
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth

from config import config
from validation import validar_apellido, validar_correo, validar_empresa, validar_nombre, validar_proveedor, validar_categoria, validar_ubicacion, validar_producto # Importaciones locales

"""
Este módulo proporciona una API para gestionar proveedores, categorías, ubicaciones, productos y usuarios.
"""

app = Flask(__name__)
CORS(
    app,
    resources={
        r"/proveedor/*": {"origins": "http://localhost:4200"},
        r"/producto/*": {"origins": "http://localhost:4200"},
        r"/categoria/*": {"origins": "http://localhost:4200"},
        r"/ubicacion/*": {"origins": "http://localhost:4200"},
        r"/usuario/*": {"origins": "http://localhost:4200"},
        r"/login/*": {"origins": "http://localhost:4200"},
        r"/historialcambio/*": {"origins": "http://localhost:4200"},
        r"/notificacion/*": {"origins": "http://localhost:4200"},
        r"/proveedor/<RutProveedor>": {"origins": "http://localhost:4200"},
        r"/producto/<IdProducto>": {"origins": "http://localhost:4200"},
    },
)

conexion = MySQL(app)
auth = HTTPBasicAuth()
users = {"root": generate_password_hash(os.getenv("ADMIN_PASSWORD", "stock")),
         "admin": generate_password_hash(os.getenv("ADMIN_PASSWORD", "12345")),
         "Javier": generate_password_hash(os.getenv("USER_PASSWORD", "admin"))}


@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username], password):
        return username
    return None


#
# JSON Proveedor
#


@app.route("/proveedor", methods=["GET"])
def listar_proveedor():
    """
    Función para listar proveedores.
    """
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM proveedor"
        cursor.execute(sql)
        datos_proveedor = cursor.fetchall()
        proveedores = []
        for f in datos_proveedor:
            proveedor = {
                "RutProveedor": f[0],
                "Empresa": f[1],
                "Nombre": f[2],
                "Apellido": f[3],
                "Telefono": f[4],
                "Correo": f[5],
            }
            proveedores.append(proveedor)
        return jsonify(proveedores)
    except Exception as e:
        app.logger.error("Error: %s", e)
        return jsonify({"Mensaje": "No se pudo realizar la consulta"}), 500


@app.route("/proveedor/<RutProveedor>", methods=["GET"])
def leer_proveedor(rut_proveedor):
    """
    Función para leer un proveedor.
    """
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM proveedor WHERE RutProveedor = %s"
        cursor.execute(sql, (rut_proveedor,))
        datos_proveedor = cursor.fetchone()
        if datos_proveedor:
            proveedor = {
                "RutProveedor": datos_proveedor[0],
                "Empresa": datos_proveedor[1],
                "Nombre": datos_proveedor[2],
                "Apellido": datos_proveedor[3],
                "Telefono": datos_proveedor[4],
                "Correo": datos_proveedor[5],
            }
            return jsonify(proveedor)
    except Exception as e:
        app.logger.error("Error: %s", e)
        return jsonify({"Mensaje": "No se pudo realizar la consulta"}), 500


@app.route("/proveedor", methods=["POST"])
def registrar_proveedor():
    """
    Función para registrar un proveedor.
    """
    data = request.get_json()

    try:
        cursor = conexion.connection.cursor()
        sql = """INSERT INTO proveedor (RutProveedor, Empresa, Nombre, Apellido, Telefono, Correo)
                 VALUES (%s, %s, %s, %s, %s, %s)"""
        cursor.execute(
            sql,
            (
                data["RutProveedor"],
                data["Empresa"],
                data["Nombre"],
                data["Apellido"],
                data["Telefono"],
                data["Correo"],
            ),
        )
        conexion.connection.commit()

        # Registrar el cambio en la tabla historailcambio
        descripcion_cambio = f"Se agregó el proveedor {data['Empresa']} ({data['Nombre']} {data['Apellido']})"
        fecha_cambio = datetime.datetime.now().strftime('%Y-%m-%d')
        sql_cambio = "INSERT INTO historailcambio (fechaCambio, DescripcionCambio) VALUES (%s, %s)"
        cursor.execute(sql_cambio, (fecha_cambio, descripcion_cambio))
        conexion.connection.commit()

        return jsonify({"Mensaje": "Proveedor registrado"}), 201
    except MySQLdb.IntegrityError as e:
        conexion.connection.rollback()
        app.logger.error("Integrity Error: %s", e)
        return jsonify({"Mensaje": "Error de integridad de datos"}), 400
    except Exception as e:
        conexion.connection.rollback()
        app.logger.error("Error: %s", e)
        return jsonify({"Mensaje": "No se pudo registrar el proveedor"}), 500



@app.route("/proveedor/<RutProveedor>", methods=["PUT"])
def actualizar_proveedor(RutProveedor):
    try:
        cursor = conexion.connection.cursor()

        # Obtener los datos antiguos
        sql_select = "SELECT * FROM proveedor WHERE RutProveedor = %s"
        cursor.execute(sql_select, (RutProveedor,))
        datos_antiguos = cursor.fetchone()

        # Realizar la actualización
        sql_update = """UPDATE proveedor SET Empresa = %s, Nombre = %s, Apellido = %s, Telefono = %s, Correo = %s
                     WHERE RutProveedor = %s"""
        cursor.execute(
            sql_update,
            (
                request.json["Empresa"],
                request.json["Nombre"],
                request.json["Apellido"],
                request.json["Telefono"],
                request.json["Correo"],
                RutProveedor,
            ),
        )
        conexion.connection.commit()

        # Crear la descripción del cambio
        descripcion = f"Proveedor actualizado: {RutProveedor}. Datos antiguos: {datos_antiguos}, Datos nuevos: {request.json}"

        # Registrar el cambio
        sql_insert_cambio = """INSERT INTO historailcambio (fechaCambio, DescripcionCambio) 
                               VALUES (CURDATE(), %s)"""
        cursor.execute(sql_insert_cambio, (descripcion,))
        conexion.connection.commit()

        return jsonify({"Mensaje": "Proveedor actualizado"})
    except Exception as e:
        app.logger.error("Error: %s", e)
        return jsonify({"Mensaje": "No se pudo actualizar el proveedor"}), 500



@app.route("/proveedor/<RutProveedor>", methods=["DELETE"])
def eliminar_proveedor(RutProveedor):
    try:
        cursor = conexion.connection.cursor()

        # Obtener los datos antiguos
        sql_select = "SELECT * FROM proveedor WHERE RutProveedor = %s"
        cursor.execute(sql_select, (RutProveedor,))
        datos_antiguos = cursor.fetchone()

        # Realizar la eliminación
        sql_delete = "DELETE FROM proveedor WHERE RutProveedor = %s"
        cursor.execute(sql_delete, (RutProveedor,))
        conexion.connection.commit()

        # Crear la descripción del cambio
        descripcion = f"Proveedor eliminado: {RutProveedor}. Datos: {datos_antiguos}"

        # Registrar el cambio
        sql_insert_cambio = """INSERT INTO historailcambio (fechaCambio, DescripcionCambio) 
                               VALUES (CURDATE(), %s)"""
        cursor.execute(sql_insert_cambio, (descripcion,))
        conexion.connection.commit()

        return jsonify({"Mensaje": "Proveedor eliminado"})
    except Exception as e:
        app.logger.error("Error: %s", e)
        return jsonify({"Mensaje": "No se pudo eliminar el proveedor"}), 500



#
# JSON Categoria
#


@app.route("/categoria", methods=["GET"])
def listar_categoria():
    """
    Función para listar categorías.
    """
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM categoria"
        cursor.execute(sql)
        datos_categoria = cursor.fetchall()
        categorias = []
        for f in datos_categoria:
            categoria = {"IdCategoria": f[0], "Nombre": f[1]}
            categorias.append(categoria)
        return jsonify(categorias)
    except Exception as e:
        app.logger.error("Error: %s", e)
        return jsonify({"Mensaje": "No se pudo realizar la consulta"}), 500


@app.route("/categoria/<IdCategoria>", methods=["GET"])
def leer_categoria(id_categoria):
    """
    Función para leer una categoría.
    """
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM categoria WHERE IdCategoria = %s"
        cursor.execute(sql, (id_categoria,))
        datos_categoria = cursor.fetchone()
        if datos_categoria:
            categoria = {"IdCategoria": datos_categoria[0], "Nombre": datos_categoria[1]}
            return jsonify(categoria)
    except Exception as e:
        app.logger.error("Error: %s", e)
        return jsonify({"Mensaje": "No se pudo realizar la consulta"}), 500


@app.route("/categoria", methods=["POST"])
def registrar_categoria():
    """
    Función para registrar una categoría.
    """
    data = request.get_json()

    try:
        cursor = conexion.connection.cursor()
        sql = "INSERT INTO categoria (Nombre) VALUES (%s)"
        cursor.execute(sql, (data["Nombre"],))
        conexion.connection.commit()
        return jsonify({"Mensaje": "Categoria registrada"}), 201
    except Exception as e:
        app.logger.error("Error: %s", e)
        return jsonify({"Mensaje": "No se pudo registrar la categoria"}), 500


@app.route("/categoria/<IdCategoria>", methods=["PUT"])
def actualizar_categoria(id_categoria):
    """
    Función para actualizar una categoría.
    """
    data = request.get_json()

    try:
        cursor = conexion.connection.cursor()
        sql = "UPDATE categoria SET Nombre = %s WHERE IdCategoria = %s"
        cursor.execute(sql, (data["Nombre"], id_categoria))
        conexion.connection.commit()
        return jsonify({"Mensaje": "Categoria actualizada"}), 200
    except Exception as e:
        app.logger.error("Error: %s", e)
        return jsonify({"Mensaje": "No se pudo actualizar la categoria"}), 500


@app.route("/categoria/<IdCategoria>", methods=["DELETE"])
def eliminar_categoria(IdCategoria):
    """
    Función para eliminar una categoría.
    """
    try:
        cursor = conexion.connection.cursor()
        sql = "DELETE FROM categoria WHERE IdCategoria = %s"
        cursor.execute(sql, (IdCategoria,))
        conexion.connection.commit()
        return jsonify({"Mensaje": "Categoria eliminada"})
    except Exception as e:
        app.logger.error("Error: %s", e)
        return jsonify({"Mensaje": "No se pudo eliminar la categoria"}), 500


#
# JSON Ubicacion
#


@app.route("/ubicacion", methods=["GET"])
def listar_ubicacion():
    """
    Función para listar ubicaciones.
    """
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM ubicacion"
        cursor.execute(sql)
        datos_ubicacion = cursor.fetchall()
        ubicaciones = []
        for f in datos_ubicacion:
            ubicacion = {"IdUbicacion": f[0], "Nombre": f[1]}
            ubicaciones.append(ubicacion)
        return jsonify(ubicaciones)
    except Exception as e:
        app.logger.error("Error: %s", e)
        return jsonify({"Mensaje": "No se pudo realizar la consulta"}), 500


@app.route("/ubicacion/<IdUbicacion>", methods=["GET"])
def leer_ubicacion(id_ubicacion):
    """
    Función para leer una ubicación.
    """
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM ubicacion WHERE IdUbicacion = %s"
        cursor.execute(sql, (id_ubicacion,))
        datos_ubicacion = cursor.fetchone()
        if datos_ubicacion:
            ubicacion = {"IdUbicacion": datos_ubicacion[0], "Nombre": datos_ubicacion[1]}
            return jsonify(ubicacion)
        return jsonify({"Mensaje": "Ubicacion no encontrada"}), 404
    except Exception as e:
        app.logger.error("Error: %s", e)
        return (
            jsonify({"Mensaje": "No se pudo realizar la consulta", "Error": str(e)}),
            500,
        )


@app.route("/ubicacion", methods=["POST"])
def registrar_ubicacion():
    """
    Función para registrar una ubicación.
    """
    data = request.get_json()

    try:
        cursor = conexion.connection.cursor()
        sql = """INSERT INTO ubicacion (Nombre) VALUES (%s)"""
        cursor.execute(sql, (data["Nombre"],))
        conexion.connection.commit()
        return jsonify({"Mensaje": "Ubicacion registrada"}), 201
    except MySQLdb.IntegrityError as e:
        app.logger.error("Integrity Error: %s", e)
        return jsonify({"Mensaje": "Error de integridad de datos"}), 400
    except Exception as e:
        app.logger.error("Error: %s", e)
        return jsonify({"Mensaje": "No se pudo registrar la ubicacion"}), 500


@app.route("/ubicacion/<IdUbicacion>", methods=["PUT"])
def actualizar_ubicacion(id_ubicacion):
    """
    Función para actualizar una ubicación.
    """
    data = request.get_json()

    try:
        cursor = conexion.connection.cursor()
        sql = """UPDATE ubicacion SET Nombre = %s WHERE IdUbicacion = %s"""
        cursor.execute(sql, (data["Nombre"], id_ubicacion))
        conexion.connection.commit()
        return jsonify({"Mensaje": "Ubicacion actualizada"})
    except Exception as e:
        app.logger.error("Error: %s", e)
        return jsonify({"Mensaje": "No se pudo actualizar la ubicacion"}), 500


@app.route("/ubicacion/<IdUbicacion>", methods=["DELETE"])
def eliminar_ubicacion(IdUbicacion):
    """
    Función para eliminar una ubicación.
    """
    try:
        cursor = conexion.connection.cursor()
        sql = "DELETE FROM ubicacion WHERE IdUbicacion = %s"
        cursor.execute(sql, (IdUbicacion,))
        conexion.connection.commit()
        return jsonify({"Mensaje": "Ubicacion eliminada"})
    except Exception as e:
        app.logger.error("Error: %s", e)
        return jsonify({"Mensaje": "No se pudo eliminar la ubicacion"}), 500


#
# JSON Producto
#


@app.route("/producto", methods=["GET"])
def listar_productos():
    """
    Función para listar productos.
    """
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM producto"
        cursor.execute(sql)
        datos_productos = cursor.fetchall()
        productos = []
        for producto in datos_productos:
            producto_dict = {
                "IdProducto": producto[0],
                "Nombre": producto[1],
                "Marca": producto[2],
                "IdCategoria": producto[3],
                "Cantidad": producto[4],
                "FechaVencimiento": producto[5].strftime('%Y-%m-%d'),
                "Precio": producto[6],
                "IdUbicacion": producto[7]
            }
            productos.append(producto_dict)
        return jsonify(productos)
    except Exception as e:
        app.logger.error("Error: %s", e)
        return jsonify({"Mensaje": "No se pudo realizar la consulta"}), 500


@app.route("/producto/<IdProducto>", methods=["GET"])
def leer_producto(IdProducto):
    """
    Función para leer un producto por su IdProducto.
    """
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM producto WHERE IdProducto = %s"
        cursor.execute(sql, (IdProducto,))
        datos_producto = cursor.fetchone()
        if datos_producto:
            producto = {
                "IdProducto": datos_producto[0],
                "Nombre": datos_producto[1],
                "Marca": datos_producto[2],
                "IdCategoria": datos_producto[3],
                "Cantidad": datos_producto[4],
                "FechaVencimiento": datos_producto[5].strftime('%Y-%m-%d'),
                "Precio": datos_producto[6],
                "IdUbicacion": datos_producto[7]
            }
            return jsonify(producto)
        return jsonify({"Mensaje": "Producto no encontrado"}), 404
    except Exception as e:
        app.logger.error("Error: %s", e)
        return jsonify({"Mensaje": "No se pudo realizar la consulta", "Error": str(e)}), 500


@app.route("/producto", methods=["POST"])
def registrar_producto():
    """
    Función para registrar un producto.
    """
    data = request.get_json()

    try:
        cursor = conexion.connection.cursor()
        sql = """INSERT INTO producto (Nombre, Marca, IdCategoria, Cantidad, FechaVencimiento, Precio, IdUbicacion)
                 VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(
            sql,
            (
                data["Nombre"],
                data["Marca"],
                data["IdCategoria"],
                data["Cantidad"],
                data["FechaVencimiento"],
                data["Precio"],
                data["IdUbicacion"],
            ),
        )
        conexion.connection.commit()

        # Registrar el cambio en la tabla historailcambio
        descripcion_cambio = f"Se agregó el producto {data['Nombre']} de marca {data['Marca']}"
        fecha_cambio = datetime.datetime.now().strftime('%Y-%m-%d')
        sql_cambio = "INSERT INTO historailcambio (fechaCambio, DescripcionCambio) VALUES (%s, %s)"
        cursor.execute(sql_cambio, (fecha_cambio, descripcion_cambio))
        conexion.connection.commit()

        return jsonify({"Mensaje": "Producto registrado"}), 201
    except MySQLdb.IntegrityError as e:
        app.logger.error("Integrity Error: %s", e)
        return jsonify({"Mensaje": "Error de integridad de datos"}), 400
    except Exception as e:
        app.logger.error("Error: %s", e)
        return jsonify({"Mensaje": "No se pudo registrar el producto"}), 500



@app.route("/producto/<IdProducto>", methods=["PUT"])
def actualizar_producto(IdProducto):
    data = request.get_json()

    try:
        cursor = conexion.connection.cursor()

        # Obtener los datos antiguos
        sql_select = "SELECT * FROM producto WHERE IdProducto = %s"
        cursor.execute(sql_select, (IdProducto,))
        datos_antiguos = cursor.fetchone()

        # Realizar la actualización
        sql_update = """UPDATE producto SET Nombre = %s, Marca = %s, IdCategoria = %s, Cantidad = %s,
                         FechaVencimiento = %s, Precio = %s, IdUbicacion = %s WHERE IdProducto = %s"""
        cursor.execute(
            sql_update,
            (
                data["Nombre"],
                data["Marca"],
                data["IdCategoria"],
                data["Cantidad"],
                data["FechaVencimiento"],
                data["Precio"],
                data["IdUbicacion"],
                IdProducto,
            ),
        )
        conexion.connection.commit()

        # Crear la descripción del cambio
        descripcion = f"Producto actualizado: {IdProducto}. Datos antiguos: {datos_antiguos}, Datos nuevos: {data}"

        # Registrar el cambio
        sql_insert_cambio = """INSERT INTO historailcambio (fechaCambio, DescripcionCambio) 
                               VALUES (CURDATE(), %s)"""
        cursor.execute(sql_insert_cambio, (descripcion,))
        conexion.connection.commit()

        return jsonify({"Mensaje": "Producto actualizado"})
    except Exception as e:
        app.logger.error("Error: %s", e)
        return jsonify({"Mensaje": "No se pudo actualizar el producto"}), 500


@app.route("/producto/<IdProducto>", methods=["DELETE"])
def eliminar_producto(IdProducto):
    try:
        cursor = conexion.connection.cursor()

        # Obtener los datos antiguos
        sql_select = "SELECT * FROM producto WHERE IdProducto = %s"
        cursor.execute(sql_select, (IdProducto,))
        datos_antiguos = cursor.fetchone()

        # Realizar la eliminación
        sql_delete = "DELETE FROM producto WHERE IdProducto = %s"
        cursor.execute(sql_delete, (IdProducto,))
        conexion.connection.commit()

        # Crear la descripción del cambio
        descripcion = f"Producto eliminado: {IdProducto}. Datos: {datos_antiguos}"

        # Registrar el cambio
        sql_insert_cambio = """INSERT INTO historailcambio (fechaCambio, DescripcionCambio) 
                               VALUES (CURDATE(), %s)"""
        cursor.execute(sql_insert_cambio, (descripcion,))
        conexion.connection.commit()

        return jsonify({"Mensaje": "Producto eliminado"})
    except Exception as e:
        app.logger.error("Error: %s", e)
        return jsonify({"Mensaje": "No se pudo eliminar el producto"}), 500

#
# JSON notificacion
#

# Ruta para listar todas las notificaciones
@app.route('/notificacion', methods=['GET'])
def listar_notificaciones():
    try:
        verificar_productos()  # Verificar productos antes de listar las notificaciones
        cursor = conexion.connection.cursor()
        
        # Obtener los parámetros de consulta
        fecha_notificacion = request.args.get('fecha')
        descripcion = request.args.get('descripcion')
        
        # Construir la consulta SQL
        sql_query = "SELECT * FROM notificacion WHERE 1=1 ORDER BY FechaNotificacion DESC"
        params = []
        
        if fecha_notificacion:
            sql_query += " AND FechaNotificacion = %s"
            params.append(fecha_notificacion)
        
        if descripcion:
            sql_query += " AND DescripcionNotificacion LIKE %s"
            params.append(f"%{descripcion}%")
        
        cursor.execute(sql_query, tuple(params))
        notificaciones = cursor.fetchall()
        
        # Convertir los resultados a una lista de diccionarios
        notificaciones_lista = []
        for notificacion in notificaciones:
            IdNotificacion, FechaNotificacion, DescripcionNotificacion = notificacion
            notificacion_dict = {
                "IdNotificacion": IdNotificacion,
                "FechaNotificacion": FechaNotificacion.strftime('%Y-%m-%d'),
                "DescripcionNotificacion": DescripcionNotificacion,
            }
            notificaciones_lista.append(notificacion_dict)
        
        return jsonify(notificaciones_lista)
    except Exception as e:
        app.logger.error("Error: %s", e)
        return jsonify({"Mensaje": "No se pudieron obtener las notificaciones"}), 500

# Función para verificar productos y crear notificaciones
def verificar_productos():
    try:
        cursor = conexion.connection.cursor()
        cursor.execute("SELECT * FROM producto")
        productos = cursor.fetchall()
        
        hoy = datetime.date.today()
        for producto in productos:
            IdProducto, Nombre, Marca, IdCategoria, Cantidad, FechaVencimiento, Precio, IdUbicacion = producto

            if Cantidad < 6:
                descripcion = f"El producto {Nombre} tiene un stock bajo de {Cantidad} unidades."
                registrar_notificacion(hoy, descripcion)

            if FechaVencimiento <= hoy + datetime.timedelta(days=5):
                descripcion = f"El producto {Nombre} está próximo a vencer el {FechaVencimiento}."
                registrar_notificacion(hoy, descripcion)
    except Exception as e:
        print(f"Error al verificar productos: {str(e)}")

# Función para registrar una notificación
def registrar_notificacion(fecha, descripcion):
    try:
        cursor = conexion.connection.cursor()
        # Comprobar si la notificación ya existe
        sql_check = """SELECT * FROM notificacion WHERE FechaNotificacion = %s AND DescripcionNotificacion = %s"""
        cursor.execute(sql_check, (fecha, descripcion))
        notificacion = cursor.fetchone()

        if not notificacion:
            # Solo registrar la notificación si no existe
            sql_insert = """INSERT INTO notificacion (FechaNotificacion, DescripcionNotificacion)
                            VALUES (%s, %s)"""
            fecha = datetime.datetime.now().strftime('%Y-%m-%d')
            cursor.execute(sql_insert, (fecha, descripcion))
            conexion.connection.commit()
    except Exception as e:
        print(f"Error al registrar notificación: {str(e)}")

#
# JSON Cambio
#

@app.route("/historialcambio", methods=["GET"])
def obtener_cambios():
    try:
        cursor = conexion.connection.cursor()
        
        # Obtener los parámetros de consulta
        fecha_cambio = request.args.get('fecha')
        descripcion = request.args.get('descripcion')
        
        # Construir la consulta SQL
        sql_query = "SELECT * FROM historailcambio WHERE 1=1 ORDER BY fechaCambio DESC"
        params = []
        
        if fecha_cambio:
            sql_query += " AND fechaCambio = %s"
            params.append(fecha_cambio)
        
        if descripcion:
            sql_query += " AND DescripcionCambio LIKE %s"
            params.append(f"%{descripcion}%")
        
        cursor.execute(sql_query, tuple(params))
        cambios = cursor.fetchall()

        # Convertir los resultados a una lista de diccionarios
        cambios_lista = []
        for cambio in cambios:
            cambio_dict = {
                "IdCambio": cambio[0],
                "fechaCambio": cambio[1].strftime('%Y-%m-%d'),
                "DescripcionCambio": cambio[2],
            }
            cambios_lista.append(cambio_dict)
        
        return jsonify(cambios_lista)
    except Exception as e:
        app.logger.error("Error: %s", e)
        return jsonify({"Mensaje": "No se pudieron obtener los cambios"}), 500
    
@app.route("/historialcambio/delete_older_than_20_days", methods=["DELETE"])
def eliminar_cambios_antiguos():
    """
    Función para eliminar cambios en la tabla historailcambio que tengan más de 20 días de antigüedad.
    """
    try:
        cursor = conexion.connection.cursor()
        # Calcular la fecha límite: 20 días antes de hoy
        fecha_limite = datetime.date.today() - datetime.timedelta(days=20)
        sql = "DELETE FROM historailcambio WHERE fechaCambio < %s"
        cursor.execute(sql, (fecha_limite,))
        conexion.connection.commit()
        return jsonify({"Mensaje": "Cambios antiguos eliminados"}), 200
    except Exception as e:
        app.logger.error("Error: %s", e)
        return jsonify({"Mensaje": "No se pudieron eliminar los cambios antiguos", "Error": str(e)}), 500

#
# JSON causa dano
#

# Ruta para listar todas las causas de daño
@app.route('/causadano', methods=['GET'])
def listar_causas_dano():
    try:
        cursor = conexion.connection.cursor()
        cursor.execute("SELECT * FROM causadano")
        causas_dano = cursor.fetchall()
        return jsonify(causas_dano)
    except Exception as e:
        return jsonify({'error': str(e)})

# Ruta para obtener una causa de daño específica por IdCausaDano
@app.route('/causadano/<int:id>', methods=['GET'])
def obtener_causa_dano(id):
    try:
        cursor = conexion.connection.cursor()
        cursor.execute("SELECT * FROM causadano WHERE IdCausaDano = %s", (id,))
        causa_dano = cursor.fetchone()
        if causa_dano:
            return jsonify(causa_dano)
        else:
            return jsonify({'error': 'Causa de daño no encontrada'}), 404
    except Exception as e:
        return jsonify({'error': str(e)})

# Ruta para crear una nueva causa de daño
@app.route('/causadano', methods=['POST'])
def crear_causa_dano():
    try:
        datos = request.json
        cursor = conexion.connection.cursor()
        sql = """INSERT INTO causadano (IdCausaDano, CausaDano)
                 VALUES (%s, %s)"""
        cursor.execute(sql, (datos['IdCausaDano'], datos['CausaDano']))
        conexion.connection.commit()
        return jsonify({'message': 'Causa de daño creada exitosamente'}), 201
    except Exception as e:
        return jsonify({'error': str(e)})

# Ruta para actualizar una causa de daño existente
@app.route('/causadano/<int:id>', methods=['PUT'])
def actualizar_causa_dano(id):
    try:
        datos = request.json
        cursor = conexion.connection.cursor()
        sql = """UPDATE causadano SET CausaDano = %s
                 WHERE IdCausaDano = %s"""
        cursor.execute(sql, (datos['CausaDano'], id))
        conexion.connection.commit()
        return jsonify({'message': 'Causa de daño actualizada exitosamente'})
    except Exception as e:
        return jsonify({'error': str(e)})

# Ruta para eliminar una causa de daño
@app.route('/causadano/<int:id>', methods=['DELETE'])
def eliminar_causa_dano(id):
    try:
        cursor = conexion.connection.cursor()
        cursor.execute("DELETE FROM causadano WHERE IdCausaDano = %s", (id,))
        conexion.connection.commit()
        return jsonify({'message': 'Causa de daño eliminada exitosamente'})
    except Exception as e:
        return jsonify({'error': str(e)})

#
# JSON Historial Pedido
#

# Ruta para listar todos los pedidos
@app.route('/historialpedido', methods=['GET'])
def listar_pedidos():
    try:
        cursor = conexion.connection.cursor()
        cursor.execute("SELECT * FROM historialpedido")
        pedidos = cursor.fetchall()
        return jsonify(pedidos)
    except Exception as e:
        return jsonify({'error': str(e)})

# Ruta para obtener un pedido específico por IdPedido
@app.route('/historialpedido/<int:id>', methods=['GET'])
def obtener_pedido(id):
    try:
        cursor = conexion.connection.cursor()
        cursor.execute("SELECT * FROM historialpedido WHERE IdPedido = %s", (id,))
        pedido = cursor.fetchone()
        if pedido:
            return jsonify(pedido)
        else:
            return jsonify({'error': 'Pedido no encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)})

# Ruta para crear un nuevo pedido
@app.route('/historialpedido', methods=['POST'])
def crear_pedido():
    try:
        datos = request.json
        cursor = conexion.connection.cursor()
        sql = """INSERT INTO historialpedido (IdPedido, nombreProducto, cantidadEmpaque, UnidadPorEmpaque, FechaPedido)
                 VALUES (%s, %s, %s, %s, %s)"""
        cursor.execute(sql, (datos['IdPedido'], datos['nombreProducto'], datos['cantidadEmpaque'], datos['UnidadPorEmpaque'], datos['FechaPedido']))
        conexion.connection.commit()
        return jsonify({'message': 'Pedido creado exitosamente'}), 201
    except Exception as e:
        return jsonify({'error': str(e)})

# Ruta para actualizar un pedido existente
@app.route('/historialpedido/<int:id>', methods=['PUT'])
def actualizar_pedido(id):
    try:
        datos = request.json
        cursor = conexion.connection.cursor()
        sql = """UPDATE historialpedido SET nombreProducto = %s, cantidadEmpaque = %s, UnidadPorEmpaque = %s, FechaPedido = %s
                 WHERE IdPedido = %s"""
        cursor.execute(sql, (datos['nombreProducto'], datos['cantidadEmpaque'], datos['UnidadPorEmpaque'], datos['FechaPedido'], id))
        conexion.connection.commit()
        return jsonify({'message': 'Pedido actualizado exitosamente'})
    except Exception as e:
        return jsonify({'error': str(e)})

# Ruta para eliminar un pedido
@app.route('/historialpedido/<int:id>', methods=['DELETE'])
def eliminar_pedido(id):
    try:
        cursor = conexion.connection.cursor()
        cursor.execute("DELETE FROM historialpedido WHERE IdPedido = %s", (id,))
        conexion.connection.commit()
        return jsonify({'message': 'Pedido eliminado exitosamente'})
    except Exception as e:
        return jsonify({'error': str(e)})

#
# JSON Usuario
#

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if verify_password(username, password):
        return jsonify({"message": "Logeo exitoso"}), 200
    else:
        return jsonify({"message": "Credenciales incorrectas"}), 401


@app.route("/usuario", methods=["GET"])
def listar_usuario():
    """
    Función para listar usuarios.
    """
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT IdUsuario, Usuario, Correo FROM usuario"
        cursor.execute(sql)
        datos_usuario = cursor.fetchall()
        usuarios = []
        for f in datos_usuario:
            usuario = {"IdUsuario": f[0], "Usuario": f[1], "Correo": f[2]}
            usuarios.append(usuario)
        return jsonify(usuarios)
    except Exception as e:
        app.logger.error("Error: %s", e)
        return (
            jsonify({"Mensaje": "No se pudo realizar la consulta", "Error": str(e)}),
            500,
        )


@app.route("/usuario/<IdUsuario>", methods=["GET"])
def ver_usuario(id_usuario):
    """
    Función para ver un usuario.
    """
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT IdUsuario, Usuario, Correo FROM usuario WHERE IdUsuario = %s"
        cursor.execute(sql, (id_usuario,))
        datos_usuario = cursor.fetchone()
        if datos_usuario:
            usuario = {
                "IdUsuario": datos_usuario[0],
                "Usuario": datos_usuario[1],
                "Correo": datos_usuario[2],
            }
            return jsonify(usuario)
        return jsonify({"Mensaje": "Usuario no encontrado"}), 404
    except Exception as e:
        app.logger.error("Error: %s", e)
        return (
            jsonify({"Mensaje": "No se pudo realizar la consulta", "Error": "%s"}),
            500,
        )


@app.route("/usuario", methods=["POST"])
def registrar_usuario():
    """
    Función para registrar un usuario.
    """
    data = request.get_json()

    if not all(key in data for key in ("Usuario", "Correo", "Contrasena")):
        return jsonify({"Mensaje": "Datos incompletos"}), 400

    hashed_password = generate_password_hash(data["Contrasena"], method="pbkdf2:sha256")

    try:
        cursor = conexion.connection.cursor()
        sql = """INSERT INTO usuario (Usuario, Correo, Contrasena)
                 VALUES (%s, %s, %s)"""
        cursor.execute(sql, (data["Usuario"], data["Correo"], hashed_password))
        conexion.connection.commit()
        return jsonify({"Mensaje": "Usuario registrado"}), 201
    except Exception as e:
        app.logger.error("Error: %s", e)
        return (
            jsonify({"Mensaje": "No se pudo registrar el usuario", "Error": "%s"}),
            500,
        )


@app.route("/usuario/<IdUsuario>", methods=["PUT"])
def actualizar_usuario(id_usuario):
    """
    Función para actualizar un usuario.
    """
    data = request.get_json()

    if not all(key in data for key in ("Usuario", "Correo")):
        return jsonify({"Mensaje": "Datos incompletos"}), 400

    hashed_password = (
        generate_password_hash(data["Contrasena"], method="pbkdf2:sha256")
        if "Contrasena" in data
        else None
    )

    try:
        cursor = conexion.connection.cursor()
        if hashed_password:
            sql = """UPDATE usuario SET Usuario = %s, Correo = %s, Contrasena = %s WHERE IdUsuario = %s"""
            cursor.execute(
                sql, (data["Usuario"], data["Correo"], hashed_password, id_usuario)
            )
        else:
            sql = (
                """UPDATE usuario SET Usuario = %s, Correo = %s WHERE IdUsuario = %s"""
            )
            cursor.execute(sql, (data["Usuario"], data["Correo"], id_usuario))
        conexion.connection.commit()
        return jsonify({"Mensaje": "Usuario actualizado"}), 200
    except Exception as e:
        app.logger.error("Error: %s", e)
        return (
            jsonify({"Mensaje": "No se pudo actualizar el usuario", "Error": "%s"}),
            500,
        )


@app.route("/usuario/<IdUsuario>", methods=["DELETE"])
def eliminar_usuario(IdUsuario):
    """
    Función para eliminar un usuario.
    """
    try:
        cursor = conexion.connection.cursor()
        sql = "DELETE FROM usuario WHERE IdUsuario = %s"
        cursor.execute(sql, (IdUsuario,))
        conexion.connection.commit()
        return jsonify({"Mensaje": "Usuario eliminado"}), 200
    except Exception as e:
        app.logger.error("Error: %s", e)
        return (
            jsonify({"Mensaje": "No se pudo eliminar el usuario", "Error": "%s"}),
            500,
        )

if __name__ == "__main__":
    app.config.from_object(config["development"])
    app.run()
