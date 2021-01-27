import pymysql
from claseDetalleCotizacion import DetalleCotizacion
#Conexion a la base de datos
def conectar():
    try:
        #pymsql.connect necesita 4 parametros
        conexion = pymysql.connect(host='localhost',user='root',password='',db='lemonvintage')
    except:
        print("Fallo en la conexion a la db")    
    return conexion
    

def insertar(detalle_cotizacion):
    conectar()
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "INSERT INTO detalle_cotizacion(id_detallecotizacion,detalle,total,cotizacion_id_cotizacion,producto_id_producto,servicio_id_servicio) VALUES (%s,%s,%s,%s,%s,%s);"
            cursor.execute(consulta,
                (detalle_cotizacion.id_detallecotizacion,
                detalle_cotizacion.detalle,
                detalle_cotizacion.total, 
                detalle_cotizacion.cotizacion_id_cotizacion,
                detalle_cotizacion.producto_id_producto,
                detalle_cotizacion.servicio_id_servicio))
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
            cursor.execute("SELECT * FROM detalle_cotizacion")
            #usamos fetchall para traer todos los datos
            auxDetalleCotizacion = cursor.fetchall()
            #recorrer la coleccion
            for detcot in auxDetalleCotizacion:
                print(detcot)
            return auxDetalleCotizacion
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Ocurrio un error al consultar: ", e)
    conexion.close
    #-----------------
def buscar(id_detallecotizacion):
    conectar()
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "SELECT * FROM detalle_cotizacion WHERE id_detallecotizacion = %s;"
            cursor.execute(consulta,(id_detallecotizacion))
            #usamos fetchall para traer todos los datos
            auxDetalleCotizacion = cursor.fetchall()
            #recorrer la coleccion
            for detcot in auxDetalleCotizacion:
                print(detcot)
            return auxDetalleCotizacion
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Ocurrio un error al buscar: ", e)
    conexion.close
    #-----------------
#actualizar servicio por id_servicio
def actualizar(detalle_cotizacion):
    conectar()
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "UPDATE detalle_cotizacion SET detalle = %s, total = %s, cotizacion_id_cotizacion = %s, producto_id_producto = %s, servicio_id_servicio = %s WHERE id_detallecotizacion = %s;"
            cursor.execute(consulta,
                (detalle_cotizacion.detalle,
                detalle_cotizacion.total,
                detalle_cotizacion.cotizacion_id_cotizacion,
                detalle_cotizacion.producto_id_producto,
                detalle_cotizacion.servicio_id_servicio,
                detalle_cotizacion.id_detallecotizacion))
    #commit para que ejecute la consulta y almacene
        conexion.commit
    #rescatamos el error operacional y el error interno para luego guardar en ex
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as ex:
        print("Error al actualizar datos ", ex)
    conexion.close
    #-----------------
def eliminar(id_detallecotizacion):
    conectar()
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "DELETE FROM detalle_cotizacion WHERE id_detallecotizacion = %s;"
            cursor.execute(consulta,(id_detallecotizacion))
    #commit para que ejecute la consulta y almacene
        conexion.commit
    #rescatamos el error operacional y el error interno para luego guardar en ex
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as ex:
        print("Error al eliminar datos ", ex)
    conexion.close

#Programa principal TESTER
#Prueba insertar OK
#print("Conectado")
#auxDetalleCotizacion= DetalleCotizacion(0,"producto 3 10000 \n producto 4 30000",40000,1,1,1)
#insertar(auxDetalleCotizacion)
#consultar()
#print("Datos guardados")
#---------------------------
#Prueba Consultar OK
#consultar()
#--------------------------
#Prueba buscar OK
#buscar(1)
#--------------------------
#Prueba actualizar id  OK 
#auxDetalleCotizacion = DetalleCotizacion(3,"producto 666",666,1,1,1)
#actualizar(auxDetalleCotizacion)
#consultar()
#--------------------------
#Prueba de eliminar servicio por id servicio OK
#eliminar(3)
#consultar()
