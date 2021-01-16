import pymysql
from claseCliente import Cliente

def Conectar():
    try:
        #pymsql.connect necesita 4 parametros
        conexion = pymysql.connect(host='localhost',user='root',password='',db='LemonVintage')
    except:
        print("Fallo en la conexion a la db")
    return conexion

Conectar()
print("Conectado")
        