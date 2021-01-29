import pymysql
from claseVendedor import Vendedor
#Conexion a la base de datos
def conectar():
    try:
        #pymsql.connect necesita 4 parametros
        conexion = pymysql.connect(host='localhost',user='root',password='',db='lemonvintage')
    except:
        print("Fallo en la conexion a la db")    
    return conexion
    

def insertar(vendedor):
    conectar()
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "INSERT INTO vendedor(id_vendedor,nombre,apellido,rut,telefono,correo,direccion,comuna,region) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);"
                        #%s hace referencia a una variable string
                        #%d hace referencia a un int
                        #%f hace referencia a un float
                        #En la siguiente linea excecute nos permite ejecutar varias veces con distintos datos
            cursor.execute(consulta,
                (vendedor.id_vendedor,
                vendedor.nombre,
                vendedor.apellido,
                vendedor.rut,
                vendedor.telefono,
                vendedor.correo,
                vendedor.direccion,
                vendedor.comuna,
                vendedor.region))
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
            cursor.execute("SELECT * FROM vendedor")
            #usamos fetchall para traer todos los datos
            auxVendedor = cursor.fetchall()
            #recorrer la coleccion
            for ven in auxVendedor:
                print(ven)
            return auxVendedor
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Ocurrio un error al consultar: ", e)
    conexion.close
    #-----------------
def buscar(Rut):
    conectar()
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "SELECT * FROM vendedor WHERE rut = %s;"
            cursor.execute(consulta,(Rut))
            #usamos fetchall para traer todos los datos
            auxVendedor = cursor.fetchall()
            #recorrer la coleccion
            for ven in auxVendedor:
                print(ven)
            return auxVendedor
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Ocurrio un error al buscar: ", e)
    conexion.close
    #-----------------
#actualizar vendedor por id_vendedor
def actualizar(vendedor):
    conectar()
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "UPDATE vendedor SET nombre = %s, apellido = %s, rut = %s, telefono = %s, correo = %s, direccion = %s, comuna = %s, region = %s WHERE rut = %s;"
                        #%s hace referencia a una variable string
                        #%d hace referencia a un int
                        #%f hace referencia a un float
                        #En la siguiente linea excecute nos permite ejecutar varias veces con distintos datos
            cursor.execute(consulta,
                (vendedor.nombre,
                vendedor.apellido,
                vendedor.rut,
                vendedor.telefono,
                vendedor.correo,
                vendedor.direccion,
                vendedor.comuna,
                vendedor.region,
                vendedor.rut))
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
            consulta = "DELETE FROM vendedor WHERE rut = %s;"
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

def contar():
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT COUNT(id_vendedor)FROM vendedor")
            #usamos fetchall para traer todos los datos
            contVendedor = cursor.fetchone()
            return contVendedor[0]
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Ocurrio un error al consultar: ", e)
    conexion.close

#Programa principal
#Prueba insertar OK
#print("Conectado")
#auxVendedor = Vendedor(0,"luci","fer","666","91560522","jcubillos@tooldesign.cl","americo vespucio 7732","la florida","RM")
#insertar(auxVendedor)
#consultar()
#print("Datos guardados")
#---------------------------
#Prueba Consultar OK
#consultar()
#--------------------------
#Prueba buscar rut OK
#buscar("666")
#--------------------------
#Prueba actualizar vendedor por rut OK 
#auxVendedor = Vendedor(2,"luci","fer","666","666","jona@tooldesign.cl","americo vespucio 7732","la florida","RM")
#actualizar(auxVendedor)
#consultar()
#buscar("5555")
#--------------------------
#Prueba de eliminar vendedor por rut OK
#eliminar(666)
#consultar()
#print(contar())