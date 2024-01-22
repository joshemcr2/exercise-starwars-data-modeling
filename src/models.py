import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

association_table = Table(
    "association_table",
    Base.metadata,
    Column("left_id", ForeignKey("left_table.id"), primary_key=True),
    Column("right_id", ForeignKey("right_table.id"), primary_key=True)
)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    apellidos = Column(String(40))
    email = Column(String(50))
    contraseña = Column(String(50))
    

class Planetas(Base):
    __tablename__ = 'planetas'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    diameter = Column(Float)
    gravity = Column(String(20))
    surface_water = Column(Integer)
    Favoritos = relationship("Favoritos")

class Personajes(Base):
    __tablename__ = 'personajes'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    height = Column(Float)
    mass = Column(Float)
    gender = Column(String(10))
    created_date_time = Column(DateTime)
    Favoritos = relationship("Favoritos")

class Vehiculos(Base):
    __tablename__ = 'vehiculos'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    model = Column(String(50))
    passenger = Column(Integer)
    Favoritos = relationship("Favoritos")

class Favoritos(Base):
    __tablename__ = 'favoritos'
    id = Column(Integer, primary_key=True)
    id_del_usuario = Column(Integer, ForeignKey('user.id'))
    id_del_planeta = Column(Integer, ForeignKey('planetas.id'))
    id_del_personaje = Column(Integer, ForeignKey('personajes.id'))
    id_del_vehiculo = Column(Integer, ForeignKey('vehiculos.id'))


def to_dict(self):
    return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
