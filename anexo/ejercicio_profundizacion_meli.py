
__author__ = "phv"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import sqlite3
import sqlalchemy
from sqlalchemy import  Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import numpy as np
import csv

#Creo DB
engine = sqlalchemy.create_engine('sqlite:///data.db')
base = declarative_base()
session = sessionmaker(bind=engine)()


#Creando la Clase y la tabla Articulo
class Articulo(base):
    __tablename__ = 'articulo'

    id = Column(Integer,primary_key=True)
    site_id = Column(String)

def create_schema():
    base.metadata.drop_all(engine)

    base.metadata.create_all(engine)
'''
    ## fill()

Deben crear una función "fill" que lea los datos del archivo CSV y cargue las respuestas de la API como filas de la tabla SQL.
 Pueden resolverlo de la forma que mejor crean. Deben usar la sentencia INSERT para insertar los datos.\
'''

def fill():
    with open ('technical_challenge_data.csv') as fo:
        data = list(csv.DictReader(fo))

        for i in data:
            acceso = i['site'] , i['id']

            url = 'https://api.mercadolibre.com/items?ids={acceso}'
            response = request.get(url)
            data = response.json


if __name__ == "__main__":
  # Crear DB
  create_schema()

  # Completar la DB con el CSV
  fill()

  # Leer filas
  #fetch('MLA845041373')
  #fetch('MLA717159516')

