import pymysql
from claseTipoProducto import Tipo_Producto
#Conexion a la base de datos
def conectar():
    try:
        #pymsql.connect necesita 4 parametros
        conexion = pymysql.connect(host='localhost',user='root',password='',db='lemonvintage')
    except:
        print("Fallo en la conexion a la db")    
    return conexion
    

def insertar(tipo_producto):
    conectar()
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "INSERT INTO tipo_producto(id_tipo_producto,nombre,descripcion) VALUES (%s,%s,%s);"
                        #%s hace referencia a una variable string
                        #%d hace referencia a un int
                        #%f hace referencia a un float
                        #En la siguiente linea excecute nos permite ejecutar varias veces con distintos datos
            cursor.execute(consulta,
                (tipo_producto.id_tipo_producto,
                tipo_producto.nombre,
                tipo_producto.descripcion))
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
            cursor.execute("SELECT * FROM tipo_producto")
            #usamos fetchall para traer todos los datos
            auxTipo_producto = cursor.fetchall()
            #recorrer la coleccion
            for tprod in auxTipo_producto:
                print(tprod)
            return auxTipo_producto
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Ocurrio un error al consultar: ", e)
    conexion.close
    #-----------------
def buscar(Id_tipo_producto):
    conectar()
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "SELECT * FROM tipo_producto WHERE id_tipo_producto = %s;"
            cursor.execute(consulta,(Id_tipo_producto))
            #usamos fetchall para traer todos los datos
            auxTipo_producto = cursor.fetchall()
            #recorrer la coleccion
            for tprod in auxTipo_producto:
                print(tprod)
            return auxTipo_producto
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Ocurrio un error al buscar: ", e)
    conexion.close
    #-----------------
#actualizar tipo_producto por id_tipo_producto
def actualizar(tipo_producto):
    conectar()
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "UPDATE tipo_producto SET nombre = %s, descripcion = %s WHERE id_tipo_producto = %s;"
            #%s hace referencia a una variable string
                        #%d hace referencia a un int
                        #%f hace referencia a un float
                        #En la siguiente linea excecute nos permite ejecutar varias veces con distintos datos
            cursor.execute(consulta,
                (tipo_producto.nombre,
                tipo_producto.descripcion,
                tipo_producto.id_tipo_producto))
    #commit para que ejecute la consulta y almacene
        conexion.commit
    #rescatamos el error operacional y el error interno para luego guardar en ex
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as ex:
        print("Error al actualizar datos ", ex)
    conexion.close
    #-----------------
def eliminar(Id_tipo_producto):
    conectar()
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "DELETE FROM tipo_producto WHERE id_tipo_producto = %s;"
                        #%s hace referencia a una variable string
                        #%d hace referencia a un int
                        #%f hace referencia a un float
                        #En la siguiente linea excecute nos permite ejecutar varias veces con distintos datos
            cursor.execute(consulta,(Id_tipo_producto))
    #commit para que ejecute la consulta y almacene
        conexion.commit
    #rescatamos el error operacional y el error interno para luego guardar en ex
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as ex:
        print("Error al eliminar datos ", ex)
    conexion.close

#Programa principal
#Prueba insertar OK
#print("Conectado")
#auxTipo_producto = Tipo_Producto(0,"ventana","ventanas de madera nativa restauradas")
#insertar(auxTipo_producto)
#consultar()
#print("Datos guardados")
#---------------------------
#Prueba Consultar OK
#consultar()
#--------------------------
#Prueba buscar id tipo_producto OK
#buscar(1)
#--------------------------
#Prueba actualizar tipo_producto por id tipo_producto OK 
#auxTipo_producto = Tipo_Producto(2,"SUPER MEGA ventana","ventanas de madera nativa restauradas")
#actualizar(auxTipo_producto)
#consultar()
#buscar("5555")
#--------------------------
#Prueba de eliminar tipo_producto por id tipo_producto OK
#eliminar(2)
#consultar()
