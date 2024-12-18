from typing import Union
from pydantic import BaseModel

class ClienteSchema(BaseModel):
    id: Union[str, None] = None
    nombres: Union[str, None] = None 
    class Config:
        from_attributes = True
class Incidentes(BaseModel):
    cliente: Union[ClienteSchema, None] = None
    fechacreacion: Union[str, None] = None
    usuario: Union[ClienteSchema, None] = None
    gestor: Union[ClienteSchema, None] = None
    correo: Union[str, None] = None
    direccion: Union[str, None] = None
    telefono: Union[str, None] = None
    descripcion: Union[str, None] = None
    prioridad: Union[str, None] = None
    estado: Union[str, None] = None
    comentarios: Union[str, None] = None
    canal: Union[str, None] = None
    tipo: Union[str, None] = None
    class Config:
        from_attributes = True
