import bcrypt
from .database import Database

class UsuariosModel:
    def __init__(self):
        self.db = Database()
        
    def registrar(self, usuario_data):
        salt = bcrypt.gensalt()
        hashed_pw = bcrypt.hashpw(usuario_data['contrasena'].encode('utf-8'), salt)
        
        conn = self.db.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute(
                "INSERT INTO usuarios (nombre, apellido_paterno, apellido_materno, nombre_usuario, correo, contrasena) VALUES(%s,%s,%s,%s,%s,%s)",
                (usuario_data['nombre'], usuario_data['apellido_paterno'], usuario_data['apellido_materno'],
                 usuario_data['nombre_usuario'], usuario_data['correo'], hashed_pw.decode('utf-8'))
            )
            conn.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            conn.close()
            
    def validar_login(self, email, password):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        
        cursor.execute("SELECT * FROM usuarios WHERE correo = %s", (email,))
        user = cursor.fetchone()
        conn.close()
        
        if user and bcrypt.checkpw(password.encode('utf-8'), user['contrasena'].encode('utf-8')):
            return user
        
        return None