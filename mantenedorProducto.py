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
            consulta = "INSERT INTO producto(id_producto,nombre,descripcion,color,material,cantidad,ancho,alto,espesor,peso,precio,divisiones,accesorios,tipo_producto_id_tipo_producto) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
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
                producto.espesor,
                producto.peso,
                producto.precio,
                producto.divisiones,
                producto.accesorios,
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
            auxProducto = cursor.fetchall()
            #recorrer la coleccion
            for pro in auxProducto:
                print(pro)
            return auxProducto
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Ocurrio un error al consultar: ", e)
    conexion.close
    #-----------------
def buscar(Id_producto):
    conectar()
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "SELECT * FROM producto WHERE id_producto = %s;"
            cursor.execute(consulta,(Id_producto))
            #usamos fetchall para traer todos los datos
            auxProducto = cursor.fetchall()
            #recorrer la coleccion
            for pro in auxProducto:
                print(pro)
            return auxProducto
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
            consulta = "UPDATE producto SET nombre = %s, descripcion = %s, color = %s, material = %s, cantidad = %s, ancho = %s, alto = %s, espesor = %s, peso = %s, precio = %s, divisiones = %s, accesorios = %s, tipo_producto_id_tipo_producto = %s WHERE id_producto = %s;"
            #%s hace referencia a una variable string
                        #%d hace referencia a un int
                        #%f hace referencia a un float
                        #En la siguiente linea excecute nos permite ejecutar varias veces con distintos datos
            cursor.execute(consulta,
                (producto.nombre,
                producto.descripcion,
                producto.color,
                producto.material,
                producto.cantidad,
                producto.ancho,
                producto.largo,
                producto.espesor,
                producto.peso,
                producto.precio,
                producto.divisiones,
                producto.accesorios,
                producto.tipo_producto_id_tipo_producto))
    #commit para que ejecute la consulta y almacene
        conexion.commit
    #rescatamos el error operacional y el error interno para luego guardar en ex
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as ex:
        print("Error al actualizar datos ", ex)
    conexion.close
    #-----------------
def eliminar(Id_producto):
    conectar()
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "DELETE FROM producto WHERE id_producto = %s;"
                        #%s hace referencia a una variable string
                        #%d hace referencia a un int
                        #%f hace referencia a un float
                        #En la siguiente linea excecute nos permite ejecutar varias veces con distintos datos
            cursor.execute(consulta,(Id_producto))
    #commit para que ejecute la consulta y almacene
        conexion.commit
    #rescatamos el error operacional y el error interno para luego guardar en ex
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as ex:
        print("Error al eliminar datos ", ex)
    conexion.close

#Programa principal
#Prueba insertar OK
#print("Conectado")
auxProducto = Producto(0,"puerta entrada","puerta roble","natural","roble",4,90,235.5,4.5,50,90000,2,"españoleta",1)
insertar(auxProducto)
consultar()
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
