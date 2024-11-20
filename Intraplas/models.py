from django.db import models

# Create your models here.

#USUARIOS INTRAPLAS MODELS

class usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=20)
 
    rol_opciones = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    
    area = models.CharField(max_length=20, null=True)
    rol = models.IntegerField(choices=rol_opciones, null=True, blank=True)

