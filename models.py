from sqlalchemy import Column, Integer, String
import db

class Usuario(db.Base):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return "Usuario {}: {}".format(self.id, self.username)

    def __str__(self):
        return "Usuario {}: {}".format(self.id, self.username)

class Caja(db.Base):
    __tablename__ = 'caja'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(255), unique=True, nullable=False)
    descripcion = Column(String(255), unique=True, nullable=False)
    pista = Column(String(255), nullable=False)
    intentos = Column(Integer, nullable=False, default=0)
    password = Column(String(255), nullable=False)

    def __init__(self, nombre, descripcion, pista, intentos, password):
        self.nombre = nombre
        self.descripcion = descripcion
        self.pista = pista
        self.intentos = intentos
        self.password = password

    def __repr__(self):
        return "Caja {}: {}".format(self.id, self.nombre)

    def __str__(self):
        return "Caja {}: {}".format(self.id, self.nombre)
