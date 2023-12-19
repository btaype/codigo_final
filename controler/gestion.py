import copy
from model.personas import *
from DB.base_datos import db
from activos.sesion import sesion_activo
from model.evento import *
from controler.funciones_p import *
class gestionar:
    @staticmethod
    def obtener_evento_completo():
        pass

    @staticmethod
    def obtener_inscritos3():
        session = db.get_session()
        ehp =  session.query(inscripcion).filter_by(evento_id=sesion_activo.id_evento).all()
        data=[]
        for i in ehp:
            data.append({
                "nombre": i.nombre_apellido,
                "documento":i.numero_docuemnto,
                "email":i.email
        

            })
        return  {"inscripcion":data}
    
    @staticmethod
    def obtener_preinscritos3():
        session = db.get_session()
        ehp = session.query(preinscripcion).filter_by(id_evento=sesion_activo.id_evento).all()
        data=[]
        for i in ehp:
            data.append({
                "nombre": i.nombre_apellido,
                "documento":i.numero_documento,
                "email":i.email

            })
        return  {"preinscripcion":data}

    @staticmethod
    def obtener_ingresos():
        print("hollllaaa")
        session = db.get_session()
        inscripciones = session.query(inscripcion).filter_by(evento_id=sesion_activo.id_evento).all()
        data=[]
        total=0.0 
        for i in inscripciones:
            boleta1=session.query(boleta).filter_by(id_preinscripcion=i.id_inscripcion).first()
            data.append({
                "id":boleta1.id_boleta,
                "name":"boletas",
                "monto_total":boleta1.monto_total})
            total=total+boleta1.monto_total 

        return  {"boletas":data,"total":total}
    
    @staticmethod
    def obtener_materiales():
       
            session = db.get_session()
            data=[]
            total=0.0 
            actividades_1=session.query(actividades).filter_by(id_evento=eventoselect.id_evento).all()
            for i in actividades_1:
                materiales1=session.query(materiales).filter_by(id_actividad=i.id_actividad).all()
                for j in materiales1:
                    data.append({
                        "id":j.id_materiales,
                        "nombre":j.nombre,
                        "monto_total":j.preico_total})
                    
                    total=total-j.preico_total
            session.close()
            return  {"materiales":data,"total":total}
    
    

    @staticmethod  
    def actializar_idvento(data): 
       sesion_activo.id_evento=data["id_evento"]
       return 0

