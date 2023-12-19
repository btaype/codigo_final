import copy
from model.personas import *
from DB.base_datos import db
from activos.sesion import sesion_activo
from model.evento import *
from werkzeug.utils import secure_filename
import os
from activos.activo_evento import  eventoActivo
from controler.funciones_p import *
from activos.evento_select_ import eventoselect

class gestionar:
    @staticmethod
    def obtener_evento_completo():
        pass

    @staticmethod
    def obtener_incritos():
        session = db.get_session()
        ehp = session.query(inscripcion).filter_by(id_evento=eventoselect.id_evento).all()
        data=[]
        for i in ehp:
            data.append({
                "nombre": i.nombre_apellido,
                "documento":i.numero_documento,
                "email":i.email
        

            })
        return  {"inscripcion":data}
    
    @staticmethod
    def obtener_preinscritos():
        session = db.get_session()
        ehp = session.query(preinscripcion).filter_by(id_evento=eventoselect.id_evento).all()
        data=[]
        for i in ehp:
            data.append({
                "nombre": i.nombre_apellido,
                "documento":i.numero_documento,
                "email":i.email

            })
        return  {"inscripcion":data}

    @staticmethod
    def obtoptener_ingresos():
        session = db.get_session()
        inscripciones = session.query(inscripcion).filter_by(id_evento=eventoselect.id_evento).first()
        data=[]
        for i in inscripciones:
            boleta1=session.query(boleta).filter_by(id_preinscripcion=i.id_inscripcion).first()
            data.append({
                "nombre": i.nombre_apellido,
                "documento":i.numero_documento,
                "email":i.email

            })
        return  {"inscripcion":data}
