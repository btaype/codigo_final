import copy
from model.personas import personas
from DB.base_datos import db
from activos.sesion import sesion_activo
from model.evento import *
from werkzeug.utils import secure_filename
import os
from activos.activo_evento import  eventoActivo
from controler.funciones_p import *
class crear_evento:
    @staticmethod
    def inicio():
        session = db.get_session()
        plantillas1 = session.query(plantillas).filter_by(id_persona=sesion_activo.id_persona).all()
        print(plantillas1)
        resultados = []

        if plantillas1:
            for plantilla in plantillas1:
                resultado_plantilla = {
                    'id_plantilla': plantilla.id_plantilla,
                    'nombre': plantilla.nombre,
                    'ingreso_libre':plantilla.ingreso_libre,
                    'turno': plantilla.turno,
                    'categoria_edad': plantilla.categoria_edad,
                    'permitir_invitaciones': plantilla.permitir_invitaciones,

                }
                resultados.append(resultado_plantilla)
        return {"plantillas":resultados}

       
    @staticmethod
    def obtenerevento():
        return eventoActivo.evento

    @staticmethod
    def actilizar(data):
        eventoActivo.evento["nombre"]=data["nombre"]
        eventoActivo.evento["descripcion"]=data["descripcion"]
        eventoActivo.evento["fecha_mostrar_inicio"]=data["fecha_mostrar_inicio"]
        eventoActivo.evento["fecha_mostrar_fin"]=data["fecha_mostrar_fin"]
        eventoActivo.evento["fecha_inicio_evento"]=data["fecha_inicio_evento"]
        eventoActivo.evento["fecha_fin_evento"]=data["fecha_fin_evento"]
        eventoActivo.evento["nombre_plantilla"]=data["nombre_plantilla"]
        eventoActivo.evento["id_plantilla"]=data["id_plantilla"]
    @staticmethod
    def agregar_plantilla(data):
        plantilla=plantillas( 
        nombre=data["nombre"],
        ingreso_libre=data["ingreso_libre"],
        turno=data["turno"],
        categoria_edad=data["categoria_edad"],
        permitir_invitaciones=data["permitir_invitaciones"],
        id_persona=sesion_activo.id_persona)
        db.session.add(plantilla)
        db.session.commit()
        return True
    @staticmethod
    def obetener_imagen_ubicacion():
        session = db.get_session()
        ubicaciones_persona = session.query(ubicaciones).filter_by(id_persona=sesion_activo.id_persona).all()
        data = []
        for ubicacion in ubicaciones_persona:
            imagen = session.query(imagen_ubicacion).filter_by(id_ubicacion=ubicacion.id_ubicacion).first()
            data.append({
            
                'id_ubicacion': ubicacion.id_ubicacion,
                'pais': ubicacion.pais,
                'departamento': ubicacion.departamento,
                'direccion': ubicacion.direccion,
                'aforo': ubicacion.aforo,
                'imagen': imagen.imagen 
            })
        return {'ubicaciones': data}
    @staticmethod
    def crear_ubicacion(data):
       
       
        pais = data.form['pais']
        departamento = data.form['departamento']
        direccion = data.form['direccion']
        aforo = data.form['aforo']

        nueva_ubicacion = ubicaciones(
        pais=pais,
        departamento=departamento,
        direccion=direccion,
        aforo=aforo,
        id_persona=sesion_activo.id_persona)

        db.session.add(nueva_ubicacion)
        db.session.commit()

        return nueva_ubicacion
    @staticmethod
    def agregar_material_temporal(data):
        
        material1=  copy.deepcopy(eventoActivo.model_materiales)
        material1["nombre"]=data["nombre"]
        material1["descripcion"]=data["descripcion"]
        material1["cantidad"]=data["cantidad"]
        material1["precio_total"]=data["precio_total"]
        eventoActivo.actividad1["materiales"].append(material1)
        material1=eventoActivo.model_materiales
        return True
    @staticmethod
    def agregar_expositor_temporal(data):
        expositor1=copy.deepcopy(eventoActivo.model_expositores)
        expositor1["nombre"]=data["nombre"]
        expositor1["apellido"]=data["apellido"]
        expositor1["cargo"]=data["cargo"]
        eventoActivo.actividad1["expositores"].append(expositor1)
        
        return True
    
    @staticmethod
    def obtener_materiales():
        return eventoActivo.actividad1
    @staticmethod
    def obtener_expositores():
        return eventoActivo.actividad1
    @staticmethod
    def actulizar_actividad(data):
        eventoActivo.actividad1["nombre"]=data["nombre"]
        eventoActivo.actividad1["descripcion"]=data["descripcion"]
        eventoActivo.actividad1["horario_inicio"]=data["horario_inicio"]
        eventoActivo.actividad1["horario_fin"]=data["horario_fin"]
        eventoActivo.actividad1["id_ubicacion"]=data["id_ubicacion"]
        eventoActivo.actividad1["direccion"]=data["id_ubicacion"]
    @staticmethod
    def cargando_actividad_temp(data,direx):
        eventoActivo.actividad1["nombre"]=data.form["nombre"]
        eventoActivo.actividad1["descripcion"]=data.form["descripcion"]
        eventoActivo.actividad1["horario_inicio"]=data.form["horario_inicio"]
        eventoActivo.actividad1["horario_fin"]=data.form["horario_fin"]
        eventoActivo.actividad1["id_ubicacion"]=data.form["id_ubicacion"]
        eventoActivo.actividad1["direccion"]=data.form["direccion"]
        imagen = data.files['imagen']
        nombre_imagen = generate_unique_filename(secure_filename(imagen.filename))
        print (nombre_imagen)
        ruta_guardado = os.path.join(direx, nombre_imagen)
        imagen.save(ruta_guardado)
        eventoActivo.actividad1["imagen"]=nombre_imagen
        eventoActivo.actividad1["id_temp"]= (eventoActivo.actividad1["id_temp"])+1
        id_temp1=eventoActivo.actividad1["id_temp"]
        eventoActivo.list_actividades.append(eventoActivo.actividad1)
        eventoActivo.actividad1=copy.deepcopy(eventoActivo.model_actividad)
        eventoActivo.actividad1["id_temp"]=id_temp1
        return eventoActivo.list_actividades
    @staticmethod
    def obtener_actividades():
        return eventoActivo.list_actividades
    @staticmethod     
    def crear_evento_bd(data,direx):
        estado1=False
        if (data.form["estado"]=="inscripciones"):
            estado1=True

        evento_creado=eventos(
            estado=estado1,
            nombre=data.form["nombre"],
            descripcion=data.form["descripcion"],
            fecha_mostrar_inicio=data.form["fecha_mostrar_inicio"],
            fecha_mostrar_fin=data.form["fecha_mostrar_fin"],
            fecha_inicio_evento=data.form["fecha_inicio_evento"],
            fecha_fin_evento=data.form["fecha_fin_evento"],
            id_plantilla=data.form["id_plantilla"],
        )
        db.session.add(evento_creado)
        db.session.commit()
        imagen = data.files['imagen']
        nombre_imagen = generate_unique_filename(secure_filename(imagen.filename))
        print (nombre_imagen)
        ruta_guardado = os.path.join(direx, nombre_imagen)
        imagen.save(ruta_guardado)
        imgagencreado=images_evento(
            imagen =  nombre_imagen,
            id_evento = evento_creado.id_evento,
             )
        db.session.add(imgagencreado)
        db.session.commit()

        for i in eventoActivo.list_actividades:
            actividad_crear=actividades(
            nombre = i["nombre"],
            horario_inicio =i["horario_inicio"],
            descripcion = i["descripcion"],
            horario_fin = i["horario_fin"],
            id_evento = evento_creado.id_evento,
            id_ubicacion = i["id_ubicacion"]
            )
            db.session.add(actividad_crear)
            db.session.commit()
            igamagencrea=imagenes_actividas(
                imagen = i["imagen"],
                id_actividad = actividad_crear.id_actividad
                )
            i["id_actividad"]=actividad_crear.id_actividad
            db.session.add(igamagencrea)
            db.session.commit()
            for j in i["expositores"]:
                expositr_cr=expositor(
               
                nombre = j["nombre"],
                apellido = j["apellido"],
                cargo = j["cargo"],
                id_actividad = actividad_crear.id_actividad
                )
                db.session.add(expositr_cr)
                db.session.commit()
            
            for k in i["materiales"]:
                material_cr= materiales(

                    nombre = k["nombre"],
                    descripcion = k["descripcion"],
                    cantidad =k["cantidad"] ,
                    preico_total = k["precio_total"],
                    id_actividad = actividad_crear.id_actividad )
                db.session.add(material_cr)
                db.session.commit()
        for p in eventoActivo.list_paquetes:
            paquete_creado=paquetes(   
                nombre_general =p["nombre_general"],
                precio = p["precio"],
                cantidad = p["cantidad"],
                id_evento =evento_creado.id_evento )
            db.session.add(paquete_creado)
            db.session.commit()
            for l in p["actividades"]:
                id_act=bucaActividadtemp(l["id_temp"],eventoActivo.list_actividades)
                if(id_act):
                    paque_acti=actividad_paquetes(
                    id_paquete = paquete_creado.id_paquete,
                    id_actividad =id_act
                    )
                    db.session.add(paque_acti)
                    db.session.commit()
            for t in p["extras"]:
                extras_cre=extras_paquetes(
    
                nombre = t["nombre"],
                descripcion = t["descripcion"],
                id_paquete = paquete_creado.id_paquete

                )
                db.session.add(extras_cre)
                db.session.commit()
        return True
    
    @staticmethod 
    def obtener_paquetes():
        return eventoActivo.list_paquetes
    @staticmethod 
    def actualizar_paquetes(data):
        eventoActivo.list_paquetes.append(data)
    @staticmethod 
    def evento_imagen():
        session = db.get_session()
        ehp = session.query(personas_has_eventos).filter_by(id_persona=sesion_activo.id_persona).all()
        data = []
        for eventod in ehp :
            evento_r = session.query(eventos).filter_by(id_evento=eventod.id_evento).all()
            for imagen_evento in evento_r:
                imagen=session.query(images_evento).filter_by(id_evento=imagen_evento.id_evento).first()
                data.append({
                    'nombre': imagen_evento.nombre,
                    "imagen":imagen.imagen,
                    "id_evento":imagen_evento.id_evento
                })
        return {'eventos': data}
    
        