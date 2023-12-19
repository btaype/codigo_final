from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_cors import CORS
from activos.sesion import sesion_activo
from werkzeug.utils import secure_filename
from io import BytesIO
from werkzeug.utils import secure_filename
from DB.base_datos import db
from model.evento import ubicaciones,imagen_ubicacion
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
   
    if request.method == 'POST':
        data = request.get_json()
        if(data["solicitud"]==1):
            return jsonify({'redireccionar': url_for('crearEvento')})
        elif(data["solicitud"]==2):
            return jsonify({'redireccionar': url_for('gestionarEevento')})

    else:
        return render_template('vista_encargado.html')
    
@app.route('/encargadoVista/crearEvento', methods=['GET', 'POST'])
def crearEvento():
    if request.method == 'POST':
        data = request.get_json()
        crear_evento.actilizar(data)
        if (data["solicitud"]==1):  
            return jsonify({'redireccionar': url_for('agregarPlantilla')})
        
        elif (data["solicitud"]==2): 
            return jsonify({'redireccionar': url_for('agregar_actividad')})
        
        elif (data["solicitud"]==3):
            
            return jsonify({'redireccionar': url_for('agregarPaquete')})
    else:
        resultado=crear_evento.obtenerevento()
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
        crear_evento.actulizar_actividad(data)
        if(data["solicitud"]==1):
            print ("hollaa")
            return jsonify({'redireccionar': url_for('agregarUbiacion')}) 
        elif(data["solicitud"]==2):
            return jsonify({'redireccionar': url_for('agregarMateriales')}) 
        elif(data["solicitud"]==3):
            return jsonify({'redireccionar': url_for('agregarExpositor')}) 
              
    else:
        resultado=crear_evento.obtener_expositores()
        return render_template('crear_actividad.html',resultado=resultado)

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
    actividades=crear_evento.obtener_actividades()
    return  {"actividades":actividades} 



@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    pass

@app.route('/agregarUbiacion', methods=['GET', 'POST'])
def agregarUbiacion():
    if request.method == 'POST':
        nuevo_ubicacion = crear_evento.crear_ubicacion(request)
        imagen = request.files['imagen']
        nombre_imagen = generate_unique_filename(secure_filename(imagen.filename))
        ruta_guardado = os.path.join(app.config['UPLOAD_FOLDER'], nombre_imagen)
        imagen.save(ruta_guardado)
        print(nuevo_ubicacion.id_ubicacion)
        print (nombre_imagen)
        nueva_imagen_ubicacion =imagen_ubicacion(
        imagen=nombre_imagen,
        id_ubicacion=nuevo_ubicacion.id_ubicacion
        )
        
        db.session.add(nueva_imagen_ubicacion)
        db.session.commit()
        print ("eeee")
 
        return jsonify({'redireccionar': url_for('agregar_actividad')})  
    else:
        print
        return render_template('agregar_ubicacion.html')     

@app.route('/obtener_expositores', methods=['GET', 'POST'])
def obtener_expositor():
    resultado=crear_evento.obtener_expositores()
    print(resultado)
    resultado=resultado["expositores"]
    return jsonify({'expositores':resultado})
    pass
@app.route('/obtener_materiales', methods=['GET', 'POST'])
def opteenr_material():
    resultado=crear_evento.obtener_materiales()
    resultado=resultado["materiales"]
    return jsonify({'materiales':resultado})

@app.route('/obtener_paquetes', methods=['GET', 'POST'])
def obtener_paquetes_p():
    print("aqui")
    resultado=crear_evento.obtener_paquetes()
    return jsonify({'paquetes':resultado})


@app.route('/encargadoVista/crearEvento/agregarActividad/agregarMateriales', methods=['GET', 'POST'])
def agregarMateriales():
    if request.method == 'POST':
        data = request.get_json()
        if(crear_evento.agregar_material_temporal(data)):
            return jsonify({'redireccionar': url_for('agregar_actividad')})
           
    else :
        return render_template('agragr_material.html')
@app.route('/encargadoVista/crearEvento/agregarActividad/agregarExpositor', methods=['GET', 'POST'])
def agregarExpositor():
    if request.method == 'POST':
        data = request.get_json()
        if(crear_evento.agregar_expositor_temporal(data)):
            return jsonify({'redireccionar': url_for('agregar_actividad')})
           
    else :
        return render_template('agrgar_expositor.html')
@app.route('/cargarActividad', methods=['GET', 'POST'])
def cargarActividad():
    if request.method == 'POST':
        liste=crear_evento.cargando_actividad_temp(request,app.config['UPLOAD_FOLDER'])
        print (liste)
        return jsonify({'redireccionar': url_for('crearEvento')})
    else:
        return jsonify({'redireccionar': url_for('crearEvento')})

@app.route('/cargarEventoCompleto', methods=['GET', 'POST'])
def cargarEventoCompleto():
    if request.method == 'POST':
        liste=crear_evento.crear_evento_bd(request,app.config['UPLOAD_FOLDER'])
        if (liste):
            return jsonify({'redireccionar': url_for('encargadoVista')})
    else:
        return jsonify({'redireccionar': url_for('crearEvento')})
    
@app.route('/encargadoVista/crearEvento/agregarPaquete', methods=['GET', 'POST'])
def agregarPaquete():
    if request.method == 'POST':
        data=request.get_json()
        crear_evento.actualizar_paquetes(data)
        return jsonify({'redireccionar': url_for('crearEvento')})
    else:
       return render_template('agregar_paquete.html')
    
@app.route('/encargadoVista/gestionarEevento', methods=['GET', 'POST'])
def gestionarEevento():
    if request.method == 'POST':
        data=request.get_json()
        crear_evento.actualizar_paquetes(data)
        return jsonify({'redireccionar': url_for('crearEvento')})
    else:
       return render_template('gestion_vistaprincipal.html')
    
@app.route('/obtenerEventos_img', methods=['GET', 'POST'])
def obtenerEventos_img():
    data=crear_evento.evento_imagen()
    return data
    
if __name__ == '__main__':
    
    app.run(debug=True)