import db
from models import Caja

def populate_db():
    cajas = [
        Caja(nombre="Caja 1", descripcion="Soy una bestia hibrida, metal y silicio son mis esenciales.", pista="Soy un Mecha-Dragon, el más prestigioso del mundo.", intentos=0, password="MSI"),
        Caja(nombre="Caja 2", descripcion="Algunos me llamaban Steve", pista="Suelo hacer muy bien mi Jobbs", intentos=0, password="Apple"),
        Caja(nombre="Caja 3", descripcion="Madonna aprueba este producto", pista="El cuerpo humano tiene 206", intentos=0, password="DeadPool"),
        Caja(nombre="Caja 4", descripcion="Soy el rey del miedo", pista="Aunque ya somos dos terrorificos reyes", intentos=0, password="King"),
        Caja(nombre="Caja 5", descripcion="Soy como una nube que te aisla del mundo para unirte personalmente a él", pista="Soy la corona de un rey que reina en silencio, mi cetro es digital y mi reino se oye por todo el mundo.", intentos=0, password="Apple"),
        Caja(nombre="Caja 6", descripcion="Surco los mares sin prisa y con admiración", pista="Yo me convertiré en el...", intentos=0, password="One Piece"),
        Caja(nombre="Caja 7", descripcion="Tan único que es raro ser visto 2 veces", pista="Un lienzo humano como mapa de los recuerdos", intentos=0, password="Tatuaje"),
        Caja(nombre="Caja 8", descripcion="Pronto se empieza una nueva etapa", pista="Necesitarás muchos .......... para empezar el cole", intentos=0, password="Materiales"),
        Caja(nombre="Caja 9", descripcion="Formaba parte de tu infancia", pista="Por qué Solo 3 OSITOS tienen un libro", intentos=0, password="123"),
        Caja(nombre="Caja 10", descripcion="Descripción de la Caja 10", pista="Pista de la Caja 10", intentos=0, password="123"),
    ]

    db.session.bulk_save_objects(cajas)
    db.session.commit()

if __name__ == '__main__':
    populate_db()
    print("Base de datos poblada con éxito.")
