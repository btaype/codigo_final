from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_cors import CORS
from activos.sesion import sesion_activo
from io import BytesIO
import os

from os import path

from controler.iniciar_seison import inicioSesion
from controler.inscripcion import GestorPersonas
from controler.funciones_p import *
from controler.crear_evento import crear_evento
app = Flask(__name__)


UPLOAD_FOLDER = 'static/imagenEvento'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


CORS(app)
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        if (inicioSesion.iniciando(data)):
            print("TURE")
            if (sesion_activo.estado and sesion_activo.rol=='encargado'):
                print("TURE")
                return jsonify({'redireccionar': url_for('encargadoVista')})
            elif (sesion_activo.estado and sesion_activo.rol=='usuario'):
                return render_template('login.html')
            elif (sesion_activo.estado and sesion_activo.rol=='administrador'):
                return render_template('login.html')
            else:
                return render_template('login.html')
        else:
            print("false")
            return render_template('login.html')
    else:
        return render_template('login.html')
    

@app.route('/registro', methods=['GET', 'POST'])
def registrar():
    if request.method == 'POST':
        data = request.get_json();
        print(data)
        return jsonify({'redireccionar': url_for('login')})
    else:
        return render_template('registro.html')
    
@app.route('/terminos')
def terminos():
    return render_template('terminos.html')

@app.route('/encargadoVista', methods=['GET', 'POST'])
def encargadoVista():
    print("holaa")
    if request.method == 'POST':
        data = request.get_json();
        print(data)
        return jsonify({'redireccionar': url_for('crearEvento')})
    else:
        return render_template('vista_encargado.html')
    
@app.route('/encargadoVista/crearEvento', methods=['GET', 'POST'])
def crearEvento():
    if request.method == 'POST':
        data = request.get_json()
        if (data["solicitud"]==1):
            crear_evento.actilizar(data)
            return jsonify({'redireccionar': url_for('agregarPlantilla')})
        elif (data["solicitud"]==2):
            crear_evento.actilizar(data)
            return jsonify({'redireccionar': url_for('agregar_actividad')})
    else:
        resultado=crear_evento.inicio()
        print (resultado)
        return render_template('crear_evento.html ',resultado=resultado)
    
@app.route('/encargadoVista/crearEvento/agregarPlantilla', methods=['GET', 'POST'])
def agregarPlantilla():
    if request.method == 'POST':
        data = request.get_json()
        if(crear_evento.agregar_plantilla(data)):
            return jsonify({'redireccionar': url_for('crearEvento')})
        
    else:
        return render_template('agregar_plantilla.html ')

@app.route('/encargadoVista/crearEvento/agregarActividad', methods=['GET', 'POST'])
def agregar_actividad():
    if request.method == 'POST':
        data = request.get_json()
        if(crear_evento.agregar_plantilla(data)):
            return jsonify({'redireccionar': url_for('crearEvento')})
        
    else:
        return render_template('crear_actividad.html ')

@app.route('/obtener_ubicaciones')
def obtener_ubicaciones():
    resultado=crear_evento.obetener_imagen_ubicacion()
    return jsonify(resultado)
      
@app.route('/obtener_plantillas')
def obtener_plantillas():
    resultado=crear_evento.inicio()
    return jsonify(resultado)

@app.route('/obtener_actividades')
def obtener_actividades():
    actividades={"actividades": [{'nombre': "Actividad 1", 'descripcion': "Descripción corta de la actividad 1" },
        {'nombre': "Actividad 2", 'descripcion': "Descripción larga de la actividad 2 que puede contener hasta 200 letras. Esta descripción es solo un ejemplo para ilustrar el desbordamiento de texto." },
    ]   }
    return jsonify( actividades) 
 
@app.route('/usuarioVista')
def usuarioVista():
    return render_template('crear_actividad.html ')

@app.route('/upload', methods=['POST'])
def upload_file():
    pass
    
if __name__ == '__main__':
    
    app.run(debug=True)