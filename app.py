#importar controladores
import mantenedorCliente
import mantenedorVendedor
import mantenedorServicio
import mantenedorProducto
import mantenedorTipoProducto
import mantenedorAbono
import mantenedorDetalleBoleta
import mantenedorBoleta
import mantenedorDetalleCotizacion
import mantenedorCotizacion
#importar modelos
import claseCliente
import claseVendedor
import claseServicio
import claseProducto
import claseTipoProducto
import claseAbono
import claseDetalleBoleta
import claseBoleta
import claseDetalleCotizacion
import claseCotizacion
#importar flask y las librerias a ocupar
from flask import Flask,render_template,request,flash,redirect,url_for
from datetime import date
app = Flask(__name__)
#Programa Principal de Arranque
#Rutear el home (la raiz del sitio)

#renderiza la pagina principal
@app.route('/')
def Index():
    return render_template('Index.html')

#--RENDER MANTENEDORES
#para redireccionar las otras paginas es necesario agregar como ruta el nombre de la funcion 
#y renderizar cada pagina
#Renderizar pagina mantenedorCliente.html
@app.route('/MantenedorCliente')
def MantenedorCliente():
    datos = mantenedorCliente.consultar()
    #renderiza el template y al mismo rescata la consulta de la db con los datos para mostrar en la grilla
    return render_template('mantenedorCliente.html',clientes=datos)

#Es necesario cambiar el nombre del route para las acciones del mantenedor
# El action del form debe ir apuntando a este route
@app.route('/CRUDCliente',methods=['POST']) 
def CRUDCliente():
    if request.method == 'POST':
        #CREATE
        try:
            auxBotonRegistrar = request.form['btnRegistrar']
            if auxBotonRegistrar == 'Registrar':
                auxRut = request.form['txtRut']
                auxNombe = request.form['txtNombre']
                auxApellido = request.form['txtApellido']
                auxTelefono = request.form['txtTelefono']
                auxCorreo = request.form['txtCorreo']
                auxDireccion = request.form['txtDireccion']
                auxComuna = request.form['txtComuna']
                auxRegion = request.form['txtRegion']
                auxCliente = claseCliente.Cliente(0,auxNombe,auxApellido,auxRut,auxTelefono,auxCorreo,auxDireccion,auxComuna,auxRegion)
                mantenedorCliente.insertar(auxCliente)
                print("Datos guardados")
                #flash("Datos Guardados")
        except:
            print("Datos no guardados")
            #flash("Datos no guardados")
        #FIN CREATE
        #UPDATE
        try:
            auxBotonActualizar = request.form['btnActualizar']
            if auxBotonActualizar == 'Actualizar':
                auxIdcliente = request.form['txtIdcliente']
                auxRut = request.form['txtRut']
                auxNombe = request.form['txtNombre']
                auxApellido = request.form['txtApellido']
                auxTelefono = request.form['txtTelefono']
                auxCorreo = request.form['txtCorreo']
                auxDireccion = request.form['txtDireccion']
                auxComuna = request.form['txtComuna']
                auxRegion = request.form['txtRegion']
                auxCliente = claseCliente.Cliente(auxIdcliente,auxNombe,auxApellido,auxRut,auxTelefono,auxCorreo,auxDireccion,auxComuna,auxRegion)
                mantenedorCliente.actualizar(auxCliente)
                print("Datos Actualizados")
                #flash("Datos Actualizados")
        except:
            print("Datos no Actualizados")
            #flash("Datos no Actualizados")
        #FIN UPDATE
        #ELIMINAR
        try:
            auxBotonEliminar = request.form['btnEliminar']
            if auxBotonEliminar == 'Eliminar':
                auxRut = request.form['txtRut']
                mantenedorCliente.eliminar(auxRut)
                print("Datos Eliminados")
                #flash("Datos Eliminados")
        except:
            print("Datos no se han podido Eliminar")
            #flash("Datos no se han podido Eliminar")
        #FIN ELIMINAR

        #es necesario redireccionar para que no se caiga luego de insertar
        return redirect(url_for('MantenedorCliente'))
#----------------------------Fin CRUD Cliente-------------

