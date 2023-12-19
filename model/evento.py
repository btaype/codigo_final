from sqlalchemy import Column, Integer, String, Boolean, ForeignKey,LargeBinary,Date,DateTime,Float
from sqlalchemy.orm import relationship
from DB.base_datos import db
from model.personas import personas

class plantillas(db.Base):
    __tablename__ = 'plantillas'
    id_plantilla = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(80))
    ingreso_libre = Column(Boolean)
    turno = Column(String(45))
    categoria_edad = Column(String(45))
    permitir_invitaciones = Column(Boolean)
    id_persona = Column(Integer, ForeignKey('personas.id_persona'))  
    persona = relationship('personas') 

class ubicaciones(db.Base):
    __tablename__ = 'ubicaciones'
    id_ubicacion = Column(Integer, primary_key=True,autoincrement=True)
    pais = Column(String(80))
    departamento = Column(String(80))
    direccion = Column(String(80))
    aforo = Column(Integer)
    id_persona = Column(Integer,ForeignKey('personas.id_persona'))
    persona = relationship('personas') 

class imagen_ubicacion(db.Base):
    __tablename__ = 'imagen_ubicacion'
    id_imagen_ubicacion = Column(Integer, primary_key=True,autoincrement=True)
    imagen = Column(String(100)) 
    id_ubicacion = Column(Integer,ForeignKey('ubicaciones.id_ubicacion'))
    ubicacion = relationship('ubicaciones')

class eventos(db.Base):
    __tablename__ = 'eventos'

    id_evento = Column(Integer, primary_key=True,autoincrement=True)
    estado = Column(Integer)
    nombre = Column(String(80))
    descripcion = Column(String(200))
    fecha_mostrar_inicio = Column(Date)
    fecha_mostrar_fin = Column(Date)
    fecha_inicio_evento = Column(Date)
    fecha_fin_evento = Column(Date)
    id_plantilla = Column(Integer, ForeignKey('plantillas.id_plantilla'))
    plantilla = relationship('plantillas')  

class images_evento(db.Base):
    __tablename__ = 'images_evento'

    id_imagen = Column(Integer, primary_key=True,autoincrement=True)
    imagen = Column(String(100))
    id_evento = Column(Integer, ForeignKey('eventos.id_evento')) 
    evento = relationship('eventos')


class actividades(db.Base):
    __tablename__ = 'actividades'

    id_actividad = Column(Integer, primary_key=True,autoincrement=True)
    nombre = Column(String(80))
    horario_inicio = Column(DateTime)
    descripcion = Column(String(200))
    horario_fin = Column(DateTime)
    id_evento = Column(Integer, ForeignKey('eventos.id_evento')) 
    id_ubicacion = Column(Integer, ForeignKey('ubicaciones.id_ubicacion')) 
    evento = relationship('eventos')  
    ubicacion = relationship('ubicaciones') 

class imagenes_actividas(db.Base):
    __tablename__ = 'imagenes_actividas'
    id_imagen_actividad = Column(Integer, primary_key=True, autoincrement=True)
    imagen = Column(String(100))
    id_actividad = Column(Integer, ForeignKey('actividades.id_actividad'))  # Ajustar si es necesario
    actividad = relationship('actividades')

class materiales(db.Base):
    __tablename__ = 'materiales'
    id_materiales = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(80))
    descripcion = Column(String(250))
    cantidad = Column(Float)
    preico_total = Column(Float)
    id_actividad = Column(Integer, ForeignKey('actividades.id_actividad'))  # Ajustar si es necesario
    actividad = relationship('actividades') 


class paquetes(db.Base):
    __tablename__ = 'paquetes'

    id_paquete = Column(Integer, primary_key=True, autoincrement=True)
    nombre_general = Column(String(80))
    precio = Column(Float)
    cantidad = Column(Integer)
    id_evento = Column(Integer, ForeignKey('eventos.id_evento')) 
    evento = relationship('eventos')  
 
class actividad_paquetes(db.Base):
    __tablename__ = 'actividad_paquetes'

    id_actividad_paquete = Column(Integer, primary_key=True, autoincrement=True)
    id_paquete = Column(Integer, ForeignKey('paquetes.id_paquete'))  
    id_actividad = Column(Integer, ForeignKey('actividades.id_actividad'))  
    paquete = relationship('paquetes')  
    actividad = relationship('actividades') 

class extras_paquetes(db.Base):
    __tablename__ = 'extras_paquetes'

    id_extras_paquetes = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(80))
    descripcion = Column(String(250))
    id_paquete = Column(Integer, ForeignKey('paquetes.id_paquete'))  # Ajustar si es necesario

    paquete = relationship('paquetes') 

class expositor(db.Base):
    __tablename__ = 'expositor'
    id_expositor = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(80))
    apellido = Column(String(45))
    cargo = Column(String(45))
    id_actividad = Column(Integer, ForeignKey('actividades.id_actividad')) 
    actividad = relationship('actividades')  
class personas_has_eventos(db.Base):
    __tablename__ = 'personas_has_eventos'

    id_persona = Column(Integer, ForeignKey('personas.id_persona'), primary_key=True)
    id_evento = Column(Integer, ForeignKey('eventos.id_evento'), primary_key=True)

    # Relaciones
    persona = relationship('personas')
    evento = relationship('eventos')