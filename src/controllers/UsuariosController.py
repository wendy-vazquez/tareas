from src.models.UsuariosModel import UsuariosModel
from src.models.schemasModel import UsuariosSchema
from pydantic import ValidationError

class AuthController:
    def __init__(self):
        self.model = UsuariosModel()

    def registrar_usuario(self, nombre, email, password):
        try:
            # validar datos con el Schema
            nuevo_usuario = UsuariosSchema(
                nombre=nombre,
                email=email,
                password=password
            )

            success = self.model.registrar(nuevo_usuario.dict())

            return success, "Usuario creado correctamente"

        except ValidationError as e:
            return False, e.errors()[0]['msg']
        