#Renderizar pagina mantenedorVendedor
@app.route('/MantenedorVendedor')
def MantenedorVendedor():
    datos = mantenedorVendedor.consultar()
    return render_template('mantenedorVendedor.html',vendedor=datos)

@app.route('/CRUDVendedor',methods=['POST']) 
def CRUDVendedor():
    if request.method == 'POST':
        #CREATE
        try:
            auxBotonRegistrar = request.form['btnRegistrar']
            if auxBotonRegistrar == 'Registrar':
                auxRut = request.form['txtRut']
                auxNombe = request.form['txtNombre']
                auxApellido = request.form['txtApellido']
                auxTelefono = request.form['txtTelefono']
                auxCorreo = request.form['txtCorreo']
                auxDireccion = request.form['txtDireccion']
                auxComuna = request.form['txtComuna']
                auxRegion = request.form['txtRegion']
                auxVendedor = claseVendedor.Vendedor(0,auxNombe,auxApellido,auxRut,auxTelefono,auxCorreo,auxDireccion,auxComuna,auxRegion)
                mantenedorVendedor.insertar(auxVendedor)
                print("Datos guardados")
                #flash("Datos Guardados")
        except:
            print("Datos no guardados")
            #flash("Datos no guardados")
        #FIN CREATE
        #UPDATE
        try:
            auxBotonActualizar = request.form['btnActualizar']
            if auxBotonActualizar == 'Actualizar':
                auxIdvendedor = request.form['txtIdvendedor']
                auxRut = request.form['txtRut']
                auxNombe = request.form['txtNombre']
                auxApellido = request.form['txtApellido']
                auxTelefono = request.form['txtTelefono']
                auxCorreo = request.form['txtCorreo']
                auxDireccion = request.form['txtDireccion']
                auxComuna = request.form['txtComuna']
                auxRegion = request.form['txtRegion']
                auxVendedor = claseVendedor.Vendedor(auxIdvendedor,auxNombe,auxApellido,auxRut,auxTelefono,auxCorreo,auxDireccion,auxComuna,auxRegion)
                mantenedorVendedor.actualizar(auxVendedor)
                print("Datos Actualizados")
                #flash("Datos Actualizados")
        except:
            print("Datos no Actualizados")
            #flash("Datos no Actualizados")
        #FIN UPDATE
        #ELIMINAR
        try:
            auxBotonEliminar = request.form['btnEliminar']
            if auxBotonEliminar == 'Eliminar':
                auxRut = request.form['txtRut']
                mantenedorVendedor.eliminar(auxRut)
                print("Datos Eliminados")
                #flash("Datos Eliminados")
        except:
            print("Datos no se han podido Eliminar")
            #flash("Datos no se han podido Eliminar")
        #FIN ELIMINAR
        #es necesario redireccionar para que no se caiga luego de insertar
        return redirect(url_for('MantenedorVendedor'))
#----------------------------Fin CRUD Vendedor-------------

#Renderizar pagina mantenedorProducto
@app.route('/MantenedorProducto')
def MantenedorProducto():
    datos = mantenedorProducto.consultar()
    return render_template('mantenedorProducto.html',producto=datos)

