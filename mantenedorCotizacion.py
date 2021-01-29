import pymysql
import datetime
from claseCotizacion import Cotizacion
#Conexion a la base de datos
def conectar():
    try:
        #pymsql.connect necesita 4 parametros
        conexion = pymysql.connect(host='localhost',user='root',password='',db='lemonvintage')
    except:
        print("Fallo en la conexion a la db")    
    return conexion
    

def insertar(cotizacion):
    conectar()
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "INSERT INTO cotizacion(id_cotizacion,fecha,cliente_id_cliente,vendedor_id_vendedor) VALUES (%s,%s,%s,%s);"
            cursor.execute(consulta,
                (cotizacion.id_cotizacion,
                cotizacion.fecha,
                cotizacion.cliente_id_cliente, 
                cotizacion.vendedor_id_vendedor,))
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
            cursor.execute("SELECT * FROM cotizacion")
            #usamos fetchall para traer todos los datos
            auxCotizacion = cursor.fetchall()
            #recorrer la coleccion
            for cot in auxCotizacion:
                print(cot)
            return auxCotizacion
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Ocurrio un error al consultar: ", e)
    conexion.close
    #-----------------
def buscar(id_cotizacion):
    conectar()
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "SELECT * FROM cotizacion WHERE id_cotizacion = %s;"
            cursor.execute(consulta,(id_cotizacion))
            #usamos fetchall para traer todos los datos
            auxCotizacion = cursor.fetchall()
            #recorrer la coleccion
            for cot in auxCotizacion:
                print(cot)
            return auxCotizacion
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Ocurrio un error al buscar: ", e)
    conexion.close
    #-----------------
#actualizar servicio por id_servicio
def actualizar(cotizacion):
    conectar()
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "UPDATE cotizacion SET fecha = %s, cliente_id_cliente = %s, vendedor_id_vendedor = %s WHERE id_cotizacion = %s;"
            cursor.execute(consulta,
                (cotizacion.fecha,
                cotizacion.cliente_id_cliente,
                cotizacion.vendedor_id_vendedor,
                cotizacion.id_cotizacion))
    #commit para que ejecute la consulta y almacene
        conexion.commit
    #rescatamos el error operacional y el error interno para luego guardar en ex
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as ex:
        print("Error al actualizar datos ", ex)
    conexion.close
    #-----------------
def eliminar(id_cotizacion):
    conectar()
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "DELETE FROM cotizacion WHERE id_cotizacion = %s;"
            cursor.execute(consulta,(id_cotizacion))
    #commit para que ejecute la consulta y almacene
        conexion.commit
    #rescatamos el error operacional y el error interno para luego guardar en ex
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as ex:
        print("Error al eliminar datos ", ex)
    conexion.close

def contar():
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT COUNT(id_cotizacion)FROM cotizacion")
            #usamos fetchall para traer todos los datos
            contCotizacion = cursor.fetchone()
            return contCotizacion[0]
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Ocurrio un error al consultar: ", e)
    conexion.close
    #-----------------

#Programa principal TESTER
#Prueba insertar OK
#print("Conectado")
#auxCotizacion= Cotizacion(0,"2021-04-06",1,1)
#insertar(auxCotizacion)
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
#auxCotizacion = Cotizacion(1,"2021-01-01",1,1)
#actualizar(auxCotizacion)
#consultar()
#--------------------------
#Prueba de eliminar servicio por id servicio OK
#eliminar(2)
#consultar()
