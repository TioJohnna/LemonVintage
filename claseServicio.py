import datetime
class Servicio:
    def __init__(self,id_servicio,nombre,descripcion,fecha_inicio,fecha_termino,estado):
        self.id_servicio = id_servicio
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio= fecha_inicio
        self.fecha_termino = fecha_termino
        self.estado = estado 
#prueba de clase Vendedor
#auxServicio = Servicio(0,"Restauracion","eliminado de pintura","01/01/2020","30/01/2020","En taller")
#print(auxServicio.nombre + " " + auxServicio.fecha_inicio)