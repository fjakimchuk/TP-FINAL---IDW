# librerias
import os
import json

# modelos
from modelos.artista import Artista
from modelos.banda import Banda
from modelos.cancion import Cancion
from modelos.album import Album
from modelos.genero import Genero


class Biblioteca:

    __archivoDeDatos = "biblioteca.json"
    __artistas = []
    __canciones = []
    __albumes = []
    __generos = []

    def inicializar():
        datos = Biblioteca.__parsearArchivoDeDatos()
        Biblioteca.__convertirJsonAListas(datos)

    def obtenerArtistas(orden=None, reverso=False):
        if isinstance(orden, str):
            if orden == 'nombre':
                pass
            elif orden == 'tipo':
                pass
        pass

    def obtenerCanciones(orden=None, reverso=False):
        if isinstance(orden, str):
            if orden == 'nombre':
                pass
            elif orden == 'artista':
                pass
        pass

    def obtenerAlbumes(orden=None, reverso=False):
        if isinstance(orden, str):
            if orden == 'nombre':
                pass
            elif orden == 'artista':
                pass
            elif orden == 'anio':
                pass
        pass

    def obtenerGeneros(orden=None, reverso=False):
        if isinstance(orden, str):
            if orden == 'nombre':
                pass
        pass
    
    def buscarArtista(id):
        pass

    def buscarCancion(id):
        pass
    
    def buscarAlbum(id):
        pass

    def buscarGenero(id):
        pass
    
    def __parsearArchivoDeDatos():
        pass

    def __convertirJsonAListas(lista):
        pass
