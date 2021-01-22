#importar controlador
import mantenedorCliente
#importar modelo
import claseCliente
from flask import Flask,render_template,request,flash,redirect,url_for

app = Flask(__name__)
#Programa Principal de Arranque
#Rutear el home (la raiz del sitio)
@app.route('/')


def Index():
    #return señala cual es la pagina que va levantar
    #return render_template('Index.html') #levanta la pagina home

    #guarda una coleccion con los datos 
    datos = mantenedorCliente.consultar()
    #renderiza la pagina clientes y a la vez manda los datos almacenados en un arreglo clientes
    return render_template('registroCliente.html',clientes=datos)

    #renderizacion de la pagina limpia
    #return render_template('registroCliente.html')

#route de la accion del formulario y agregar el metodo del formulario
#metodo post esconde los datos
#metodo get muestra los datos
@app.route('/ingresarCliente',methods=['POST'])

def ingresarCliente():
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
        #es necesario redireccionar para que no se caiga luego de insertar
        return redirect(url_for('Index'))


if __name__ == '__main__':
    #agregar un puerto que no se ocupe 500,5000,300,etc
    #debug=True sirve para no estar levantando el programa por cada modificacion, solo se hace un refresh
    app.run(port=3000,debug=True)

#despus de haber probado tienes que crear una carpeta llamada "templates"