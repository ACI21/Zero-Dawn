import db
from models import Caja

def populate_db():
    db.session.query(Caja).delete()

    cajas = [
        # ordenador - check
        Caja(nombre="Caja 1", descripcion="Soy una bestia hibrida, metal y silicio son mis esenciales.", pista="Antes solia ser chachi", intentos=0, contrasenya="pcchachi", abierta=True),
        # osito amoroso en caja - check
        Caja(nombre="Caja 2", descripcion="Soy un osito pero no haribo", pista="Me suelen llevar a tous partes", intentos=0, contrasenya="Tous", abierta=False),
        # funko desdentao - check
        Caja(nombre="Caja 3", descripcion="Soy negro, del norte y puedo volar", pista="Suelo comer estan desdentado", intentos=0, contrasenya="Furia Nocturna", abierta=False),
        # libro king - Angel - check
        Caja(nombre="Caja 4", descripcion="Soy el rey del miedo", pista="Aunque ya somos dos terrorificos reyes", intentos=0, contrasenya="King", abierta=True),
        # mochila para el cole
        Caja(nombre="Caja 5", descripcion="Soy muy cuqui y me puedes llevar al cole", pista="Soy Parfuecto para todas las ocasiones", intentos=0, contrasenya="Parfois", abierta=False),
        # libros one piece
        Caja(nombre="Caja 6", descripcion="Surco los mares en busca del tesoro", pista="Yo me convertiré en el...", intentos=0, contrasenya="One Piece", abierta=False),
        # tatuaje - check
        Caja(nombre="Caja 7", descripcion="Tan único que es raro ser visto 2 veces", pista="Un lienzo humano como mapa de los recuerdos", intentos=0, contrasenya="Tatuaje", abierta=False),
        # Material escolar - Lola - check
        Caja(nombre="Caja 8", descripcion="Pronto se empieza una nueva etapa", pista="Necesitarás muchos .......... para empezar el cole", intentos=0, contrasenya="Materiales", abierta=False),
        # Juego ps3 - check
        Caja(nombre="Caja 9", descripcion="Formaba parte de tu infancia", pista="Osito que mata ositos por no ser invitado a la fiesta", intentos=0, contrasenya="PS3", abierta=False),
        # funko diurna - check
        Caja(nombre="Caja 10", descripcion="Soy blanca, del norte y un poco diurna", pista="Chimuelo pero en blanco", intentos=0, contrasenya="Furia Diurna", abierta=False),
    ]

    db.session.bulk_save_objects(cajas)
    db.session.commit()

if __name__ == '__main__':
    populate_db()
    print("Base de datos poblada con éxito.")
