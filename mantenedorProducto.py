import pymysql
from claseProducto import Producto
#Conexion a la base de datos
def conectar():
    try:
        #pymsql.connect necesita 4 parametros
        conexion = pymysql.connect(host='localhost',user='root',password='',db='lemonvintage')
    except:
        print("Fallo en la conexion a la db")    
    return conexion
    

def insertar(producto):
    conectar()
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "INSERT INTO producto(id_producto,nombre,descripcion,color,material,cantidad,ancho,largo,espesor,peso,precio,divisiones,accesorios,tipo_producto_id_tipo_producto) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
                        #%s hace referencia a una variable string
                        #%d hace referencia a un int
                        #%f hace referencia a un float
                        #En la siguiente linea excecute nos permite ejecutar varias veces con distintos datos
            cursor.execute(consulta,
                (producto.id_producto,
                producto.nombre,
                producto.descripcion,
                producto.color,
                producto.material,
                producto.cantidad,
                producto.ancho,
                producto.alto,
                producto.espesor
                producto.peso
                producto.precio
                producto.divisiones
                producto.accesoios
                producto.tipo_producto_id_tipo_producto))
    #commit para que ejecute la consulta y almacene
        conexion.commit
    #rescatamos el error operacional y el error interno para luego guardar en ex
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as ex:
        print("Error al insertar datos ", ex)
    conexion.close
    #-----------------
def consultar():
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM producto")
            #usamos fetchall para traer todos los datos
            auxproducto = cursor.fetchall()
            #recorrer la coleccion
            for ven in auxproducto:
                print(ven)
            return auxproducto
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Ocurrio un error al consultar: ", e)
    conexion.close
    #-----------------
def buscar(Rut):
    conectar()
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "SELECT * FROM producto WHERE rut = %s;"
            cursor.execute(consulta,(Rut))
            #usamos fetchall para traer todos los datos
            auxproducto = cursor.fetchall()
            #recorrer la coleccion
            for ven in auxproducto:
                print(ven)
            return auxproducto
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Ocurrio un error al buscar: ", e)
    conexion.close
    #-----------------
#actualizar producto por id_producto
def actualizar(producto):
    conectar()
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "UPDATE producto SET nombre = %s, apellido = %s, rut = %s, telefono = %s, correo = %s, direccion = %s, comuna = %s, region = %s WHERE id_producto = %s;"
                        #%s hace referencia a una variable string
                        #%d hace referencia a un int
                        #%f hace referencia a un float
                        #En la siguiente linea excecute nos permite ejecutar varias veces con distintos datos
            cursor.execute(consulta,
                (producto.nombre,
                producto.apellido,
                producto.rut,
                producto.telefono,
                producto.correo,
                producto.direccion,
                producto.comuna,
                producto.region,
                producto.id_producto))
    #commit para que ejecute la consulta y almacene
        conexion.commit
    #rescatamos el error operacional y el error interno para luego guardar en ex
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as ex:
        print("Error al actualizar datos ", ex)
    conexion.close
    #-----------------
def eliminar(Rut):
    conectar()
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "DELETE FROM producto WHERE rut = %s;"
                        #%s hace referencia a una variable string
                        #%d hace referencia a un int
                        #%f hace referencia a un float
                        #En la siguiente linea excecute nos permite ejecutar varias veces con distintos datos
            cursor.execute(consulta,(Rut))
    #commit para que ejecute la consulta y almacene
        conexion.commit
    #rescatamos el error operacional y el error interno para luego guardar en ex
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as ex:
        print("Error al eliminar datos ", ex)
    conexion.close

#Programa principal
#Prueba insertar OK
#print("Conectado")
#auxproducto = producto(0,"luci","fer","666","91560522","jcubillos@tooldesign.cl","americo vespucio 7732","la florida","RM")
#insertar(auxproducto)
#consultar()
#print("Datos guardados")
#---------------------------
#Prueba Consultar OK
#consultar()
#--------------------------
#Prueba buscar rut OK
#buscar("666")
#--------------------------
#Prueba actualizar producto por rut OK 
#auxproducto = producto(2,"luci","fer","666","666","jona@tooldesign.cl","americo vespucio 7732","la florida","RM")
#actualizar(auxproducto)
#consultar()
#buscar("5555")
#--------------------------
#Prueba de eliminar producto por rut OK
#eliminar(666)
#consultar()