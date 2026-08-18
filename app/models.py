from sqlalchemy import Boolean, Column, ForeignKey, Integer, Unicode
from sqlalchemy.orm import relationship

from app.database import Base


class Editorial(Base):
    __tablename__ = "editoriales"

    id = Column(Integer, primary_key=True)
    nombre = Column(Unicode(250), nullable=False)

    comics = relationship("Comic", back_populates="editorial")


class Comic(Base):
    __tablename__ = "comics"

    id = Column(Integer, primary_key=True)
    titulo = Column(Unicode(200), nullable=False)
    numero = Column(Unicode(5), nullable=True)
    volumen = Column(Unicode(200), nullable=True)
    id_editorial = Column(Integer, ForeignKey("editoriales.id"), nullable=False)
    url = Column(Unicode, nullable=True)
    url_portada = Column(Unicode, nullable=True)
    calificacion = Column(Integer, nullable=True)
    leido = Column(Boolean, nullable=False, default=False)
    anno_publicacion = Column(Integer, nullable=True)

    editorial = relationship("Editorial", back_populates="comics")
