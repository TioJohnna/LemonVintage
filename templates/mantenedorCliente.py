import pymysql
from claseCliente import Cliente
#Conexion a la base de datos
def conectar():
    try:
        #pymsql.connect necesita 4 parametros
        conexion = pymysql.connect(host='localhost',user='root',password='',db='lemonvintage')
    except:
        print("Fallo en la conexion a la db")    
    return conexion
    

def insertar(cliente):
    conectar()
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "INSERT INTO cliente(id_cliente,nombre,apellido,rut,telefono,correo,direccion,comuna,region) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);"
                        #%s hace referencia a una variable string
                        #%d hace referencia a un int
                        #%f hace referencia a un float
                        #En la siguiente linea excecute nos permite ejecutar varias veces con distintos datos
            cursor.execute(consulta,
                (cliente.id_cliente,
                cliente.nombre,
                cliente.apellido,
                cliente.rut,
                cliente.telefono,
                cliente.correo,
                cliente.direccion,
                cliente.comuna,
                cliente.region))
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
            cursor.execute("SELECT * FROM cliente")
            #usamos fetchall para traer todos los datos
            auxCliente = cursor.fetchall()
            #recorrer la coleccion
            for cli in auxCliente:
                print(cli)
            return auxCliente
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Ocurrio un error al consultar: ", e)
    conexion.close
    #-----------------
def buscar(idCliente):
    conectar()
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "SELECT * FROM cliente WHERE id_cliente = %s;"
            cursor.execute(consulta,(idCliente))
            #usamos fetchall para traer todos los datos
            auxCliente = cursor.fetchall()
            #recorrer la coleccion
            for cli in auxCliente:
                print(cli)
            return auxCliente
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Ocurrio un error al buscar: ", e)
    conexion.close
    #-----------------
#actualizar cliente por id_cliente
def actualizar(cliente):
    conectar()
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "UPDATE cliente SET nombre = %s, apellido = %s, rut = %s, telefono = %s, correo = %s, direccion = %s, comuna = %s, region = %s WHERE id_cliente = %s;"
                        #%s hace referencia a una variable string
                        #%d hace referencia a un int
                        #%f hace referencia a un float
                        #En la siguiente linea excecute nos permite ejecutar varias veces con distintos datos
            cursor.execute(consulta,
                (cliente.nombre,
                cliente.apellido,
                cliente.rut,
                cliente.telefono,
                cliente.correo,
                cliente.direccion,
                cliente.comuna,
                cliente.region,
                cliente.id_cliente))
    #commit para que ejecute la consulta y almacene
        conexion.commit
    #rescatamos el error operacional y el error interno para luego guardar en ex
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as ex:
        print("Error al actualizar datos ", ex)
    conexion.close
    #-----------------
def eliminar(idCliente):
    conectar()
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "DELETE FROM cliente WHERE id_cliente = %s;"
                        #%s hace referencia a una variable string
                        #%d hace referencia a un int
                        #%f hace referencia a un float
                        #En la siguiente linea excecute nos permite ejecutar varias veces con distintos datos
            cursor.execute(consulta,(idCliente))
    #commit para que ejecute la consulta y almacene
        conexion.commit
    #rescatamos el error operacional y el error interno para luego guardar en ex
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as ex:
        print("Error al eliminar datos ", ex)
    conexion.close

#Programa principal
#Prueba insertar OK
#print("Conectado")
#auxCliente = Cliente(0,"barbie","reyes","5555","91560522","jcubillos@tooldesign.cl","americo vespucio 7732","la florida","RM")
#insertar(auxCliente)
#print("Datos guardados")
#---------------------------
#Prueba Consultar OK
#consultar()
#--------------------------
#Prueba buscar OK
#buscar("22222")
#--------------------------
#Prueba actualizar cliente por id_cliente OK 
#auxCliente = Cliente(5,"barbara","reyes","5555","91560522","samanttta@tooldesign.cl","americo vespucio 7732","la florida","RM")
#actualizar(auxCliente)
#buscar("5555")
#--------------------------
#Prueba de eliminar cliente por id_cliente OK
#eliminar(5)
#consultar()