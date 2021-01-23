import datetime
import pymysql
from claseServicio import Servicio
#Conexion a la base de datos
def conectar():
    try:
        #pymsql.connect necesita 4 parametros
        conexion = pymysql.connect(host='localhost',user='root',password='',db='lemonvintage')
    except:
        print("Fallo en la conexion a la db")    
    return conexion
    

def insertar(servicio):
    conectar()
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "INSERT INTO servicio(id_servicio,nombre,descripcion,fecha_inicio,fecha_termino,estado) VALUES (%s,%s,%s,%s,%s,%s);"
                        #%s hace referencia a una variable string
                        #%d hace referencia a un int
                        #%f hace referencia a un float
                        #En la siguiente linea excecute nos permite ejecutar varias veces con distintos datos
            cursor.execute(consulta,
                (servicio.id_servicio,
                servicio.nombre,
                servicio.descripcion,
                #la insercion de fecha tiene que ser formato YYYY-MM-DD 
                servicio.fecha_inicio,
                servicio.fecha_termino,
                servicio.estado))
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
            cursor.execute("SELECT * FROM servicio")
            #usamos fetchall para traer todos los datos
            auxServicio = cursor.fetchall()
            #recorrer la coleccion
            for ser in auxServicio:
                print(ser)
            return auxServicio
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Ocurrio un error al consultar: ", e)
    conexion.close
    #-----------------
def buscar(Id_servicio):
    conectar()
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "SELECT * FROM servicio WHERE id_servicio = %s;"
            cursor.execute(consulta,(Id_servicio))
            #usamos fetchall para traer todos los datos
            auxServicio = cursor.fetchall()
            #recorrer la coleccion
            for ser in auxServicio:
                print(ser)
            return auxServicio
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Ocurrio un error al buscar: ", e)
    conexion.close
    #-----------------
#actualizar servicio por id_servicio
def actualizar(servicio):
    conectar()
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "UPDATE servicio SET nombre = %s, descripcion = %s, fecha_inicio = %s, fecha_termino = %s, estado = %s WHERE id_servicio = %s;"
            #%s hace referencia a una variable string
                        #%d hace referencia a un int
                        #%f hace referencia a un float
                        #En la siguiente linea excecute nos permite ejecutar varias veces con distintos datos
            cursor.execute(consulta,
                (servicio.nombre,
                servicio.descripcion,
                servicio.fecha_inicio,
                servicio.fecha_termino,
                servicio.estado,
                servicio.id_servicio))
    #commit para que ejecute la consulta y almacene
        conexion.commit
    #rescatamos el error operacional y el error interno para luego guardar en ex
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as ex:
        print("Error al actualizar datos ", ex)
    conexion.close
    #-----------------
def eliminar(Id_servicio):
    conectar()
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "DELETE FROM servicio WHERE id_servicio = %s;"
                        #%s hace referencia a una variable string
                        #%d hace referencia a un int
                        #%f hace referencia a un float
                        #En la siguiente linea excecute nos permite ejecutar varias veces con distintos datos
            cursor.execute(consulta,(Id_servicio))
    #commit para que ejecute la consulta y almacene
        conexion.commit
    #rescatamos el error operacional y el error interno para luego guardar en ex
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as ex:
        print("Error al eliminar datos ", ex)
    conexion.close

#Programa principal
#Prueba insertar OK
#print("Conectado")
#auxServicio = Servicio(0,"Pintura","pintar ventana",'2021-01-20','2021-01-30',"en taller")
#insertar(auxServicio)
#consultar()
#print("Datos guardados")
#---------------------------
#Prueba Consultar OK
#consultar()
#--------------------------
#Prueba buscar id servicio OK
#buscar(1)
#--------------------------
#Prueba actualizar servicio por id servicio OK 
#auxServicio = Servicio(2,"SUPER MEGA restauracion","restauracion full","2021-01-01","2021-01-02","Super lista")
#actualizar(auxServicio)
#consultar()
#buscar("5555")
#--------------------------
#Prueba de eliminar servicio por id servicio OK
#eliminar(2)
#consultar()
