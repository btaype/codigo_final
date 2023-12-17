from model.personas import personas
from DB.base_datos import db

class GestorPersonas:
    @staticmethod
    def registro(nombre, apellido, email, telefono, contraseña, tipo_documento,
                       numero_documento, fecha_nacimiento, sexo):
      
            nueva_persona = personas(
                nombre=nombre,
                apellido=apellido,
                email=email,
                telefono=telefono,
                contraseña=contraseña,
                tipo_documento=tipo_documento,
                numero_documento=numero_documento,
                fecha_nacimiento=fecha_nacimiento,
                sexo=sexo,
                estado=True,
                rol="usuario"
            )
            db.session.add(nueva_persona)
            db.session.commit()
            return True
        
