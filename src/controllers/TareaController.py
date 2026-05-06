from models.TareasModel import TareaModel

class TareaController:
    def __init__(self):
        self.model = TareaModel()

    def obtener_lista(self, id_usuario):
        return self.model.listar_por_usuario(id_usuario)

    def cambiar_estado(self, id_tarea, nuevo_estado):
        self.model.cambiar_estado(id_tarea, nuevo_estado)

    def guardar_nueva(self, id_usuario, descripcion, clasificacion):
        if not descripcion:
            return False, "La descripción es obligatoria"
        self.model.crear(id_usuario, descripcion, clasificacion)
        return True, "Tarea guardada"
