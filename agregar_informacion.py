"""
    Agregar información en una colección de MongoDB
    desde Python
"""
from enlace_base import client

# se obtiene la colección general (base de datos)

db = client.ejemploMongo001
coleccion = db.autores
print(coleccion)
