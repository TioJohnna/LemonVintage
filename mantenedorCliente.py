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

#Programa principal
conectar()
print("Conectado")
auxCliente = Cliente(0,"Jona","Cubi","167255280","91560522","jcubillos@tooldesign.cl","americo vespucio 7732","la florida","RM")
insertar(auxCliente)
print("Datos guardados")
