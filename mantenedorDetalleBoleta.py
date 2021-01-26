import pymysql
from claseDetalleBoleta import DetalleBoleta
#Conexion a la base de datos
def conectar():
    try:
        #pymsql.connect necesita 4 parametros
        conexion = pymysql.connect(host='localhost',user='root',password='',db='lemonvintage')
    except:
        print("Fallo en la conexion a la db")    
    return conexion
    

def insertar(detalle_boleta):
    conectar()
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "INSERT INTO detalle_boleta(id_detalleboleta,detalle,total,boleta_id_boleta,producto_id_producto,servicio_id_servicio) VALUES (%s,%s,%s,%s,%s,%s);"
            cursor.execute(consulta,
                (detalle_boleta.id_detalleboleta,
                detalle_boleta.detalle,
                detalle_boleta.total, 
                detalle_boleta.boleta_id_boleta,
                detalle_boleta.producto_id_producto,
                detalle_boleta.servicio_id_servicio))
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
            cursor.execute("SELECT * FROM detalle_boleta")
            #usamos fetchall para traer todos los datos
            auxDetalleboleta = cursor.fetchall()
            #recorrer la coleccion
            for detbol in auxDetalleboleta:
                print(detbol)
            return auxDetalleboleta
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Ocurrio un error al consultar: ", e)
    conexion.close
    #-----------------
def buscar(id_detalleboleta):
    conectar()
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "SELECT * FROM detalle_boleta WHERE id_detalleboleta = %s;"
            cursor.execute(consulta,(id_detalleboleta))
            #usamos fetchall para traer todos los datos
            auxDetalleboleta = cursor.fetchall()
            #recorrer la coleccion
            for detbol in auxDetalleboleta:
                print(detbol)
            return auxDetalleboleta
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Ocurrio un error al buscar: ", e)
    conexion.close
    #-----------------
#actualizar servicio por id_servicio
def actualizar(Detalle_boleta):
    conectar()
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "UPDATE detalle_boleta SET detalle = %s, total = %s, boleta_id_boleta = %s, producto_id_producto = %s, servicio_id_servicio = %s WHERE id_detalleboleta = %s;"
            cursor.execute(consulta,
                (Detalle_boleta.detalle,
                Detalle_boleta.total,
                Detalle_boleta.boleta_id_boleta,
                Detalle_boleta.producto_id_producto,
                Detalle_boleta.servicio_id_servicio,
                Detalle_boleta.id_detalleboleta))
    #commit para que ejecute la consulta y almacene
        conexion.commit
    #rescatamos el error operacional y el error interno para luego guardar en ex
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as ex:
        print("Error al actualizar datos ", ex)
    conexion.close
    #-----------------
def eliminar(id_detalleboleta):
    conectar()
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "DELETE FROM detalle_boleta WHERE id_detalleboleta = %s;"
            cursor.execute(consulta,(id_detalleboleta))
    #commit para que ejecute la consulta y almacene
        conexion.commit
    #rescatamos el error operacional y el error interno para luego guardar en ex
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as ex:
        print("Error al eliminar datos ", ex)
    conexion.close

#Programa principal TESTER
#Prueba insertar OK
#print("Conectado")
#auxDetalleboleta= DetalleBoleta(0,"producto 2 10000 \b producto 4 30000",40000,4,4,4)
#insertar(auxDetalleboleta)
#consultar()
#print("Datos guardados")
#---------------------------
#Prueba Consultar OK
#consultar()
#--------------------------
#Prueba buscar OK
#buscar(4)
#--------------------------
#Prueba actualizar id  OK 
#auxDetalleboleta = DetalleBoleta(4,"producto 666",666,6,6,6)
#actualizar(auxDetalleboleta)
#consultar()
#--------------------------
#Prueba de eliminar servicio por id servicio OK
#eliminar(2)
#consultar()
