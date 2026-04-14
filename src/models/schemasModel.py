from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import date, time

class UsuariosSchema(BaseModel):
    nombre: str = Field(min_lenght=3, max_lenght=100)
    email: EmailStr
    password : str = Field(min_length=8)
    
class TareaSchema(BaseModel):
    titulo: str = Field(min_length=5, max_length=200)
    descripcion: str = Field(min_length=10)
    pioridad: str = "media"
    clasificacion: str = "personal"
