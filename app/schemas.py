from typing import Optional

from pydantic import BaseModel, ConfigDict


class EditorialOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    nombre: str


class ComicOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    titulo: str
    numero: Optional[str] = None
    volumen: Optional[str] = None
    id_editorial: int
    url: Optional[str] = None
    url_portada: Optional[str] = None
    calificacion: Optional[int] = None
    leido: bool
    anno_publicacion: Optional[int] = None