@app.route('/CRUDProducto',methods=['POST']) 
def CRUDProducto():
    if request.method == 'POST':
        #CREATE
        try:
            auxBotonRegistrar = request.form['btnRegistrar']
            if auxBotonRegistrar == 'Registrar':
                auxIdproducto = request.form['txtIdProducto']
                auxNombre = request.form['txtNombre']
                auxDescripcion = request.form['txtDescripcion']
                auxColor = request.form['txtColor']
                auxMaterial = request.form['txtMaterial']
                auxCantidad = request.form['txtCantidad']
                auxAncho = request.form['txtAncho']
                auxAlto = request.form['txtAlto']
                auxEspesor = request.form['txtEspesor']
                auxPeso = request.form['txtPeso']
                auxPrecio = request.form['txtPrecio']
                auxDivisiones = request.form['txtDivisiones']
                auxAccesorios = request.form['txtAccesorios']
                auxTipoProducto = request.form['txtTipoProducto']
                auxProducto = claseProducto.Producto(auxIdproducto,auxNombre,auxDescripcion,auxColor,auxMaterial,auxCantidad,auxAncho,auxAlto,auxEspesor,auxPeso,auxPrecio,auxDivisiones,auxAccesorios,auxTipoProducto)
                mantenedorProducto.insertar(auxProducto)
                print("Datos guardados")
                #flash("Datos Guardados")
        except:
            print("Datos no guardados")
            #flash("Datos no guardados")
        #FIN CREATE
        #UPDATE
        try:
            auxBotonActualizar = request.form['btnActualizar']
            if auxBotonActualizar == 'Actualizar':
                auxIdproducto = request.form['txtIdProducto']
                auxNombre = request.form['txtNombre']
                auxDescripcion = request.form['txtDescripcion']
                auxColor = request.form['txtColor']
                auxMaterial = request.form['txtMaterial']
                auxCantidad = request.form['txtCantidad']
                auxAncho = request.form['txtAncho']
                auxAlto = request.form['txtAlto']
                auxEspesor = request.form['txtEspesor']
                auxPeso = request.form['txtPeso']
                auxPrecio = request.form['txtPrecio']
                auxDivisiones = request.form['txtDivisiones']
                auxAccesorios = request.form['txtAccesorios']
                auxTipoProducto = request.form['txtTipoProducto']
                auxProducto = claseProducto.Producto(auxIdproducto,auxNombre,auxDescripcion,auxColor,auxMaterial,auxCantidad,auxAncho,auxAlto,auxEspesor,auxPeso,auxPrecio,auxDivisiones,auxAccesorios,auxTipoProducto)
                mantenedorProducto.actualizar(auxProducto)
                print("Datos actualizados")
                #flash("Datos actualizados")
        except:
            print("Datos no Actualizados")
            #flash("Datos no Actualizados")
        #FIN UPDATE
        #ELIMINAR OK
        try:
            auxBotonEliminar = request.form['btnEliminar']
            if auxBotonEliminar == 'Eliminar':
                auxIdproducto = request.form['txtIdProducto']
                mantenedorProducto.eliminar(auxIdproducto)
                print("Datos Eliminados")
                #flash("Datos Eliminados")
        except:
            print("Datos no se han podido Eliminar")
            #flash("Datos no se han podido Eliminar")
        #FIN ELIMINAR
        #es necesario redireccionar para que no se caiga luego de insertar
        return redirect(url_for('MantenedorProducto'))
#----------------------------Fin CRUD Producto-------------

#Renderizar pagina mantenedorServicio
@app.route('/MantenedorServicio')
def MantenedorServicio():
    datos = mantenedorServicio.consultar()
    return render_template('mantenedorServicio.html',servicio=datos)


@app.route('/CRUDServicio',methods=['POST']) 
def CRUDServicio():
    if request.method == 'POST':
        #CREATE
        try:
            auxBotonRegistrar = request.form['btnRegistrar']
            if auxBotonRegistrar == 'Registrar':
                auxIdservicio = request.form['txtIdservicio']
                auxNombre = request.form['txtNombre']
                auxDescripcion = request.form['txtDescripcion']
                auxInicio = request.form['txtInicio']
                auxTermino = request.form['txtTermino']
                auxEstado = request.form['txtEstado']
                auxServicio = claseServicio.Servicio(0,auxNombre,auxDescripcion,auxInicio,auxTermino,auxEstado)
                mantenedorServicio.insertar(auxServicio)
                print("Datos guardados")
                #flash("Datos Guardados")
        except:
            print("Datos no guardados")
            #flash("Datos no guardados")
        #FIN CREATE
        #UPDATE
        try:
            auxBotonActualizar = request.form['btnActualizar']
            if auxBotonActualizar == 'Actualizar':
                auxIdservicio = request.form['txtIdservicio']
                auxNombre = request.form['txtNombre']
                auxDescripcion = request.form['txtDescripcion']
                auxInicio = request.form['txtInicio']
                auxTermino = request.form['txtTermino']
                auxEstado = request.form['txtEstado']
                auxServicio = claseServicio.Servicio(0,auxNombre,auxDescripcion,auxInicio,auxTermino,auxEstado)
                mantenedorServicio.insertar(auxServicio)
                print("Datos Actualizados")
                #flash("Datos Actualizados")
        except:
            print("Datos no Actualizados")
            #flash("Datos no Actualizados")
        #FIN UPDATE
        #ELIMINAR
        try:
            auxBotonEliminar = request.form['btnEliminar']
            if auxBotonEliminar == 'Eliminar':
                auxIdservicio = request.form['txtIdservicio']
                mantenedorServicio.eliminar(auxIdservicio)
                print("Datos Eliminados")
                #flash("Datos Eliminados")
        except:
            print("Datos no se han podido Eliminar")
            #flash("Datos no se han podido Eliminar")
        #FIN ELIMINAR

        #es necesario redireccionar para que no se caiga luego de insertar
        return redirect(url_for('MantenedorServicio'))
