from flask import Flask, jsonify, render_template, request, redirect, url_for, flash
import mysql.connector

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
        conn = mysql.connector.connect(**db_config)
        conn.cursor().execute('SELECT * FROM tb_albums')
        return jsonify({'status': 'ok', 'message': 'Conectado con éxito'}), 200
    except mysql.connector.Error as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/')
def home():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM tb_albums')
        consultaTodo = cursor.fetchall()
        return render_template('formulario.html', errores=(), albums=consultaTodo)
        
    except Exception as e:
        print('Error al consultar todo: ' + str(e))
        return render_template('formulario.html', errores=(), albums=[])

    finally:
        cursor.close()
        
@app.route('/detalles/<int:id>')
def detalle(id):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM tb_albums WHERE id=%s',((id,)))
        consultaId = cursor.fetchone()
        return render_template('consulta.html', errores=(), album= consultaId)
        
    except Exception as e:
        print('Error al consultar por Id: ' +e )
        return redirect(url_for=('home'))

    finally:
        cursor.close()

@app.route('/consulta')
def consulta():
    return render_template('consulta.html')

@app.route('/guardarAlbum', methods=['POST'])
def guardar():
    Vtitulo = request.form.get('txtTitulo', '').strip()
    VArtista = request.form.get('txtArtista', '').strip()
    VAnio = request.form.get('txtAnio', '').strip()

    if not VAnio.isdigit():
        flash('El año debe ser un número entero válido')
        return redirect(url_for('home'))

    VAnio = int(VAnio)
    conn = None

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO tb_albums (album, artista, anio) VALUES (%s, %s, %s)',
            (Vtitulo, VArtista, VAnio)
        )
        conn.commit()
        flash('Álbum se guardó en BD')
    except mysql.connector.Error as e:
        if conn:
            conn.rollback()
        flash('Algo falló: ' + str(e))
    finally:
        if conn:
            cursor.close()
            conn.close()

    return redirect(url_for('home'))

@app.errorhandler(404)
def paginaNoE(e):
    return 'Cuidado: Error de capa 8 !!!', 404

if __name__ == '__main__':
    app.run(port=8888, debug=True)