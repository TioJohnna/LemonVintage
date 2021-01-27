class DetalleCotizacion   :
    def __init__(self,id_detallecotizacion,detalle,total,cotizacion_id_cotizacion,servicio_id_servicio,producto_id_producto):
        self.id_detallecotizacion = id_detallecotizacion
        self.detalle = detalle
        self.total  = total
        self.cotizacion_id_cotizacion = cotizacion_id_cotizacion
        self.producto_id_producto = producto_id_producto
        self.servicio_id_servicio = servicio_id_servicio