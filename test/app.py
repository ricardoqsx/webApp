from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Ruta principal para mostrar y actualizar datos
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Obtener datos del formulario HTML
        nombre = request.form['nombre']
        edad = request.form['edad']

        # Insertar o actualizar los datos en la base de datos
        conn = sqlite3.connect('mi_base_de_datos.db')
        cursor = conn.cursor()
        cursor.execute("INSERT OR REPLACE INTO mi_tabla (nombre, edad) VALUES (?, ?)", (nombre, edad))
        conn.commit()
        conn.close()

    # Consulta de datos existentes
    conn = sqlite3.connect('mi_base_de_datos.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM mi_tabla')
    datos = cursor.fetchall()
    conn.close()

    return render_template('index.html', datos=datos)

if __name__ == '__main__':
    app.run(debug=True)
