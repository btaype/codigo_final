class sesion_activo:
    
    id_persona = None
    nombre = None
    apellido = None
    email = None
    rol = None
    estado = False
    id_evento=6

    @classmethod
    def iniciar_sesion(cls, id_persona, nombre, apellido, email, rol,estado):
        cls.id_persona = id_persona
        cls.nombre = nombre
        cls.apellido = apellido
        cls.email = email
        cls.rol = rol
        cls.estado = estado
    @classmethod
    def cambiar(cls,id_evento1):
        cls.id_evento=id_evento1
    @classmethod
    def cerrar_sesion(cls):
        cls.id_persona = None
        cls.nombre = None
        cls.apellido = None
        cls.email = None
        cls.rol = None
        cls.estado = False