#----------------------------Fin CRUD Servicio-------------
#Renderizar pagina mantenedorTipoProducto
@app.route('/MantenedorTipoProducto')
def MantenedorTipoProducto():
    datos = mantenedorTipoProducto.consultar()
    return render_template('mantenedorTipoProducto.html',tipoproducto=datos)

@app.route('/CRUDTipoProducto',methods=['POST']) 
def CRUDTipoProducto():
    if request.method == 'POST':
        #CREATE
        try:
            auxBotonRegistrar = request.form['btnRegistrar']
            if auxBotonRegistrar == 'Registrar':
                auxIdtipoproducto = request.form['txtIdtipoproducto']
                auxNombre = request.form['txtNombre']
                auxDescripcion = request.form['txtDescripcion']
                auxTipoproducto = claseTipoProducto.Tipo_Producto(0,auxNombre,auxDescripcion)
                mantenedorTipoProducto.insertar(auxTipoproducto)
                print("Datos guardados")
                #flash("Datos Guardados")
        except:
            print("Datos no guardados")
            #flash("Datos no guardados")
        #FIN CREATE
        #UPDATE
        try:
            auxBotonActualizar = request.form['btnActualizar']
            if auxBotonActualizar == 'Actualizar':
                auxIdtipoproducto = request.form['txtIdtipoproducto']
                auxNombre = request.form['txtNombre']
                auxDescripcion = request.form['txtDescripcion']
                auxTipoproducto = claseTipoProducto.Tipo_Producto(auxIdtipoproducto,auxNombre,auxDescripcion)
                mantenedorTipoProducto.actualizar(auxTipoproducto)
                print("Datos Actualizados")
                #flash("Datos Actualizados")
        except:
            print("Datos no Actualizados")
            #flash("Datos no Actualizados")
        #FIN UPDATE
        #ELIMINAR
        try:
            auxBotonEliminar = request.form['btnEliminar']
            if auxBotonEliminar == 'Eliminar':
                auxIdtipoproducto = request.form['txtIdtipoproducto']
                mantenedorTipoProducto.eliminar(auxIdtipoproducto)
                print("Datos Eliminados")
                #flash("Datos Eliminados")
        except:
            print("Datos no se han podido Eliminar")
            #flash("Datos no se han podido Eliminar")
        #FIN ELIMINAR

        #es necesario redireccionar para que no se caiga luego de insertar
        return redirect(url_for('MantenedorTipoProducto'))
#----------------------------Fin CRUD Tipo Producto-------------
#--FIN RENDER MANTENEDORES------------------------

#--RENDER TRANSACCIONES----------------------------
#Renderizar pagina Ventas
@app.route('/Ventas')
def Ventas():
    datosClientes = mantenedorCliente.consultar()
    datosVendedores = mantenedorVendedor.consultar()
    datosProductos = mantenedorProducto.consultar()
    return render_template('ventaProductoServicio.html',clientes=datosClientes,vendedores=datosVendedores,productos=datosProductos)
@app.route('/Comprar',methods=['POST'])
def Comprar():
    if request.method == 'POST':
        try:
            auxBtnComprar = request.form['btnComprar']
            if auxBtnComprar == 'Comprar':
                auxFechaBoleta=date.today()
                auxIdCliente=request.form['txtId_cliente']
                auxIdVendedor=request.form['txtId_vendedor']
                auxBoleta=claseBoleta.Boleta(0,auxFechaBoleta,auxIdCliente,auxIdVendedor)
                mantenedorBoleta.insertar(auxBoleta)
                auxDetalle = request.form['txtDetalle']
                auxTotal= request.form['txtTotal']
                auxDetalleBoleta=claseDetalleBoleta.DetalleBoleta(0,auxDetalle,auxTotal,1,1,1)
                mantenedorDetalleBoleta.insertar(auxDetalleBoleta)
        except:
            print("Compra no realizada")
            #flash("Compra no realizada")
        return redirect(url_for('Ventas'))

