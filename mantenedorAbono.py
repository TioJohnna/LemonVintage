import datetime
import pymysql
from claseAbono import Abono
#Conexion a la base de datos
def conectar():
    try:
        #pymsql.connect necesita 4 parametros
        conexion = pymysql.connect(host='localhost',user='root',password='',db='lemonvintage')
    except:
        print("Fallo en la conexion a la db")    
    return conexion
    

def insertar(abono):
    conectar()
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "INSERT INTO abono(id_abono,monto,fecha,db_id_detalleboleta) VALUES (%s,%s,%s,%s);"
                        #%s hace referencia a una variable string
                        #%d hace referencia a un int
                        #%f hace referencia a un float
                        #En la siguiente linea excecute nos permite ejecutar varias veces con distintos datos
            cursor.execute(consulta,
                (abono.id_abono,
                abono.monto,
                abono.fecha, 
                abono.db_id_detalleboleta))
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
            cursor.execute("SELECT * FROM abono")
            #usamos fetchall para traer todos los datos
            auxAbono = cursor.fetchall()
            #recorrer la coleccion
            for abo in auxAbono:
                print(abo)
            return auxAbono
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Ocurrio un error al consultar: ", e)
    conexion.close
    #-----------------
def buscar(id_abono):
    conectar()
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "SELECT * FROM abono WHERE id_abono = %s;"
            cursor.execute(consulta,(id_abono))
            #usamos fetchall para traer todos los datos
            auxAbono = cursor.fetchall()
            #recorrer la coleccion
            for abo in auxAbono:
                print(abo)
            return auxAbono
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Ocurrio un error al buscar: ", e)
    conexion.close
    #-----------------
#actualizar servicio por id_servicio
def actualizar(abono):
    conectar()
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "UPDATE abono SET monto = %s, fecha = %s, db_id_detalleboleta = %s WHERE id_abono = %s;"
            cursor.execute(consulta,
                (abono.monto,
                abono.fecha,
                abono.db_id_detalleboleta,
                abono.id_abono))
    #commit para que ejecute la consulta y almacene
        conexion.commit
    #rescatamos el error operacional y el error interno para luego guardar en ex
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as ex:
        print("Error al actualizar datos ", ex)
    conexion.close
    #-----------------
def eliminar(id_abono):
    conectar()
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "DELETE FROM abono WHERE id_abono = %s;"
            cursor.execute(consulta,(id_abono))
    #commit para que ejecute la consulta y almacene
        conexion.commit
    #rescatamos el error operacional y el error interno para luego guardar en ex
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as ex:
        print("Error al eliminar datos ", ex)
    conexion.close

#Programa principal TESTER
#Prueba insertar OK
#print("Conectado")
#auxAbono= Abono(0,10000,'2021-01-26',0)
#insertar(auxAbono)
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
#auxAbono = Abono(1,777,"2021-04-06",7)
#actualizar(auxAbono)
#consultar()
#--------------------------
#Prueba de eliminar servicio por id servicio OK
eliminar(2)
consultar()
