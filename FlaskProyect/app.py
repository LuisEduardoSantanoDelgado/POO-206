from flask import Flask

app= Flask(__name__)

#ruta simple
#@app.route('/')
#def Home():
        #return "Hola Mundo Flask"

#ruta con parametros
#@app.route('/saludo/<nombre>')
#def saludar(nombre):
        #return 'Hola,' +nombre+ '!!'

#ruta try-Catch
#@app.errorhandler(404)
#def PaginaNoEncontrada(a):
        #return 'Ten cuidado:Error de capa 8!!!!!'

#ruta doble
#@app.route('/usuario')
#@app.route('/usuaria')
#def dobleroute():
       #return "Soy e mismo recurso del servidor"


#ruta POST
@app.route('/formulario',methods=['POST'])
def formulario():
        return 'Soy un formulario'

if __name__ == '__main__':
    app.run(port=3000,debug=True)
    
    