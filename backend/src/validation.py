import datetime
import re

# Tabla Proveedor

def validar_rut_proveedor(RutProveedor: str) -> bool:
    rut_proveedor = rut_proveedor.strip()
    return len(rut_proveedor) > 0 and len(rut_proveedor) <= 9

def validar_empresa(empresa: str) -> bool:
    empresa = empresa.strip()
    return len(empresa) > 0 and len(empresa) <= 40

def validar_nombre(nombre: str) -> bool:
    nombre = nombre.strip()
    return len(nombre) > 0 and len(nombre) <= 40

def validar_apellido(apellido: str) -> bool:
    apellido = apellido.strip()
    return len(apellido) > 0 and len(apellido) <= 40

def validar_telefono(telefono: str) -> bool:
    return telefono.isnumeric() and len(telefono) <= 15

def validar_correo(correo: str) -> bool:
    correo = correo.strip()
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return len(correo) > 0 and len(correo) <= 40 and re.match(email_regex, correo) is not None

# tabla categooria

def validar_nombre_categoria(nombre: str) -> bool:
    nombre = nombre.strip()
    return len(nombre) > 0 and len(nombre) <= 40

def validar_categoria(data):
    errors = []
    if 'Nombre' not in data or not validar_nombre_categoria(data['Nombre']):
        errors.append('Nombre inválido')
    return errors

# Tabla Ubicacion

def validar_id_ubicacion(id_ubicacion: int) -> bool:
    return isinstance(id_ubicacion, int) and id_ubicacion > 0

def validar_nombre_ubicacion(nombre: str) -> bool:
    nombre = nombre.strip()
    return len(nombre) > 0 and len(nombre) <= 40

# Tabla Producto

def validar_id_producto(id_producto: int) -> bool:
    return isinstance(id_producto, int) and id_producto > 0

def validar_nombre_producto(nombre: str) -> bool:
    nombre = nombre.strip()
    return len(nombre) > 0 and len(nombre) <= 100

def validar_marca_producto(marca: str) -> bool:
    marca = marca.strip()
    return len(marca) > 0 and len(marca) <= 40

def validar_cantidad_producto(cantidad: int) -> bool:
    return isinstance(cantidad, int) and cantidad > 0

def validar_precio_producto(precio: int) -> bool:
    return isinstance(precio, int) and precio > 0

def validar_id_categoria(id_categoria: str) -> bool:
    return len(id_categoria) > 0 and len(id_categoria) <= 20

def validar_id_ubicacion(id_ubicacion: str) -> bool:
    return len(id_ubicacion) > 0 and len(id_ubicacion) <= 20

# Tabla Productodanado

def validar_id_danado(id_danado: int) -> bool:
    return isinstance(id_danado, int) and id_danado > 0

def validar_costo(costo: int) -> bool:
    return isinstance(costo, int) and costo > 0

def validar_causa_dano(causa_dano: int) -> bool:
    return isinstance(causa_dano, int) and causa_dano > 0

# Tabla Historialpedido
def validar_id_pedido(id_pedido: int) -> bool:
    return isinstance(id_pedido, int) and id_pedido > 0

def validar_nombre_producto(nombre_producto: int) -> bool:
    return isinstance(nombre_producto, int) and nombre_producto > 0

def validar_cantidad_empaque(cantidad_empaque: int) -> bool:
    return isinstance(cantidad_empaque, int) and cantidad_empaque > 0

def validar_unidad_por_empaque(unidad_por_empaque: int) -> bool:
    return isinstance(unidad_por_empaque, int) and unidad_por_empaque > 0

def validar_fecha_pedido(fecha_pedido: str) -> bool:
    try:
        datetime.strptime(fecha_pedido, '%Y-%m-%d')
        return True
    except ValueError:
        return False
    
# Tabla Historialcambio
def validar_id_cambio(id_cambio: int) -> bool:
    return isinstance(id_cambio, int) and id_cambio > 0

