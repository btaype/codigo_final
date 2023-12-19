import copy
from model.personas import *
from DB.base_datos import db
from activos.sesion import sesion_activo
from model.evento import *
from controler.funciones_p import *

class controlador_us:
    @staticmethod
    def obtener_todo_eventos():
        lista=[]
        db.session
        sesion=db.get_session()
        eventospp=sesion.query(eventos).all
        for i in eventospp:
            imagen=sesion.query(images_evento).filter_by(id_evento=i.id_evento).firts()
            lista.append(
                {
                "id_evento":i.id_evento,
                "nombre":i.nombre,
                "imagen":imagen.imagen
                }

            )
        return {"eventos":list}