from sqlalchemy import Column, Integer, String, Boolean, ForeignKey,LargeBinary,Date,DateTime,Float
from sqlalchemy.orm import relationship
from DB.base_datos import db
from model.personas import personas

class personas(db.Base):
    __tablename__ = 'personas'
    id_persona = Column(Integer, primary_key=True)
    nombre = Column(String(80), nullable=False)
    apellido = Column(String(80), nullable=False)
    email = Column(String(80), nullable=False)
    telefono = Column(String(9), nullable=False)
    contraseña = Column(String(15), nullable=False)
    tipo_documento = Column(String(15), nullable=False)
    numero_documento = Column(String(15), nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)
    sexo = Column(String(15), nullable=False)
    estado = Column(Boolean, nullable=False)
    rol = Column(String(15), nullable=False)

class inscripcion(db.Base):
    __tablename__ = 'inscripcion'
    id_inscripcion = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(80))
    nombre_apellido = Column(String(100))
    qr = Column(String(100))
    tipo_documento = Column(String(15))
    numero_documento = Column(String(15))

    id_persona = Column(Integer, ForeignKey('persona.id_persona'))
    persona = relationship('personas')

    evento_id = Column(Integer, ForeignKey('evento.id_evento'))
    evento = relationship('eventos')

    id_paquete = Column(Integer, ForeignKey('paquete.id_paquete'))
    paquete = relationship('paquetes')

class preinscripcion(db.Base):
    __tablename__ = 'preinscripcion'

    id_presincripcion = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(80))
    nombre_apellido = Column(String(100))
    fecha = Column(DateTime)
    tipo_documento = Column(String(15))
    numero_documento = Column(String(15))

    id_persona = Column(Integer, ForeignKey('persona.id_persona'))
    persona = relationship('personas')

    id_evento = Column(Integer, ForeignKey('eventos.id_evento'))
    evento = relationship('eventos')
class boleta(db.Base):
    __tablename__ = 'boleta'

    id_boleta = Column(Integer, primary_key=True, autoincrement=True)
    monto_total = Column(String(45))
    fecha = Column(DateTime)

    # Relaciones
    id_preinscripcion = Column(Integer, ForeignKey('preinscripcion.id_preinscripcion'))
    preinscripcion = relationship('preinscripcion')
