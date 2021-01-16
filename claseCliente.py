class Cliente:
    def __init__(self,nombre,apellido,rut,telefono,correo,direccion,comuna,region):
        self.nombre = nombre
        self.apellido = apellido
        self.rut = rut 
        self.telefono = telefono
        self.correo = correo 
        self.direccion = direccion
        self.comuna = comuna 
        self.region = region 
#prueba de clase cliente
#auxCliente = Cliente("Jona","Cubi",167255280,991450522,"jcubillos@tooldesign.cl","Americo Vespucio 7732","La Florida","RM")
#print(auxCliente.nombre + " " +auxCliente.apellido)