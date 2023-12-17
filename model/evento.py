from sqlalchemy import Column, Integer, String, Boolean, ForeignKey,LargeBinary
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
    id_ubicacion = Column(Integer, primary_key=True)
    pais = Column(String(80))
    departamento = Column(String(80))
    direccion = Column(String(80))
    aforo = Column(Integer)
    id_persona = Column(Integer,ForeignKey('personas.id_persona'))
    persona = relationship('personas') 

class imagen_ubicacion(db.Base):
    __tablename__ = 'imagen_ubicacion'
    id_imagen_ubicacion = Column(Integer, primary_key=True)
    imagen = Column(LargeBinary) 
    id_ubicacion = Column(Integer,ForeignKey('ubicaciones.id_ubicacion'))
    ubicacion = relationship('ubicaciones')
