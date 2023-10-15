from django.test import TestCase
import random
import string 
from appcoder.models import Proyectos_Ley

from datetime import datetime as dt
from .utilities.utility import return_today

class TestUtilities(TestCase):
     
    def test_day(self):
        hoy = dt.now()
        self.assertEqual( 15, return_today())

class estUsers(TestCase):

    def test_crear_proyecto(self):
        informacion = {
            "tematica": "",    
        }
        KEY_LEN = 20
        keylistNombre = [random.choice((string.ascii_letters + string.digits )) for i in range(KEY_LEN)]
        nombrePrueba = "".join(keylistNombre)

        print(f"-----> Prueba con: {nombrePrueba}")

        proyecto = Proyectos_Ley(
            nombre=nombrePrueba,
            tematica= informacion['tematica']
        )

        proyecto.save()