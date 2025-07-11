from flask import Flask, jsonify, render_template, request, redirect, url_for, flash
import mysql.connector
from contextlib import closing

app = Flask(__name__)
app.secret_key = 'mysecretKey'

db_config = {
    'host': '127.0.0.1',
    'port': 8889,
    'user': 'root',
    'password': 'root',
    'database': 'dbflask',
    'unix_socket': '/Applications/MAMP/tmp/mysql/mysql.sock'
}


@app.route("/")
def home():
    return render_template("POOproyecto/Examen.html")

@app.route('/guardarContacto', methods=['POST'])
def guardar():
    Vnombre = request.form.get('txtNombre', '').strip()
    Vcorreo = request.form.get('txtCorreo', '').strip()
    Vtelefono = request.form.get('txtTelefono', '').strip()
    Vedad = request.form.get('txtEd', '').strip()

    errores = {}

    if not Vnombre:
        errores['txtNombre'] = 'Nombre obligatorio'
    if not Vcorreo:
        errores['txtCorreo'] = 'Correo obligatorio'
    if not Vtelefono:
        errores['txtTelefono'] = 'Teléfono obligatorio'
    if not Vedad or not Vedad.isdigit() or int(Vedad) < 1 or int(Vedad) > 105:
        errores['txtEd'] = 'Edad inválida'

    if errores:
        for err in errores.values():
            flash(err)
        return redirect(url_for('home'))

    try:
        with closing(mysql.connector.connect(**db_config)) as conn:
            with closing(conn.cursor()) as cursor:
                cursor.execute(
                    'INSERT INTO tb_contactos (nombre, correo, telefono, edad, state) VALUES (%s, %s, %s, %s, 1)',
                    (Vnombre, Vcorreo, Vtelefono, int(Vedad))
                )
                conn.commit()
        flash('Contacto guardado correctamente.')
    except mysql.connector.Error as e:
        flash('Error al guardar contacto: ' + str(e))
    
    return redirect(url_for('home'))

@app.route('/detalles/<int:id>')
def detalle(id):
    try:
        with closing(mysql.connector.connect(**db_config)) as conn:
            with closing(conn.cursor()) as cursor:
                cursor.execute('SELECT * FROM tb_contactos WHERE id=%s AND state = 1', (id,))
                contacto = cursor.fetchone()
        return render_template('consulta.html', contacto=contacto)
    except Exception as e:
        flash('Error al consultar el contacto: ' + str(e))
        return redirect(url_for('home'))

@app.route('/confirmarEliminacion/<int:id>')
def confirmarEliminacion(id):
    try:
        with closing(mysql.connector.connect(**db_config)) as conn:
            with closing(conn.cursor()) as cursor:
                cursor.execute('SELECT * FROM tb_contactos WHERE id=%s AND state = 1', (id,))
                contacto = cursor.fetchone()
        return render_template('confirmDel.html', contacto=contacto)
    except Exception as e:
        flash('Error al cargar confirmación: ' + str(e))
        return redirect(url_for('home'))

@app.route('/eliminarContacto/<int:id>', methods=['POST'])
def eliminarContacto(id):
    try:
        with closing(mysql.connector.connect(**db_config)) as conn:
            with closing(conn.cursor()) as cursor:
                cursor.execute('UPDATE tb_contactos SET state = 0 WHERE id = %s', (id,))
                conn.commit()
        flash('Contacto eliminado correctamente.')
    except Exception as e:
        flash('Error al eliminar contacto: ' + str(e))
    return redirect(url_for('home'))

@app.route('/actualizar/<int:id>')
def actualizar(id):
    try:
        with closing(mysql.connector.connect(**db_config)) as conn:
            with closing(conn.cursor()) as cursor:
                cursor.execute('SELECT * FROM tb_contactos WHERE id = %s AND state = 1', (id,))
                contacto = cursor.fetchone()
        return render_template('formUpdate.html', contacto=contacto)
    except Exception as e:
        flash('Error al cargar el contacto: ' + str(e))
        return redirect(url_for('home'))

@app.route('/actualizarContacto/<int:id>', methods=['POST'])
def actualizarContacto(id):
    nombre = request.form.get('txtNombre', '').strip()
    correo = request.form.get('txtCorreo', '').strip()
    telefono = request.form.get('txtTelefono', '').strip()
    edad = request.form.get('txtEdad', '').strip()

    errores = {}
    if not nombre:
        errores['txtNombre'] = 'Nombre obligatorio'
    if not correo:
        errores['txtCorreo'] = 'Correo obligatorio'
    if not telefono:
        errores['txtTelefono'] = 'Teléfono obligatorio'
    if not edad or not edad.isdigit() or int(edad) < 1 or int(edad) > 120:
        errores['txtEdad'] = 'Edad inválida'

    if errores:
        for err in errores.values():
            flash(err)
        return redirect(url_for('actualizar', id=id))

    try:
        with closing(mysql.connector.connect(**db_config)) as conn:
            with closing(conn.cursor()) as cursor:
                cursor.execute(
                    'UPDATE tb_contactos SET nombre=%s, correo=%s, telefono=%s, edad=%s WHERE id=%s',
                    (nombre, correo, telefono, int(edad), id)
                )
                conn.commit()
        flash('Contacto actualizado correctamente.')
    except Exception as e:
        flash('Error al actualizar contacto: ' + str(e))
        tu_proyecto/
├── app.py
└── templates/
    └── Examen.html

    return redirect(url_for('home'))

@app.errorhandler(404)
def paginaNoE(e):
    return 'Cuidado: Error de capa 8 !!!', 404

if __name__ == '__main__':
    app.run(port=8888, debug=True)
    
    