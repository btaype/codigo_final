import copy

class eventoActivo:
    model_evento={"nombre":"","estado":"","descripcion":"","fecha_mostrar_inicio":"","fecha_mostrar_fin":"","fecha_inicio_evento":"","fecha_fin_evento":"","id_plantilla":0,"nombre_plantilla":"","imagen":""}
    model_actividad={"id_temp":0,"nombre":"","descripcion":"","horario_inicio":"","horario_fin":"","materiales":[],"expositores":[],"id_ubicacion":0,"direccion":"","imagen":""}
    model_materiales={"nombre":"","descripcion":"","cantidad":0,"precio_total":0.0}
    model_expositores={"nombre":"","aplellido":"","cargo":""}
    model_paquete={"nombre_general":"","precio":0.0,"cantidad":0,"actividades":[],"extras":[]}
    model_paquet_actividad={"id_tem_a":0}
    model_extra={"nombre":"","descripcion":""}

    evento = copy.deepcopy(model_evento)
    actividad1 = copy.deepcopy(model_actividad)
    list_actividades = []
    material1 = copy.deepcopy(model_materiales)
    expositor1 = copy.deepcopy(model_expositores)
    paquete1= copy.deepcopy(model_paquete)
    paquete_a=copy.deepcopy(model_paquet_actividad)
    paquete_x=copy.deepcopy(model_extra)
    list_paquetes=[]

    

    