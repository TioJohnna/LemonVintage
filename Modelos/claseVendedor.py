class Vendedor:
    def __init__(self,id_vendedor,nombre,apellido,rut,telefono,correo,direccion,comuna,region):
        self.id_vendedor = id_vendedor
        self.nombre = nombre
        self.apellido = apellido
        self.rut = rut 
        self.telefono = telefono
        self.correo = correo 
        self.direccion = direccion
        self.comuna = comuna 
        self.region = region 
#prueba de clase Vendedor
#auxVendedor = Vendedor(0,"Jona","Cubi",167255280,991450522,"jcubillos@tooldesign.cl","Americo Vespucio 7732","La Florida","RM")
#print(auxVendedor.nombre + " " +auxVendedor.apellido)