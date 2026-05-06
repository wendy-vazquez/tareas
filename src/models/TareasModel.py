from .database import Database

class TareaModel:
    def __init__(self):
        self.db = Database()
        
    def listar_por_usuario(self, id_usuario):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM tareas WHERE id_usuario = %s ORDER BY fecha_creacion ASC"
        cursor.execute(query, (id_usuario,))
        resultado = cursor.fetchall()
        conn.close()
        return resultado
    
    def cambiar_estado(self, id_tarea, nuevo_estado):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE tareas SET realizada = %s WHERE id_tarea = %s", (nuevo_estado, id_tarea))
        conn.commit()
        conn.close()

    def crear(self, id_usuario, descripcion, clasificacion):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        query = "INSERT INTO tareas (id_usuario, descripcion, clasificacion) VALUES(%s, %s, %s)"
        cursor.execute(query, (id_usuario, descripcion, clasificacion))
        conn.commit()
        conn.close()

