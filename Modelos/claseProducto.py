class Producto:
    def __init__(self,id_producto,nombre,descripcion,color,material,cantidad,ancho,alto,espesor,peso,precio,divisiones,accesorios,tipo_producto):
        self.id_producto = id_producto
        self.nombre = nombre
        self.descripcion = descripcion
        self.color = color 
        self.material = material
        self.cantidad = cantidad 
        self.ancho = ancho
        self.alto = alto 
        self.espesor = espesor 
        self.peso = peso
        self.precio = precio
        self.divisiones = divisiones
        self.accesorios = accesorios
        self.tipo_producto = tipo_producto     
#prueba de clase producto
#auxProducto = Producto(0,"puerta","puerta de madera nativa","rojo","rauli",2,90,210,3.5,50,80000,2,"españoleta","puerta")
#print(auxProducto.nombre + " " +str(auxProducto.espesor))