def validar_fecha_cambio(fecha_cambio: str) -> bool:
    try:
        datetime.strptime(fecha_cambio, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def validar_descripcion_cambio(descripcion_cambio: str) -> bool:
    return len(descripcion_cambio.strip()) > 0 and len(descripcion_cambio) <= 255

# Tabla Historialcambio
def validar_id_cambio(id_cambio: int) -> bool:
    return isinstance(id_cambio, int) and id_cambio > 0

def validar_fecha_cambio(fecha_cambio: str) -> bool:
    try:
        datetime.strptime(fecha_cambio, '%Y-%m-%d')
        return True
    except ValueError:
        return False

# Función para validar todos los campos de Proveedor
def validar_proveedor(data):
    errors = []
    
    if 'RutProveedor' not in data or not validar_rut_proveedor(data['RutProveedor']):
        errors.append('RutProveedor inválido')
    
    if 'Empresa' not in data or not validar_empresa(data['Empresa']):
        errors.append('Empresa inválida')
    
    if 'Nombre' not in data or not validar_nombre(data['Nombre']):
        errors.append('Nombre inválido')
    
    if 'Apellido' not in data or not validar_apellido(data['Apellido']):
        errors.append('Apellido inválido')
    
    if 'Telefono' not in data or not validar_telefono(data['Telefono']):
        errors.append('Telefono inválido')
    
    if 'Correo' not in data or not validar_correo(data['Correo']):
        errors.append('Correo inválido')
    
    return errors

# Función para validar todos los campos de Categoria
def validar_categoria(data):
    errors = []
    
    if 'Nombre' not in data or not validar_nombre_categoria(data['Nombre']):
        errors.append('Nombre de categoria inválido')
    
    return errors

# Función para validar todos los campos de Ubicacion
def validar_ubicacion(data):
    errors = []

    if 'Nombre' not in data or not validar_nombre_ubicacion(data['Nombre']):
        errors.append('Nombre de Ubicacion inválido')
    
    return errors

# Función para validar todos los campos de Producto
def validar_producto(data):
    errors = []
    if 'IdProducto' not in data or not validar_id_producto(data['IdProducto']):
        errors.append('IdProducto inválido')
    if 'Nombre' not in data or not validar_nombre_producto(data['Nombre']):
        errors.append('Nombre de Producto inválido')
    if 'Marca' not in data or not validar_marca_producto(data['Marca']):
        errors.append('Marca de Producto inválida')
    if 'Cantidad' not in data or not validar_cantidad_producto(data['Cantidad']):
        errors.append('Cantidad de Producto inválida')
    if 'Precio' not in data or not validar_precio_producto(data['Precio']):
        errors.append('Precio de Producto inválido')
    if 'IdCategoria' not in data or not validar_id_categoria(data['IdCategoria']):
        errors.append('IdCategoria inválido')
    if 'IdUbicacion' not in data or not validar_id_ubicacion(data['IdUbicacion']):
        errors.append('IdUbicacion inválido')
    return errors

def validar_producto_danado(data):
    errors = []
    if 'IdDanado' not in data or not validar_id_danado(data['IdDanado']):
        errors.append('IdDanado inválido')
    if 'IdProducto' not in data or not validar_id_producto(data['IdProducto']):
        errors.append('IdProducto inválido')
    if 'Nombre' not in data or not validar_nombre_producto(data['Nombre']):
        errors.append('Nombre de Producto inválido')
    if 'Cantidad' not in data or not validar_cantidad_producto(data['Cantidad']):
        errors.append('Cantidad de Producto inválida')
    if 'Costo' not in data or not validar_costo(data['Costo']):
        errors.append('Costo de Producto inválido')
    if 'CausaDano' not in data or not validar_causa_dano(data['CausaDano']):
        errors.append('Causa de Daño inválida')
    return errors

def validar_historial_pedido(data):
    errors = []
    if 'IdPedido' not in data or not validar_id_pedido(data['IdPedido']):
        errors.append('IdPedido inválido')
    if 'nombreProducto' not in data or not validar_nombre_producto(data['nombreProducto']):
        errors.append('Nombre de Producto inválido')
    if 'cantidadEmpaque' not in data or not validar_cantidad_empaque(data['cantidadEmpaque']):
        errors.append('Cantidad de Empaque inválida')
    if 'UnidadPorEmpaque' not in data or not validar_unidad_por_empaque(data['UnidadPorEmpaque']):
        errors.append('Unidad por Empaque inválida')
    if 'FechaPedido' not in data or not validar_fecha_pedido(data['FechaPedido']):
        errors.append('Fecha de Pedido inválida')
    return errors

def validar_historial_cambio(data):
    errors = []
    if 'IdCambio' not in data or not validar_id_cambio(data['IdCambio']):
        errors.append('IdCambio inválido')
    if 'fechaCambio' not in data or not validar_fecha_cambio(data['fechaCambio']):
        errors.append('Fecha de Cambio inválida')
    if 'DescripcionCambio' not in data or not validar_descripcion_cambio(data['DescripcionCambio']):
        errors.append('Descripción de Cambio inválida')
    return errors


