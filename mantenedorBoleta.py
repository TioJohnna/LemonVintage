import pymysql
import datetime
from claseBoleta import Boleta
#Conexion a la base de datos
def conectar():
    try:
        #pymsql.connect necesita 4 parametros
        conexion = pymysql.connect(host='localhost',user='root',password='',db='lemonvintage')
    except:
        print("Fallo en la conexion a la db")    
    return conexion
    

def insertar(boleta):
    conectar()
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "INSERT INTO boleta(id_boleta,fecha,cliente_id_cliente,vendedor_id_vendedor) VALUES (%s,%s,%s,%s);"
            cursor.execute(consulta,
                (boleta.id_boleta,
                boleta.fecha,
                boleta.cliente_id_cliente, 
                boleta.vendedor_id_vendedor,))
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
            cursor.execute("SELECT * FROM boleta")
            #usamos fetchall para traer todos los datos
            auxBoleta = cursor.fetchall()
            #recorrer la coleccion
            for bol in auxBoleta:
                print(bol)
            return auxBoleta
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Ocurrio un error al consultar: ", e)
    conexion.close
    #-----------------
def buscar(id_boleta):
    conectar()
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "SELECT * FROM boleta WHERE id_boleta = %s;"
            cursor.execute(consulta,(id_boleta))
            #usamos fetchall para traer todos los datos
            auxBoleta = cursor.fetchall()
            #recorrer la coleccion
            for bol in auxBoleta:
                print(bol)
            return auxBoleta
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Ocurrio un error al buscar: ", e)
    conexion.close
    #-----------------
#actualizar servicio por id_servicio
def actualizar(boleta):
    conectar()
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "UPDATE boleta SET fecha = %s, cliente_id_cliente = %s, vendedor_id_vendedor = %s WHERE id_boleta = %s;"
            cursor.execute(consulta,
                (boleta.fecha,
                boleta.cliente_id_cliente,
                boleta.vendedor_id_vendedor,
                boleta.id_boleta))
    #commit para que ejecute la consulta y almacene
        conexion.commit
    #rescatamos el error operacional y el error interno para luego guardar en ex
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as ex:
        print("Error al actualizar datos ", ex)
    conexion.close
    #-----------------
def eliminar(id_boleta):
    conectar()
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "DELETE FROM boleta WHERE id_boleta = %s;"
            cursor.execute(consulta,(id_boleta))
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
            cursor.execute("SELECT COUNT(id_boleta)FROM boleta")
            #usamos fetchall para traer todos los datos
            contBoleta = cursor.fetchone()
            return contBoleta[0]
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Ocurrio un error al consultar: ", e)
    conexion.close
    #-----------------
#Programa principal TESTER
#Prueba insertar OK
#print("Conectado")
#auxBoleta= Boleta(0,"2021-04-09",1,1)
#insertar(auxBoleta)
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
#auxBoleta = Boleta(1,"2021-04-06",2,2)
#actualizar(auxBoleta)
#consultar()
#--------------------------
#Prueba de eliminar servicio por id servicio OK
#eliminar(2)
#consultar()
