import db
from models import Caja

def populate_db():
    cajas = [
        Caja(nombre="Caja 1", descripcion="Descripción de la Caja 1", pista="Pista de la Caja 1", intentos=0),
        Caja(nombre="Caja 2", descripcion="Descripción de la Caja 2", pista="Pista de la Caja 2", intentos=0),
        Caja(nombre="Caja 3", descripcion="Descripción de la Caja 3", pista="Pista de la Caja 3", intentos=0),
        Caja(nombre="Caja 4", descripcion="Descripción de la Caja 4", pista="Pista de la Caja 4", intentos=0),
        Caja(nombre="Caja 5", descripcion="Descripción de la Caja 5", pista="Pista de la Caja 5", intentos=0),
        Caja(nombre="Caja 6", descripcion="Descripción de la Caja 6", pista="Pista de la Caja 6", intentos=0),
        Caja(nombre="Caja 7", descripcion="Descripción de la Caja 7", pista="Pista de la Caja 7", intentos=0),
        Caja(nombre="Caja 8", descripcion="Descripción de la Caja 8", pista="Pista de la Caja 8", intentos=0),
        Caja(nombre="Caja 9", descripcion="Descripción de la Caja 9", pista="Pista de la Caja 9", intentos=0),
        Caja(nombre="Caja 10", descripcion="Descripción de la Caja 10", pista="Pista de la Caja 10", intentos=0),
    ]

    db.session.bulk_save_objects(cajas)
    db.session.commit()

if __name__ == '__main__':
    populate_db()
    print("Base de datos poblada con éxito.")
