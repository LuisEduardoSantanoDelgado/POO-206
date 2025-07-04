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

@app.route('/DBcheck')
def DB_check():
    try:
        with closing(mysql.connector.connect(**db_config)) as conn:
            with closing(conn.cursor()) as cursor:
                cursor.execute('SELECT * FROM tb_albums WHERE state = 1')
                return jsonify({'status': 'ok', 'message': 'Conectado con éxito'}), 200
    except mysql.connector.Error as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/')
def home():
    try:
        with closing(mysql.connector.connect(**db_config)) as conn:
            with closing(conn.cursor()) as cursor:
                cursor.execute('SELECT * FROM tb_albums WHERE state = 1')
                consultaTodo = cursor.fetchall()
        return render_template('formulario.html', errores=(), albums=consultaTodo)
    except Exception as e:
        print('Error al consultar todo: ' + str(e))
        return render_template('formulario.html', errores=(), albums=[])

@app.route('/consulta')
def consulta():
    return render_template('consulta.html')

@app.route('/detalles/<int:id>')
def detalle(id):
    try:
        with closing(mysql.connector.connect(**db_config)) as conn:
            with closing(conn.cursor()) as cursor:
                cursor.execute('SELECT * FROM tb_albums WHERE id=%s AND state = 1', (id,))
                consultaId = cursor.fetchone()
        return render_template('consulta.html', errores=(), album=consultaId)
    except Exception as e:
        print('Error al consultar por Id: ' + str(e))
        return redirect(url_for('home'))

@app.route('/confirmarEliminacion/<int:id>')
def confirmarEliminacion(id):
    try:
        with closing(mysql.connector.connect(**db_config)) as conn:
            with closing(conn.cursor()) as cursor:
                cursor.execute('SELECT * FROM tb_albums WHERE id = %s AND state = 1', (id,))
                album = cursor.fetchone()
        if album:
            return render_template('confirmDel.html', album=album)
        else:
            flash('Álbum no encontrado o ya fue eliminado.')
            return redirect(url_for('home'))
    except Exception as e:
        print('Error en confirmarEliminacion:', str(e))
        flash('Error al cargar el álbum para confirmar eliminación.')
        return redirect(url_for('home'))
    
@app.route('/eliminarAlbum/<int:id>', methods=['POST'])
def eliminarAlbum(id):
    try:
        with closing(mysql.connector.connect(**db_config)) as conn:
            with closing(conn.cursor()) as cursor:
                cursor.execute('UPDATE tb_albums SET state = 0 WHERE id = %s', (id,))
                conn.commit()
        flash('Álbum eliminado correctamente (soft delete).')
    except Exception as e:
        print('Error al eliminar álbum: ' + str(e))
        flash('No se pudo eliminar el álbum.')
    return redirect(url_for('home'))

@app.route('/actualizar/<int:id>')
def actualizar(id):
    try:
        with closing(mysql.connector.connect(**db_config)) as conn:
            with closing(conn.cursor()) as cursor:
                cursor.execute('SELECT * FROM tb_albums WHERE id=%s AND state = 1', (id,))
                album = cursor.fetchone()
        if album:
            return render_template('formUpdate.html', album=album)
        else:
            flash('Album no encontrado')
            return redirect(url_for('home'))
    except Exception as e:
        print('Album no encontrado: ' + str(e))
        return redirect(url_for('home'))

@app.route('/actualizarAlbum/<int:id>', methods=['POST'])
def actualizarAlbum(id):
    Vtitulo = request.form.get('txtTitulo', '').strip()
    VArtista = request.form.get('txtArtista', '').strip()
    VAnio = request.form.get('txtAnio', '').strip()

    errores = {}

    if not Vtitulo:
        errores['txtTitulo'] = 'Nombre del album obligatorio'
    if not VArtista:
        errores['txtArtista'] = 'Nombre del artista obligatorio'
    if not VAnio:
        errores['txtAnio'] = 'Año del album obligatorio'
    elif not VAnio.isdigit() or int(VAnio) < 1800 or int(VAnio) > 2026:
        errores['txtAnio'] = 'En año solo ingresar un año válido'

    if errores:
        flash('Por favor corrige los errores.')
        return redirect(url_for('actualizar', id=id))

    try:
        with closing(mysql.connector.connect(**db_config)) as conn:
            with closing(conn.cursor()) as cursor:
                cursor.execute('UPDATE tb_albums SET album=%s, artista=%s, anio=%s WHERE id=%s',
                               (Vtitulo, VArtista, int(VAnio), id))
                conn.commit()
        flash('Álbum actualizado correctamente.')
        return redirect(url_for('home'))
    except Exception as e:
        print('Error al actualizar: ' + str(e))
        flash('Error al actualizar el álbum.')
        return redirect(url_for('actualizar', id=id))
    


@app.route('/guardarAlbum', methods=['POST'])
def guardar():
    Vtitulo = request.form.get('txtTitulo', '').strip()
    VArtista = request.form.get('txtArtista', '').strip()
    VAnio = request.form.get('txtAnio', '').strip()

    errores = {}

    if not Vtitulo:
        errores['txtTitulo'] = 'Nombre del album obligatorio'
    if not VArtista:
        errores['txtArtista'] = 'Nombre del artista obligatorio'
    if not VAnio:
        errores['txtAnio'] = 'Año del album obligatorio'
    elif not VAnio.isdigit() or int(VAnio) < 1800 or int(VAnio) > 2026:
        errores['txtAnio'] = 'En año solo ingresar un año válido'

    if errores:
        flash('Por favor corrige los errores.')
        return redirect(url_for('home'))

    if not VAnio.isdigit():
        flash('El año debe ser un número entero válido')
        return redirect(url_for('home'))

    VAnio = int(VAnio)

    try:
        with closing(mysql.connector.connect(**db_config)) as conn:
            with closing(conn.cursor()) as cursor:
                cursor.execute(
                    'INSERT INTO tb_albums (album, artista, anio) VALUES (%s, %s, %s)',
                    (Vtitulo, VArtista, VAnio)
                )
                conn.commit()
        flash('Álbum se guardó en BD')
    except mysql.connector.Error as e:
        flash('Algo falló: ' + str(e))
    
    return redirect(url_for('home'))

@app.errorhandler(404)
def paginaNoE(e):
    return 'Cuidado: Error de capa 8 !!!', 404

if __name__ == '__main__':
    app.run(port=8888, debug=True)