#Renderizar pagina Cotizaciones
@app.route('/Cotizaciones')
def Cotizaciones():
    datos = mantenedorProducto.consultar()
    return render_template('cotizarProductoServicio.html',ventas=datos)
@app.route('/Cotizar',methods=['POST'])
def Cotizar():
    if request.method == 'POST':
        try:
            auxBtnCotizar = request.form['btnCotizar']
            if auxBtnCotizar == 'Cotizar':
                auxFecha=date.today()
                auxIdCliente=request.form['txtId_cliente']
                auxIdVendedor=request.form['txtId_vendedor']
                auxCotizar=claseCotizacion.Cotizacion(0,auxFecha,auxIdCliente,auxIdVendedor)
                mantenedorCotizacion.insertar(auxCotizar)
                auxDetalle = request.form['txtDetalle']
                auxTotal= request.form['txtTotal']
                auxDetalleCotizacion=claseDetalleCotizacion.DetalleCotizacion(0,auxDetalle,auxTotal,1,1,1)
                mantenedorDetalleCotizacion.insertar(auxDetalleCotizacion)
        except:
            print("Compra no realizada")
            #flash("Compra no realizada")
        return redirect(url_for('Cotizaciones'))

#Renderizar pagina Cotizaciones
@app.route('/Abonos')
def Abonos():
    datosClientes = mantenedorCliente.consultar()
    datosVendedores = mantenedorVendedor.consultar()
    datosBoletas = mantenedorBoleta.consultar()
    datosDetalleBoletas = mantenedorDetalleBoleta.consultar()
    return render_template('abonarProductoServicio.html',clientes=datosClientes,vendedores=datosVendedores,boletas = datosBoletas,detalleboletas = datosDetalleBoletas)

#Funcion de abonar
@app.route('/Abonar', methods=['POST'])
def Abonar():
    if request.method == 'POST':
            #CREATE
            try:
                auxBotonAbonar = request.form['btnAbonar']
                if auxBotonAbonar == 'Abonar':
                    auxMonto = request.form['txtMonto']
                    auxFecha = date.today()
                    auxId_detalleboleta= request.form['txtId_detalleboleta']
                    auxAbono = claseAbono.Abono(0,auxMonto,auxFecha,auxId_detalleboleta)
                    mantenedorAbono.insertar(auxAbono)
                    print("Datos guardados")
                    #flash("Datos Guardados")
            except:
                print("Datos no guardados")
                #flash("Datos no guardados")
            #FIN CREATE
            return redirect(url_for('Abonos'))

#Render pagina reporte
@app.route('/Repoerte')
def Reporte():
    contarVendedores=mantenedorVendedor.contar()
    contarClientes=mantenedorCliente.contar()
    contarBoleta=mantenedorBoleta.contar()
    contarCotizacion=mantenedorCotizacion.contar()
    ventaMinima=mantenedorDetalleBoleta.minimo()
    ventaMaxima=mantenedorDetalleBoleta.maximo()
    totalVentas=mantenedorDetalleBoleta.total()
    return render_template ('reporteEstadistica.html',cantVendedores=contarVendedores,cantClientes=contarClientes,cantBoletas=contarBoleta,cantCotizaciones=contarCotizacion,ventaMenor=ventaMinima,ventaMayor=ventaMaxima,ventaTotal=totalVentas)



#--CONFIG PPORT AND RUN DEBUG--
#config puerto para lenovo JCubillos
if __name__ == '__main__':
    #agregar un puerto que no se ocupe 500,5000,300,etc
    #debug=True sirve para no estar levantando el programa por cada modificacion, solo se hace un refresh
    app.run(port=3000,debug=True)

#despus de haber probado tienes que crear una carpeta llamada "templates"