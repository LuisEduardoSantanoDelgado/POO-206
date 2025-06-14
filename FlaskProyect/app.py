from flask import Flask, jsonify
from flask_mysql import MySQL  
import MySQL  



app= Flask(__name__)

app.config['MYSQL_HOST']="localhost"

app.config['MYSQL_USER']="root"

app.config['MYSQL_USER']=""

app.config['MYSQL_USER']="dbFlask"

app.config['MYSQL_PORT']=8889

mysql= MySQL(app)

#Ruta para probar conexiónbrew install mysql

@app.route('/DBCheck')
def DB_check():
        try:
                cursor= mysql.connection.cursor()
                cursor.excecute('Select 1')
                return jsonify( {'status':'ok','message':'conectado con exito'} ),200
        except MySQLdb.MySQLError as e:
                return jsonify( {'error':'ok','message':'str(e)'} ),500



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
        
#ruta try-Catch
#@app.errorhandler(405)
#def PaginaNoEncontrada(a):
        #return 'Revisa el metofo de envio de tu ruta (GET o POST)!!!!!'

#ruta doble
#@app.route('/usuario')
#@app.route('/usuaria')
#def dobleroute():
       #return "Soy e mismo recurso del servidor"


#ruta POST
#@app.route('/formulario',methods=['POST'])
#def formulario():
#        return 'Soy un formulario'



if __name__ == '__main__':
    app.run(port=8890,debug=True)
    
    