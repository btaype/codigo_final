from model.personas import personas
from DB.base_datos import db
from activos.sesion import sesion_activo
class inicioSesion:
    @staticmethod
    def iniciando(data):
        session=db.get_session()
        persona = session.query(personas).filter_by(email=data["email"], contraseña=data["contrasena"]).first()
        if persona:
            sesion_activo.iniciar_sesion(persona.id_persona,persona.nombre,persona.apellido,persona.email,persona.rol,persona.estado)
            return True     
        else:
            return False
    