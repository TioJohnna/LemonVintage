#importar controladores
import mantenedorCliente
import mantenedorVendedor
import mantenedorServicio
import mantenedorProducto
import mantenedorTipoProducto
#importar modelos
import claseCliente
import claseVendedor
import claseServicio
import claseProducto
import claseTipoProducto
#importar flask y las librerias a ocupar
from flask import Flask,render_template,request,flash,redirect,url_for

app = Flask(__name__)
#Programa Principal de Arranque
#Rutear el home (la raiz del sitio)

#renderiza la pagina principal
@app.route('/')
def Index():
    return render_template('Index.html')

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
        try:
            auxBotonRegistrar = request.form['btnRegistrar']
            #CREATE
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
        try:
            auxBotonActualizar = request.form['btnActualizar']
            #CREATE
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
                print("Datos guardados")
                #flash("Datos Guardados")
        except:
            print("Datos no guardados")
            #flash("Datos no guardados")
            #FIN CREATE
        #es necesario redireccionar para que no se caiga luego de insertar
        return redirect(url_for('MantenedorCliente'))
#----------------------------Fin registrar datos-------------

#Renderizar pagina mantenedorVendedor
@app.route('/MantenedorVendedor')
def MantenedorVendedor():
    datos = mantenedorVendedor.consultar()
    return render_template('mantenedorVendedor.html',vendedor=datos)

#Renderizar pagina mantenedorProducto
@app.route('/MantenedorProducto')
def MantenedorProducto():
    datos = mantenedorProducto.consultar()
    return render_template('mantenedorProducto.html',producto=datos)

#Renderizar pagina mantenedorServicio
@app.route('/MantenedorServicio')
def MantenedorServicio():
    datos = mantenedorServicio.consultar()
    return render_template('mantenedorServicio.html',servicio=datos)

#Renderizar pagina mantenedorTipoProducto
@app.route('/MantenedorTipoProducto')
def MantenedorTipoProducto():
    datos = mantenedorTipoProducto.consultar()
    return render_template('mantenedorTipoProducto.html',tipoproducto=datos)


#--------------configurar registroCliente como inicio
#def Index():
    #return señala cual es la pagina que va levantar
    #return render_template('Index.html') #levanta la pagina home

    #guarda una coleccion con los datos 
    #datos = mantenedorCliente.consultar()
    #renderiza la pagina clientes y a la vez manda los datos almacenados en un arreglo clientes
    #return render_template('registroCliente.html',clientes=datos)

    #renderizacion de la pagina limpia
    #return render_template('registroCliente.html')
#------------------------------------------
#route de la accion del formulario y agregar el metodo del formulario
#metodo post esconde los datos
#metodo get muestra los datos

#@app.route('/MantenedorCliente',methods=['POST'])
#def ingresarCliente():
#    if request.method == 'POST':
#        #CREATE
#        try:
#            auxBotonRegistrar = request.form['btnRegistrar']
#            if auxBotonRegistrar == 'Registrar':
#                auxRut = request.form['txtRut']
#                auxNombe = request.form['txtNombre']
#                auxApellido = request.form['txtApellido']
#                auxTelefono = request.form['txtTelefono']
#                auxCorreo = request.form['txtCorreo']
#                auxDireccion = request.form['txtDireccion']
#                auxComuna = request.form['txtComuna']
#                auxRegion = request.form['txtRegion']
#                auxCliente = claseCliente.Cliente(0,auxNombe,auxApellido,auxRut,auxTelefono,auxCorreo,auxDireccion,auxComuna,auxRegion)
#                mantenedorCliente.insertar(auxCliente)
#                print("Datos guardados")
#                #flash("Datos Guardados")
#        except:
#            print("Datos no guardados")
#            #flash("Datos no guardados")
#        #es necesario redireccionar para que no se caiga luego de insertar
#        return redirect(url_for('MantenedorCliente'))
#----------------------------Fin registrar datos-------------

if __name__ == '__main__':
    #agregar un puerto que no se ocupe 500,5000,300,etc
    #debug=True sirve para no estar levantando el programa por cada modificacion, solo se hace un refresh
    app.run(port=3000,debug=True)

#despus de haber probado tienes que crear una carpeta llamada "templates"