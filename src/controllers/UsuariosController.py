from models.UsuariosModel import UsuariosModel
from models.schemasModel import UsuariosSchema
from pydantic import ValidationError

class AuthController:
    def __init__(self):
        self.model = UsuariosModel()

    def registrar_usuario(self, nombre, ap_paterno, ap_materno, nombre_usuario, correo, contrasena):
        try:
            success = self.model.registrar({
                'nombre': nombre,
                'apellido_paterno': ap_paterno,
                'apellido_materno': ap_materno,
                'nombre_usuario': nombre_usuario,
                'correo': correo,
                'contrasena': contrasena
            })
            return success, "Usuario creado correctamente"
        except ValidationError as e:
            return False, e.errors()[0]['msg']

    def login(self, email, password):
        user = self.model.validar_login(email, password)
        if user:
            return user, "OK"
        return None, "Credenciales incorrectas"