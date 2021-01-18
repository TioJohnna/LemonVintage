#Programa Principal de Arranque
from flask import Flask,render_template
app = Flask(__name__)

#Rutear el home (la raiz del sitio)
@app.route('/')

def Index():
    #return ("Prueba de pagina levantada por el servidor de aplicaciones")
    return render_template('mantenedorCliente.html')

#route de la accion del formulario y agregar el metodo del formulario
#metodo post esconde los datos
#metodo get muestra los datos
#@app.route('/ingresarCliente',methods=['POST'])

#def ingresarCliente():


if __name__ == '__main__':
    #agregar un puerto que no se ocupe 500,5000,300,etc
    #debug=True sirve para no estar levantando el programa por cada modificacion, solo se hace un refresh
    app.run(port=3000,debug=True)

#despus de haber probado tienes que crear una carpeta llamada "templates"