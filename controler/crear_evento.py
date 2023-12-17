from model.personas import personas
from DB.base_datos import db
from activos.sesion import sesion_activo
from model.evento import plantillas,ubicaciones,imagen_ubicacion
from activos.activo_evento import evento

class crear_evento:
    @staticmethod
    def inicio():
        session = db.get_session()
        plantillas1 = session.query(plantillas).filter_by(id_persona=sesion_activo.id_persona).all()
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
        resultado_fin=evento
        resultado_fin['plantillas']=resultados
        
        return resultado_fin
    def actilizar(data):
        evento["nombre"]=data["nombre"]
        evento["descripcion"]=data["descripcion"]
        evento["fecha_mostrar_inicio"]=data["fecha_mostrar_inicio"]
        evento["fecha_mostrar_fin"]=data["fecha_mostrar_fin"]
        evento["fecha_inicio_evento"]=data["fecha_inicio_evento"]
        evento["fecha_fin_evento"]=data["fecha_fin_evento"]
        evento["nombre_plantilla"]=data["nombre_plantilla"]
        evento["id_plantilla"]=data["id_plantilla"]

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
                'imagen': imagen.imagen if imagen else None
            })
        return {'ubicaciones': data}
       

        

       
        
    