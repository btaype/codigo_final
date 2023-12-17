from sqlalchemy import Column, Integer, String, Date, Boolean
from DB.base_datos import db

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