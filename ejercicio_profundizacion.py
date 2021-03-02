
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


#Creando DB
engine = sqlalchemy.create_engine("sqlite:///profundizacion.db")
base = declarative_base()
session = sessionmaker(bind=engine)()

class Autor(base):
    __tablename__ = "autor"
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Book(base):
    __tablename__ = "book" 
    id = Column(Integer,primary_key=True)
    title = Column(String)
    pags = Column(Integer)
    author_id = Column(Integer, ForeignKey('autor.id'))
    author = relationship('Autor')

def create_schema():
    base.metadata.drop_all(engine)

    base.metadata.create_all(engine)

def fill():
    Session = sessionmaker(bind=engine)
    session = Session()

    data_autor = np.genfromtxt('libreria_autor.csv', delimiter=',' , dtype = None, encoding = None)
    data_autor = data_autor[1:,]
    data_autor = data_autor.tolist()
    
    for i in data_autor: 
        autor_name = Autor(name=i)
        session.add(autor_name)

    with open ('libreria_libro.csv') as fo:
        data = list(csv.DictReader(fo))
        for i in data:
            query = session.query(Autor).filter(Autor.name==i['autor'])
            autor_id = query.first()
            book_add = Book(title=i['titulo'], pags=i['cantidad_paginas'],author=autor_id)
            
            session.add(book_add)   

    session.commit()

def fetch(id):
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        if id == 0 :
            query = session.query(Book).all()
            for book in query:
                print(book.title)

        if id > 0:
            book = session.query(Book).filter(Book.id == id).first()

            if book is None:
               print('El libro no esta en la base de datos')

            else:
                print(book)
            
    except:
        pass
    session.commit()

def search_author(book_title):
    Session = sessionmaker(bind=engine)
    session = Session()

    autor = session.query(Autor).join(Book.author).filter(Book.title == book_title).first()
    
    return(autor)


    session.commit()


if __name__ == "__main__":
  # Crear DB
  create_schema()

  # Completar la DB con el CSV
  fill()

  # Leer filas
  #fetch(0)  # Ver todo el contenido de la DB
  fetch(3)  # Ver la fila 3
  fetch(20)  # Ver la fila 20

  #Buscar autor
  #print(search_author('Relato de un naufrago'))


